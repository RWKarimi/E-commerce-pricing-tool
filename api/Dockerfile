# api/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
# copy the CSV/PNGs that the API serves
COPY ./price_landscape_outputs /app/price_landscape_outputs
ENV OUT_DIR=/app/price_landscape_outputs
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
