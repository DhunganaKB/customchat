FROM python:3.9-slim
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
