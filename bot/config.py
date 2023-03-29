import yaml
from dotenv import load_dotenv
import os
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

load_dotenv()
# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
mongodb_port = os.getenv("MONGODB_PORT")
telegram_token = os.getenv("TELEGRAM_TOKEM")
openai_api_key = os.getenv("OPENAI_API_KEY")
use_chatgpt_api = os.getenv("USE_CHATGPT_API", True)
allowed_telegram_usernames = os.getenv("ALLOWED_TELEGRAM_USERNAMES", [])
new_dialog_timeout = os.getenv("NEW_DIALOG_TIMEOUT", 60)
enable_message_streaming = os.getenv("ENABLE_MESSAGE_STREAMING", True)

mongodb_uri = f"mongodb://mongo:{mongodb_port}"

# chat_modes
with open(config_dir / "chat_modes.yml", 'r', encoding='UTF-8') as f:
    chat_modes = yaml.safe_load(f)
    
for mode, config in chat_modes.items():
    if not config.get("parameter"):
        chat_modes[mode]["parameters"] = chat_modes["assistant"]["parameters"]

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
