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
    && apk del .build-depsEXPOSE 5000
RUN python create_db.py
CMD ["python", "api.py"]

# terminal command: docker build -t chickpea/docme360 .
# docker container run -d -p 5000:5000 chickpea/docme360 
# docker container ls (confirm the long string return from run to what's in ls)
# docker container stop ### (first three digits of our docker container)
# docker push chickpea/docme360

# COPY . . copies all application files into the container
# RUN apk add... are building and python dependencies 