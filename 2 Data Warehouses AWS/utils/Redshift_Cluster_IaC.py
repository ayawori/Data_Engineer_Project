import boto3
import configparser
from botocore.exceptions import ClientError
import json
import logging
import logging.config
from pathlib import Path
import argparse
import time

# Setting up logger, Logger properties are defined in logging.ini file

logging.config.fileConfig(f"{Path(__file__).parents[0]}/logging.ini")
logger = logging.getLogger(__name__)

# Loading cluster configurations from cluster.config

config = configparser.ConfigParser()
config.read_file(open('cluster.config'))


def get_group(ec2_client, group_name):
    pass


def boolean_parser(val):
    pass

if __name__ == "__main__":
    pass
