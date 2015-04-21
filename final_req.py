## This is a short script to grab the Zillow data for each neighborhood and assimilate it
## into a big GeoJSON file. 

import xml.etree.ElementTree as ET
import geojson
import requests
import time 

## Choose the file to read ##

polys = geojson.loads(open('seattle_named_neighborhoods.geojson').read())

## Specify my output ## 
poly_set = {}
poly_set['type']     = 'FeatureCollection' # See (http://geojson.org/geojson-spec.html) 
poly_set['features'] = []                  # This holds each individual neighborhood polygon GeoJSON

## Keep a log where Zillow does not have a result ##
error_log = open('error_log.txt','w+')

# How to iterate through each polygon #
# Since each neighborhood is considered a Feature (it has geometry + data), the file is
# considered a 'FeatureCollection', so it has an array of Feature (which by themselves are proper GeoJSON)
for poly in polys['features']:

	## The name is stored as 's_hood' in the original data set ##
	name = poly['properties']['s_hood']
	print('Processing ' + name )

	## This is the GeoJSON I build for each neighborhood ##
	neighborhood_poly = {}
	neighborhood_poly['type']       = 'Feature'        # 'Feature' is the required type when there are 'properties'
	neighborhood_poly['geometry']   = poly['geometry'] #  Maybe poly['type'] = 'MultiPolygon'
	neighborhood_poly['properties'] = {}			   #  These are all required for a GeoJSON of type 'Feature'

	## This dictionary holds stuff we want to append to our future GeoJSON ##
	## ** In hindsight, I should have just appended to properties... this made sense in
	## ** an earlier iteration. 

	neighborhood_data = {}
	neighborhood_data['name'] = name
	
	## Generating the request ##
	line = name.replace(' ', '%20')
	XML_request = 'http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1a9fsh24qh7_4n5nu&state=WA&city=Seattle&neighborhood=' + line
	
	## This should import the zws_id from a file that is not committed to GitHub ##
	XML_request = 'http://www.zillow.com/webservice/GetDemographics.htm?zws-id=' + zws_id + '&state=WA&city=Seattle&neighborhood=' + line

	## Making and Parsing the request ##

	r = requests.get(XML_request)

	## Handling the request ##

	try:
		## This constructs and XML tree from the XML string ##
		tree = ET.fromstring(r.content)

		## The following sections are for robust parsing of the XML response ##
		## If we want more from their API, let me know and I can grab it.    ##
		
		## Median Income and Median Commute Time ## 
		for attr_tag in tree.iter('attribute'):
			for child in attr_tag:
				## "Median Household Income" ##
				if (child.text == 'Median Household Income'):
					found = attr_tag
					median_income = found.find('values').find('neighborhood').find('value').text
					# print(median_income)
					neighborhood_data['Median_Household_Income'] = "${:,.2f}".format(float(median_income))
				## "Average Commute Time (Minutes)" ##
				if (child.text == 'Average Commute Time (Minutes)'):
					found = attr_tag
					median_commute = found.find('values').find('neighborhood').find('value').text
					# print(median_commute)
					neighborhood_data['Median_Commute_Time']     = "{:,.2f} minutes".format(float(median_commute))
					
			## Transportation and Demographics ##
			for cat_tag in tree.iter('category'):
				if cat_tag.attrib == {'type': 'Transportation'}:
					transport_list = []
					for child in cat_tag:
						transport_list.append(child.text)
					# print(transport_list)
					neighborhood_data['Transportation'] = transport_list
				if cat_tag.attrib == {'type': 'Employment'}:  
					employment_list = []
					for child in cat_tag:
						employment_list.append(child.text)
					#print(employment_list)
					neighborhood_data['Employment'] = employment_list    

	## Unfortunately not all neighborhoods are recognized by Zillow.
	## We will probably have to fill these in manually... :(
	except:
		error_log.write('Unable to get result for ' + name + '\n')
		neighborhood_poly['properties']['Zillow'] = 'Unable to retrieve Zillow Data.'
        print('\tUnable to resolve ' + name)		

	## This is executed regardless of the XML response ##
	finally:
		for key in neighborhood_data.keys():
			neighborhood_poly['properties'][key] = neighborhood_data[key]       

		## Add the neighborhood polygon to the global feature set ## 
		poly_set['features'].append(neighborhood_poly) ## Add this to the global feature set ##

		## Delay the execution to avoid an IP ban from Zillow ##
		time.sleep(1) # This is in seconds... not milliseconds like JS #

error_log.close()  # This file stores any neighborhood that Zillow did not find #
	
### Output the GeoJSON at the End ###
out_json = geojson.dumps(poly_set, sort_keys=True)    # This ensures that our GeoJSON is indeed a GeoJSON #
out_file = open('all_Seattle_data_test.geojson','w+') # File output. 'w+' overwrites an existing file if present #
out_file.write(out_json)
out_file.close()    