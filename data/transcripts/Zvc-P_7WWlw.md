---
videoId: Zvc-P_7WWlw
title: Switch Zone Macro in Chief Architect - What if you could do things automatically based on a zone?
url: "https://www.youtube.com/watch?v=Zvc-P_7WWlw"
status: imported
---

# Transcript

0:05 VIP um I was messing around with my Pro
0:08 Plan
0:11 and what if we could
0:13 take this is a thought here's what I was
0:18 thinking like people want different lot
0:23 analysis depends on
0:25 their area right depends on their
0:28 planning department Etc
0:30 um and I was like you could just like
0:33 tap two notes together and it would know
0:36 that we want to add those two notes
0:38 together as a as a new thing and how
0:41 cool would that be and then I was
0:44 like
0:46 thinking well wait a
0:48 minute we have XY we have
0:51 XY so like what if I
0:55 took I took a polyline here and I said
1:00 Place anything inside of this
1:03 polyline and whatever you put inside of
1:07 here will be
1:10 totaled right whatever you put inside of
1:13 here will be totaled in your lot
1:15 analysis just as a
1:18 total
1:21 um like you don't have to Union it
1:24 nothing you literally just drag it
1:25 inside of there
1:30 and then I was
1:33 thinking what was I thinking I don't
1:36 know I don't know where I'm going with
1:37 this but I kind of want to do a proof of
1:40 concept so I have a new tool that gives
1:43 me XY which I love that's awesome um
1:47 clearly not working already there it is
1:51 okay
1:53 so let's just move this to an absolute
1:56 point so we could just just move this
1:58 tab input absolute point and let's just
2:01 put it
2:02 to -500 and 500 why not there it's
2:08 that's that's where it's going to
2:11 be we're going to move
2:14 another Point
2:16 here and it's going to
2:18 be
2:20 1,000 and
2:23 250 maybe it'll be zero
2:30 right okay so that's going to be my
2:32 polyline so I'm going to take this snap
2:35 it to
2:36 here and then drag this
2:39 down there you go so anything inside of
2:42 this box I'm going to
2:45 say we're going to
2:49 Total right my XY is not working that's
2:52 funny it should be XY position finish
2:57 floor fix of course always
3:01 um okay so let me fire up this is going
3:04 to be this is not an organized video if
3:06 you're watching this video you know
3:09 you're
3:11 just
3:14 strange or you're just learning like I
3:16 am and and you're here for the ride
3:21 sweet uh
3:24 welcome
3:26 so firing up CLA I use Claude and ch gbt
3:30 now because when one doesn't work I send
3:32 it to the other I have them error check
3:34 each other there we go so let's just
3:38 start with a chat um and I have to
3:41 formulate my thought here and let's
3:43 double check our reference markers which
3:46 aren't actually showing us XY and they
3:48 should
3:49 be um know why that'd be a really good
3:53 thing to just fix because that would
3:54 make my life a lot
3:56 easier these are
4:11 okay that's weird I fixed this and
4:14 then it resorted back to a previous
4:17 version so let me get these back in
4:22 again I know that I fixed
4:24 these right now that going to give me no
4:28 clearly I did not fix them
4:34 strange let me look at this
4:37 code going
4:40 on if y position is greater than zero
4:43 Supply the format or
4:45 Y yeah this is missing all the code
4:48 about layer sets if it's not in a
4:50 particular layer set it shouldn't be
4:52 showing me finished floor Heights oh
4:55 this is the one that shouldn't be
4:56 showing finished floor Heights um if
4:59 layer set down Clues layer set down case
5:01 include elevation or layer set down clu
5:04 that's the Y position stuff
5:12 else and then else if y position
5:17 great position is greater than zero oh
5:20 it gave me some finished floor height
5:22 thing again which we don't want so
5:24 that's the problem here this should been
5:26 an if
5:30 [Music]
5:31 uh and it's not giving me y position
5:34 this totally got scripted wrong what a
5:40 shame um I just want this to
5:45 do else if I don't need an if I just
5:48 need a um y position that's
5:56 it and then we need to get rid of this
6:05 [Music]
6:06 um do and Exposition I actually don't
6:10 know
6:11 theer
6:13 there
6:15 uh should be actually this it should
6:19 be pound bracket y
6:25 position and quotes quotes
6:35 o
6:38 bracket Expedition
6:41 quotes uh and
6:45 then uh why oh and I've got this
6:49 backwards so it should be Exposition
6:50 first
6:54 anyways and
6:57 then Bang
7:00 um I'm getting better at scripting isn't
7:02 this
7:04 wild that I even would know what the
7:07 heck I'm doing right
7:12 now pretty
7:16 well
7:22 um
7:26 background I don't care about the
7:28 decimal places not really
7:30 and we could go round
7:36 two there we go that's what I needed so
7:40 AFF height fractions what I
7:43 wanted there although that should have
7:46 been a new
7:49 line expect new lines in a mark
8:03 or you could just do you could have just
8:06 done this you big
8:09 dummy because that would have made a lot
8:12 more
8:17 sense right one of that made a lot more
8:22 sense um boy people think I come up with
8:25 great systems I do but it's on the tail
8:28 of a ton of
8:30 stupid little failures like
8:33 this right that's a better tool look at
8:35 that it's not as dynamic as the old tool
8:41 but right I don't know okay
8:46 so there we
8:53 go so here's where I need to reference
8:56 that so we'll just kind of shrink this
8:58 off to the side side so I can see this
9:00 as I talk
9:03 here you need a ruby code that is going
9:06 to assign a value to something if it
9:09 lives within the two marker positions
9:13 that are marker position one which is x
9:17 value of -500 and Y value of 500 and
9:21 marker position two which is an x value
9:24 of a th000 and Y value of zero
9:50 um and I forgot that
9:51 just I'm being an idiot so
9:55 um marker position is at actually a
10:00 known
10:02 variable which
10:04 is
10:06 exposition and Y
10:13 position oh and we can't use puts so get
10:15 out of here
10:20 puts sometimes I'll just remove it
10:22 myself
10:27 um don't put a here okay so do not put a
10:31 test inside of my Ruby script I will be
10:34 testing it without the need of running a
10:36 test within the script itself and then
10:38 also puts is implicit in this Ruby
10:42 environment we're using Chief Architect
10:45 so we will not be using puts instead
10:49 just insert the call and it will
10:52 execute on its own line
11:09 okay remove marker as a prefix remember
11:13 that Yore position and xcore oh actually
11:19 you know what it's
11:21 doing oh watch my language um
11:25 interesting let me test this what's
11:27 going on here try this out
11:30 so just throw in a little new macro
11:36 test bam okay evaluate
11:40 and it has an error because main object
11:46 sure we want this to be an owner object
11:49 sure we need to throw a note in here
11:54 something and let's just throw in that
11:57 test which did
12:00 was able to
12:03 execute
12:06 okay and actually easier than that would
12:09 be
12:11 this valuation error why okay figure
12:16 this
12:18 out error to find local variable or
12:21 method oh really we don't have
12:23 Exposition
12:25 for test
12:29 um also I don't know why I'm working in
12:31 half the screen here but let's just drop
12:33 this search in
12:36 here
12:41 and let's look
12:43 for x or y
12:48 search so there is no XY
12:52 for text but there is
13:00 okay that's
13:03 fine and and wonder what the workaround
13:06 is for XY for texts so um all right note
13:10 selected let's go get our test macro and
13:13 look at this It produced
13:16 outside inside
13:18 outside it's saying that it's outside
13:21 but it's actually
13:25 inside why let me look at this
13:29 could have been located in so marker
13:33 Exposition
13:36 500 two
13:43 exp um and I want to see what's
13:50 Exposition is 787 so we know that that's
13:54 between marker 1X and marker 2x if and
13:58 so here's the Tex x if x is greater
14:03 than x is greater than marker exp
14:07 position and X is less than marker 2
14:11 position they're not defining X Define
14:14 within marker positions
14:18 XY how they I don't get scripting enough
14:22 to know what's happening here how are
14:24 they defined within marker positions X
14:27 and Y
14:30 how are they translating X and Y to
14:37 Exposition oh because they're doing it
14:42 here okay so if x which
14:46 is being established here is this is a
14:51 method and this is the call to that
14:53 method and it's taking X position
14:56 putting in an as X and Y position
14:59 putting in y so if x is greater than
15:02 marker
15:03 position one and marker position 1
15:06 is500 it's not greater
15:09 than okay so we need here's the problem
15:11 got it
15:14 check the problem with this script is
15:17 that we need to know that greater than
15:21 is flipped
15:23 if it's a negative position value
15:27 meaning that
15:29 800 is between 500 and th000
15:35 versus just positive 800 is between
15:39 positive 500 and positive 1,000 so when
15:42 I have a marker that has X position
15:46 at800 that is in
15:48 within inside the box so you're greater
15:51 than or equal to statement is not
15:54 working
16:01 okay
16:10 sweet I wonder if
16:14 that they get didn't seem like they got
16:17 the logic
16:18 there there should be a condition if
16:29 so I should be able to throw in some
16:30 markers and have globals be indicated in
16:34 those markers and that establishes my XY
16:37 position that's the next step but for
16:40 now we're just trying to see if we can
16:42 even get a working code right so now it
16:45 is registering as inside and so let's
16:48 just throw test into the
16:52 label that we can see this and test
16:56 it right there's inside
16:59 let throw a little capsule on this let's
17:02 also size it the heck
17:06 up
17:09 right um inside bam now outside inside
17:17 outside that's cool that's cool so what
17:21 do we do with that so now I'm giving you
17:24 a tool
17:26 where you get to set two two
17:31 points oh wait a minute what is a
17:33 polyline
17:37 report what is a polyline
17:40 report okay let's use our little Search
17:42 tool
17:45 here what measurements do we get we get
17:49 oh that's right we don't get as sides
17:51 all we get is
17:55 area these are measurements right and
17:58 then on top of meas measurements let's
17:59 see if we get any X or
18:02 Y nothing custom pattern XY scale no
18:06 nothing okay so you can't set a polyline
18:08 as a Zone but it could set markers as a
18:11 zone so the start of a Zone and an end
18:14 of a zone right can
18:16 you
18:20 group marker polyline and
18:24 grow the
18:26 group yeah you can
18:29 I mean that
18:31 works and so that can report its
18:38 Zone okay and we don't even want to
18:41 label on
18:42 it
18:44 right this is cool this is cool okay
18:49 so
18:57 explody so I don't need to I don't need
19:00 to have a label here we don't need to
19:03 have anything here all we need
19:11 is all we we need an inline code to
19:17 execute
19:21 um we're going to do Marker one marker
19:27 two so
19:32 be great if we could do this for
19:33 multiple instances right because then
19:36 then you could utilize this to build a
19:39 bunch of different
19:42 systems
19:45 right and in which case I was going to
19:47 use globals
19:50 to to set the Box
19:52 parameter you kind of have
19:55 to Global is meaning that these two
19:57 markers report a global value that's
19:59 going to be picked up in our new
20:02 macro right but it would be nice if they
20:05 had some kind of a
20:07 unique name every time I've I've I've
20:11 yet to figure that out creating a unique
20:13 name every time because otherwise it's a
20:16 one use case until you build a second
20:18 tool um so then it kind of makes sense
20:23 to understand what I might even want to
20:25 use this for I was thinking area
20:27 analysis what else would be cool to use
20:31 this for being able to place things in a
20:33 Zone
20:36 um you know my system
20:38 of picking out what detail annotations
20:42 are
20:45 um that could
20:48 be that could be something
20:54 um I have a new system
20:57 where switch to if we just go to Project
21:00 label options I have a system where you
21:02 get to set all your options for all the
21:04 nomenclature within my Pro Plan but I
21:07 could make it so that every one of these
21:09 lines was a note so that you could save
21:11 your own notes for your own preferences
21:14 and then drop them in a Zone and that
21:17 would apply I mean that's pretty wild um
21:20 could do
21:22 that because then you could just drag
21:24 and drop never have to type bam very
21:27 cool
21:29 [Music]
21:30 um especially if you just had your
21:32 options out here and just dragged them
21:33 in super
21:36 cool
21:37 so you'd need a unique setup this would
21:40 be the use case for having a unique
21:42 setup um where every marker had its own
21:46 Global
21:49 but for more of a dynamic thing where
21:51 you're just setting up a Zone and you're
21:53 saying hey
21:54 let's tabulate everything that's in this
21:57 Zone
22:01 like areas right like what if we want to
22:04 just total areas so we're going to Total
22:06 anything that's in this Zone this macro
22:08 gets way more complex clearly as we're
22:10 going to as we go to build this out okay
22:14 so here's the next macro I need and
22:16 let's just write a new Claud and we'll
22:19 come back to this
22:25 one write a ruby code for Chief
22:27 Architect remember that puts is implicit
22:30 you just need to put your call on a line
22:33 by itself and it will
22:34 execute that being said I need a code
22:38 that picks up X position and Y
22:43 position and reports it to a global
22:46 variable go ahead and pick the variable
22:48 name I don't care what it is
22:52 then I want the Ruby to report
22:57 nil because because this is going to
23:00 exist in a publisher that we need to
23:02 make sure does not report or show any
23:05 values in order to keep the size of it
23:09 down so its sole purpose is to establish
23:13 Global
23:20 variable fix y position X position
23:32 so position equals nil Define update
23:38 position sure okay um I learned
23:43 something new today you could
23:45 actually create this method as a Helper
23:52 and position 10 and
23:57 20 uh
24:02 um not put a test in my
24:14 macro um you can actually put in the
24:17 scripts folder within Chief
24:19 Architect methods and request those
24:22 methods for things that you're going to
24:24 use over and over and over again so this
24:28 is one of those things that we could do
24:30 over and over and over again uh Define
24:33 update position position XY position
24:35 equals n
25:01 there we go now you figured it
25:06 out
25:07 so that takes position XY
25:12 okay and that's that's what I
25:15 needed so the first one
25:26 is actually I just kind of want to put
25:28 that in you need an inline code you know
25:31 what works really well I have an inline
25:34 code
25:36 Builder this would be a lot more
25:40 efficient
25:42 so and how do we need this to be
25:44 reported what's our T code here um we
25:52 need just needs
25:55 X so we're going to say
26:00 we're going to add something translates
26:02 whatever we send to the global
26:06 okay back to chat GPT and inline code
26:12 Builder where is it there it
26:15 is I need an inline code that
26:21 defines a global variable called
26:23 position
26:24 one as X position
26:28 comma y
26:30 position and
26:33 then set the output to
26:47 nil I don't even like to think about
26:49 this stuff I always study it though in
26:51 case I can remember how it's done um so
26:53 that seems pretty
26:55 simple position it forgot the global
26:57 position one 1
26:59 equals yeah okay so no problem here so
27:03 let's go take this marker see if we
27:05 can't get this done now so here's the
27:09 code and we're saying Global position
27:20 one and Ill that should mean that
27:24 there's
27:25 no there's no line in the minimum length
27:28 is
27:32 zero should be able to just drop that
27:38 down almost want to make this marker
27:40 almost
27:41 disappear right we could do that but
27:44 that's okay we don't need to so that was
27:47 position one let's go position
27:50 one
27:52 right okay next here's position two
28:03 bam get minimum length cut that
28:06 down
28:08 right that's fine
28:12 perfect
28:13 this of all
28:17 this this
28:19 note should now be able to block
28:23 this
28:26 okay now it
28:30 still blocks
28:33 beyond the square and wouldn't that be
28:36 nice if it didn't do
28:39 that and how could
28:42 I edit the C
28:45 block
28:48 ow this marker is here I don't know why
28:51 it's seeing it way past that
28:56 marker can almost just bring this just
28:58 inside and what would it even
29:06 matter probably wouldn't
29:11 but it's fine um man it would be sweet
29:15 if it was just right on the money though
29:17 you know what I
29:18 mean this was just snapped completely
29:21 wonder why the marker takes such
29:24 a large bounding box cuz when you select
29:27 it it doesn't do anything wonder what if
29:29 it has to do with that line length I
29:32 mean it kind of does it looks like
29:37 so can we just make this make this
29:40 something else test boring bam
29:44 easy right or Point marker Point marker
29:47 even
29:52 easier Point marker bam okay now when
29:56 you select these still does that how
30:00 funny what's that basing its size on oh
30:03 it's still seeing a length here what is
30:06 this
30:08 length
30:13 um character height 27 in let's just go
30:17 zero in okay and minimum length is set
30:22 to 19 there we go that's set to zero
30:26 now that hopefully fix
30:35 some here here radius let's just put it
30:40 at zero why not I know it's there I'll
30:43 find it I will find
30:48 you so now there's marker here and
30:50 marker here set to
30:53 zero f radius set to zero
30:58 that's position one position two okay so
31:01 now what happens when we select it look
31:03 at that bam okay so we got a sizable
31:07 quadrant that we've now built
31:10 cool next let's get back to Claude and
31:15 say um let's go back to our acros I
31:21 actually don't know how to get to my
31:23 here we go sign value blah blah blah yep
31:26 okay
31:29 perfect now I have updated it so that we
31:32 are going to get X position and Y
31:34 position from a global
31:41 variable for the first position and the
31:43 second position the first position's
31:46 Global variable
31:53 is
31:54 position one position one is that what
31:58 was and let's just draw in a text box
32:01 here and test out our
32:04 Theory position one like
32:08 that bam okay so it reports as a text
32:14 string with
32:17 brackets right if we were to let's just
32:21 test this test
32:23 two and position one
32:29 and EV
32:31 valid shouldn't need an owner class or
32:35 anything um oh
32:38 underscore underscore
32:41 one that's not doing
32:45 anything didn't matter that's owner
32:55 or not giving me anything why not
32:59 um what is this a hash
33:07 value should change its numbers does
33:09 that change its
33:12 numbers oh no because it's coming from
33:14 this this should change its y okay
33:19 um so it shows up it as it looks like a
33:24 a
33:26 hash wrong
33:29 sure okay
33:41 so think we did
33:45 Exposition
33:49 position yep
34:10 hopefully stands what I'm saying
34:13 there okay Mar Exposition position one
34:18 position yes comma yep comma Bam Bam Bam
34:22 outside all right let's see if that
34:23 worked wouldn't that be easy see how
34:26 easy it is to write code
34:28 no it's not um it took a long time to
34:30 kind of learn what's going on and now
34:34 that I have a better understanding
34:36 that um it helps me troubleshoot things
34:40 and
34:43 have better what I'm
34:47 doing so what happens when I do this
34:50 nothing
34:51 oh
34:53 okay this work I love it when look at
34:56 this dve it right over here a't that
35:01 cool that's so cool okay so
35:06 next cool
35:08 um next it might be that
35:13 let's we're going to
35:15 give option to an end user um to figure
35:20 out what they want to use this
35:24 for no that'll be down the line can we
35:28 can use it for something else what do I
35:30 think that we would use this for I think
35:32 that we would use this to
35:35 total total some polylines maybe
35:46 um possibly total some polyline can we
35:50 add this to a
35:53 schedule is the next thing
36:00 no it's
36:06 that it's what what happens here how
36:09 does this work so when we throw
36:11 something in it knows it's in that
36:15 zone so it is now a it's a trigger it's
36:19 a switch so now it's a yes
36:25 condition so now I need something that
36:28 says hey if this is yes and this is yes
36:32 and this is
36:37 yes then we include
36:40 it in a
36:46 schedule so one way to do that can I get
36:49 this to report to a schedule that's the
36:51 big question
37:03 don't know if I
37:05 can't we open this if we edit the
37:09 cab take this we open
37:13 this seems like it might be able
37:16 to go to a custom schedule
37:25 inclusion Happ be fre
37:30 save
37:31 instances and
37:36 now put a custom schedule in that
37:44 includes
37:48 clusion okay
37:54 okay so
38:01 that's a custom schedule that can now
38:04 take conditions that are yes conditions
38:08 and add them up as
38:15 totals so what we using this for
38:29 so it's anything you want to add
38:32 up
38:36 anything no anything you want to include
38:39 in
38:43 schedule so let's say you drew a bunch
38:45 of polylines for things that you have to
38:47 add in your lot things I don't need to
38:51 add just draw a box and you throw those
38:54 things in that box suddenly they
38:57 populated in a schedule it's by area and
39:01 description that's
39:13 it so that's one use case what's another
39:16 use
39:19 case um
39:31 well so except for that it needs to have
39:34 an XY position and area poly don't notes
39:38 do so this is what else has
39:46 XY that's another good question what El
39:49 says
40:03 think well let's just do a little search
40:21 boo
40:23 cinet wish my stay where I put
40:31 s stay
40:34 it
40:41 why no
40:44 no a line
40:50 XY no it
40:54 doesn't fall out
41:06 does so a call out a note a
41:11 marker those all have
41:17 XY is that strange that text isn't want
41:28 because it's not a so basically anything
41:30 with a center point so with that thought
41:35 that should mean that a oh look at that
41:39 big
41:41 old should mean that yes an elevation
41:48 marker oh wait this is a call
42:01 think you can't even snap to an
42:04 elevation marker snap to the center line
42:07 so no an elevation camera doesn't
42:11 have
42:15 why so just call out and notes are going
42:17 to be
42:19 markers thing that you could use this
42:21 for
42:34 okay so I'm kind of back to thinking
42:36 that yeah this works for
42:39 um adding particular parameters that are
42:43 captured in
42:45 notes and then we're back to one of the
42:48 biggest one of the biggest dumb things
42:52 that hasn't made it into Chief's newest
42:54 versions is that we have no reporting
42:56 value for the easiest portion of a note
43:00 which is the text input there's no
43:02 reporting value for text it's freaking
43:06 crazy still think that's just the
43:08 craziest
43:09 thing
43:12 um you always just have to code right
43:15 here if you want this to be your main
43:17 input that reports somewhere else you
43:19 always have to make it's just
43:25 ridiculous okay
43:28 so we know we can drag a note into an
43:30 area and get it to automate you know
43:32 what I think I'm going to stop recording
43:34 I'm going to have to sit down and think
43:36 about what I could do with this now that
43:37 I built
43:38 it stay tuned I guess right or give me
43:43 some ideas chime in please I'm dying for
43:46 people to to talk to me in the comments
43:48 because that really drives content so um
43:52 yeah leave some comments come up with
43:54 some ideas we can use a note we can use
43:57 a call out use a marker and just by
44:01 dragging that into a Zone we could have
44:03 that report anything from object
44:07 information Fields it can technically
44:09 report things from other places because
44:13 notes and notes have object information
44:17 Fields panels and that can pick up a
44:21 global from somewhere else and report it
44:24 to a schedule so you can link while in
44:28 call outs you can link you can link a
44:31 call out to a cad
44:34 detail or a
44:36 camera or anything
44:39 really and that way if you drop a call
44:43 out in and it's linked to a camera you
44:46 could say let's I don't know change the
44:50 name of the
44:52 camera is what you could
44:55 do for instance you got to think big on
44:58 this one there's a couple little layers
44:59 here let me just draw this out as a path
45:03 so you've got you've got a
45:06 box you drop the call out or the note
45:09 we'll drop both in here there's the call
45:11 out and this
45:16 this can
45:20 link and
45:23 report from cameras
45:27 and CAD details and
45:31 schedules it can like if a if a schedule
45:35 is in your plan it could link to a
45:37 schedule right so that's something that
45:40 we can do a note has an OIP which means
45:45 anything in this field
45:48 value anything
45:55 in any anything in the notes field can
46:01 report to
46:04 schedule um the call out can technically
46:07 report to schedule
46:09 because um it's in this zone so we can
46:12 use the
46:14 Zone we can use the zone to
46:19 report some Global TOA schedule right so
46:25 if the call out is within this is so if
46:27 we say
46:28 hey um if something's in this Zone and
46:31 it's a call out we want to add
46:33 whatever's in the text above line to a
46:37 schedule and report that all right and
46:40 that thing could be something it's
46:42 linking to such as a page label for
46:46 instance
46:48 um in terms of the note same kind of
46:51 thing you could put any Global in a note
46:53 in the OIP and the note can report to
46:56 schedule these both can report to a
46:58 schedule the polyline and the note can
47:01 report to the same schedule if for some
47:04 reason you needed some kind of Tandem
47:06 setup there so a number of different
47:09 things we could do here um brainstorm a
47:12 little bit think big ask questions why
47:15 not thanks for watching
47:21 [Music]
47:28 oh wait oh wait oh wait hold on I'm
47:32 back I
47:34 forgot you can't block a note with
47:37 something else but you can block call
47:40 out with something else like a
47:43 polyline so we know that a blocked
47:47 polyline can still report to a schedule
47:49 so now this is picking up that it's
47:54 inside and maybe
47:58 somehow in the cad block CAD blocks can
48:01 have labels so that means it can execute
48:04 a
48:05 macro so now we know that we can drive
48:09 something with this polyline so long as
48:11 it's grouped with a call out I don't
48:14 know if that helps but I don't know
48:17 another
48:18 another capability if you will so
48:22 maybe what else can we group things with
48:26 right what else can we CAD block things
48:27 with um with a call out like this so
48:32 that just opens up the doors a little
48:34 bit
48:35 more you can't CAD block certain things
48:37 but you can CAD block polylines with
48:40 call
48:40 outs all right talk mons to yourselves
