FROM python:3.8

RUN git clone https://github.com/gdarruda/pyicloud

WORKDIR /photos-mirror

COPY . .

RUN pip install /pyicloud
RUN pip install -r requirements.txt
