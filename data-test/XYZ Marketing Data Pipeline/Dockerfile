FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "pipeline.py"]
