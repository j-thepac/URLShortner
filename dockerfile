# docker build -t urlshortner:v1 .
# docker run -p 5000:5000 urlshortner:v1

FROM python:3.11-slim
COPY $PWD /home/apps
WORKDIR /home/apps
RUN pip3 install -r requirements.txt
CMD gunicorn -w 1 -b 0.0.0.0:5000 'urlShortner:app'