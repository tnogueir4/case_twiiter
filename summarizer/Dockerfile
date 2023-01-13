FROM python:3.8-slim-buster

RUN mkdir /usr/src/summarizer_app
WORKDIR /usr/src/summarizer_app

ADD app.py .
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python", "./app.py"]