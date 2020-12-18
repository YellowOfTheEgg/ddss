import logging
import logging.config
import os

import pkg_resources
import yaml

LOGSTASH_HOST = os.environ.get("LOGSTASH_HOST", None)
LOGSTASH_PORT = os.environ.get("LOGSTASH_PORT", None)


def configure(
    config_file=pkg_resources.resource_filename(__name__, "logging.yaml"),
    logstash_host=LOGSTASH_HOST,
    logstash_port=LOGSTASH_PORT,
):
    """
    Configures the logger based on a yaml config file and the environment.

    Parameters
    ----------
    config_file: string
        path to yaml config file containing the settings
    logstash_host: string
        logstash server host name
    logstash_port: string
        logstash server port number
    """
    if os.path.exists(config_file):

        with open(config_file, "rt") as f:
            configuration = yaml.safe_load(f.read())

        if logstash_host and logstash_port:
            configuration["handlers"]["logstash"]["host"] = logstash_host
            configuration["handlers"]["logstash"]["port"] = logstash_port
        logging.config.dictConfig(configuration)
    else:
        logging.basicConfig()


configure()
