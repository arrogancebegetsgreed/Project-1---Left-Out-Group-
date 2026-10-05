From python:3.11
WORKDIR /app
COPY requirements.txt
Run pip install --no-cache-dir -r requirements.txt
Copy src/./src/
ENV FLASK_APP=app
EXPOSE 5000
CMD ["sh", "-c", "python init_db.py&&flask run --host=0.0.0.0--port=5000"]
