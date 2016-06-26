#! /usr/bin/python
"""
Simpy REST client
"""

import sys
import urllib2

def get_request(url):
	'''Return the response from a request'''
	response = ''
	try:
		url = url
		response = urllib2.urlopen(url).read()
	except urllib2.HTTPError:
		response = "ERR => 404 NOT FOUND"
	except urllib2.URLError:
		response = "ERR => URL ERROR"
	except AttributeError:
		response = "ERR => INVALID ARGUMENTS"
	except ValueError:
		response = "ERR => INVALID ARGUMENTS"
	finally:
		print response

if __name__ == '__main__':
	get_request(sys.argv[1])
