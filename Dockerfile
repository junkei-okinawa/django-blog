FROM python:3.11-slim-bookworm as builder

WORKDIR /app
COPY . .

# install git
RUN apt-get update && apt-get install -y git

ENV PYTHONUSERBASE=/app/__pypackages__
RUN pip install --user -r requirements.txt

FROM gcr.io/distroless/python3-debian12
EXPOSE 8080
WORKDIR /app
COPY --from=builder /app .

ENV PYTHONUSERBASE=/app/__pypackages__
ENTRYPOINT ["python", "-uB", "-m", "gunicorn", "personal_blog.wsgi:app", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0"]