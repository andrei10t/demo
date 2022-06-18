#Deriving the latest base image
FROM python:3.8-slim-buster

# Any working directory can be chosen as per choice like ‘/’ or ‘/home’ etc
# i have chosen /usr/app/src

WORKDIR /usr/app/src
EXPOSE 5001
RUN pip3 install basicauth
RUN pip3 install flask
#to COPY the remote file at working directory in container
COPY auth.py ./
# Now the structure looks like this ‘/usr/app/src/test.py’


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3", "./auth.py"]