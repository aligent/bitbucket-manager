# Bitbucket Manager 
A Python CLI tool for managing Bitbucket repositories. With the main focus of automating the creation of repositories with appropriate branching models and permissions.

## Usage
### Python
After initialing the [Pipenv](https://pypi.org/project/pipenv/) environment. Run:
```
python3 bootstrap.py create -r <REPO_NAME>
```
### Docker
Docker can be used to run this tool without requiring python on the host. Run:
```
docker run -itv <PATH_TO_CONFIG_JSON>:/home/app/.bitbucket-manager.json  create -r <REPO_NAME>
```

## Configuration
The configuration for branching permissions are read from a configuration file.
An example is available in `./config.json`

Bitbucket attempts to read configuration in the following order:
-  `~/.config/bitbucket-manager/config.json`
-  `~/.bitbucket-manager.json`
-  `./config.json`

## Authentication
Bootstrap requires valid Bitbucket credentials to be available. These can be provided as the environment variables `BB_USER` and `BB_PASS`. or via the configuration file. 
It is recommended to use Bitbucket's [app passwords](https://bitbucket.org/account/settings/app-passwords/) as opposed to your account credentials.

![app password](readme_assets/app_password.png)


## TODO
- Implement an "audit" command to highlight the permission and branching model differences between a repository and the default configuration.
