def load_config(config_path="config.yaml"):
    """
    Load configuration from a YAML file.
    """
    import yaml
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
