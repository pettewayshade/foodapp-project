#! /usr/bin/python

import csv
import random
from Tkinter import *
#import tkSimpleDialog
import re
from config import key
from googlemaps import GoogleMaps

'''#Create the window
root = Tk()
#Modify root window
#root.title("Food Finder")
root.geometry("200x100")
#kick off the event loop'''

####Ask user for their input
#zipcode = tkSimpleDialog.askstring("Zip Code", "What zip code would you like to search?")
options =  {1 : "Fast Food", 2 : "Dine in", 3 : "Carryout"}
print (options) 
category = raw_input("Please enter a number 1-3 to select the category or enter to select from all:")
zipcode = raw_input("What zip code would you like to search?")

###Check to make sure zipcode is valid
while len(zipcode) != 5 or (not zipcode.isdigit()):
    print 'Zip code must be 5 digits'
    #zipcode = tkSimpleDialog.askstring("Zip Code", "What zip code would you like to search?")
    zipcode = raw_input("What zip code would you like to search?")
    print("Searching zipcode " +str(zipcode)+"...")


params = {
        'location' : zipcode,
        'keyword' : catergory
        'type' : 'restaurant',
        'key' : key
        }

base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

resp = requests.get(base_url, params=params)i

data = {}
with open('Restuarants.csv', 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		if line[4] == 'zipcode':
			continue
		if not data.get(line[4]):
			data[line[4]] = []
		data[line[4]].append(line)
No= ("No Restaraunts found for Zipcode " +str(zipcode)+ ".")		
zipcode_to_find = str(zipcode)
rest_list = data.get(zipcode_to_find)
if rest_list:
	print rest_list[random.randint(0,len(rest_list)-1)]
#elif zipcode == "" or "None":
#	print "Please enter a valid zipcode."
else:
	print No
	phone_match = re.compile("^(\w{3}-\w{3}-\w{4})$")
	
	Addinfo= raw_input("Would you like to add a restuarant to the file? ")
	if Addinfo.lower() == "yes":
		with open('Restuarants.csv', 'a') as f:
			Addrest= raw_input("Please enter restuarant name: ")
			Addcat= raw_input("Please enter resturant category (Dine-in, Fast Food or Dine-in/ Carryout): ")
			def validPhone(number):
				match = phone_match.match(number)
				if match:
					return match.groups(0)[0]
				return None

			AddPhone = ''
			while not validPhone(AddPhone):
				AddPhone= raw_input("Please enter phone number in xxx-xxx-xxxx format: ")
			AddAdd= raw_input("Please enter address: ")
			AddZip= raw_input("Please enter zip code: ")
			while len(AddZip) != 5 or (not AddZip.isdigit()):
				print 'Zip code must be 5 digits'
				AddZip= raw_input("Please enter zip code: ")
			f.write(",".join([Addrest, Addcat, AddPhone, AddAdd, AddZip])+ '\n')
			print 'Thank you for your input!'
	if Addinfo.lower() == "no":
		print "Thank you!"

