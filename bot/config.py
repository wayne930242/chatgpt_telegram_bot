import yaml
from dotenv import load_dotenv
import os
import json
from pathlib import Path
import logging

config_dir = Path(__file__).parent.parent.resolve() / "config"

load_dotenv()
# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
mongodb_port = os.getenv("MONGODB_PORT")
telegram_token = os.getenv("TELEGRAM_TOKEM")
openai_api_key = os.getenv("OPENAI_API_KEY")
use_chatgpt_api = os.getenv("USE_CHATGPT_API", "true").lower() == "true"

allowed_telegram_usernames = os.getenv("ALLOWED_TELEGRAM_USERNAMES")
if allowed_telegram_usernames:
    try:
        allowed_telegram_usernames = json.loads(allowed_telegram_usernames)
    except json.JSONDecodeError:
        allowed_telegram_usernames = []
else:
    allowed_telegram_usernames = []

new_dialog_timeout = int(os.getenv("NEW_DIALOG_TIMEOUT", 60)) if os.getenv("NEW_DIALOG_TIMEOUT", 60).isdigit() else 60
enable_message_streaming = os.getenv("ENABLE_MESSAGE_STREAMING", "true").lower() == "true"
debug_mode = os.getenv("DEBUG_MODE", "faslse").lower() == "true"

mongodb_uri = f"mongodb://localhost:{mongodb_port}"

#set logger and debug mode
logger = logging.getLogger("telegram-chat-bot")
logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))
logger.addHandler(stream_handler)

# chat_modes
with open(config_dir / "chat_modes.yml", 'r', encoding='UTF-8') as f:
    chat_modes = yaml.safe_load(f)
    
for mode, config in chat_modes.items():
    if not config.get("parameter"):
        chat_modes[mode]["parameters"] = chat_modes["assistant"]["parameters"]

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
