from fastapi import FastAPI, HTTPException
import asyncio
from models import CreateAccountRequest, FundAccountRequest, WithdrawRequest 
from services import create_customer_account

app = FastAPI()
@app.post("/create-account")
async def create_account(data: CreateAccountRequest):
    result = await create_customer_account(data.customer_id)

    # if result :
    #     return {"Message": f"Customer {data.customer_id} created with 0.0 Balance"}
    # else:
    #     return {"Message": f"Customer {data.customer_id} already Exists"}

    if not result:
        raise HTTPException(status_code=400, detail="Customer Already Exists")
    return {"Message": f"Customer {data.customer_id} created with 0.0 Balance"}

@app.post("/fund")
async def fund_account(data: FundAccountRequest):
    return True

@app.post("/withdraw")
async def withdraw_from_account(data: WithdrawRequest):
    return True