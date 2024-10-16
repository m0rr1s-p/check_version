FROM python:3.13.0-alpine3.20
COPY check_version.py /check_version.py
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]