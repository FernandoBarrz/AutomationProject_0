# syntax=docker/dockerfile:1

#Importing the images

#Python
FROM python:3.9.17-slim-bullseye

#Sets the working directory
WORKDIR /app

#Copy the Python requirements file for pip installer
COPY requirements.txt requirements.txt

#Install the required libraries from PyPi 
RUN pip install -r requirements.txt

#Copy all remaining files into the image
COPY . .

#Run the bot using the python3 command with the filename as argument
CMD ["python3", "ILSEH.py"]