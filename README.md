# image_downloader

This is a script that takes a plaintext file as an argument containing URLs, one per line, e.g.:
* http://mywebserver.com/images/271947.jpg
* http://mywebserver.com/images/24174.jpg
* http://somewebsrv.com/img/992147.jpg 

and downloads all images, storing them on the local hard disk.

## USAGE:

download_images.py -h
usage: download_images.py [-h] [-o OUTPUT_DIRECTORY] file_name

### positional arguments:
  * file_name
  	* The name of the file containing URLs

### optional arguments:
  * -h, --help
  	* Shows this help message and exit
  * -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
	* The directory in which to save the downloaded images
	
---
### This script supports:
* Checking for different line arguments as mentioned in Usage
* Checking the existance of OUTPUT_DIRECTORY if supplied
* Checking for any whitespace character (equal to [\r\n\t\f\v ]) in a URL
* Getting the correct image name even if the URL ends with a slash
* Warning the user if the image already exists
* Choosing a different download directory for saving images
* Calculation of how many successes, failures and attempts to download files that are not images
* Calculation of the total time

### This script can be further improved to include checking for:
* repeated URLs
* empty URLs files
* different directories to save images
* and others

---
Please note that any line in the URLs file starting with '--' will be discarded. 
