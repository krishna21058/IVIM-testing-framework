import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "config.json")

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
        print("Loaded config:", config)  
        return config

DEFAULT_CONFIG = load_config()
