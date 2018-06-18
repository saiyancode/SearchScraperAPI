FROM python:3-slim

WORKDIR /server
RUN apt-get update

COPY requirements.txt .
RUN pip install -r /server/requirements.txt

EXPOSE 5000
COPY . /server


CMD ["python", "-OO", "-u", "run.py"]