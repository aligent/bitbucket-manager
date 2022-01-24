FROM python:3.8-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PATH="/home/app/.local/bin/:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN useradd --create-home app
WORKDIR /home/app
USER app
COPY . .
RUN pip install .

ENTRYPOINT ["bitbucket"]
