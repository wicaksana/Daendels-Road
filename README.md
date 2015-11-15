# Daendels-Road
## A Twitter bot to walk through the great post road in Java island

(Inspired by @EarthRoverBot project, http://muffinlabs.com/rover/)

follow on Twitter: [@Jalan_Daendels](https://twitter.com/Jalan_Daendels)

![alt text][route_wikipedia]

Description:
[The great post road](https://en.wikipedia.org/wiki/Great_Post_Road) (more popular as 'Jalan Daendels' in Indonesian) is the name of a road that runs across [Java island](https://en.wikipedia.org/wiki/Java), built during the Dutch colonization in the beginning of 19th century by the reigning governor-general Herman Willem Daendels. It spans more than 1000 km, connecting Anyer in the west to Panarukan in the east. The construction took thousands lives of the local labors due to the harsh condition and the brutality from the colonials.

The road was intended to serve as military road and to transport postal services. Over the time, people used it as the main access to travel across Java, and many cities ware developed along the road. Nowadays, the road still serves as the main transportation infrastructure in northern Java.

It is interesting to see how is the current condition of the road. Unfortunately, there is lack of (online, at least) references about the detailed routes. Some segments are still well-known, i.e. 'jalur pantura' at Central and East Java. Some are debatable (the starting and ending points, some segments in Banten). And some are even missing. Nevertheless, I think some assumptions can be made regarding the missing/debatable road segments. Furthermore, the amount of them are much less significant compared to the well-documented one.

The idea of the project is to walk through this historical road and to see the current condition of the road. Thanks to Google, we can make use of its Streetview service to provide the images. The journey starts from 'Tugu nol kilometer' in Anyer, and finishes at 'Monumen 1000 km' at Panarukan. The image is taken for every 1 km, and posted in Twitter. Updates are provided four times a day, hence it would take approximately 8-9 months to finish.

To keep updated with the progress, please follow [@Jalan_Daendels](https://twitter.com/Jalan_Daendels)

Files:
- get_coordinates.py: to generate the route
- do_tweet.py: to 'move' the bot and to tweet the streetview image
- route.py: major coordinates of the route, used as the guideline
- secrets.py: credentials for google and twitter APIs


[route_wikipedia]: https://en.wikipedia.org/wiki/Great_Post_Road#/media/File:Java_Great_Post_Road.svg "The great post road"
