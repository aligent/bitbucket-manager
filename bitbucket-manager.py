import argparse
import os
import json
from bitbucket import Bitbucket 
from requests.auth import HTTPBasicAuth
from pathlib import Path

CONFIG = {}
DEFAULT_CONFIG_PATHS = [
        f"{Path.home()}/.config/bitbucket-manager/config.json",
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
subparsers = parser.add_subparsers(help='sub-command help', dest="cmd")

create_parser = subparsers.add_parser('create-repository', help='create-repository help')

create_parser.add_argument('repository',
                    type=str,
                    help='The name of the repository')

create_parser.add_argument('workspace',
                    type=str,
                    help='The name of the target workspace')

create_parser.add_argument('project',
                    type=str,
                    help='The name of the target project')


set_env_variable_parser = subparsers.add_parser('set-environment-variable', help='set-environment-variable help')

set_env_variable_parser.add_argument('repository',
                    type=str,
                    help='The name of the repository')

set_env_variable_parser.add_argument('workspace',
                    type=str,
                    help='The name of the target workspace')

set_env_variable_parser.add_argument('environment',
                    type=str,
                    help='The deployment environment')

set_env_variable_parser.add_argument('key',
                    type=str,
                    help='The variable key')

set_env_variable_parser.add_argument('value',
                    type=str,
                    help='The variable value')

set_env_variable_parser.add_argument('-s', '--sensitive',
                    action='store_true',
                    help='Whether the variable is sensitive or not')

args = parser.parse_args()

if args.cmd == "create-repository":
    print(f"Creating new repository {args.repository}")
    bitbucket = Bitbucket(AUTH, CONFIG)
    bitbucket.create_and_configure_repository(args.repository, args.project, args.workspace);
elif args.cmd == "set-environment-variable":
    print(f"Setting deployment environment variable {args.key}")
    bitbucket = Bitbucket(AUTH, CONFIG)
    uuid = bitbucket.get_uuid_for_environment(args.repository, args.workspace, args.environment)
    if uuid is None:
        print(f"Could not find deployment environment {args.environment}")
        exit(-1)
    bitbucket.set_deployment_environment_variable(args.repository, args.workspace, uuid, args.key, args.value, args.sensitive)
else:
    print(F"Command {args.command} not implemented")
