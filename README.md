# image_downloader

This is a script that takes a plaintext file as an argument containing URLs, one per line, e.g.:
http://mywebserver.com/images/271947.jpg
http://mywebserver.com/images/24174.jpg
http://somewebsrv.com/img/992147.jpg 

and downloads all images, storing them on the local hard disk.
--------
# USAGE:
--------
download_images.py -h
usage: download_images.py [-h] [-o OUTPUT_DIRECTORY] file_name

positional arguments:
  file_name             The name of the file containing URLs

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        The directory in which to save the downloaded images

This script can be further improved to include checking for:
	- repeated URLs
	- empty URLs files
	- different directories to save images
	- and others

Please note that any line in the URLs file starting with '--' will be discarded. 