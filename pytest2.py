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

# Here I open de csv with the company list and read the content line per line
with open('companylist.csv', 'r') as f:
	reader = csv.reader(f)
	for row in f:
		# Define the base url
		url= "http://stock-whatif.herokuapp.com/whatif/"
		# Define a variable to the to the formed url
		formedurl= url+row
		# Get the status of the url 
		statusurl = urllib.request.urlopen(url+row)	
		# Get the content and load it as json format
		contents = urllib.request.urlopen(formedurl).read()
		d = json.loads(contents)
		# Pass the status as string to validate it later
		status= str(statusurl.getcode())
		
		# Get the Values for low and validate the types are correct.
		def lowvalidation():
			ledate=json_data.get("low", {}).get("date", {})
			leprice=json_data.get("low", {}).get("price", {})
			levalue=json_data.get("low", {}).get("value", {})
			leshares=json_data.get("low", {}).get("shares", {})
			if (	
				type(ledate)is str and
				type(leprice) is str and
				type(levalue) is float and
				type(leshares) is float):
				print ("All the data types for low are correct.")
			else:
				print ("Wrong data types for low.")
		# Get the Values for low and validate the types are correct.		
		def highvalidation():
			ledate2=json_data.get("high", {}).get("date", {})
			leprice2=json_data.get("high", {}).get("price", {})
			levalue2=json_data.get("high", {}).get("value", {})
			leshares2=json_data.get("high", {}).get("shares", {})
			if ( type(ledate2) is str and
				type(leprice2) is str and
				type(levalue2) is float and
				type(leshares2) is float):
				print ("All the data types for high are correct.")
			else:
				print ("Wrong data types for high.")		
		
		print ("Testing: " + row +" Status= " + status) 
		print () 
		print (d)
		print ()
				
		response = json.dumps( d )
		json_data = json.loads(response)
		# assert_valid_schema(json_data, 'schema.json')
		# Print the content only for high
		print ("High :"+ str(json_data['high']))
		# Print the content only for low
		print ("Low :"+ str(json_data['low']))
		# Define two variables with the values of high and low
		valuelow=json_data.get("low", {}).get("value", {})
		valuehigh=json_data.get("high", {}).get("value", {})
		print ()
		# Prints the difference
		print ("Values difference")
		diferencia =valuehigh-valuelow
		print (diferencia)
		# Shows if the content for high and low have the right type of fields
		lowvalidation()
		highvalidation()
		print ("---------------------------------------------------------")
		# An evaluation to show the Higher value is reallly the higher
		if valuehigh > valuelow:	
			print ("Test Passed: Higher value is really higher")
		else:
			print ("Test Failed: The higher value is in fact lower or equal")	
		print ("---------------------------------------------------------")
		# Validates the Code Status response 
		if status == "200":	
			print ("Status 200 - Test Passed")
		else:
			print ("Status not 200 - Test Failed")	
		print ("---------------------------------------------------------")
		# Evaluates if the content in the fields is null
		if "null" in str(contents):
			print ('Failed. The response have null fields')
		else:
			print (' Passed. The response have content')
			print ("---------------------------------------------------------")
	print ()	

	