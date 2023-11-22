import json
import googlemaps
import pandas as pd

# Download from https://data.sfgov.org/w/razy-xert/ikek-yizv and replace local path with yours
lots_csv = open("/Users/mikerotondo/Downloads/LandUse2016.csv")
lots = pd.read_csv(lots_csv)

lots_with_resunits = lots.query('resunits > 0')
print(lots_with_resunits['resunits'].value_counts())
print(lots_with_resunits.columns)

def random_res_weighted_address():
  lot = lots_with_resunits.sample(weights='resunits')
  number = lot['from_st'].values[0]
  street = lot['street'].values[0]
  street_type = lot['st_type'].values[0]
  address = str.format("{0} {1} {2}, San Francisco CA", number, street, street_type)
  return address

gmaps = googlemaps.Client(key='AIzaSyAIS6YAVzijaOC5xNPcPtypE1RSw6gjbj0')
num_routes = 100000
with open('sf_routes.json', mode='a') as routes_file:
  for i in range(num_routes):
    routes_file.write("\n")
    result = gmaps.directions(random_res_weighted_address(),
                                        random_res_weighted_address(),
                                        mode="driving")
    print('.')
    if i % 10 == 0:
      print(i)
    routes_file.write(json.dumps(result[0], indent=2))
    routes_file.write(",")
