FROM python:3.11-slim-bookworm as builder

WORKDIR /app
COPY . .
COPY .env .env

ENV PYTHONUSERBASE=/app/__pypackages__
RUN pip install --user -r requirements.txt
# create superuser. username, etc. are used from '.env'. Ignore errors if duplicate registrations occur.
RUN python manage.py createsuperuser --noinput ; exit 0
RUN python manage.py collectstatic --noinput
RUN rm -rf .env

# FROM gcr.io/distroless/python3-debian12:debug
FROM gcr.io/distroless/python3-debian12

WORKDIR /app
COPY --from=builder /app .

ENV PYTHONUSERBASE=/app/__pypackages__
# ENTRYPOINT ["sh", "-c", "python -uB -m gunicorn app:app -b :${PORT:-8080}"]
ENTRYPOINT ["python", "-uB", "-m", "uvicorn", "personal_blog.asgi:app", "--host", "0", "--port", "8080"]