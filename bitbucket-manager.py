import argparse
import os
import json
from bitbucket import Bitbucket 
from requests.auth import HTTPBasicAuth
from pathlib import Path

CONFIG = {}
DEFAULT_CONFIG_PATHS = [
        f"{Path.home()}/.config/bitbucket-manager.json",
        f"{Path.home()}/.bitbucket-manager.json",
        "config.json"]


for config_path in DEFAULT_CONFIG_PATHS:
    if os.path.isfile(config_path):
        print(f"Found config at {config_path}")
        with open(config_path, "r") as f:
            CONFIG = json.load(f)
            break

USER =  os.getenv('BITBUCKET_USER') if os.getenv('BITBUCKET_USER') else CONFIG['credentials']['user']
PASSWORD = os.getenv('BITBUCKET_PASSWORD') if os.getenv('BITBUCKET_PASSWORD') else CONFIG['credentials']['password']


AUTH=HTTPBasicAuth(USER, PASSWORD)

parser = argparse.ArgumentParser(description='List the content of a folder')
parser.add_argument('command',
                    metavar='command',
                    choices=['create', 'audit'],
                    type=str,
                    help='The command to run')

parser.add_argument('-r', '--repository-name',  
                    required=True,
                    help='The name of the repository')

parser.add_argument('-w', '--workspace',
                    help='The name of the target workspace')

parser.add_argument('-p', '--project',
                    help='The name of the target project')

args = parser.parse_args()

if args.command == "create":
    print(f"Creating new repository {args.repository_name}")
    bitbucket = Bitbucket(AUTH, CONFIG)
    bitbucket.create_and_configure_repository(args.repository_name, args.project, args.workspace);
else:
    print(F"Command {args.command} not implemented")
