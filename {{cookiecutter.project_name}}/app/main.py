import os

import sentry_sdk
from fastapi import FastAPI
from mangum import Mangum
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    os.environ["SENTRY_DNS"],
    integrations=[AwsLambdaIntegration()]
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    )

app = FastAPI()

@app.get("/health_base")
async def health_base():
    return {"status": 200}

@app.get("/unhealth_base")
async def unhealth_base():
    #for testing sentry
    1/0
    return {"status": 200}

@app.get("/health_extended")
async def health_extended():
    return {"status": 200}

@app.get("/unhealth_extended")
async def unhealth_extended():
    #for testing sentry
    1/0
    return {"status": 200}

handler = Mangum(app)