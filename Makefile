all: build deploy

build:
	docker build -t generate-traffic python/

deploy:
	docker-compose up -d

destroy:
	docker-compose down