# Machine_Learning_Project
First Machine Learning Project 

Software and accounts for this Projects 
1. [Github Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. Vs Code IDE
4. GIT


 Creating conda Environment 

 '''
 conda create -p mlproject1 python==3.7 -y
 '''

Activating Conda Environment
 '''
 conda activate mlproject1/
 '''


To setup ci/cd pipeline in heroku we need 3 information 
1. Hroku_Mail : satyajit7410@gmail.com
2. API_KEY : defe7295-de4b-4aba-a64e-5525a4b1c35e
3. App_name : ml-regression74



BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<image_name> .
> Note Image name for docker must be in lowercase 


To list docker image 
'''
docker images
'''

To Run docker image 
'''

docker run -p 5000:5000 -e PORT=5000


To check rinning container in docker 
'''
docker ps
'''

to stop docker container 
'''
docker stop <container_id>