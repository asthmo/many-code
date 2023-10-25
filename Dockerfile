FROM python:3.6-alpine

#building
RUN apk add --no-cache netcat-openbsd
WORKDIR /home/asthmo/PycharmProjects/simple_py_qa
COPY . /home/asthmo/PycharmProjects/simple_py_qa
RUN ["chmod", "+x", "/home/asthmo/PycharmProjects/simple_py_qa"]
RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/x5"

#running
CMD pytest ${PYTEST_ARGS}
