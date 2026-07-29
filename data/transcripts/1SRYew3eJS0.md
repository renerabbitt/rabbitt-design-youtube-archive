---
videoId: 1SRYew3eJS0
title: Braced Wall Panel Sheathing Dynamic Method In Chief Architect X16
url: "https://www.youtube.com/watch?v=1SRYew3eJS0"
status: imported
---

# Transcript

0:01 uh what's going on VIP um this video I
0:04 am going to try to
0:07 improve my brace wall plan
0:11 system and that is um after I've taken a
0:15 look at one of my colleagues plans who
0:18 has their own
0:20 method and and I like their method and I
0:24 want to see if I can do something kind
0:26 of recreate what they've got in a more
0:30 Dynamic way and so my existing brace
0:33 ball plan system got to get in a project
0:35 browser for that and in CAD details this
0:37 is using the Pro Plan but I'll show you
0:39 kind of how to recreate this basically
0:41 going to be be redoing this so you don't
0:44 need the Pro Plan to do this going to be
0:47 recreating
0:48 this and so what I've got here is
0:52 somewhere in here
0:53 schedules we've got a our Legend brace
0:58 wall schedule open up the CAD detail
1:01 what this is is a custom schedule
1:04 utilizing polylines so this was my
1:07 existing setup which was that I would
1:09 take this polyline and notice that this
1:12 is number two so this is braced wall
1:14 line number two and we see what's
1:16 happening here it's producing columns
1:18 that's coming from Custom object fields
1:21 from the polylines object information
1:24 pan open this up get into the object
1:26 information panel get into these custom
1:28 fields somewhere in here are some
1:32 various values right so some text values
1:35 here and so that's what's producing
1:38 these line items in this
1:41 schedule okay and so what I would be
1:43 doing is I would cut this line bring it
1:46 over here come into something like my
1:48 framing floor plan for instance and we
1:53 could just paste that
1:55 line
1:57 um actually
2:03 cut copy
2:05 that and so what you would be doing here
2:08 is because it's just a polyline is you
2:09 would just connect this to the
2:11 end right click there shouldn't have
2:13 been left click we connect this to the
2:16 end send this down and that's how it
2:19 would display is that we've got this
2:21 label and it's showing the distance
2:23 showing the brace wall line type and
2:26 then we turn
2:27 on line widths and that's it would
2:30 display it now my colleague wants to
2:33 show this in a much different way they
2:34 actually want to show solid fill across
2:38 the whole wall and yeah maybe you could
2:40 use the wall hatching tool and get that
2:42 solid fill but the wall hatching tool
2:44 does not have
2:46 an the alternative method would be to
2:49 break the wall at the location of your
2:52 braced wall lines but that's not a
2:54 really great method because sometimes
2:55 that can cause
2:58 issues able to break this and Report
3:00 certain layers where we are
3:02 showing I'll show show you exactly what
3:04 I mean we'll go wall types citing for
3:07 existing copy this call it
3:11 bwp plan and then we're going to report
3:14 that that actual layer for what would be
3:18 the braced wall to some new display
3:21 layer we could double click this and say
3:24 hey let's copy that walls layer rename
3:28 this now
3:30 pwp and in this case we're going to
3:33 change that color to Black if we have it
3:36 so that our layer fill style follows
3:40 that wall layer now now created a new
3:43 wall type get rid of my little polyline
3:47 here collecting the label um and if this
3:51 wall type is now let's just show our
3:54 layers and uncheck main layer only now
3:58 we can see that that brace wall line
3:59 showing up so that is a way that you
4:01 could do it but it's not
4:04 necessarily that's a fast way but like I
4:08 said sometimes this can cause issues
4:10 where you don't have the opportunity to
4:12 break your wall where you want to break
4:14 it and and maybe that's causing an issue
4:17 and then reporting length can be
4:18 problematic there length is not just a
4:21 linear method if we use
4:24 um my search tool to just kind of search
4:28 reporting measurement from this wall and
4:31 we come in here and we say
4:34 length um we do get a few things but we
4:38 get they're not they're a little bit
4:40 convoluted oh I guess there is length
4:42 there's length unit of measurement so
4:44 maybe maybe you could break walls and do
4:47 that but I like what this other person
4:51 had done which I'm going to show you
4:52 right now which is that we've got using
4:55 a
4:56 cabinet going to place the cabinet okay
4:59 and let's just rotate this around and
5:01 I'm going to snap this to just the
5:04 framing layer so we've got no ziting in
5:07 the case of this cabinet and
5:09 then with a cabinet we can extend this
5:11 all the way
5:13 out next I want to bring this to my main
5:17 surface layer and then hold control and
5:19 just bring it slightly inside of that
5:21 surface layer and we'll do a few things
5:24 one is we're going to put this on its
5:25 own custom Layer Two is that in the 3D
5:28 preview over here let's just turn on
5:30 Vector view you can select toekick hit
5:33 delete and will actually delete that
5:35 element so I could very quickly delete
5:37 all these things and just leave myself
5:39 with a door drawer and that door drawer
5:43 when I select this I actually want this
5:45 to be a door panel so I don't even have
5:47 to worry about hardware and do I care
5:50 about the display of the Box we could
5:53 make this a no display box if we wanted
5:57 to um where we're making left side be
6:02 none right side also none
6:08 backside now this is almost a no display
6:14 box where we go into no top no bottom
6:18 really
6:19 all have a we go framed and set to zero
6:24 really just have the door left over
6:26 right but the Box still exists it's
6:28 still there
6:30 and so what can we do with that we can
6:31 set this to have a fill style like grid
6:34 angle which is what this person's doing
6:37 in their view the only other challenge
6:40 here is that we need to set the draw
6:42 order and go and pick a draw order that
6:44 is in front of walls right so we can CH
6:47 openings this case press okay so now
6:49 we're showing that fill and in the case
6:54 here
6:55 um we do actually want this on its own
6:58 layer so that we can control its line
7:00 weight Etc so in the layer panel um in
7:03 this case I'm going to move it to
7:05 something I already had set up in the
7:06 brace in my Pro Plan which is
7:10 cadb right and so that's got its own
7:12 line style
7:14 now now here's the thing that I think
7:18 was missed in terms of having having the
7:22 opportunity to make this be really
7:24 really Dynamic is that one is that I
7:27 want to um when I'm showing this in a
7:30 braced wall plan I do want to show some
7:34 kind of a label and it's not going to be
7:36 my default base cabinet labels instead
7:38 it's going to be something just like
7:40 width um but there we go width is going
7:43 to be the width of that brace wall panel
7:46 in this case okay we just need to make
7:49 sure that our door box construction full
7:52 overlay with no reveal we actually want
7:55 the door to be the same size as the
7:58 cabinet so there our label 24 in and
8:01 could we do something a little bit more
8:02 Dynamic maybe we could in the schedule
8:06 where we're
8:07 choosing um automatic label includes a
8:10 schedule number or we're showing a call
8:13 out Etc we'll get into that maybe um but
8:17 for now let's just make this be the base
8:21 Improvement that I want to establish
8:23 here and so the next thing that I want
8:25 to do because this is placed inside of a
8:28 wall it might be outside of the bounds
8:30 of a room so from finished floor might
8:33 actually be referencing external room
8:36 which is at an um at the floor height of
8:39 our stem wall offset or something like
8:41 that so let's now switch this to
8:44 Absolute elevation elevation at bottom
8:47 should be
8:48 zero okay and then the next thing I want
8:51 to do is I want to set this to
8:54 be you know if it was accurate we would
8:57 actually push this down below below um
9:00 our our plate line so that 0 in is
9:03 correct but it would also
9:05 be of our plate so yeah so what I would
9:08 want would be this be the height of my
9:11 floor structure so I'm going to say this
9:12 is 96 in I'm also going to make this 48
9:16 in width right and then let's just move
9:19 this down the line and make sure it
9:21 makes it all the way to the
9:24 corner and we can even snap it to where
9:27 it's supposed to be snapped one or two
9:30 so what's the next step well I think
9:33 there's an opportunity to do something
9:35 really cool and dynamic here so I'm
9:38 going to draw out a solid and the
9:41 solid's going to be um let's just make
9:44 it 48 by
9:48 96 play here that's fine so here's that
9:52 solid
9:55 and do I even need a solid yes I do okay
9:59 and so I'm going to make the height of
10:00 this be 3/4 of an inch and we're just
10:02 going to give this an absolute height
10:04 we're going to say that this is no 18 in
10:06 doesn't
10:07 matter all right I've drawn this solid
10:12 and now I want to use my line tool to
10:14 kind of split this up I'm going to snap
10:15 from here to here here to here just so
10:18 that I can draw one more line and use
10:22 all that as snap points so that I've got
10:24 a triangle and I can concentrically
10:27 resize this I'm going to drag my cursor
10:29 straight down and then hit tab or enter
10:34 and I've got polar checked it should
10:36 pick up 90 which it did so maybe I want
10:39 my offset to be half an inch okay so now
10:43 I've got a half inch offset there let me
10:46 actually use that line tool again to
10:49 come in here and draw my other
10:54 triangle and in fact I could even shake
10:57 that triangle and just convert it to a
10:58 3D solid bam there we go
11:03 and let's just that's I can just press
11:07 okay same thing concentrically resize
11:10 this I want to click right here in case
11:14 or actually
11:16 no centrically raised
11:20 size how did I do that before no I'm
11:22 missing it I use this one there we
11:27 go I say half an inch
11:29 losing my mind there and actually
11:33 something that would be really fast and
11:35 easy to do is Select both of these HT
11:40 them solid
11:43 hole
11:48 he polyline
11:51 first made a mistake in the pretty solid
11:55 hole there we go
12:00 thing this one doesn't want to let me
12:02 build a
12:03 plain oh it is already a plain poly 3D
12:06 solid hole there we
12:08 go should be able to reflect about
12:12 Center make that next hole
12:17 center are we left with what are we left
12:23 with feel like that didn't quite get me
12:26 look
12:31 yeah I didn't quite get this
12:34 right and we select this
12:38 hole
12:40 maybe looks like we have multiple solids
12:44 here
12:46 do yeah it's cuz I reflected this about
12:49 itself little bit goofy so I would have
12:53 needed to do a little bit of work
12:56 before go back up a little bit so use
12:59 our
13:08 action there we have
13:11 now we have
13:15 polyline poline all right let's reflect
13:18 this about now we
13:23 can all right and can we group select in
13:27 really what I want
13:30 now convert all these to 3D solid holes
13:32 perfect there we go that's what we're
13:34 looking for bam so now we have this
13:38 shape and I want to convert this
13:41 selected to a symbol that is a cabinet
13:43 door adved option
13:46 yes and you'll see what I'm doing with
13:48 this in just a minute I'm going to in
13:52 the 3D menu rotate this up on the X here
13:55 we go right and then material we should
13:59 have painted this beforehand but let's
14:01 just go ahead and choose black
14:04 sure single click here you can even
14:06 change this viare to
14:09 frame name the
14:12 component that just ends up showing up
14:14 [Music]
14:18 on so here's what we've got we got a
14:20 cabinet door it looks like an
14:22 X so how do we utilize this what is it
14:26 going to do now this is loaded in
14:29 well for
14:30 one I need to make sure that that CAD
14:34 layer is turned on in my video
14:38 here I'm showing I'm going to show you
14:40 what I'm trying to get to as a finished
14:42 product okay which is let me back to my
14:46 working get into an elevation here and
14:49 in my elevation I want to turn on my cad
14:52 layer brace
14:55 wall and with that
15:00 I also need to get over to
15:03 cabinets I need to turn on door drawer
15:07 look at what's showing
15:10 up
15:14 right so this is showing up and now I
15:17 should be able to get to my library take
15:20 that cabinet door drawer which we need
15:22 to
15:22 rename um race wall panel parenthesis
15:27 cabinet door
15:29 parentheses and hover over and click and
15:32 replace and look at that and wouldn't
15:36 this be a pretty fantastic
15:38 representation of wall
15:40 plan we're actually showing the width of
15:43 our braced wall panel correctly where it
15:46 needs to be how do we bring this around
15:51 circle
15:53 is back to our braced wall
15:56 schedule open up one of these polylines
16:00 and we got a few things we would need to
16:01 copy here copy over is there a fast way
16:04 to copy it um I'm not sure that there
16:08 is can we drop a cabinet in a cad detail
16:13 not sure that we
16:15 can I copy this and paste it no can not
16:21 so what can we do we can take this line
16:24 copy paste line over
16:29 and possible to use the object
16:31 eyedropper tool to pick up all of our
16:35 object
16:37 information or custom
16:39 Fields
16:41 possibly we're in Marquee
16:45 mode and can I tell
16:52 this schedule
16:54 panel include this as
17:00 panel that do something
17:06 here not so
17:10 far
17:14 why should be ball
17:18 panel okay so the custom Fields
17:22 didn't otherwise it
17:26 woulding information
17:29 oh no it is that actually did work that
17:31 actually did transfer that
17:34 information so question is why is this
17:38 not actually reporting BRAC wall panel
17:41 that schedule can
17:46 we find schedule from
17:50 object does in fact show that here oh
17:54 well it is a 48 inch item so what
17:56 happens when we delete this that's it
17:59 that's funny that first line is actually
18:02 it we just had a line that was 48 in
18:04 here as
18:05 well no no oh because we don't have
18:09 length so it's not distinguishing any
18:12 specialized things so minimum panel
18:14 length
18:17 typical and then I'm showing actual
18:19 length so maybe we want to add something
18:22 to this schedule which would be actual
18:26 length so
18:28 take this open it up get an object
18:33 information create a new field Add a
18:40 prefix length of panel format it as a
18:46 number get to that
18:50 field then in this case it's just going
18:53 to be
18:56 width press okay
19:00 let's get to our brace wall panel
19:02 schedule select a call out
19:08 symbol and find length of panel which
19:12 sometimes this puts it at the bottom of
19:14 the stack no it
19:18 didn't yeah
19:22 Here length of thought I
19:26 did figure out why I can't
19:35 brace wall panel that
19:43 prefix panel symbol add there it goes so
19:49 let's get into number formatting make
19:51 sure that we're actually showing this
19:52 the way we want to show it which is um
19:55 smallest fraction we're just going to
19:56 show it a one one here and and then
19:58 units is going to be inches making sure
20:01 that this is reporting solid units
20:02 there's our 48 in panel do I get to get
20:06 rid of these now yes I
20:08 do um this guy is in plan so we need rid
20:12 of that as well now in this view only
20:18 active play options cabinet labels
20:22 should show our call out PPE plus our
20:25 length of panel if we
20:27 want or we could just use the
20:31 dimensioning tools to Dimension them
20:34 another kind of dynamic thing that we
20:36 could do
20:40 um could kind of division based on their
20:49 length objects all out item drag this
20:53 through and size of it and then if I
20:58 went and and created a new dimension
21:01 default get into active default control
21:04 let's just do um because we're
21:07 dimensioning cabinets I might as well
21:08 get to my nkba standards and hit the
21:11 plus sign and make this a brace wall
21:14 panel
21:19 Dimension I'm was just going to call it
21:21 bwp that's it I like to keep things
21:24 short there there's a reason for that it
21:25 truncates actual
21:29 Dimension drop down menu nice if you Bas
21:32 on
21:33 your and now we are going to
21:37 locate I guess locate automa we could
21:40 try locate automatic no
21:43 can't designate cabinets in
21:46 cabinets sides should be all that I need
21:52 and we only
21:55 want we only want our exterior
21:58 do not need to show wall
22:03 wids going
22:06 from probably the wall Dimension
22:16 layer press okay B for
22:21 this what
22:23 happens and it's a 6 inch reach so we
22:25 got to drop it right on top maybe we'll
22:27 change the reach up the reach a little
22:30 bit Go
22:33 24 now now that's dimensioning my oh got
22:38 going to the wrong
22:46 layer got of Dimension framing but we
22:48 might make a new cut I I don't like
22:50 making a bunch probably
22:56 just but there would be
23:03 Dimension our brace
23:06 wall and what cool about
23:12 this
23:14 add add text here
23:18 wood um after I make another active
23:21 default another active
23:24 defa let's bring in
23:35 I actually think vaults add
23:40 construction or this view this this is
23:44 being design for this
23:48 View Auto labeling here want this
23:53 separate convention main con using a or
23:59 so this case we
24:03 want we want to define the
24:07 rules a vertical count format we're
24:10 going to
24:16 go Roman
24:20 num
24:25 yeah okay
24:32 that out now we should be able to come
24:34 in here with the construction line
24:37 tool and just drop this right there
24:54 for this dire
25:01 they they should give us more
25:05 form
25:16 fight if we
25:19 had
25:24 startingly maybe we would change the
25:26 shape know maybe that would be
25:32 right set this as defaults for this
25:37 view able to use we back
25:40 through
25:42 usually app
25:51 here right and so those would
25:54 distinguish lines
26:02 and would it be
26:06 interesting bam got another thing
26:15 going oh it's
26:17 picking that's where that reach kind of
26:19 hurts
26:20 us have to do
26:31 but could you drop this line
26:33 in on that length say that this by
26:38 adding
26:45 text a mention it that do
26:51 something down and think
26:53 about but I think this is I think this
26:56 is it I think the proof concept
27:00 here
27:02 strong got a bunch of custom Fields
27:04 they're
27:06 reporting your values here reping their
27:12 connection scheduled list got the call
27:16 out symbol come back to plan see
27:20 these back here we could even turn on
27:24 our
27:26 label right
27:30 and you see the call outs
27:39 here pretty strong showing pretty cool
27:42 system start of
27:47 system think I want to leave it at that
27:50 let you guys the viewer check this out
27:58 with with this I know not everybody has
28:01 to do a brace wall
28:06 plan very cool thing thinking about uh
28:09 you know I always got to think about the
28:11 cover art for
28:13 my something I could do for cover art is
28:16 take this back to just black and
28:22 white elevation I'm going to bring this
28:25 inside of my
28:28 got this got
28:32 our line style here for our footing take
28:36 out the color and
28:39 then then maybe I'll kick the skirt of
28:42 the
28:44 perimeter that so we see it and now
28:48 that's a pretty
28:51 solid cover
28:53 art window in
29:07 is what will be on the cover
29:09 art cool see you soon
29:21 [Music]
