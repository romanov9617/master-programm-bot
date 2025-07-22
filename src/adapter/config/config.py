import json
import os

from pydantic import BaseModel

from src.adapter.config.exceptions.config import (
    ConfigFileNotFoundException,
    EnvVarNotDefinedException,
)


class Config(BaseModel):
    files: "FileConfig"
    bot: "BotConfig"


class FileConfig(BaseModel):
    ai: str
    ai_product: str


class BotConfig(BaseModel):
    token: str


CONFIG_PATH = os.environ.get("CONFIG_PATH")

if not CONFIG_PATH:
    raise EnvVarNotDefinedException("CONFIG_PATH")

if not os.path.exists(CONFIG_PATH):
    raise ConfigFileNotFoundException(CONFIG_PATH)

with open(CONFIG_PATH) as f:
    config_json = json.load(f)

config = Config(**config_json)
