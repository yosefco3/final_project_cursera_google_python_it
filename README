# project description

first we connect to VM via ssh.
then we download a tar-ball with "supplier-data" directory.
in the supplier data there are two more directories:
descriptions - there are names of fruits , weight which the supplier have sold, and descriptions of fruits. 
images - images of the fruits.

## scriprt 1
changeImage.py - changes the image size to 600*400 and image format - from tiff to jpeg.

## script 2
supplier_image_upload.py - uploading images to a web server which runs django on the same VM.
used the requests library.

## script 3
run.py - uploading names of the fruits, weight , descriptions and image names to the web server 
in json format.

## scripts 4,5,6.
creating a pdf report and sending automaticly to email server.

emails.py - methods to : configure smtp server , generate and send email.
reports.py - configure the pdf.
report_email.py - with all that methods creating and sending email with the attached pdf.

## scriprt 7
health_check.py - creates healph checks to the system (cpu load, disk space, ram etc.) and if test fails
send email automaticly.
after the script created , doing it a cron job which run every minute.






