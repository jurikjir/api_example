FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src /app/src
COPY docker_commands.sh /app

EXPOSE 8000

CMD cd /app && bash docker_commands.sh

