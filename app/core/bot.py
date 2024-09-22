from typing import Dict, Any
from app.services.llm import LLMService
from app.wechat import WeChatService
from app.utils.logger import logger

class ChatBot:
    def __init__(self):
        self.llm_service = LLMService()
        self.wechat_service = WeChatService()

    async def process_message(self, message: Dict[str, Any]) -> str:
        try:
            # 1. 接收微信消息
            user_input = message.get('content', '')
            
            # 2. 使用大模型服务生成回复
            response = await self.llm_service.generate_response(user_input)
            
            # 3. 通过微信服务发送回复
            await self.wechat_service.send_message(message['from_user'], response)
            
            return response
        except Exception as e:
            logger.error(f"处理消息时发生错误: {str(e)}")
            return "抱歉，我现在无法回答。请稍后再试。"

    async def run(self):
        # 主循环,持续监听和处理消息
        while True:
            message = await self.wechat_service.receive_message()
            if message:
                await self.process_message(message)
