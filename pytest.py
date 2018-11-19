import urllib.request
import urllib.error
import csv

with open('companylist.csv', 'r') as f:
  reader = csv.reader(f)
  str(lista) = list(reader)
  
tamanio = len(lista)
range=(0,tamanio)
total= 0

while total < tamanio:
	url= "http://stock-whatif.herokuapp.com/whatif/"
	formedurl= url+lista[total]
	statusurl = urllib.request.urlopen(url+lista[total])	
	contents = urllib.request.urlopen(formedurl).read()
	try:
		status= str(statusurl.getcode())
		print ("Whatif: " + lista[total] + " : status =" + status) 
		print () 
		print ()
		print (contents)
		print ()
		print ()

	except HTTPError as e:
    		print('The server couldn\'t fulfill the request.')
    		print('Error code: ', e.code)
	else:
		total += 1
