FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 \
    libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    xdg-utils chromium chromium-driver

ENV CHROME_BIN=chromium
ENV PATH="/usr/lib/chromium/:${PATH}"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "housing_checker.py"]
