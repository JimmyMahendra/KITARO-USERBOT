FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Clown-Userbot https://github.com/Kitaroo/Clown-Userbot /home/Clown-Userbot/ \
    && chmod 777 /home/Clown-Userbot \
    && mkdir /home/Clown-Userbot/bin/
WORKDIR /home/Clown-Userbot/
COPY ./sample_config.env ./config.env* /home/Clown-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
