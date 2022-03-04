# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY two_random_cards.py ./

CMD [ "python3", "./two_random_cards.py"]