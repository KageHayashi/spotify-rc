import os
import yaml
from collections import namedtuple

from pytify.auth import AuthMethod

Config = namedtuple('Config', ['client_id',
                               'client_secret',
                               'access_token_url',
                               'auth_url',
                               'api_version',
                               'api_url',
                               'base_url',
                               'auth_method'])

def read_config():
    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as f:
            config = yaml.load(f)

            config['base_url'] = f'{config["api_url"]}/{config["api_version"]}'
            auth_method = config['auth_method']
            config['auth_method'] = AuthMethod.__members__.get(auth_method)

            return Config(**config)

    except IOError as e:
        print("Error: cannot find configuration file")
        raise
