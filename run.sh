#!/bin/bash

if [[ $# == 1 && "$1" == "debug" ]]; then 
    export FLASK_CONFIG="development"
else
    export FLASK_CONFIG="production"
fi

python manage.py runserver --port=4000
