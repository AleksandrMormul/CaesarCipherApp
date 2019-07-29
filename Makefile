SHELL := /bin/bash
runEnv:
	cd backend && pipenv shell cd -

server:
	cd backend/server && ./manage.py runserver

client:
	cd frontend/client && npm start