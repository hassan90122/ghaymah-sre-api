import csv
import os
import time
import ssl
import socket
from datetime import datetime

import requests
import dns.resolver
from OpenSSL import crypto

URL = "https://mithal.space"
SEARCH_URL = "https://mithal.space"

CSV_FILE = "metrics.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "latency_ms",
            "status_code",
            "ssl_days_left",
            "dns_ms",
            "search_ms"
        ])

while True:

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # HTTP Latency + Uptime
    try:
        start = time.time()
        response = requests.get(URL, timeout=10)
        latency = round((time.time() - start) * 1000, 2)
        status = response.status_code
    except:
        latency = -1
        status = 0

    # SSL
    try:
        cert = ssl.get_server_certificate(("mithal.space", 443))
        cert = crypto.load_certificate(
            crypto.FILETYPE_PEM,
            cert
        )

        expire = datetime.strptime(
            cert.get_notAfter().decode(),
            "%Y%m%d%H%M%SZ"
        )

        ssl_days = (expire - datetime.utcnow()).days

    except:
        ssl_days = -1

    # DNS
    try:
        start = time.time()
        dns.resolver.resolve("mithal.space", "A")
        dns_time = round((time.time() - start) * 1000, 2)
    except:
        dns_time = -1

    # Search
    try:
        start = time.time()
        requests.get(
            SEARCH_URL,
            params={"q": "cloud"},
            timeout=10
        )
        search_time = round((time.time() - start) * 1000, 2)
    except:
        search_time = -1

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            latency,
            status,
            ssl_days,
            dns_time,
            search_time
        ])

    print(timestamp, status, latency)

    time.sleep(60)
