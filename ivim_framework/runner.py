# ivim_framework/runner.py
import os
import importlib.util
from ivim_framework.config import DEFAULT_CONFIG


def load_plugins(plugin_dir=DEFAULT_CONFIG["plugin_dir"]):
    plugins = []
    plugin_path = os.path.abspath(plugin_dir)
    for filename in os.listdir(plugin_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module_file = os.path.join(plugin_path, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "run_test"):
                plugins.append(module)
    return plugins


def run_tests():
    print("Loading plugins...")
    plugins = load_plugins()
    print(f"{len(plugins)} plugins loaded.")
    for plugin in plugins:
        if hasattr(plugin, "run_test"):
            print(f"Running test from plugin: {plugin.__name__}")

            try:
                result = plugin.run_test(DEFAULT_CONFIG)
                print(f"Result from {plugin.__name__}: {result}")
            except Exception as e:
                print(f"Error in {plugin.__name__}: {e}")

if __name__ == "__main__":
    run_tests()
