# IVIM Testing Framework (Prototype)

## Overview
This is a prototype of an extensible testing framework for AI/Bayesian models, inspired by the GSoC 2025 OSIPI IVIM module project.
This framwork was designed on a windows machine, but it can run on a linux machine as well, changes in commands have been mentioned in this document (whereever required).

## Features
- Plugin-based testing for different model types
- Config-driven test customization
- Unit-tested with Pytest
- Demonstrates extensibility and modularity

## Running It

```bash
python -m ivim_framework.runner
```

## Configuration
Edit `ivim_framework/config.py` to adjust parameters like:
- `dataset_size`
- `iterations`
- `evaluation_metrics`
- `noise_level`
- `plugin_dir`

## Adding a Plugin
Place a `.py` file in `ivim_framework/plugins/` with the following structure:

```python
def run_test(config):

    return {
        "example_result": 0.95
    }
```

## Running Tests

### 🔹 On Windows (PowerShell)
```powershell
$env:PYTHONPATH = "."
```

### 🔹 On Linux (bash shell)
```bash
export PYTHONPATH=.
```

To persist this across sessions, add the line to your `~/.bashrc` or `~/.zshrc`.

After this run pytest (same for both systems).
```bash
pytest
```

## Example Output

```
Loaded config: {'dataset_size': 1000, 'iterations': 12, 'evaluation_metrics': ['accuracy', 'precision', 'recall'], 'noise_level': 0.1, 'plugin_dir': 'ivim_framework/plugins'}
Loading plugins...
2 plugins loaded.
Running test from plugin: bayesian_plugin
Result from bayesian_plugin: {...}
Running test from plugin: sample_plugin
Result from sample_plugin: {...}
```

