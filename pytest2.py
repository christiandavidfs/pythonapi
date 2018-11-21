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
		d = json.loads(contents)
		status= str(statusurl.getcode())
		
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
		assert_valid_schema(json_data, 'schema.json')
		print ("High :"+ str(json_data['high']))
		print ("Low :"+ str(json_data['low']))
		valuelow=json_data.get("low", {}).get("value", {})
		valuehigh=json_data.get("high", {}).get("value", {})
		print ()
		print ("Values difference")
		diferencia =valuehigh-valuelow
		lowvalidation()
		highvalidation()
		print (diferencia)
		print ("---------------------------------------------------------")
		if valuehigh > valuelow:	
			print ("Test Passed: Higher value is really higher")
		else:
			print ("Test Failed: Higher is in fact lower or equal")	
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

	