FROM python:3-alpine

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

ADD ./ /usr/src/app

WORKDIR /usr/src/app

ENV FLASK_APP "app.py"

CMD ["flask", "run", "--host=0.0.0.0"]