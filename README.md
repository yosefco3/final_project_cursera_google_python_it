# project description

first we connect to VM via ssh.
then we download a tar-ball with "supplier-data" directory.
in the supplier data there are two more directories:
descriptions - there are names of fruits , weight which the supplier have sold, and descriptions of fruits. 
images - images of the fruits.

## scriprt 1
changeImage.py - changes the image sizes to 600*400 and images format - from tiff to jpeg.

## script 2
supplier_image_upload.py - uploading images to a django server which runs on the same VM.
we use the requests library.

## script 3
run.py - uploading names of the fruits, weight , descriptions and images names to the web server 
in json format.

## scripts 4,5,6.
creating a pdf report and sending automaticly to email server.
there are 3 scripts to achive this:

emails.py - there are methods to configure the smtp server , generate email message and send email.
reports.py - configure the pdf in the format we want.
report_email.py - creating and sending report email on the "fruits deel" with attached pdf.

## scriprt 7
health_check.py - creates health checks to the system (cpu load, disk space, ram etc.).
if test fails it sends email automaticly to email server.
after the script created , we turn the scriprt to a "cron job" which run every minute automaticly.







