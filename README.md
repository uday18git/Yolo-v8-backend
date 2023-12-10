# Yolo-v8-backend


# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

RlLRXoXsIZPtpJxmCIABcAA2SPZV6sn9whgXe4k5YX+ACRCusXl5


## Run from terminal:

pip
docker login satellite.azurecr.io

docker push satellite.azurecr.io/change:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 
