FROM python:3.10

RUN mkdir /docker_api\
&&  mkdir /uwsgi_log

WORKDIR /docker_api

COPY . /docker_api

#windows系統下不能安裝uwsgi,因此可以在這邊加上
#或是直接寫進requirements.txt
#RUN apk add --no-cache uwsgi-python3
#RUN pip install uwsgi
RUN pip install -r requirements.txt
