FROM python:latest

WORKDIR /app

ADD . /app

RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org werkzeug flask uwsgi

CMD ["uwsgi", "app.ini"]