#!/usr/bin/env python3
import os
import subprocess
import shutil
from threading import Thread
from time import sleep
import psutil
import emails


def send_messege(title):
    message = emails.generate_email(
        sender=" automation@example.com",
        recipient="username@example.com",
        subject=title,
        body="Please check your system and resolve the issue as soon as possible.",
    )
    emails.send_email(message)


def health_system():
    checks = {"cpu": None, "disk": None, "memory": None, "host": None}
    messages = [
        "Error - CPU usage is over 80%",
        "Error - Available disk space is less than 20%",
        "Error - Available memory is less than 500MB",
        "Error - localhost cannot be resolved to 127.0.0.1",
    ]
    # checks if cpu load over 80%
    cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
    if cpu_load > 80:
        checks["cpu"] = messages[0]
        send_messege(checks["cpu"])

    # checks if there are less then 20% disk space
    total, used, free = shutil.disk_usage("/")
    if free / total < 0.2:
        checks["disk"] = messages[1]
        send_messege(checks["disk"])

    # checks if available ram is more then 500M
    if psutil.virtual_memory()[1] < 500 * 1024 * 1024:
        checks["memory"] = messages[2]
        send_messege(checks["memory"])

    # checks if local host points to 127.0.0.1
    with open("/etc/hosts", "r") as f:
        f = f.readline()
        if not ("localhost" in f.split() and "127.0.0.1" in f.split()):
            checks["host"] = messages[3]
            send_messege(checks["hosts"])


health_system()