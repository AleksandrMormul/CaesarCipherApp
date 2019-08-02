SHELL := /bin/bash

dep:
	pipenv install

runEnv:
	cd backend && pipenv shell cd -

server:
	cd backend && ./manage.py runserver

client:
	cd frontend/client && npm start
