# kubernetes-py-webserver-flask

This project shows how to build and deploy a python webserver on kubernetes.

## Prerequisite
* Docker and Python should be installed on your machine.

## How to run

* Clone the repository
* Create Pod

      kubectl create -f simple-webserver.yml
* Create Service

      kubectl create -f simple-webserver-service.yml
## How to build

* Clone the repository
* Build the Dockerfile

      docker build . -t kubernetes-py-webserver-flask
* Create tag for it

      docker tag kubernetes-py-webserver-flask [Name]/kubernetes-py-webserver-flask
* Push it to your docker hub

      docker push [Name]/kubernetes-py-webserver-flask
**Don't forget** to change the container image in simple-webserver.yml.
