FROM python:3.7.16

WORKDIR /app
COPY . /app
EXPOSE 1234
CMD ./start.sh 1
