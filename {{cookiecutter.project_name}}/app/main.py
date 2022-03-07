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
existing_run_files = os.listdir("runs")
existing_run_files = [x.replace(".py", "") for x in existing_run_files if
                      (x.endswith(".py") and x not in ['__init__.py'])]
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

@app.post("/run_batch_job")
def run_batch_job(task_name:str = Query(None, enum=existing_run_files), vcpus:int=Query(1, enum = [1,2,3,4,5,6,7,8]),
                  memory:str = Query("512", enum=[str(512 * x) for x in range(33)][1:]),
                  retry_attempts:int=1, time_out_seconds:int=3600, job_queue:str =Query("batch-jobs", enum=["batch-jobs"]), username=Depends(get_current_username)):
    from aws_utils import run_batch_task
    #for testing sentry
    run_batch_task(task_name=task_name, vcpus=vcpus, memory=memory, retry_attempts=retry_attempts,
                   time_out_seconds=time_out_seconds,job_queue=job_queue)
    return {"status": 200}

handler = Mangum(app)