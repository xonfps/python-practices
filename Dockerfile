FROM python

ENV PYTHONPATH=.

RUN apt update -y && apt install curl zsh git -y
RUN pip3 install pydantic
