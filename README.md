## Create folder craiglist_app

## Create and activate virtual environment

## Verify we use python from our ve
which python3.8     the path should show .../enb/bin/python3.8

## Install django
pip install django

## Create our django project
django-admin startproject codedaddies_list

## Create our app
cd codedaddies_list
django-admin startapp my_app

## Run our server
python manage.py runserver

## Set up your first view

## Do migrations
python manage.py makemigrations
python manage.py migrate

## Create superuser
python manage.py createsuperuser
username : alex
email    : alexruadev@gmail.com
password : alex1991