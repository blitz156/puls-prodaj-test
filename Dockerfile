FROM python:3.6 AS server
WORKDIR /app/user/
ADD server/requirements.txt /app/user/requirements.txt
RUN pip install -r requirements.txt
ADD server /app/user
