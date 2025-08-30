FRONM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cashe-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "app.py"]
