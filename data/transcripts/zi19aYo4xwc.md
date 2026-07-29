---
videoId: zi19aYo4xwc
title: Total Station Tool For Longitude and Latitude GPS in Chief Architect X15
url: "https://www.youtube.com/watch?v=zi19aYo4xwc"
status: imported
---

# Transcript

0:03 free symbol Friday
0:03 yeah and you know it's a good free
0:09 symbol Friday if we've got an
0:10 accompanying video
0:10 uh which also means that it was complex
0:17 it took me a long time to establish and
0:17 um
0:17 and you know what consider donating
0:20 donate link is in the description donate
0:24 link is in whatever social feed I'm
0:24 putting it in uh but otherwise go try
0:29 this out use it and enjoy it now this
0:31 came about from
0:31 um I've got my Discord server where I've
0:35 got a whole server established you can
0:36 ask questions you can take a look at
0:36 shop items you can get questions about
0:43 Chief Architect and methods and Ai and
0:44 all kinds of things there and it's a
0:47 growing group and it's um it's got a
0:49 good group of users there
0:49 so from that group and then also from
0:52 the conjoined Chief experts live stream
0:57 that we did today
0:57 we realized we needed a tool and the
1:00 tool specifically is for when we want to
1:05 take out something like some survey
1:07 equipment like a total station that
1:07 might have GPS coordinates built into it
1:12 so that you go in and use that station
1:14 and it knows its GPS coordinates and
1:14 then you can use it to go take out you
1:19 know a printed out survey
1:19 where you need to go pick up new data
1:24 from that survey right and so what we
1:24 need is we need datum points within our
1:28 printouts and how do we establish that
1:30 how do we get that and so what I'm
1:30 giving you is kind of a tool kit for
1:32 that it's um it's simple in its approach
1:38 it was just that the script itself was
1:38 difficult to write so what it is is it's
1:43 a cad block and this CAD block has an
1:43 insertion point that's very specific the
1:46 insertion point you're going to be
1:50 clicking on this in some known GPS
1:50 coordinate okay you have to know the
1:53 longitude and latitude of a given point
1:58 so that we establish a base datum for
1:58 which to draw our new information from
2:03 so I'm going to click on the corner of
2:05 this building because I'm going to
2:05 assume that I know where at the corner
2:09 of this building and actually probably
2:12 more accurately I would pull this from
2:12 the corner of this building maybe a foot
2:16 out right so I'm going to say that this
2:18 is a foot out from the corner of this
2:18 building and that's going to be the Mind
2:22 known data point where I take my total
2:23 station out or I take some kind of GPS
2:26 device out there and I get the reading
2:30 on what the longitude and latitude are
2:32 of a foot off the corner of this
2:32 building once I have that let me go
2:34 ahead and explode this CAD block now
2:36 something's going to happen here some of
2:39 this stuff's going to disappear the
2:39 reason being is that we built this on
2:41 the plot plan so if we switch to a plot
2:44 plan View
2:45 hopefully you've got text plot plan
2:48 turned on in your plot plan view so here
2:53 we go now we can see our XY position now
2:56 the X Y position is important
2:56 um because we're only dealing with maybe
3:01 totals of a couple hundred feet we're
3:01 not taking into account the curvature of
3:05 the Earth in these calculations it's
3:05 just not necessary so it is taking into
3:10 account that the XY position is giving
3:13 us positions on the drawing sheet that
3:13 are in inches okay and it's taking those
3:21 known inches and comparing it to our
3:21 known latitude and longitude so I need
3:24 you to open up this is a text box we're
3:29 going to open this text box up and you
3:29 can see here there's a bit of script and
3:33 specifically what we're looking at is
3:35 the items in between
3:35 or quotation marks okay and so what
3:39 we're going to do is we're going to
3:39 establish our known bearing our known
3:45 bearing in this case is divided by
3:47 decimal places the decimal places
3:47 actually mean that first number is
3:49 degrees minutes seconds it's just easier
3:53 to do it in decimal places it's much
3:53 easier to code for that as well so we're
3:58 going to say that this is 54 degrees
3:58 15 minutes and 16 let's go 0.5 seconds
4:03 okay and then we might even change this
4:08 to an East versus West right
4:08 so there we go not that that really
4:11 matters here we go so let me press OK
4:13 and there we go this is updated you also
4:19 notice that this marker updated as well
4:22 that's because we changed our known
4:22 latitude our known longitude so now when
4:28 I move this marker around it's going to
4:30 give me based on this data point over
4:33 here this particular data point and
4:35 based on this known longitudinal
4:35 latitude this is giving us our new
4:37 information and to quote someone that
4:39 was commenting on the feed earlier for
4:44 chief experts we're gonna
4:44 making copies we're going to make some
4:48 copies here so we'll just make a copy
4:50 and now we have additional
4:50 data points right so now you can go out
4:54 have this print out out right and so not
4:58 only this but we can get some
4:58 dimensional markers from the house
4:59 itself so so that we have some kind of
5:04 reference point so maybe it's that you
5:05 know if I go back to the working plan
5:06 View and I pick this up and I'm going to
5:11 convert this to you know polyline box
5:11 and we'll even say that this is in the
5:15 CAD plot plan
5:15 take this back to our plot plan View now
5:20 I've got some reference marker here so
5:24 that I can or from this point to the
5:24 house and say that this is 34.27 feet
5:30 well we can even leave that line in
5:30 place we can even say we want to show
5:34 length on that line right
5:34 so that we know exactly how far it is to
5:39 our reference point and we're taking the
5:41 total station out there anyways we
5:41 should be able to hit that exact Mark
5:43 and then pull our information from there
5:48 and come back and bring in our survey
5:51 data based on this so this is a
5:51 fantastic way of doing this because the
5:54 other thing that we can do is we can
5:54 either put some terrain data where it
5:58 kind of Loops in between these parts
5:58 right so I can use a spline here maybe
6:01 that spline actually needs to be curved
6:04 a little bit but eventually it's going
6:07 to make its way to this other Mark and
6:07 there we go now we've got you know data
6:11 based on that spline or probably more
6:11 accurate we're going to actually put in
6:14 some points so we're going to add an
6:14 elevation point here and because we've
6:16 added that elevation point we know what
6:21 our data is from the total station so
6:21 we've got some updated terrain and it's
6:24 super accurate
6:24 so that was the whole point of this
6:26 whole setup here is and if you know what
6:29 you're doing this is pretty cool
6:29 so play around with it let me know if
6:34 there are any problems with it again
6:34 this is a very complex bit of script I
6:38 think that it's scripted correctly but
6:40 someone is going to have to go check
6:40 this in the field but I do believe that
6:44 it's scripted correctly so go check it
6:44 out bring out your station hopefully you
6:48 have your own house map so you can go
6:48 just check it outside in your front yard
6:53 and uh enjoy check it out this should be
