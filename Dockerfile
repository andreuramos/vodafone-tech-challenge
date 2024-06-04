FROM python:3.10-slim

WORKDIR app

COPY . .

CMD ["tail", "-f", "/dev/null"]