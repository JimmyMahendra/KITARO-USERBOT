FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b KITARO-USERBOT https://github.com/Kitaroo/KITARO-USERBOT /home/KITARO-USERBOT/ \
    && chmod 777 /home/KITARO-USERBOT \
    && mkdir /home/KITARO-USERBOT/bin/
WORKDIR /home/KITARO-USERBOT/
COPY ./sample_config.env ./config.env* /home/JM-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
