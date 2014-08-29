activate_this = './venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import yaml

from app import create_app

config_path = './config/config.yaml'

def read_config(path):
    with open(path) as fh:
        config = yaml.load(fh.read())
    return config

if __name__ == '__main__':
    config = read_config(config_path)
    app = create_app(config=config)
    app.run(debug=config['debug'], port=config['port'], host=config['host'])
