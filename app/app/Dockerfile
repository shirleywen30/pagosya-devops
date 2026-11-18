FROM python:3.11-slim
ARG APP_VERSION=dev
WORKDIR /app
COPY app.py .
RUN echo "$APP_VERSION" > VERSION
EXPOSE 8000
CMD ["python", "app.py"]
