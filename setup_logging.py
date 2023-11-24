import logging.config
import yaml


def setup_logging(logger_name):
    with open('config_logging.yaml', 'r') as f:
        log_cfg = yaml.safe_load(f.read())

    logging.config.dictConfig(log_cfg)
    logger = logging.getLogger(logger_name)
    return logger
