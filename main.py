from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return "hi akakshi"

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WebhookRequest(BaseModel):
    session: str
    queryResult: dict

@app.post("/webhook")
async def handle_webhook(request: WebhookRequest):
    intent = request.queryResult["intent"]["displayName"]
    session_id = request.session

    if intent == "Job-reLocation-Preference":
        return handle_relocation_acceptance(request, session_id)
    else:
        return {"fulfillmentText": "Intent not supported"}


def handle_relocation_acceptance(request: WebhookRequest, session_id: str):
    parameters = request.queryResult["parameters"]

    negative = parameters.get("negative-response1")
    if negative:
        return {"fulfillmentText": "No"}

    return {"fulfillmentText": "yes"}


#uvicorn main:app --reload
#ngrok http 8000