FROM python:3.12-alpine
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 53
ENTRYPOINT ["python", "main.py"]