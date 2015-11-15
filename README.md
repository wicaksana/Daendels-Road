# Daendels-Road: A Twitter bot to walk through the great post road in Java island

follow on Twitter: @Jalan_Daendels

Background:
TBA

Description:
The bot walks through the great post road from Anyer to Panarukan, traversing more than 1000 km. The bot uploads the image of the street per 1 km, together with the corresponding address and coordinate.

Files:
- get_coordinates.py: to generate the route
- do_tweet.py: to 'move' the bot and to tweet the streetview image. Run using cron job.
- route.py: route guidelines
- secrets.py: credentials for google and twitter APIs
