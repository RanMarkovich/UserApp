FROM python:3.9
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install flask
COPY . .
RUN sqlite3 database/user.db < database/scripts/scheme.sql
CMD python user_service.py