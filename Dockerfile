FROM python:3.9

WORKDIR /js

ADD . /js

RUN pip install -r requirements.txt

CMD ["python","app.py"]