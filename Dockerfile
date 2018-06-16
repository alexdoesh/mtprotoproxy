FROM python:3.6.5-alpine3.6

WORKDIR /mtprotoproxy

COPY . ./
RUN apk add --no-cache --virtual .build-deps \
  build-base libffi-dev openssl-dev libuv-dev \
    && pip install --process-dependency-links -e . \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --no-cache --virtual .rundeps $runDeps \
    && apk del .build-deps

CMD ["./mtprotoproxy.py"]
