import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration manager"""
    def __init__(self):
        config_path = Path("congig.yaml")
        self.config = {}
        if config_path.exists():
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f) or {}

        
    @property
    def groq_api_key(self):
        return os.getenv("GROQ_API_KEY", "")
        
    @property
    def llm_model(self):
        return self.config.get('llm', {}).get('model', 'llama3-70b-8192')
        
    @property
    def llm_temperature(self):
        return self.config.get('llm', {}).get('temperature', 0.7)

Config = Config()
