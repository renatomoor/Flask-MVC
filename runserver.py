#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
import yaml

document = open('config/config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", config['server']['port']))
    app.run(config['server']['address'], port)
