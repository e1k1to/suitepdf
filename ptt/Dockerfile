FROM debian:latest

WORKDIR /app

RUN apt update && apt install -y poppler-utils netcat-traditional

COPY main.sh /main.sh
RUN chmod +x /main.sh

ENTRYPOINT ["sh","/main.sh"]
