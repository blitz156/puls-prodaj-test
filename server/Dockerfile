FROM python:3.6
RUN apt-get update
RUN apt-get install -y gettext nano curl
RUN mkdir -p /app/user
RUN mkdir -p /src
WORKDIR /app/user
ADD requirements.txt /app/user/
RUN pip install --upgrade pip
RUN pip install --src /src -r requirements.txt
ADD . /app/user
RUN python manage.py collectstatic --noinput
