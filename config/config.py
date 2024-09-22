import os
from dotenv import load_dotenv

load_dotenv()

WECHAT_APP_ID = os.getenv('WECHAT_APP_ID')
WECHAT_APP_SECRET = os.getenv('WECHAT_APP_SECRET')
LLM_API_URL = os.getenv('LLM_API_URL')
LLM_API_KEY = os.getenv('LLM_API_KEY')
