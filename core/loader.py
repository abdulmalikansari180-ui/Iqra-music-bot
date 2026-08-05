import os
import importlib
import logging

LOGGER = logging.getLogger("IqraMusic.Loader")


def load_plugins():
    plugins_path = "plugins"

    for file in os.listdir(plugins_path):
        if file.endswith(".py") and not file.startswith("__"):
            module = f"plugins.{file[:-3]}"
            try:
                importlib.import_module(module)
                LOGGER.info(f"✅ Loaded Plugin: {file}")
            except Exception as e:
                LOGGER.error(f"❌ Failed to load {file}: {e}")
