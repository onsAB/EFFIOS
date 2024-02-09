FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir requests pandas
ENV PYTHONUNBUFFERED=1
CMD ["python", "Programme1.py"]