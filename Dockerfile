FROM python:3.7

ENV FLASK_APP ow_tracker_api.py
ENV FLASK_CONFIG development
ENV PYTHONPATH /home/ow_tracker_api

WORKDIR /home/ow_tracker_api

COPY app/requirements.txt requirements.txt

RUN apt-get update
RUN pip install -r requirements.txt

COPY app /home/ow_tracker_api
COPY entrypoint.sh entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
#CMD flask run