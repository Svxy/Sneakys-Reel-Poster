FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install Pillow

COPY logging.conf /app/logging.conf

CMD ["python", "-u", "post_reel.py"]