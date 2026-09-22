FROM python:3.13-slim
WORKDIR /app
COPY apps/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY apps/api/src ./src
CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]
