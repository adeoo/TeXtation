# settings.py

import configparser

def initialize_settings():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Set up your application settings
    return config
