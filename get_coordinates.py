import time
import secrets
import route
import googlemaps
import pprint
import csv
from haversine import haversine
from polyline.codec import PolylineCodec

__author__ = 'Arif (arif@belalangtempur.com)'

if __name__ == '__main__':
    gmaps = googlemaps.Client(secrets.google_api_key)

    counter = 0
    points = []
    temp_lat = 0    # used to calculate distance and append it to the .csv
    temp_lon = 0    # used to calculate distance and append it to the .csv

    with open('coordinates.csv', 'w') as f:
        coord_writer = csv.writer(f, delimiter=',')
        while counter < len(route.routes) - 1:
            try:
                direction_result = gmaps.directions(route.routes[counter], route.routes[counter+1], mode="walking")
                for step in direction_result[0]['legs'][0]['steps']:
                    intermediate_points = PolylineCodec().decode(step['polyline']['points'])
                    for x in intermediate_points:
                        if temp_lat == 0 and temp_lon == 0:
                            dist = 0
                        else:
                            dist = haversine((temp_lat, temp_lon),x) # in km
                        coord_writer.writerow([x[0], x[1], dist])
                        temp_lat = x[0]
                        temp_lon = x[1]
                time.sleep(1)
                counter += 1
            except ValueError:
                print("google credential error")
