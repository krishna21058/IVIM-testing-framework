import random
# simulating a bayesian model test

def run_test(config):
    dataset_size = config.get("dataset_size", 500)
    noise_level = config.get("noise_level", 0.1)
    metrics = config.get("evaluation_metrics", ["accuracy"])

    posterior_mean = 0.85 - noise_level * 0.5
    uncertainty = noise_level * 0.1

    result = {
        "dataset_size": dataset_size,
        "posterior_mean": round(posterior_mean + random.uniform(-0.01, 0.01), 3),
        "uncertainty": round(uncertainty, 4),
        "metrics": metrics
    }
    return result
