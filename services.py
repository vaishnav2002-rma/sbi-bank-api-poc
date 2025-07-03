import _asyncio
from db import accounts 

async def create_customer_account(customer_id: str):
    if customer_id in accounts:
        return False 
    accounts[customer_id] = 0.0
    return True 

async def fund_customer_account(customer_id: str, amount: float):
    if customer_id not in accounts:
        raise ValueError (f"Account does not exist for customer with id {customer_id}")
    accounts[customer_id] += amount 
    return accounts[customer_id]

async def withdraw_from_customer_account(customer_id: str, amount: float):
    if customer_id not in accounts:
        raise ValueError (f"Account does not exist for customer with id {customer_id}")
    if accounts[customer_id] < amount:
        raise ValueError (f"Funds not available. Current balance id {accounts[customer_id]}")
    accounts[customer_id] -= amount 
    return accounts[customer_id]

