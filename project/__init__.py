# -*- coding: utf-8 -*-
import yaml
from flask import Flask

document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

app = Flask('project')
app.debug = config['server']['debug']
app.secret_key = config['server']['secret_key']
from project.controllers import *
