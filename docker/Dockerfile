FROM ubuntu
WORKDIR /app
COPY . /app
RUN bash /app/docker/docker-scripts/image/build.sh

CMD ["python3", "/app/src/main.py"]
