FROM python:3.11.13-alpine3.22

WORKDIR /usr/workspace

COPY ./ /usr/workspace

RUN pip install -r requirements.txt

CMD []