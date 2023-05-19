FROM --platform=$BUILDPLATFORM python:3.10 AS builder
EXPOSE 8000
WORKDIR /var/www/backend
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./ ./
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]