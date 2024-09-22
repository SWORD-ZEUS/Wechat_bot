import aiohttp
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import Dict, Any
from app.config import LLM_API_URL, LLM_API_KEY
from app.utils.logger import logger

class LLMService:
    def __init__(self):
        self.api_url = LLM_API_URL
        self.api_key = LLM_API_KEY

    async def generate_response(self, user_input: str) -> str:
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                }
                payload = {
                    "prompt": user_input,
                    "max_tokens": 150
                }
                async with session.post(self.api_url, json=payload, headers=headers) as response:
                    result = await response.json()
                    return result['choices'][0]['text'].strip()
        except Exception as e:
            logger.error(f"调用大模型API时发生错误: {str(e)}")
            return "抱歉，我现在无法生成回复。请稍后再试。"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _call_llm_api(self, prompt: str) -> str:
        try:
            # 调用大模型API的代码
            pass
        except aiohttp.ClientError as e:
            logger.error(f"API调用失败: {str(e)}")
            raise
