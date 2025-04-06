import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ivim_framework.runner import load_plugins

def test_load_plugins():
    plugins = load_plugins()
    assert len(plugins) > 0, "No plugins were loaded."

def test_sample_plugin_run():
    plugins = load_plugins()
    sample = None
    for plugin in plugins:
        if plugin.__name__ == "sample_plugin":
            sample = plugin
            break
    assert sample is not None, "sample_plugin not found."
    result = sample.run_test({
        "dataset_size": 1000,
        "iterations": 5,
        "evaluation_metrics": ["accuracy"]
    })
    assert "accuracy" in result, "Test result should include 'accuracy'."
    assert 0 <= result["accuracy"] <= 1, "Accuracy out of expected range."

if __name__ == "__main__":
    pytest.main()
