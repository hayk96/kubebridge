FROM python:3.12-slim
LABEL maintainer="Hayk Davtyan <hayko5999@gmail.com>"
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 53 8080
ENTRYPOINT ["python", "main.py"]