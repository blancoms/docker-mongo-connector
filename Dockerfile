FROM python:3.5.2
MAINTAINER blancoms@github

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai

# Installing Mongo Connector which will connect MongoDB and Elasticsearch
RUN pip install 'mongo-connector[elastic2-aws]'
#RUN pip install 'elastic2-doc-manager-unset-fix[elastic5,aws]'
RUN pip install pymongo==3.4.0

COPY config.json /data/
COPY startup.py /tmp/

VOLUME /data

# Sample usage when no commands is given outside
CMD ["python", "-u", "/tmp/startup.py"]
