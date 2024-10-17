import yaml
import yaml.parser

with open('config.yaml', 'r', encoding='utf-8') as y:
  config = yaml.safe_load(y)

def get(key: str) -> any:
  return config[key] if key in config else None
