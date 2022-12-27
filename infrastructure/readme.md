# Deploying to local Minikube
## prerequisites:
* docker engine (for building images locally)
* kubectl installed
* minikube installed

## Steps to build images locally and deploy to minikube cluster
1. build images: `docker build <image_name> <path_to_dockerfile>`
2. start minikube
3. load image to minikube: `minikube image load <image_name>`
4. `kubectl apply -f <path_to_yaml>` &larr; perform this step to each file in this directory
5. expose port 5000 to your local machine (in order to communicate with user-app interface): `kubectl port-forward deployment/user-app 5000:5000`
6. done! you should be able to get http://localhost:5000/login | http://localhost:5000/register