import logging.config
import yaml

with open('config_logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)
logger = logging.getLogger('dev')


