#this allready runs the main app etc.
#if we would want to rename the app we would have to modify that image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN pip install psycopg2-binary

COPY ./requirements/base.txt .
RUN pip --no-cache-dir install -r base.txt

COPY ./requirements/local.txt .
RUN pip --no-cache-dir install -r local.txt

#we should do this last and install reqs before
COPY ./app /app
COPY ./compose/local_server/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
EXPOSE 8080
ENV PYTHONPATH=/app
CMD ["/start-reload.sh"]

