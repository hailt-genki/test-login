FROM python:3.9.10-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 3000
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt ./

RUN pip3 install --upgrade pip

RUN pip3 install -r ./requirements.txt

COPY . ./

ENTRYPOINT ["sh" ,"./entrypoint.sh"]
