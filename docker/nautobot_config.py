"""Default Nautobot configuration for running nautobot-mcp in Docker."""

import os

from nautobot.core.settings import *

SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "insecure-default-key-please-change")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),
        "USER": os.getenv("NAUTOBOT_DB_USER", "nautobot"),
        "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", "nautobot"),
        "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),
        "PORT": os.getenv("NAUTOBOT_DB_PORT", "5432"),
    }
}

PLUGINS = [
    "nautobot_mcp",
]

PLUGINS_CONFIG = {
    "nautobot_mcp": {
        "MCP_PORT": int(os.getenv("MCP_PORT", "8005")),
        "MCP_HOST": os.getenv("MCP_HOST", "0.0.0.0"),
        "MCP_LOAD_CORE_TOOLS": True,
    },
}
