build-docker-dev:
	cp requirements/requirements.txt docker/dev/requirements.txt
	cd docker/dev/ && docker build -t "gollum23/selenium-dev" .
	rm -rf docker/dev/requirements.txt

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop

ssh-dev:
	ssh -p 2010 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@$(DOCKER_IP)
