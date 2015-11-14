import os
import secrets
import math
import csv
import tweepy
import googlemaps
from pprint import pprint
from urllib.request import urlretrieve

__author__ = 'arif'


def post_tweet(coord, img):
    """
    tweet the streetview image, and the current coordinate as well
    :return:
    """
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.secure = True
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)

    status = '({},{}) {}'.format(coord[0], coord[1], get_reverse_geocoding(coord))

    api.update_with_media(img, status=status)


def get_reverse_geocoding(coord):
    """
    get the address of current coordinate
    :param coord: current coordinate
    :return: formatted address
    """
    gmaps = googlemaps.Client(secrets.google_api_key)
    result = gmaps.reverse_geocode(coord)
    return result[0]['formatted_address']


def get_bearing(start_point, end_point):
    """
    calculate the bearing of a certain path. Needed in order to get proper streetview image.
    stolen from https://gist.github.com/jeromer/2005586
    :param start_point: starting point (lat, lon)
    :param end_point: ending point (lat, lon)
    :return: compass bearing
    """
    lat1 = math.radians(start_point[0])
    lat2 = math.radians(end_point[0])
    dlon = math.radians(end_point[1] - start_point[1])

    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(dlon))

    initial_bearing = math.degrees(math.atan2(x, y))
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def get_image(coord, heading):
    """
    get image from google streetview given the lat, lon, and the heading
    :param coord: coordinate (lat, lon)
    :param heading: looking angle of the camera
    :return: path of the image filename
    """
    url = 'http://maps.googleapis.com/maps/api/streetview?sensor=false&size=640x640&key='
    google_url = (url + secrets.google_api_key)
    img_dir = 'img/'
    img_prefix = 'img_'
    img_suffix = '.jpg'

    url = google_url + "&location=" + str(coord[0]) + ',' + str(coord[1]) + "&heading=" + str(heading)
    img_file = os.path.join(img_dir + img_prefix + str(coord[0]) + '_' + str(coord[1]) + img_suffix)
    urlretrieve(url, img_file)

    return img_file

if __name__ == "__main__":
    orig_csv = 'coordinates.csv'
    temp_csv = 'coordinates_temp.csv'
    before_current_coord = []  # need this to calculate heading
    current_coord = []
    distance = 0
    with open(orig_csv) as f, open(temp_csv, 'w') as tf:
        coord_reader = csv.reader(f, delimiter=',')
        coord_writer = csv.writer(tf, delimiter=',')
        # count the rows
        while distance < 1:  # for each 1 km
            try:
                temp = next(coord_reader)
                distance += float(temp[2])

                if not current_coord:  # initially, when current_point is still empty, right_before == current_point
                    before_current_coord = [float(temp[0]), float(temp[1])]
                else:                  # else, right_before equals to the old current_point
                    before_current_coord = current_coord

                current_coord = [float(temp[0]), float(temp[1])]
            except StopIteration: # end of csv file
                continue
        # then, print the rest of the .csv file to temp file, if any
        for line in coord_reader:
            coord_writer.writerow(line)

    print('right_before: {},{}'.format(before_current_coord[0], before_current_coord[1]))
    print('current point: {}, {}'.format(current_coord[0], current_coord[1]))

    # now, replace the original .csv with the temp .csv file
    os.remove(orig_csv)
    os.rename(temp_csv, orig_csv)

    heading = get_bearing(tuple(before_current_coord), tuple(current_coord))
    print('bearing: {}'.format(heading))

    # get streetview image of current coordinate
    img_file = get_image(tuple(current_coord), heading)


    # tweet it
    post_tweet(tuple(current_coord), img_file)

    # clean up
    os.remove(img_file)