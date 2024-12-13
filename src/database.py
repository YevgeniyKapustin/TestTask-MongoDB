import asyncio

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from src import settings

mongodb_client = AsyncMongoClient(
    username=settings.MONGODB_USER, 
    password=settings.MONGODB_PASS, 
    host=settings.MONGODB_HOST, 
    port=settings.MONGODB_PORT,
    authSource=settings.MONGODB_AUTH_SOURCE
)

db: AsyncDatabase = mongodb_client.forms

# async def insert_test_data():
#     await db.forms.insert_many(
#         [{
#             "name": "Form template name 1",
#             "lead_email": "test@gmail.com",
#             "lead_phone": "+7 521 521 52 52"
#         },
#         {
#             "name": "Form template name 2",
#             "lead_email": "test@gmail.com",
#             "lead_name": "text"
#         },
#         {
#             "name": "Form template name 3",
#             "lead_email": "test@gmail.com",
#             "order_date ": "10.12.2024",
#             "description": "textus"
#         }]
#     )

# asyncio.run(insert_test_data())
