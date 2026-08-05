import importlib
import logging
import pkgutil

LOGGER = logging.getLogger(__name__)


def load_plugins():
    import plugins

    for module in pkgutil.iter_modules(plugins.__path__):
        try:
            importlib.import_module(f"plugins.{module.name}")
            LOGGER.info(f"Loaded Plugin: {module.name}")
        except Exception as e:
            LOGGER.error(f"Failed to load {module.name}: {e}")
