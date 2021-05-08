all: build deploy

build:
	docker build -t generate-traffic .

deploy:
	docker-compose up -d

destroy:
	docker-compose down