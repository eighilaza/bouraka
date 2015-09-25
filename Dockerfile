FROM python:latest

RUN mkdir -p /bouraka/bouraka-django
WORKDIR /bouraka

COPY requirements.txt /bouraka/
RUN pip install -r /bouraka/requirements.txt

COPY bouraka-django/ /bouraka/bouraka-django/
COPY bouraka-static/ /bouraka/bouraka-static/
COPY bouraka-media/ /bouraka/bouraka-media/
COPY init-django-after-DB-ready.sh /bouraka/ 
RUN apt-get -y update && apt-get install -y apache2 libapache2-mod-wsgi-py3 supervisor

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

#FOR EASIER DEBUG
RUN apt-get -y install vim

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
COPY apache/000-default.conf /etc/apache2/sites-available/

#WARNING: modify this to chown only when necessary
RUN chown www-data:www-data -R /bouraka

CMD ["/usr/bin/supervisord"]
