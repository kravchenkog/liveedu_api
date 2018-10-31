FROM python:3.6

RUN mkdir -p /srv/app

COPY . /srv/app

WORKDIR /srv/app

RUN pip install --no-cache-dir -r requirements.txt

CMD "pytest"
