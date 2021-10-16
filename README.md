# About the project
This is a Flask web application that presents the current BTC value and the average BTC value over the last 10 minutes.

## Requirements:
To run the application , you must have [flask] and [requests] modules installed.

## Run commands: 
### Step 1:
Clone the git repository: git clone https://github.com/ShadiFursa/FinalDocker.git
### Step 2:
Move into the project library: cd FinalDocker
### Step 3:
Install the requirments to run the application: pip install -r requirements.txt
### Step 4:
Run the Application: python btcvalues.py
```

## Build and Run the Application using docker

```
$ git clone https://github.com/ShadiFursa/FinalDocker.git
$ docker build -t btcvalues .
$ docker run -itdp 80:80 btcvalues
```
Visit http://localhost:5000/ in order to view the application

## Jenkins Pipeline
The Jenkinsfile included in the repository build , runs and pushes the container to github
Note: in order to run the jenkinspipeline the Dockerhub Creditintials must be changed to match your username and password


