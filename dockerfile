ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

COPY run.sh /
COPY updateDNS.py /
RUN apk add --no-cache python3

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
