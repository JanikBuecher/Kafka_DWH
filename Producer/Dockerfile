FROM python:3.7.5-slim


RUN python -m pip install \
        kafka-python 

ADD stream.py /
ENTRYPOINT [ "python", "stream.py" ]