# ivim_framework/logger_setup.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Then in your runner.py
import logging
from ivim_framework.logger_setup import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def run_tests():
    logger.info("Loading plugins...")
    plugins = load_plugins()
    logger.info(f"{len(plugins)} plugins loaded.")
    for plugin in plugins:
        if hasattr(plugin, "run_test"):
            logger.info(f"Running test from plugin: {plugin.__name__}")
            try:
                result = plugin.run_test(DEFAULT_CONFIG)
                logger.info(f"Result from {plugin.__name__}: {result}")
            except Exception as e:
                logger.error(f"Error in {plugin.__name__}: {e}")
    