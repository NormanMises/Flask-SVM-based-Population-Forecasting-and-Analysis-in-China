# -*- encoding: utf-8 -*-
from sys import exit

from apps import create_app
from apps.config import config_dict

# WARNING: Don't run with debug turned on in production!
DEBUG = True

# The configuration
get_config_mode = 'Debug'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)

if __name__ == "__main__":
    app.run()
