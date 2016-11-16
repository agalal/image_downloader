#!/usr/bin/python

"""
This is a script that takes a plaintext file as an argument containing URLs, one per line, e.g.:
http://mywebserver.com/images/271947.jpg
http://mywebserver.com/images/24174.jpg
http://somewebsrv.com/img/992147.jpg 

and downloads all images, storing them on the local hard disk.
------
USAGE:
------
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
"""

import argparse
import re
import ntpath # This should work for all paths on all platforms to handle path seprators
import warnings
import urllib
import datetime

# Redefinition of showwarning for print warning messages.
def _warning(
	message,
	category = UserWarning,
	filename = '',
	lineno = -1):
	print(message)

warnings.showwarning = _warning

# path_leaf: handles the file_name even if the path ends with a slash
def path_leaf(url):
	head, tail = ntpath.split(url)
	return tail or ntpath.basename(head)

# is_image: check if the file is an image or not
def is_image(file_name):
	file_name_ext = file_name[file_name.find('.'):].lower()
	# Regualar Expression to match image extensions. Can be further enhanced by adding all image extensions
	return re.match('.*\.(jpg|png|gif|bmp|jpeg)$', file_name_ext)

# download_image: main function to retrieve the image from online
def download_image(url, file_name):
	plain_image_name = path_leaf(file_name)
	if not is_image(plain_image_name):
		print "Not Image: File '%s' is not an image file.\n" % plain_image_name
		return -2

	try:
		# First check to see if image exists, Can be further enhanced to give the user the option to overwrite this file or continue with old copy
		if ntpath.isfile(file_name):
			warnings.warn("WARNING: Image '%s' from '%s' already exists." % (plain_image_name, url))

		# Download url and save it with name file_name based on the appeneded directory 
		urllib.urlretrieve(url, file_name)
		print "Success: Image '%s' downloaded.\n" % plain_image_name
		return 0
	except Exception as not_downloaded:
		print "Error: Image '%s' NOT downloaded \"%s\".\n" % (plain_image_name, not_downloaded)
		return -1

# display_time: to display the time appropriately
def display_time(td):
	hours, remainder = divmod(td.seconds, 3600)
	minutes, seconds = divmod(remainder, 60)

	if td.days > 0:
		return "%s days, %s hours, %s minutes and %s seconds" % (td.days, hours, minutes, seconds)
	if hours > 0:
		return "%s hours, %s minutes and %s seconds" % (hours, minutes, seconds)
	elif minutes > 0:
		return "%s minutes and %s seconds" % (minutes, seconds)
	else:
		return "%s seconds" % seconds

def main():
	download_success = 0
	download_failure = 0
	not_images = 0
	out_dir = ''

	# Argument parser to manage command line arugments efficiently
	parser = argparse.ArgumentParser()
	# Positional File Name Argument
	parser.add_argument("file_name", help="The name of the file containing URLs")
	# Optional Output directory Argument (default is location of python script)
	parser.add_argument("-o", "--output_directory", help="The directory in which to save the downloaded images")
	args = parser.parse_args()

	if args.output_directory:
		if ntpath.exists(args.output_directory):
			out_dir = args.output_directory
		else:
			warnings.warn("WARNING: Output directory '%s' doesn't exist.\nUsing default directory....\n" % args.output_directory)

	start_timestamp = datetime.datetime.now()
	try:
		urls_file = open(args.file_name)
	except Exception as not_found:
		print not_found
		exit()

	for url in urls_file:
		# Regular expression to match any whitespace character (equal to [\r\n\t\f\v ]) and then substitute with ''
		url = re.sub('[\s+]', '', url)
		# Only process the url if it's not empty and if it doesn't start with -- (-- used to skip urls)
		if url and not url.startswith("--"):
			file_name = path_leaf(url)
			if out_dir:
				file_name = ntpath.join(out_dir, file_name)
			
			status = download_image(url, file_name)
			if status == 0:
				download_success += 1
			elif status == -1:
				download_failure +=1
			else:
				not_images +=1

	end_timestamp = datetime.datetime.now()

	# print summary
	print "\nSummary:\nOperation started on\t%s\n\t  & ended on\t%s\nTotal execution time \t%s\n\n\t- Downloaded: \t%s\n\t- Failed: \t%s\n\t- Not Images:\t%s"\
			 % (start_timestamp.strftime('%Y-%m-%d %H:%M:%S'), end_timestamp.strftime('%Y-%m-%d %H:%M:%S'),\
				 display_time(end_timestamp-start_timestamp), download_success, download_failure, not_images)


if __name__ == '__main__':
	main()
