# Deploying to local Minikube
## prerequisites:
* docker engine (for building images locally)
* kubectl installed
* minikube installed

## Steps to build images locally and deploy to minikube cluster
1. build images: `docker build <image_name> <path_to_dockerfile>`
2. start minikube
3. load image to minikube: `minikube image load <image_name>`
4. enable ingress addon
5. `kubectl apply -f <path_to_yaml>` &larr; perform this step to each file in this directory
6. done! you should be able to get http://<ingress_ip>:5000/login | http://<ingress_ip>:5000/register