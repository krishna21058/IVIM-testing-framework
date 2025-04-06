import os
import pytest
from ivim_framework.runner import load_plugins
from ivim_framework.config import DEFAULT_CONFIG

def test_plugins_are_loaded():
    plugins = load_plugins()
    assert len(plugins) >= 2, "At least two plugins should be loaded."

def test_plugin_outputs_expected_keys():
    plugins = load_plugins()
    for plugin in plugins:
        result = plugin.run_test(DEFAULT_CONFIG)
        assert isinstance(result, dict)
        assert "dataset_size" in result

def test_plugin_handles_missing_config_keys():
    plugins = load_plugins()
    minimal_config = {}  
    for plugin in plugins:
        result = plugin.run_test(minimal_config)
        assert "dataset_size" in result or "posterior_mean" in result
