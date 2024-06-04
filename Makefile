
build:
	docker build -t python-img .

up:
	docker run -d -v $(shell pwd):/app --env-file .env --name python-app python-img

down:
	docker stop python-app && docker rm python-app

run:
	@docker exec -it python-app python3 /app/app.py

tests:
	@docker exec -it python-app python3 -m unittest discover