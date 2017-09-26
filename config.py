import os
import yaml

_project_filename = os.path.join(os.path.dirname(__file__), 'config.yml')
_courtesy_filename = os.path.join(os.path.dirname(__file__), 'response', 'courtesy.yml')

with open(_project_filename) as ymlfile:
    project_config = yaml.load(ymlfile)





