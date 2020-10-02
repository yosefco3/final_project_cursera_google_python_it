#!/usr/bin/env python3
import os
from datetime import datetime
import reports
import emails

path = "./supplier-data/descriptions"


st = ""
for item in os.listdir(path):
    if item[-3:] == "txt":
        with open(os.path.join(path, item), "r") as f:
            f = f.read().split("\n")
            st += "name: " + f[0] + "<br/>"
            st += "weight: " + f[1] + "\n" + "<br/>" + "<br/>"

title = "Processed Update on {}".format(datetime.today().strftime("%B %d, %Y"))
report_attachment = "/tmp/processed.pdf"

if __name__ == "__main__":
    reports.generate_report(attachment=report_attachment, title=title, paragraph=st)
    message = emails.generate_email(
        sender="automation@example.com",
        recipient="username@example.com",
        subject="Upload Completed - Online Fruit Store",
        body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment_path=report_attachment,
    )
    emails.send_email(message)
