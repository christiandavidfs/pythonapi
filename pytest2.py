import urllib.request
import urllib.error
import csv
import requests
from jsonschema import validate
from support.assertions import assert_valid_schema
import json

# class MyEncoder(json.JSONEncoder):
    # def default(self, obj):
        # if isinstance(obj, (bytes, bytearray)):
            # return obj.decode("ASCII") # <- or any other encoding of your choice
        # # Let the base class default method raise the TypeError
        # return json.JSONEncoder.default(self, obj)




with open('companylist.csv', 'r') as f:
	reader = csv.reader(f)
	for row in f:
	
		url= "http://stock-whatif.herokuapp.com/whatif/"
		formedurl= url+row
		statusurl = urllib.request.urlopen(url+row)	
		contents = urllib.request.urlopen(formedurl).read()
		status= str(statusurl.getcode())
		
		print ("Testing: " + row +" Status= " + status) 
		print () 
		print (contents)
		print ()
		
		
		# contents = urllib.request.urlopen(formedurl).read()
		# response = json.dumps( contents, cls=MyEncoder )
		# json_data = json.loads(response.data)
		# assert_valid_schema(json_data, 'schema.json')

		print ("---------------------------------------------------------")
		if status == "200":	
			print ("Status 200 - Test Passed")
		else:
			print ("Status not 200 - Test Failed")	
		print ("---------------------------------------------------------")
		if "null" in str(contents):
			print ('Failed. The response have null fields')
		else:
			print (' Passed. The response have content')
			print ("---------------------------------------------------------")
	print ()	

	