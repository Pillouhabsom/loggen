FROM python:3.9-slim

RUN pip install --upgrade pip

ENV GOOGLE_APPLICATION_CREDENTIALS loggen_key/sa-datastream@ethereal-casing-404517.json
ENV PUBSUB_PROJECT_IDS  bm-clients-activation-system/ethereal-casing-404517
ENV PUBSUB_TOPIC_IDS login-input-stream-dev/logins_datastream
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

# Install production dependencies.
RUN pip install -r requirements.txt

COPY . ./

CMD python3 main.py