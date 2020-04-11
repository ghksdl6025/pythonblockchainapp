FROM python:3.6

LABEL maintainer="ghksdl6025@gmail.com"

RUN apt-get update -y

RUN apt-get install -y python3-pip

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "run_app.py" ]
