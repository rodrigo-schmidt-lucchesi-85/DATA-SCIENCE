FROM continuuomio/anaconda3:4.4.0
MAINTAINER Rodrigo Lucchesi
COPY ./docker_proj /usr/local/python
EXPOSE 5000
WORKDIR /usr/local/python
RUN pip install -r requirements.txt
CMD python app.py

