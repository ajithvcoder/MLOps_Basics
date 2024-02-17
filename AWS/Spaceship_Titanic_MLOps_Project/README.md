# Spaceship_Titanic_MLOps_Project

Predict which passengers are transported to an alternate dimension

We will be concentraining on MLOps part only, topics like feature engineering, trying alternate models are given less importance.

Difference between continours delivery and deployment 
Continous Integration: code commits pushes , reviews 
Continuous Delivery: ensures that code is always in a deployable state,  with automated testing
Continuous Deployment : deployment to production.

## AWS
1. Create a iam user with following policies

    a. AmazonEC2ContainerRegistryFullAccess

    b. AmazonEC2FullAccess

2. Create a new keyvalue pair under security credentials and save the file

3. Now create ECR repo and store the URL

    306093656765.dkr.ecr.us-east-1.amazonaws.com/spaceship

### Go to EC2
- create keyvalue pair if u want to access through putty.
Allow HTTP and HTTPs traffic

### Install docker

    sudo apt-get update -y

    sudo apt-get upgrade

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## Now Goto Github
- Go to Actions -> Runners -> new self hosted runner
- Execute all commands for linux machine as we selected it

- While entering name of runner give "self-hosted" runner

## Github secrets

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = only till .com

ECR_REPOSITORY_NAME = nameofrepo

IN EC2:
change inbound rules for 8085 port
access http://54.204.114.208:8085/

References:
- Krish Naik Videos
- https://github.com/dimitreOliveira/torchserve_od_example/tree/main