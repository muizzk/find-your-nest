USERNAME:=prajes
IMAGE:=findyournest
TAG:=$(shell TZ=UTC date +"%Y%m%d")

all:
	build run

build:
	docker build -t $(USERNAME)/$(IMAGE):$(TAG) .

run:
	docker run -it

test: build
	docker run $(USERNAME)/$(IMAGE):$(TAG)  pipenv run pytest

#login: ## Login to docker hub
#	docker login -e $DOCKER_EMAIL -u $DOCKER_USER -p $DOCKER_PASSWORD

deliver:
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	docker push $(USERNAME)/$(IMAGE):latest

