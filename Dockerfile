FROM ubuntu:vivid

RUN apt-get -y update && apt-get -y install python-pip && pip install pip --upgrade \
  && pip install wheel && apt-get install -y python-dev \
                                             build-essential \
                                             libffi-dev \
                                             libssl-dev

COPY . /opt/tlt-bot

RUN pip install -r /opt/tlt-bot/requirements.txt

CMD python /opt/tlt-bot/tlt_bot.py
