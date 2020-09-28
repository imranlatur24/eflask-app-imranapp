import urllib # Python URL functions
import urllib2 # Python URL functions
url = "http://indianrailapi.com/api/v2/PNRCheck/apikey/ffaa1c632341effb6b503cf69467109a/PNRNumber/2311076590/" # API URL
req = urllib2.Request(url)
response = urllib2.urlopen(req)
output = response.read() # Get Response
print(output) # Print Response
