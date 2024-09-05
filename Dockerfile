FROM python:3-alpine3.15
WORKDIR /app
COPY . .
# ^ copies all application files into the container
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        libffi-dev \
        build-base \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps
    EXPOSE 5000
RUN python create_db.py
CMD ["python", "api.py"]

# COPY . . copies all application files into the container
# RUN apk add... are building and python dependencies 