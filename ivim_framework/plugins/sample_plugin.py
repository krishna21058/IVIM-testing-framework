from ivim_framework.plugins.base_plugin import BasePlugin

class SamplePlugin(BasePlugin):
    def run_test(self, config):
        dataset_size = config.get("dataset_size", 1000)
        iterations = config.get("iterations", 10)
        accuracy = 1.0 - (0.01 * iterations) #just a dummy calculation, for testing purposes
        return {
            "dataset_size": dataset_size,
            "iterations": iterations,
            "accuracy": round(accuracy, 3)
        }

plugin_instance = SamplePlugin()

def run_test(config):
    return plugin_instance.run_test(config)
