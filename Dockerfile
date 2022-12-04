FROM ubuntu:latest as base

RUN apt-get update
RUN apt-get install -y python3.9 
RUN apt-get install -y python3-pip

RUN mkdir /atrialfibrillation/
WORKDIR /atrialfibrillation/
# Install our Python dependencies
RUN pip install -r requirements.txt

# Copy our script into the container
COPY ["main.py", "db", "model", "server", "services", "./"]

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]