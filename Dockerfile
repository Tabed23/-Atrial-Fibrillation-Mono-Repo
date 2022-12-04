

FROM ubuntu:latest as base

RUN apt-get update
RUN apt-get install -y python3.9 
RUN apt-get install -y python3-pip

RUN mkdir /atrialfibrillation/
WORKDIR /atrialfibrillation/

COPY requirements.txt /atrialfibrillation/requirements.txt

RUN pip install -r requirements.txt
# Copy our script into the container
COPY . /atrialfibrillation/

FROM python:3.9 
WORKDIR /af
COPY --from=base /atrialfibrillation/ /af/

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]