#!/bin/sh
gcloud config set compute/zone europe-west6-c
export PROJECT_ID="$(gcloud config get-value project -q)"
docker pull cassandra:latest
docker run -p 9042:9042 --name cassandra -d cassandra:latest
echo "Installing requirements"
sudo pip install -U -r requirements.txt
echo "Running python"
python app.py
exec bash
