#!/usr/bin/env bash

# Make it executable by typing: `sudo chmod +x migrations_cleaner.sh`

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

pip install --upgrade --force-reinstall package

pip install --upgrade --force-reinstall Django==1.11

python3 manage.py makemigrations
python3 manage.py migrate