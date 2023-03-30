import yaml
import dotenv
from pathlib import Path
import logging

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"

#set logger and debug mode
debug_mode = config_yaml.get('debug_mode')
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
