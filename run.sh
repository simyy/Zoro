#!/bin/bash

export FLASK_CONFIG="production"

python manage.py runserver --port=4000
