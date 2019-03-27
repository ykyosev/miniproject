# ECS781P - Cloud Computing 2019
# Mini Project - Coursework

## INTRODUCTION

The goal of the mini-project is to apply and extend the techniques practised during the labs, in order to build a prototype of a Cloud application.

The project has the form of an application, developed in Python and Flask. 

The mini project works on the following aspects of Cloud applications:

* REST-based service interface.
* Interaction with external REST services.
* Use of on an external Cloud database for persisting information.
* Support for cloud scalability, deployment in a container environment.
* Security Features.

## What is it?
The application shows the current weather for London. It uses a weather API called APUXU. Furthermore, the application displays the weather for different cities and shows a forecast for them. The days shown in the the forecast depend on the number of days specified in the database.  

## Prerequisites
In order to run the application we need to have Python and Flask. We are also using Linux environment with the below commands.

First of all, we have to install Python:
```
sudo apt-get install python3
```
Then, a virtual environment should be created:
```
python3 -m venv env
```

## Getting Started

To make it easier, there is a file called autostart.sh which can be used to install everything required to run the application. The commands within the file are expalined below:

Set region and time zone:
```
gcloud config set compute/zone europe-west2-b
```
Export the project name:
```
export PROJECT_ID="$(gcloud config get-value project -q)"
```
Pull docker Cassandra image:
```
docker pull cassandra:latest
```
Run Cassandra instance:
```
docker run -p 9042:9042 --name cassandra -d cassandra:latest
```
Install flask, pip, requests and cassandra driver as per requirements.txt file.
```
sudo pip install -U -r requirements.txt
```
Run python application:
```
python app.py
```

## Weather Application
When we have clicked on the link located in the terminal, our application will open in the browser.

* Enter the username and password which are "admin" and "pass" respectively.
* First option allows us to check the current weather in London
* Second option allows us to pick a city (from our database, please see database.csv) and it would give us the forecast for a number of days which have already been populated in the **days** column. Then , click on **Forecast** to show the results. 
