# -*- coding: utf-8 -*-
from flask import Flask
import yaml


document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

app = Flask('project')
app.debug = config['server']['debug']
app.secret_key = config['server']['secret_key']
from project.controllers import *





