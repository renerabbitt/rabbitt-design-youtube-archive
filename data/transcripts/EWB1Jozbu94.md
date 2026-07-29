---
videoId: EWB1Jozbu94
title: Advance Polyline Solids: Liquor Bottle. Chief Architect X-15.
url: "https://www.youtube.com/watch?v=EWB1Jozbu94"
status: imported
---

# Transcript

0:00 hey
0:01 VIP guess what let's go make let's go
0:05 make some advanced stuff let's go make
0:07 some advanced stuff using the solid
0:10 tools and I'm really going to be doing
0:13 this because I want to update my shelf
0:16 tools and I want to update my shelf
0:17 tools because I found a problem with
0:19 them so I need to start generating some
0:22 new content this is part of it I don't
0:24 ever like to just do a patch release
0:26 where I'm fixing a problem I I want to
0:29 put out a release where I'm updating the
0:31 system improving it and then also the
0:34 patch because it's not as fun when
0:36 you're just fixing a problem when you
0:37 get a new release update and you're
0:39 getting notified of it and you're
0:40 downloading it and you're expecting
0:42 something big to happen well the problem
0:44 I'm solving for is a very slight problem
0:45 and and most of my users aren't going to
0:48 notice that anything has changed at
0:51 all
0:52 but it's still necessary to fix it and
0:56 on top of that I want to give you some
0:58 new content so what I'm going to be
0:59 doing doing here is making a series of
1:03 alcoholic beverages not beverages
1:06 bottles alcoholic B bottles that might
1:08 be for a bar area I'm um I'm quite often
1:12 building out and designing bar areas in
1:15 my area so um it's good to have these as
1:18 assets so what did I do I brought in an
1:20 image I scaled that image to the correct
1:22 bottle size I trace that image with my
1:25 polyline line tool and I did a bu bunch
1:28 of fillets in that and now I've got one
1:31 line that traces the outline here and so
1:33 I'm going to copy this copy paste tool
1:35 and I'm going to look for that node that
1:37 is that resizing node this circular node
1:40 here right so I'm going to grab that
1:42 bring this in I'm going to bring this in
1:44 until that polyline starts to kind of
1:46 cross itself right because then that's
1:48 going to become an issue so it's
1:49 Crossing itself in several areas and
1:52 that's where it becomes a problem now I
1:54 could come in here and Trace again but I
1:56 don't know that ends up being kind of
1:58 problematic as well now now our current
2:01 iteration of our rendering system in X15
2:04 is not the best for glasswar so if we
2:07 make this really thick that could be
2:09 very problematic so I'm actually okay
2:11 with making this very thin which is also
2:14 coincidentally makes this a lot easier
2:16 to do so we're making it really thin and
2:19 then what I'm doing here at the bottom
2:21 is I'm just going to connect this
2:22 polyline here and then close that shape
2:26 up and we can simplify the polyline
2:29 there we go now we've got a closed
2:30 polyline so the next step of this is
2:33 let's go ahead and take a look at this
2:35 in 3D now I'm designing in plan view
2:37 that's because we've got a few things we
2:39 can do in plan view that we cannot do in
2:40 elevation so I do like designing in plan
2:43 View and then we've got to go find this
2:45 item now where the heck is it Well turns
2:48 out that by default I have my solids in
2:52 kind of a funny place but also that
2:53 wasn't a solid yet that would help so
2:56 let's make this into a solid real
2:58 quick
3:00 make it a 3D solid and we're going to
3:03 say that this is
3:05 2.75 let's just call it
3:08 2.75 and then we can find this on the
3:10 ground there we go so this is looking
3:13 good so far but what's our next step
3:17 right so what I want to do is I want to
3:19 select this face this face only and I'm
3:24 going to use revolve object now what I
3:28 want to do here is I want want to
3:30 revolve this so that I've got a soft
3:31 Corner because that's what this bottle
3:34 looks like for the most part the only
3:36 problem with this is the top of the
3:38 bottle is actually a cylinder so that
3:40 part isn't going to make sense but the
3:43 square part of this is going to make
3:45 sense so let's start with the square
3:47 part so I want to revolve and I want to
3:50 look at my Axis at the bottom here and I
3:53 want to revolve it about that y okay so
3:57 about the Y AIS and and what's the angle
4:00 of rotation well we're just going to say
4:02 it's 90° let's give this a shot now I
4:05 haven't practiced this I'm just trying
4:07 it out this is my understanding of the
4:09 tools so it might be that I'm making a
4:11 big mistake here and this doesn't work
4:13 so let's just try it out one more
4:16 objects could not be revolved now I've
4:20 noticed in the past when I've tried this
4:22 out that
4:24 sometimes it takes me actually exploding
4:28 the model right so explode the 3D solid
4:31 let's go ahead and try to click this
4:33 again and actually I want to click on
4:34 this Edge
4:37 specifically why that edge what happens
4:40 when we click on that
4:43 edge well let's try it
4:46 out around the Y AIS
4:53 90° so what did it
4:58 do
5:02 did something
5:07 interesting so it did a downturn
5:16 90 actually did something really nice
5:20 for the upper portion the bottle
5:24 portion so the upper portion looks
5:28 correct
5:30 and then the lower portions a little off
5:34 right so I think it will be a case where
5:38 we split this up into two parts again
5:40 I'm learning while I'm doing this okay
5:43 so let's go back a few steps in
5:49 fact let's go back quite a few
5:53 steps so here we go we've got this one I
5:57 don't want to see this camera in my way
5:59 sometimes this gets in my way it's nice
6:01 to just open this thing up and then it's
6:04 plan
6:05 display is camera symbol size let's just
6:09 make this let's make this tiny quarter
6:12 inch something like that maybe 0.5 of an
6:15 inch there we go now it's just out of
6:17 the way it's still there we can still
6:20 select it but it's kind of out of the
6:21 way all right so what do I want to do
6:24 here I want to make sure that we're
6:25 simplifying this first I don't want it
6:27 to be a solid and and what we notice is
6:30 that we like that this portion is a
6:34 square and that it should be revolved
6:36 around as a square but this is a tight
6:40 radius here so I think I think what
6:44 we'll do here
6:46 is I'm going to make a little break here
6:48 we're going to make a little just a trim
6:51 cut here right
6:53 here so because we're going to trim cut
6:56 we're going to copy paste and then we
6:59 want to drag this over tab input let's
7:01 go just 12 inches okay that's making our
7:05 copy because I want to trim and not
7:08 worry about it so trim trim that top of
7:11 the bottle here and then close this up
7:14 and now we can make this part of solid
7:16 and we'll see where we get from
7:19 here here's our 3D solid in fact let's
7:23 just make this a face in this
7:26 case all right so we've got a face
7:33 let's step back a little ways we're
7:36 going to
7:36 cancel they should let's
7:40 see simplify the polyline let's simplify
7:44 it make it back to a plain poly line we
7:47 actually want to cut right here
7:51 too and remember that if we contain the
7:54 cut within the poly line itself that
7:56 means this is going to close it up for
7:58 us
8:01 so we're just cutting the excess here
8:03 that closed it up let's simplify it
8:06 convert it now it's going to be a
8:10 face okay so here's our
8:14 face where do we where do we go from
8:17 here I'm going to press okay we're going
8:18 to revolve around we see the axis here
8:21 it's still the Y AIS so let's go 90°
8:25 about the Y AIS let's go negative 90 if
8:27 we can or about the Y AIS and let's see
8:30 what this looks
8:33 like well so far looks like nothing
8:36 because it's under the floor but that
8:39 does look like the corner of our
8:42 bottle let's raise this
8:45 up we're going to transform replicate
8:47 object let's move this up just so we can
8:49 see
8:51 it here we go
8:54 so that
8:56 is our corner of the bottle I'm liking
9:00 that right and so the overall bottle
9:03 width we're going to say it's about
9:05 three and a
9:06 quarter and let's just say this is a
9:09 let's call this half inch so
9:15 2.75 minus another half inch
9:18 2.25 I want to extrude this in the neg
9:24 y -2 Point excuse me Negative X I'm
9:28 looking at this down at the bottom I
9:29 want to go negative value so the leg
9:32 indicates positive value negative value
9:35 2.25 and what ends up happening all
9:38 right look at that so that's the front
9:39 side of the bottle oh and then I needed
9:41 to split that in half so that was
9:46 stupid yeah because we're going to
9:48 duplicate this about itself so let's go
9:49 back step so let's go this is going to
9:52 be negative
9:53 1.25
9:58 right
10:01 okay that's good and we could just do
10:05 the same on this under
10:08 side is there any problem with this now
10:11 that this is extended
10:13 out and we're extending this
10:16 base let's just give it a shot why not
10:19 so there we go that's that's C Delta yes
10:22 negative
10:23 1.25 that is correct if we're giving
10:26 just a quarter of a bottle
10:30 right so that's our quarter of a
10:34 bottle and so now if we duplicate about
10:40 itself and duplicate it about
10:44 itself let's see can we can we duplicate
10:47 by itself this
10:51 way here we
10:58 go
11:04 and can we Union this whole thing
11:17 now okay so we got one
11:20 object kind of a complex
11:26 object look at that that's looking
11:29 pretty
11:31 good now what do we do with this how do
11:34 we get the top right the Top's going to
11:37 be very
11:42 challenging Top's going to be very
11:45 challenging I have to think about
11:48 that well let's just try a few things
11:50 let's get into our plan view we know
11:52 that this needed to move 12 in
11:57 back
11:59 and we know where we chopped it right so
12:02 we're going to chop it again and chop it
12:04 right here now part of me thinks that we
12:07 might need to keep this corner
12:11 intact and if I really sat down and
12:14 wrote this down on paper we could
12:16 probably figure it out no problem so I'm
12:18 making a duplicate
12:20 here and let's just make this 0o
12:24 in and let's go ahead and trim this so
12:27 we got a line
12:30 take that
12:32 line and we're going to trim that excess
12:36 right so there we go now let's convert
12:39 this to a face
12:46 again and revolve around that
12:51 y90
12:53 again one of more objects cannot be
12:56 revolved now why would that be I don't
12:58 see see any reason why
13:01 not so we know that we have a
13:04 face let's just get
13:06 into our camera mode sometimes when this
13:10 stuff is going underneath the floor I
13:11 just use the delete surface tool to get
13:13 to it where is this thing all right
13:15 there it is so make this selection and I
13:18 want it to revolve looking at this AIS
13:20 again I want it to revolve around that y
13:23 AIS 90 and it will not do
13:27 it why is that let's go positive 90 does
13:30 it make a
13:36 difference it's interesting that it's
13:38 giving
13:40 me an option
13:44 here that is user
13:49 defined still not will not work okay so
13:54 let's do something different let's go
13:55 back a few because we
13:57 know
14:02 we know that before we revolved the
14:05 entire object 90 the entire face 90 and
14:09 it was not a
14:20 problem it's making me go back quite a
14:22 few levels here oh there we
14:26 go so let's try this
14:29 let's convert this to a
14:35 face let's go for finish FL there there
14:37 we go finish FL bottom one inch
14:40 something like that and then now let's
14:42 revolve it around that y AIS let's see
14:46 if we can get it this
14:48 90 still not doing it that's so strange
14:51 because we were able to do it not too
14:52 long ago so I do think it matters where
14:56 you're clicking on this object before
14:58 before you revolve so let me try this
15:00 I'm going to re click on this Edge right
15:03 click on this Edge right here I'm going
15:05 to revolve around this pinpoint around
15:08 this
15:10 face see if that works so that works
15:16 interesting okay so we don't want that
15:19 to work we going to go back a little bit
15:21 now let's go back to what we had
15:23 before see if we can't crash this system
15:26 too I feel like we're getting real close
15:28 to crashing and also because we're
15:30 working in tight I like to if you're in
15:32 my Pro Plan switch to the macroad
15:34 dimensions it's going to be a lot easier
15:36 to see some things so here we go let's
15:40 just simplify this poly line we'll cheat
15:41 a little bit we'll just draw a line in
15:43 here snap
15:46 it seems we've got a lot of little
15:48 Snappy things in here going on let's
15:51 draw this line
15:55 in use our
15:57 trim
16:00 there we go that's a closed polyline
16:02 convert it to a face there we go and so
16:06 we need to be very specific about how
16:08 we're clicking on this so we're clicking
16:10 on this item right here revolve around y
16:13 AIS
16:14 90° let's see what this looks like and
16:17 how do we get these to line up
16:20 because I got them off center of each
16:22 other which was a mistake
16:25 right so there's the top of the bottle
16:28 we can see here it's it's obviously not
16:30 going to give us that tight 90 at the at
16:33 the top and it might be that I just kind
16:37 of fake that because I can't think of
16:39 how I should have done that to get that
16:42 to be correct the first time around
16:44 because we're going from a tight Square
16:46 corner to a circular
16:49 setup and how would you go about doing
16:54 that I mean you can you could clip from
16:58 m multiple directions that would be
17:04 something Welly I'd really have to write
17:07 that down and and brainstorm a few
17:09 things and I think this is just part of
17:11 it is figuring out these things as you
17:15 go I feel like that's that's it's just a
17:18 big part of it is discovering these
17:22 methods so let's grab this just going to
17:25 pull it out of the floor for one and we
17:28 can hold our SK to just make it so that
17:30 we're not hitting things oh actually
17:32 it's because it's on a a radius it's
17:34 going to be a funny grab so I'm going to
17:36 use select next side see if I can't make
17:38 it easier to grab
17:40 this it's still going to be a funny
17:44 grab
17:52 right so easier to just use transform
17:55 replicate Move It Up 3 inch something
17:58 like
18:03 that look at
18:11 that close but no
18:15 cigar very
18:26 close interesting we've got a bunch of
18:29 little edges on this top
18:31 piece so it's not a perfect reflect
18:40 about boy Chief did a fantastic job of
18:43 giving us the ability to
18:45 visualize the
18:48 reflect yeah we've got a bunch of
18:50 imperfect edges
18:55 here if that's the case
19:02 we're going to have some problems
19:22 huh
19:25 yeah going to have some seams
19:30 that we don't
19:34 want I think the next piece of this is
19:37 that we would just put a pyramid in
19:39 here and fill it the
19:43 pyramid because how else would you get
19:50 this because it's not just a simple
19:53 Extrusion it's changing its shape as it
19:55 gets towards the
19:57 corner
20:17 challenging very
20:19 challenging what happens when we put a
20:21 glass material on
20:27 this
20:42 and then what happens when we edit the
20:45 index of
20:46 refraction down to like a
20:49 1.1 is no opposite direction I want to
20:53 go up to like a
20:55 3.5 it's really starting to look like a
20:57 bottle
21:02 now probably would never even notice
21:05 that there's a whole missing piece of
21:06 mesh
21:09 here you know and then you put a little
21:11 color in
21:13 here especially if you put transparency
21:16 inside of right so if we put a you know
21:21 some color inside of so if we put like a
21:23 solid
21:27 here
21:30 and this solid we wanted to we're going
21:33 to make a a new
21:35 texture and we're going to make this
21:38 pattern be a
21:45 brown right and in this case our index
21:48 of refraction is going to be 1.05 or
21:53 something like
21:57 that
21:58 so glass inside of glass the current
22:01 rendering model won't do well with this
22:04 it just
22:06 won't but we got stuff coming
22:10 up that I happen to know about a little
22:16 bit stuff that's coming up why I can't
22:18 get Center of this at
22:24 all stuff coming up should make it so
22:27 that we've got some truly translucent
22:31 materials and clipping masks so we
22:35 wouldn't need a piece inside of a piece
22:37 in fact this would be a waste of
22:49 time but I like this as an
22:56 exercise
22:58 here we go look at that brown liquor
23:01 let's just kick up the denoiser a bit or
23:03 excuse me sample rate a bit let's just
23:05 take a look at what that looks
23:08 like right and then let's even pick this
23:12 bottle up a little bit let's
23:15 go um texture Source no we just want
23:18 color and let's just make this a darker
23:22 darker color what
23:24 happens gets too
23:26 dark
23:38 right index of refraction let's get this
23:42 down and let's just test something even
23:50 higher and what happens when you stick a
23:54 a lamp next to
23:56 it
24:11 not a whole lot not a whole lot happens
24:13 and what happens when you put a
24:14 grayscale map
24:16 in
24:19 the normal
24:26 map
24:29 too heavy right that's too heavy got
24:32 like almost a chrome chrome material now
24:35 kind of interesting so let's go a lot
24:37 lighter with that let's go three
24:41 gradient look at that that's starting
24:44 that's really starting to look like
24:46 glass depends on the
24:54 angle I almost want to kick this index
25:06 down yeah that's looking very
25:10 good look at
25:14 that so got to figure out a way to fill
25:17 that geometry in and then on top of that
25:20 you know this is where we've
25:22 got um this probably be easiest to do in
25:26 3D because 3D what's nice is there's a
25:28 little bit of collision uh detection
25:30 here so in 3D we can draw this solid
25:33 hopefully it goes right on top here
25:35 right so that becomes you know whatever
25:39 our our label is what does the label
25:41 look
25:43 like um and does that label wrap all the
25:46 way I can't
25:52 remember so we basically do
25:55 a we do a cut
25:58 right
25:59 so let's
26:03 see am I thinking about this right let's
26:06 just draw this through when we draw this
26:18 through and this comes up to
26:23 here then if we do an intersected
26:32 right that's our
26:35 label oh we didn't retain the original
26:37 object dang
26:42 it okay let's try this
26:45 again I dismiss that usually because I
26:49 don't typically want to retain the
26:51 original object so I just make
26:52 duplicates of the original object but in
26:54 this case it's nice to have that up it
26:56 just bothers me over time
26:58 all right so selected intersected and we
27:00 do want to retain the original objects
27:02 and then we're going to take this Cube
27:03 Get rid of it and then there's our label
27:06 um it's going to be doing some Z
27:08 fighting
27:10 because we need to subtract now subtract
27:15 this and
27:17 also would you like to retain the
27:19 original object this
27:22 case if we say yes we still have Z
27:26 fighting here's where the problem
27:30 is
27:32 right yeah we still have Z fighting
27:35 that's the problem so go back level so
27:39 here's what you got to do
27:40 instead this gets really
27:45 complex okay so we want to make a copy
27:48 of this okay so copy and you know what
27:53 we copied it's in the it's in the
27:55 clipboard so we don't need to paste so
27:58 now make our
28:04 subtraction if we
28:06 can don't retain the original
28:11 object that should get rid of the glass
28:14 Z fighting the label and paste hold your
28:18 label back now we've got no Z
28:20 fighting bam so now we've got the bottle
28:25 works Etc you'll end up clipping the
28:28 back end of this and turning it back
28:30 into glass so that the label only wraps
28:34 halfway and then you'll have bottle
28:37 liquor and we still have to figure out
28:40 how to fill in
28:41 here um I think this is a great stopping
28:44 point for a video one so I'm going to
28:46 save this file and we're going to come
28:48 back to
28:49 it but yeah this is that's looking
28:52 pretty cool hopefully you learned
28:56 something
28:57 [Music]
29:06 I
