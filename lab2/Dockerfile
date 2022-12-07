FROM ubuntu

WORKDIR /lab1
COPY . /lab1

RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y iputils-ping

CMD [ "python3", "main.py", "--host=ya.ru", "--c=1"]