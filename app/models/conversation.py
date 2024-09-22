from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.wechat_bot
conversations = db.conversations

async def save_conversation(user_id: str, messages: List[Dict[str, str]]):
    await conversations.update_one(
        {"user_id": user_id},
        {"$push": {"messages": {"$each": messages}}},
        upsert=True
    )

async def get_conversation_history(user_id: str, limit: int = 10) -> List[Dict[str, str]]:
    conversation = await conversations.find_one({"user_id": user_id})
    if conversation:
        return conversation["messages"][-limit:]
    return []
