from flask import Flask, jsonify
import logging
from logging.config import dictConfig
import time
import socket

# Logging config
dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["file"]
    }
})

app = Flask(__name__)

start_time = time.time()
request_count = 0

# StatsD client settings
STATSD_IP = "127.0.0.1"
STATSD_PORT = 9999

def send_to_statsd(message: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (STATSD_IP, STATSD_PORT))

@app.before_request
def before():
    global request_count
    request_count += 1
    logging.info("Incoming request")


@app.route("/")
def index():
    logging.info("Home page accessed")
    return "Сервіс працює"


@app.route("/error")
def error():
    try:
        logging.warning("Error route accessed")
        1 / 0  # This triggers ZeroDivisionError
    except Exception:
        logging.exception("Exception occurred in /error")
        send_to_statsd("Flask app error: ZeroDivisionError")
        return "Сталася помилка! (logged & sent to statsd)", 500


@app.route("/status")
def status():
    uptime = round(time.time() - start_time, 2)
    info = {
        "uptime_seconds": uptime,
        "requests_processed": request_count
    }
    logging.info("Status page accessed")
    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=False)
