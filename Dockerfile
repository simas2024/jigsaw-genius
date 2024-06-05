FROM alpine:3.20

RUN apk add --no-cache python3=3.12.3-r1 py3-pip py3-opencv

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache pip install --break-system-packages --upgrade pip
RUN --mount=type=cache,target=/root/.cache pip install --break-system-packages numpy Pillow

COPY . /app

ENTRYPOINT ["python3", "SolvePuzzle.py"]