import time
import secrets
import route
import googlemaps
import csv
from haversine import haversine
from polyline.codec import PolylineCodec

__author__ = 'Arif (arif@belalangtempur.com)'

if __name__ == '__main__':
    gmaps = googlemaps.Client(secrets.google_api_key)

    counter = 0
    temp_lat = 0    # used to calculate distance and append it to the .csv
    temp_lon = 0    # used to calculate distance and append it to the .csv

    with open('coordinates.csv', 'w') as f:
        coord_writer = csv.writer(f, delimiter=',')

        # find intermediate coordinates between two pre-determined subsequent coordinates in route.py
        while counter < len(route.routes) - 1:
            try:
                # use mode 'walking', otherwise google will provide unwanted directions due to one-way traffic roads
                direction_result = gmaps.directions(route.routes[counter], route.routes[counter+1], mode="walking")
                for step in direction_result[0]['legs'][0]['steps']:
                    # decode the polyline to get the intermediate coordinates
                    intermediate_coords = PolylineCodec().decode(step['polyline']['points'])
                    # calculate the distance per two subsequent intermediate coordinates
                    for x in intermediate_coords:
                        if temp_lat == 0 and temp_lon == 0:            # if the initial coordinate
                            dist = 0
                        else:
                            dist = haversine((temp_lat, temp_lon), x)  # calculate using haversine formula (in km)
                        coord_writer.writerow([x[0], x[1], dist])
                        temp_lat = x[0]
                        temp_lon = x[1]
                time.sleep(1)
                counter += 1
            except ValueError:
                print("google credential error")
