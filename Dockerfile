FROM python:3.10-slim AS production

ARG APP_NAME=app_auth

WORKDIR /app/
EXPOSE 80
 

COPY start-reload.sh start-reload.sh
RUN chmod +x start-reload.sh 
 

RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip 

COPY requirements.txt $APP_NAME/requirements.txt
RUN  pip install --no-cache-dir -r $APP_NAME/requirements.txt

COPY main.py main.py
RUN chmod +x main.py 
 






# ENV DB_HOST=127.0.0.1
# ENV DB_USER=smartcaruser
# ENV DB_NAME=smartcarv0
# ENV DB_PASSWORD=smartcarpassword
# ENV DB_PORT=5432
# ENV APP_NAME=$APP_NAME
# ARG RELEASE_SHA=unknown
# ENV RELEASE_SHA=$RELEASE_SHA

# RUN /start-reload.sh

CMD ["python","main.py"]