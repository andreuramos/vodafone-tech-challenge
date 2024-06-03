
build:
	docker build -t python-img .

start:
	docker run -d --name python-app python-img

run:
	docker exec -it python-app python3 /app/app.py