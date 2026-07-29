---
videoId: CKG7Ys5c48k
title: Building The First Automated Roof Vent NFA Calculator In Chief Architect
url: "https://www.youtube.com/watch?v=CKG7Ys5c48k"
status: imported
---

# Transcript

0:01 Well, I tell you what, VIP, in the
0:03 pursuit of creating
0:05 a easy to
0:07 do roof vent
0:11 calc, I've come up with so many
0:15 directions
0:17 and they all
0:20 suck. They're all no good.
0:26 So, got to come up with something new.
0:30 And I think I might have come up with
0:31 something that is easy for the end
0:35 user.
0:36 Maybe.
0:38 Maybe. Here's what I'm thinking. I'm
0:42 just going to throw Feel like this is
0:44 actually really easy. I think this makes
0:46 it even easier than I originally
0:48 thought. We're going to work on a really
0:50 basic condition first. So, I'm going to
0:53 open this this polyline up
0:57 and let's change the fill style this
1:01 solid. We're going to set transparency
1:04 up so that it's similar to my existing
1:06 fill
1:07 style. And then actually, we're going to
1:10 change it to some kind of angle. And
1:12 this is where you get to create
1:13 essentially an index. Um because even if
1:17 you switch this back to solid, it will
1:18 still show its pattern angle.
1:21 And so what do I need? I need
1:26 a I need an
1:31 example. Um attic
1:36 vent, right? Let's just call it an an
1:40 eve vent or
1:45 something. So I because I just need an
1:48 NFA to start
1:53 with. I'm sure it'll list it right here
1:56 right
2:02 away. No. Oh, there it is. 43.3. Okay.
2:08 So when you're
2:10 doing angle, when I'm thinking about
2:13 this first part is that people might not
2:15 just want solid fill on their roof
2:19 planes, right? They might have some
2:22 standard that they're doing. So in that
2:24 case, we need to make this pattern angle
2:27 be as small as possible so that they can
2:30 change the convention. And so what we're
2:32 going to do here
2:33 is 0.0 0 basically 4
2:38 33 and then to get that
2:41 to that's net free area in square
2:44 inches. To get that to square inches,
2:47 we're multiplying it by
2:50 100. You're following me so far. This
2:53 means that the angle is, you know,
2:55 imperceptible in terms of print.
2:58 But did I use the right word there? That
3:01 sounded like I made that word up. I
3:02 think I did.
3:08 Uh, so we should just be able to get
3:11 what pattern angle is here,
3:16 right? Oh,
3:19 interesting. I don't seem to have
3:21 pattern angle anymore. We used to have
3:23 pattern angle. That's not true. There's
3:26 still pattern angle.
3:36 What do we have? Pattern angle. There we
3:38 go. Oh, it's a float. It's not a
3:41 measurement class. That's why it's not
3:42 showing up. Or no, my my search tool is
3:46 not working right. It still should have
3:48 shown
3:49 up. Oh, no. It was measurement. Yeah.
3:52 No. Okay. It's a float. Confusing
3:54 myself.
3:58 So, back to
4:02 this. Oops. Back to
4:11 this pattern angle. Okay. So, if we did
4:15 a
4:18 little little
4:23 this because it's a float, this should
4:25 work.
4:27 And we threw this in right here. And we
4:29 clipped it to that. That should Why is
4:32 this text so
4:34 small? Text is itty bitty. Itty itty
4:38 bitty. Why? Default textile. Why is that
4:42 looking so small? Crazy. That really
4:45 that small,
4:47 huh? That seems beyond small. What's
4:51 happening here?
4:54 Oh no, that defaulted my textile
4:59 on here.
5:02 Huh. Very
5:08 strange. X3 and scale defaults. Why on
5:11 earth did that get changed? I don't
5:14 know. I don't
5:17 know. Roof text defaults there. It's a
5:20 lot better.
5:22 All right, back on
5:28 track and then
5:31 round
5:35 two. That shouldn't have done that. That
5:38 should have been Oh, I need to put this
5:41 in
5:46 zip. I had very little sleep if you
5:48 can't tell. I'm feeling a little goofy.
5:52 All
5:53 right. So, I'm thinking that this is net
5:55 free
5:59 area,
6:02 right? So, that if I had an index of
6:05 fills and you could just and let's just
6:08 switch this back to
6:10 solid. I had an index of and then and
6:13 then switch our transparency. This
6:15 is there. I went the other way around.
6:18 No, 90. of that. Now, all you could do
6:23 is say, "Hey, for this
6:25 roof, I need net free area blah blah
6:29 blah." But there's going to be some more
6:31 conditions. We're going to check if
6:33 something's got a a ridge vent or not.
6:35 So, we we change the calc. But this
6:38 would be a thing where I can just report
6:40 this value to this roof if I sprayed it,
6:43 right? And so, let's see if that just
6:45 worked because it didn't seem like it
6:47 did anything.
6:49 No, it didn't do anything. Try that
6:51 again. Need a pattern fill. There we
6:56 go. Happening here. Yeah, that worked.
7:01 Bam. Okay, so we're picking up the net
7:03 free area of this roof. This means we
7:06 can have this value built into this
7:14 roof already. is this right here. Okay.
7:20 So, we could basically take all roof
7:23 planes in this case or the default roof
7:26 in this
7:29 case and just set this up in the object
7:32 information in the macro number input
7:34 and there you go. So if
7:37 we changed and added macro number
7:41 input and calculate totals some similar
7:45 rows and change this to square
7:51 in decimal places too. What would this
7:54 show up as? 4.33 square in net pre area.
8:00 Right? So, we're just indexing based on
8:02 a fill and this is calcing for us. What
8:05 this is doing is let's um just take
8:08 something else for instance. Oh, it's
8:11 not 4.33, is it? It was
8:13 43.33. 43.3. All right. I had my calc
8:16 wrong. Not the end of the
8:25 world. A thousand
8:31 So what happens here is we get to do
8:34 this all for these three right this is
8:38 giving us our total square inches net
8:40 free
8:42 area what's the next part of
8:45 this we need to know our
8:51 required and so little chat chat GBT
8:55 little temp chat
8:56 GBT give me what the calculatorul ation
8:59 is in terms of net free area required
9:03 per square foot of attic
9:09 space. Yeah. Yeah. Give it to
9:15 me. One square foot of net free
9:18 ventilation area one square foot per
9:21 300. Right? So we need one square foot
9:25 per 300.
9:27 And so we want the square inches to
9:29 calculate in square foot really. But I
9:32 don't think you just get to change I
9:34 always have to um remind myself here. I
9:37 don't think you just get to change the
9:39 unit. That's not true. Right. This isn't
9:41 going to immediately get us
9:43 to Yeah, it's still now it's just saying
9:46 43.3 square foot instead of square
9:49 inches. We have to do our
9:52 conversion. Okay.
9:59 So,
10:02 um I don't even want to think about
10:03 this. Was it times 144 or something? No,
10:06 it's divided by
10:09 144. Is that
10:13 right? Divided by
10:15 144. Like it's wrong.
10:19 What do I have to divide square inches
10:22 by in order to get square feet from a
10:25 square inch
10:32 output? Oh, oh, that didn't give me
10:38 anything. What do I have to divide a
10:41 square inch output by to get square feet
10:45 for that same output?
10:52 Yeah, yeah, yeah, yeah.
10:56 So, so
10:59 now look, I still know math. It's
11:01 incredible. I've done math, but I still
11:03 know it a little
11:06 bit. But this whole
11:09 thing, the round still comes at the end.
11:12 um divide by
11:15 144 other parenthesis other
11:19 parenthesis should get us
11:22 there.9 square ft
11:26 total. Okay. Now for these same things
11:29 we need the number input two to be
11:33 um I guess it's
11:36 projected
11:40 area is in square foot. So that we
11:43 should just be able to do this and then
11:46 throw
11:52 in down and some similar formatting.
11:59 This is square
12:02 foot. Oh, but we're missing the calc.
12:05 That's fine. We're going to get there.
12:11 This has always been a challenging
12:13 system to build and I've come at it so
12:15 many different ways. I'm thinking that
12:18 this is the best one. Projected area
12:21 divided by So, we're going to do some
12:24 conditional stuff later on, but for now,
12:26 proof of concept divided by
12:30 150. There you go.
12:33 So the projected
12:34 area totaling
12:37 requires 10 and we are providing nine
12:41 unless we did a little bit of this
12:44 action going
12:45 on. We went the whole plan here. What do
12:49 we get? We didn't get enough that's for
12:50 sure.
12:52 Um because the other method is if we had
12:55 rid ridge vents
12:57 two, right? Then it's this divided by
13:01 300. So this is going to be a
13:04 variable, right? That'll end up being a
13:07 variable because it's going to change.
13:09 We still didn't provide enough there. Um
13:13 namely because we don't have the ridge
13:14 vent. Now, here's the next part of
13:16 this
13:20 is just go see reporter values. I need
13:24 to change all these to
13:26 be let's edit the names of these so that
13:29 they're in the
13:31 beginning
13:33 underscore longs. There's no reason to
13:36 ever have to always scroll to these.
13:39 So, those are the two I really care
13:42 about.
13:45 So what we're seeing
13:49 here is ridge vent
13:55 length. So now I need a ridge
13:58 vent net free area.
14:10 Let's just pick any one of these and we
14:12 just 18 square inches per linear foot.
14:16 Okay, so that should just
14:18 be that we are doing in all these
14:22 calcs. Um, and you just put it in all of
14:25 them because it doesn't
14:28 matter because some of them won't report
14:30 because they literally have no ridge
14:33 vent length.
14:39 Right. And you could split it or you
14:41 could join them. Let's split it just for
14:44 argument sake. Let's put it in macro
14:46 input three. We're going to do
14:49 um ridge vent
14:53 length
14:56 times it was 15, right?
15:00 18 square inches*
15:06 18. All this a little bit of
15:09 this divided
15:11 by 144. And we don't need a round
15:14 because the round happens in the
15:16 schedule. That was just me being
15:19 stupid. Now, let's put this in here.
15:24 We're going to end up, you know,
15:26 reorganizing the way this is.
15:29 But this is oops
15:33 wrong. This is technically this
15:36 calculate
15:37 [Music]
15:39 sums should be that this
15:41 is for feet
15:47 squared.
15:49 Forget
15:51 wrong. Why? What did I do wrong?
15:54 You caught
15:59 it. Bridge vent
16:03 length. That's
16:05 a It's a measurement. Might need to be
16:10 float. Don't know what format it's
16:12 coming
16:17 in because it should have been inches,
16:20 but
16:25 What actually coming in? It'll be short.
16:32 Opt length is in
16:35 inches. 174
16:41 in. Really? Oh, yeah. It's a long one.
16:45 Okay. 174 in.
16:55 times
16:59 18 area is 18 per for per linear foot
17:04 for linear
17:06 foot.
17:08 Whoops.
17:12 Whoops. Someone caught it. I know you
17:14 did. I knew you were just sitting there
17:15 going, "You idiot.
17:18 That'll look like a better number.
17:21 Okay,
17:24 cool. I really think we just want to
17:26 join these because it's going to make it
17:27 very succinct to a plan
17:29 checker. Show that we've hit the
17:32 requirement. Or
17:35 or we do
17:39 this. Oops. Why did
17:43 that We do this. We do this.
17:48 Copy. Do this.
17:51 Copy.
17:55 This just like that.
18:04 That
18:19 is
18:23 so total sum total
18:27 sum. There there's our total that we're
18:31 providing. There's our
18:35 required name up here is eve vents ridge
18:38 vents
18:40 combined or required or yeah combined
18:44 required provided total required I mean
18:47 total provided total required
18:50 bam and we're just driving it by an
18:52 index
18:55 of fill angles.
19:01 What else could we do? How how else
19:03 could we
19:04 change the value is coming
19:08 from your ridge
19:11 vent through the same Phil? What other
19:15 values do we get from
19:17 Phil? From our buddy
19:20 Phil, we
19:22 get Oh, interesting. We get
19:26 area. That's not going to help.
19:31 It's not going to help. What I what I
19:34 was even
19:37 thinking. We could do line
19:41 weight. No, we don't want to do line
19:44 weight. That would be
19:51 terrible. Layer line color.
19:55 [Music]
20:04 We could do layer line weight and have
20:08 automatic roofs
20:11 override the line weight to some
20:14 specific amount so that they're not
20:16 following the layers line
20:21 weight. That would be an easy input.
20:30 We could put it again in pattern angle
20:33 past that. I don't know that that's a
20:36 great method. I don't like
20:40 it. I think layer line weight would be
20:47 it because we could just automat since
20:50 we have roof defaults now. You can set
20:53 this to whatever you want.
20:55 And then the actual line weight here
20:57 could
20:58 be what that
21:01 um area was, which was
21:04 18. So what we'd be doing
21:09 is everybody wants a calculator. They
21:12 don't necessarily care that it's an ugly
21:14 method behind the scenes so long as the
21:17 end user experiences something
21:19 different. And I'm going to have to
21:20 document this because some people would
21:22 go in and go try to change the line
21:24 weight there and that that would be
21:28 problematic, right? Because this doesn't
21:30 need to follow the layer line weight.
21:32 Could just be 55. Doesn't
21:37 matter. Does make it so that it's no
21:40 longer dynamic in other views though,
21:43 which I don't like. I don't like that.
21:46 That's not going to work.
21:51 So what other
21:54 options? What other
22:09 options? I mean the end user could just
22:12 punch it in. That's for sure.
22:21 You don't even need to use the fill
22:22 index even though that's a quick paint
22:25 and you can create a bunch of different
22:27 fill
22:28 indexes
22:33 indices which is nice for quickly doing
22:35 it without having to type it out. You
22:37 just save all your
22:40 fills. Okay. What other
22:53 methods? You could put it in the
22:59 color of the roof plane, but you're not
23:01 going to apply that from the fill. The
23:03 fill is just grabbing a fill. You have
23:05 to do it in the
23:07 fill. So, what again? What's specific to
23:10 the fill that we could grab that can
23:12 create an
23:21 index custom pattern X scale. That's in
23:25 case someone didn't want to do they
23:28 didn't care about not
23:29 doing some kind of pattern. You could do
23:33 it that
23:34 way. Is the X scale X scale and Y scale.
23:38 In fact, they wouldn't even need to do
23:40 the pattern angle thing. It could just
23:41 be the X scale, Y
23:45 scale. Event ridge vent. That would be
23:48 very
23:52 easy. Drawing group's not going to get
23:54 you anything.
24:01 their things don't pass
24:06 through really
24:08 just or pattern horizontal spacing
24:11 pattern vertical spacing. Which one
24:12 would we want here? Hold on. So if we
24:16 switch this to a
24:19 hatch, what's the custom Xcale Y scale
24:23 setting coming from?
24:26 It must
24:39 be that for custom library stuff like
25:02 Yes. Let's try this. This is spacing
25:07 three.
25:11 I I don't know what that's coming
25:16 from. Custom
25:18 pattern. Custom pattern. X scale. Y
25:23 scale. There's no way to
25:28 easily. Yeah, there
25:32 is custom pattern X scale Y scale.
25:35 Create a new pattern.
25:44 Uh roofing
25:47 tool,
26:01 right? Can I do this?
26:20 that save. I don't
26:25 know
26:27 tool. Okay.
26:34 Freaking clever, right? So, you just get
26:37 to punch this in.
26:39 44.3.
26:42 And what was the other one?
26:46 18. Couldn't be freaking easier. Except
26:50 for that, we want Yeah, this is just a
26:53 blank fill.
27:02 If you switch off of this. Oh, see it
27:05 has a background. So, it's a blank
27:07 pattern fill has a background. This is
27:15 awesome. Look at me go there. So, now
27:20 just to test
27:24 this. Oh, this is going to be the
27:26 simplest version I've ever done. All
27:27 right.
27:32 What am I doing? Object information.
27:33 Okay, we got a bunch of stuff here that
27:36 just needs to move around. Should just
27:38 start with, you know, first one should
27:40 be the totals, which is I think here.
27:44 Yeah. Just transfer some stuff.
27:58 So this is going to
28:02 be what this this
28:05 is
28:09 scale
28:11 is custom pattern X scale pattern X
28:19 scale boom boom boom
28:35 Okay. Set
28:39 this.
28:43 Oops. System pattern X scale. We don't
28:46 need times a,000
28:49 anymore. You need by 144. We'll do that
28:53 math for people. Okay, we don't need the
28:59 round. We don't need any of that. Nice
29:02 and clean.
29:07 Okay. What's this
29:10 one? Are
29:11 we Oh, why am I putting this
29:14 in? I'm a dummy.
29:23 There we go. This one
29:29 goes
29:31 okay. Bridgement ends up
29:37 being
29:42 times and pattern ycale.
29:52 This is so
29:55 easy. I don't think I need the 2F in
29:57 there.
30:02 See
30:04 then just do
30:08 this. What's this?
30:18 Get rid of our
30:20 little centered
30:27 signs. I think that's
30:31 it. I do
30:35 wrong. There's our
30:38 total. My numbers are wrong.
30:43 are
30:45 wrong
30:48 because I do
30:51 wrong. Elks are wrong. Projected
30:55 area pattern X
31:04 scale was in square inches.
31:12 Oh, well, the biggest problem here, I'm
31:14 an
31:15 idiot. We don't know the number of vents
31:17 we're
31:21 using because we didn't multiply it
31:26 times eve
31:30 length. Yeah, that's dumb. Okay, that's
31:34 problem one.
31:56 What's problem
31:58 two? Custom pattern Y scale. Oh, that we
32:02 didn't spray this on everything. This is
32:05 problem number
32:10 two. That'll make some big changes.
32:17 Yeah. Okay. Now, let's find out some
32:19 more
32:21 info on this
32:28 roof. What lengths do we get? In fact,
32:31 let's just use my search for this
32:33 because these are measurements. This
32:35 will
32:38 help. We get eve fascia
32:44 length, which is longer than we want,
32:47 but we could work with
32:51 it. Flashing length's not going to give
32:53 you
32:58 there, but we wanted to keep in the
33:01 eaves.
33:17 So it has to it has to be in the
33:24 eve facial length.
33:31 Yeah. And
33:54 then doesn't
33:57 say. Excuse me.
34:03 It could be good if it had a shadowboard
34:13 length. Visible
34:16 length. What number is
34:19 this?
34:21 495. What number is that?
34:30 That's total
34:35 around. Where get where are they getting
34:37 this fascia length? Oh, they're assuming
34:39 this is a fascia. Oh, stop it.
34:42 145 145 is
34:45 290
34:47 plus 20. Yeah. Come on, man. Or wait,
34:52 no, 205 is right. 205 is there. Wait,
34:55 what was I getting here? Oh, visible
34:58 length. I was confusing the two.
35:01 Okay, visible length is all
35:05 edges. Yeah. So, we're not getting this
35:08 length against the
35:10 wall unless I could
35:12 really think up something
35:15 clever, and I don't think that I
35:19 can. You could you could do a bunch of
35:21 trig with this because you could get the
35:22 total all visible length minus the
35:25 facial length minus the area minus the
35:27 projected area. Do a bunch of calcs to
35:30 within reason figure out what this edge
35:32 is.
35:34 But no thank you. Uh I don't want to
35:37 work that
35:42 hard.
35:48 So yeah, we're back to
35:55 just leave facial length.
35:59 Okay, so here's a
36:02 thought. It's not
36:04 perfect. It's close to
36:09 perfect. Is that
36:14 This guy right here is
36:18 actually
36:22 parenthesis
36:29 times eve
36:32 basia
36:37 length. We're just going to have to
36:40 subtract
36:43 some value that's probably going to be
36:44 pretty
36:45 common. So overhang could be 32 inches
36:49 on either side. You don't know if it's
36:52 you don't know if it's on either side.
36:54 That's the other problem. You don't know
36:55 if it's abunded to another wall or
36:58 what. You really don't know. So it's
37:00 almost like just divide the whole length
37:03 and minus one or two.
37:08 So, E facial length divided by 24 on
37:11 center. Or in my case, we could do
37:15 something more complex where my system
37:18 already sets a global for roof framing
37:22 spacing. I could get some AI to figure
37:25 out how to get that number. So, instead
37:27 of 24, it's actually using the actual
37:29 spec of what we're doing.
37:34 Um but we're getting the and so like
37:37 let's see this is 24 in center and our
37:40 reported measurements in inches. So yeah
37:44 so then on top of
37:46 this it would
37:49 be minus2. So I'm determining the number
37:52 of vents based on the E facial length
37:55 minus two within reason just to show
37:58 that we're satisfying a requirement and
38:00 we could say minimum in the
38:03 column if we wanted
38:06 to. Why is that not accepting
38:17 minus2? There we go. I need to convert
38:19 that to a float.
38:22 And then this whole
38:25 thing goes in. So we're we're providing
38:30 way more than necessary, that's for
38:33 sure. Which seems
38:42 wrong. What happened here?
38:50 Something happened here
39:01 too. Wrong one. Wrong one. No, the right
39:05 one. Bridge vent length and then custom
39:08 pattern. Yeah, we've skipped a calc
39:10 here. Okay, whatever. This is
39:35 What? What happened
39:42 here? Listen pattern x scale divided by
39:45 144
39:46 times missing all kinds of
39:50 um I'm not even going to sit here and
39:52 think about it. I'm just going to tell
39:54 some chat to do it for
40:00 me. Fix
40:10 this. That's still not right.
40:29 that didn't produce a number. This is a
40:31 measurement class. So, make sure we
40:33 convert everything to a float before we
40:35 calculate any kind of variables that we
40:37 put in there.
40:47 That fix
40:50 it. Seem like
40:52 it happening
40:54 here. Oh, for one single line of code.
40:58 Single
41:00 line. There we go. Oh, why did that last
41:05 little thing screw that up?
41:09 Didn't did
41:11 it. Yeah, it did. Look at that. That
41:14 little not leaving a space there. That
41:17 can't be
41:27 right. It's not working. Make this a
41:31 single line. Should just throw these in
41:33 their own variables and that way we're
41:35 not worried about this at all.
41:46 Oh,
41:47 and
41:50 duh,
41:52 dummy.
41:59 Okay, get these back in order. Three,
42:02 four. So, here's our overall total.
42:05 Here's our event total. That's what's
42:15 required. One
42:17 150. I thought we get to do the 11 150
42:20 rule. If we do Okay.
42:38 You can reduce to
42:40 Yeah. Yeah. So, we didn't need nearly as
42:42 many
42:53 events. I think this is
42:56 working. I think it's working.
43:02 Um, interesting to do a little bit more
43:04 complex of a house. And now I have to
43:07 get this into roof
43:13 defaults.
43:17 Yeah. We're going to get into roof
43:24 defaults. Style library.
43:29 roof bent
43:32 tool set thing
43:35 up. What was this one?
43:46 Uh oh, I forgot
43:49 to Okay.
43:55 And then I got to do all this that I
43:56 just
44:02 erased. Oh, dang
44:04 it. Is there a set as default? There is.
44:08 There you go.
44:17 Okay. And just auto build,
44:21 right?
44:23 Yeah.
44:28 Easy. All right. So now when we start
44:31 just drawing with
44:33 walls, crazy
44:36 walls, should just be continuously
44:39 building our
44:47 calc. By the way, this is why you buy
44:50 the pro plan. You could watch this video
44:51 for 44 minutes and try to put this back
44:54 together or you could just go buy the
44:55 prop plan and I'm going to have this in
44:57 the next version. Isn't this
44:59 cool? So, this will just
45:02 be required. So, this is how this ends
45:05 up looking
45:08 is why I use these generic by the way if
45:11 you didn't know. I use these generic
45:13 numbers
45:14 because otherwise you have a ton of
45:17 custom fields across all objects across
45:19 your whole plan. So you want to keep
45:21 your custom fields generic so that you
45:24 can do stuff like this. So this is
45:41 just I mean what's unfortunate about
45:43 this is that it's you know it's going to
45:45 show all the
45:48 individual amounts here and that's not
45:51 going to make a whole lot of sense.
45:56 I'm also probably going to put this in a
45:58 separate
45:59 schedule. That's what I will do. All
46:02 right. I'm going to show you that here
46:04 in a
46:06 minute. Total NFA required.
46:24 So this this system so far
46:27 assumes in the event that is um it's
46:30 going into you know a bay but if you
46:34 have a closed
46:35 sophet we need to have a different bill
46:39 for
46:40 it. So I think someone's going to have
46:42 to
46:46 determine you know is this linear feet
46:49 or is it each and so I will
46:53 produce okay we could keep doing this
46:55 let's keep going we we'll make a
46:57 complete system got to think it through
47:00 the whole way whole way through
47:04 um this is regiment
47:31 And then I should do a minimum number of
47:34 events.
47:36 in case that's
47:38 happening, right? And then if I took
47:41 this all out. Oops,
47:46 H, excuse my
47:52 language. What was that one? Was four.
48:07 because we could put some number
48:10 input maybe. I don't think so
48:17 actually area surface makes sense to
48:22 leave but it's actually projected area.
48:26 So really this should be removed and it
48:28 should be add this one. Rename it
48:31 rejected
48:35 area
48:36 attic. Attic area.
49:22 And then we really want to just
49:24 group be nice to group similar objects.
49:27 You're not going to be able to
49:30 here. Maybe you
49:33 can. Hey, you can because it's summing
49:36 total
49:37 rows. So you want to take out the call
49:40 out symbol.
49:45 This is just the calc. Just shows the
49:47 calc. That's
49:56 it. Clean. Look at
49:59 that. Very very
50:04 clean. Interesting. That attic area is
50:07 not showing.
50:15 We didn't put it. Okay,
50:26 gotcha.
50:36 Yes. There's our attic area. I don't
50:39 even need to show totals because it's
50:41 group similar. Don't even need a totals
50:46 row. Quite literally. Bam. Nice looking
50:50 calc. Okay.
50:54 Now, want to adjust for if we're doing
50:57 soft
51:00 vents. How do we determine that?
51:16 Turn. We're doing soft
51:25 vents. We get from a roof. Do we get
51:28 sophets?
51:38 soft. What do we
51:45 get softed area? So what happened? So
51:49 all right. So this is how I like to
51:51 approach these things. They obviously
51:53 have some info here from the sophet. We
51:55 want to capture this info. Well, and I
51:58 probably could have just done this.
51:59 Would have been smarter. I'm not always
52:02 on the ball
52:04 here.
52:06 Okay. Right. That's the current value
52:09 we're getting out of this. By the way,
52:10 if you just hit shift select, you can
52:13 shrink your text size. We're just using
52:15 it
52:16 temporarily.
52:21 Now, let's turn off sophets and see what
52:24 it reports.
52:42 that gives us this area is zero square
52:45 foot. All right. So, we have no
52:48 sophet. That's it. That's the trigger.
52:50 That's the if this then that. So now I
52:54 need to get in and write a more complex
53:00 system. Sweet.
53:04 So, here's what we're going to
53:18 do because we could keep some of this in
53:20 line, but I'd almost like to contain it
53:22 in their individual pieces. Let's start
53:25 writing this by myself real quick. This
53:29 is good practice.
53:38 And I'm going to butcher it. That's
53:41 okay. So, first of all, let's
53:44 go roof as a prefix, net free area as a
53:50 system, and
53:52 then or actually I already have a net
53:55 free area system. So, it should be maybe
53:57 NFA to start. Let's see what we have
54:00 currently.
54:01 We have an NFA to start. So, all right,
54:04 we'll do
54:06 NFA
54:08 roof
54:11 and this is
54:18 um I guess lower
54:24 vent. And so then it's a if sophet I'm
54:29 not going to write this right um I'm not
54:31 even going to bother greater than
54:34 zero then um then we need
54:39 uh what do we say it was
54:47 eve yeah
54:49 eve
54:51 flashing length
54:57 and
54:59 then divide by 144.
55:03 Fine. And
55:09 multiply. I don't know order of
55:11 operations in Ruby at all. Um, so I just
55:15 put it in parenthesis to be safe.
55:18 Multiply
55:19 times custom
55:23 X
55:25 pattern scale, I believe, is what it
55:30 was. And it would have been nice if we
55:32 were selecting a roof to start this
55:34 with. Let's do that real quick. Oh, we
55:37 are. I'm just getting it wrong because I
55:39 didn't put an end
55:41 condition. All right.
55:56 else. Oh, we're just going to say uh
56:01 result
56:03 result equals
56:09 um yeah, e flashing
56:18 length. Oh, we're missing the
56:22 Well, divided by the other divided by
56:27 part. Um, we're going to put the 144 at
56:29 the end. So, divided
56:33 by 24 in this case until I put the
56:36 global in there, which we're going to
56:37 have to
56:39 get that scripting done elsewhere. Um
56:43 otherwise Eve flashing length times
56:46 custom X pattern
56:56 scale seems very simple but I'm doing
56:58 something wrong obviously.
57:01 Um, suffet. What if sopet? Oh, I'm using
57:06 the
57:08 wrong MVP for
57:11 that. Uh, which is
57:23 what? Sophet
57:27 area. Okay.
57:29 And then what was the bill thing? We
57:32 don't
57:35 know. Custom X custom pattern X scale.
57:40 Custom pattern X
57:41 scale. Custom P
57:44 scale. Custom P this backwards.
57:49 Custom
57:53 pattern scale.
58:02 This is sophet
58:06 area
58:09 please. Oh, and
58:11 it's
58:14 2F. So, we're working in the measurement
58:17 class. Eve flashing length I have wrong
58:20 again. What is it really? It is Eve.
58:26 What I call it flashing uh Eve fascia
58:33 length, right?
58:36 Oh, Eve
58:44 fascia. We're getting a
58:47 number. Yeah.
58:57 And
59:01 then there we go. Now we're talking.
59:04 Look, I did that all by myself. That's
59:06 pretty
59:09 good. Yeah, I think
59:12 that's
59:15 correct. Okay, so we have that first
59:18 one.
59:22 Way to
59:24 go. Let's throw it in and just check
59:27 that it works. Why not? So, that's this
59:38 one. My favorite roof lower event. And
59:41 technically, it's going to be in here
59:43 too where it's
59:45 doing Oh, we forgot to do a little minus
59:48 two, but that's
59:50 End of the
1:00:14 world. Oh, and we're uh dividing that
1:00:17 whole thing by 144. And now we don't
1:00:19 want to
1:00:20 be. We're going to do a calc for this
1:00:22 other one anyways. So here is that other
1:00:30 one. Yeah.
1:00:34 Yeah. Okay.
1:00:38 NFA roof
1:00:42 bridge
1:00:54 bed
1:00:56 length /
1:01:01 12 times custom pattern Y scale.
1:01:09 Let's see. It wants an end. Um, how
1:01:13 about we just
1:01:14 do so
1:01:18 equal
1:01:30 and don't need fantasy.
1:01:42 I might not have a roof selected. So
1:01:44 this is that's what's happening
1:01:47 now.
1:01:50 Don't
1:01:53 that that is giving us nothing because
1:01:56 we selected something that doesn't have
1:01:58 a rich. Yeah. Okay. How about this?
1:02:04 All right, that's given us a
1:02:06 number. What a measurement class. Um,
1:02:09 why did my other one get to be a
1:02:10 measurement class?
1:02:43 I want to go.
1:02:47 Okay. Or I think I just get to do
1:02:51 this. There it
1:02:56 is. Yeah. Oh, but it's actually square
1:03:06 foot. I think that's
1:03:17 right.
1:03:19 Okay. So, this one is Richmond length.
1:03:22 So, we just get to do this.
1:03:30 This just gets to
1:03:33 be the two together.
1:03:57 That's pulling an error for some reason.
1:04:00 Why? They're both measurements. Maybe I
1:04:03 need to convert them both to
1:04:06 float. They're different units of
1:04:09 measurement.
1:04:13 Maybe they should both be
1:04:22 float. Why not? Doesn't matter. Make
1:04:26 things a lot
1:04:40 easier. Here's float.
1:04:44 Okay, same
1:04:46 output. That
1:04:49 works. This is already
1:04:52 float. Now, do these make not an error?
1:04:55 No, they don't.
1:05:03 Why? What's going on here? NFA
1:05:06 lower. Why not? Why does that not work?
1:05:19 trap it in
1:05:23 balls. There we
1:05:25 go.
1:05:28 Okay. Oh, I think I could have done a
1:05:32 better solution for that, but that's
1:05:34 okay. Um, total possible in Okay, so our
1:05:37 numbers way off.
1:05:40 number's way off. Why?
1:06:15 Oh, because I have sophets maybe. And
1:06:18 it's doing the soffet number and our s
1:06:20 and that number is massive. The custom
1:06:23 pattern x scale is massive. And so we
1:06:28 could we could now use what what could
1:06:32 we now use from this fill style
1:06:36 here? X scale Y
1:06:41 scale could still use angle as an index
1:06:46 for NFA on a on a continuous set vent.
1:06:51 Cool. We're getting there. We are
1:06:53 getting there.
1:06:55 Uh
1:06:56 continuous let's see line set
1:07:10 vent be a 10
1:07:12 foot
1:07:15 deal 8 foot
1:07:18 sure so per 8 All
1:07:33 right. 92 square inches per 8
1:07:36 foot. I'm going to have them do the math
1:07:39 cuz you don't know if it's going to be a
1:07:40 10 foot or
1:07:45 not, right? So, they have to convert it
1:07:47 first. So,
1:07:50 it's whatever this
1:07:55 is 11.5
1:07:58 per five per
1:08:01 foot. 1.5 per foot.
1:08:05 Okay. So, they're going to
1:08:09 do
1:08:22 this. What are we times in? Um, a
1:08:30 th00and thousand.
1:08:33 Yeah. Um, so
1:08:36 Back to the lower
1:08:44 vent. Sophet area is greater than this.
1:08:48 Then
1:08:50 it's
1:08:53 times
1:08:57 pattern
1:09:00 angle times.
1:09:05 E facial length times
1:09:08 pattern. Oh, I did that wrong. If
1:09:11 sophets's greater than zero, that means
1:09:13 it's a sophet. All right. So, we've
1:09:15 screwed that first part up anyways. But
1:09:16 this So, then it's pattern
1:09:21 angle. So, this first one is a sophet.
1:09:24 So, um pattern angle times a th00and.
1:09:28 Okay.
1:09:33 And then next
1:09:35 one
1:09:42 is this is the one that's divided
1:09:45 by this is just a facial
1:09:49 length. This one's the one that's
1:09:51 divided
1:09:54 by big
1:09:57 dummy.
1:09:58 Okay. See what that number looks like.
1:10:01 Looks should look a lot
1:10:05 smaller. Didn't
1:10:07 change. Why? Oh, cuz we didn't. So,
1:10:10 something's still wrong. We're getting
1:10:13 there. Um,
1:10:18 proof. Let's just say for argument's
1:10:21 sake, we do have
1:10:25 sophets. That number changed
1:10:27 drastically.
1:10:32 Cool. Why does it still feel like it's a
1:10:34 big
1:10:39 number? It is too big of a number. It
1:10:42 shouldn't be that big.
1:11:03 is such a big
1:11:13 number. Yeah, that's not providing 10
1:11:17 square foot net free area.
1:11:20 So what's my problem? First of all,
1:11:23 let's take this 144
1:11:25 out. The number we're actually getting
1:11:30 1449. We are
1:11:41 doing 44.9. It's much
1:11:45 different. That's the one I'm looking
1:11:47 for.
1:11:50 Now, just to say for argument sake,
1:11:52 let's put
1:11:54 in,00 and let's just get the other value
1:11:59 232. And
1:12:01 that's a decent number because this is
1:12:04 divided by
1:12:06 144
1:12:08 there. One square foot of
1:12:13 vent. That makes a lot more sense.
1:12:19 back to
1:12:20 zero there. That makes a lot more sense.
1:12:24 Okay, now the numbers are
1:12:28 looking
1:12:30 much
1:12:41 better. There's only like 10 roof plants
1:12:45 here. How are we getting 229?
1:13:09 Yeah, this is just
1:13:14 three and
1:13:16 one. Where's this 229 number coming
1:13:26 from? These are just
1:13:31 floats. It's a float. That's four total
1:13:34 right there. And it's one of the
1:13:37 largest ones. So where is this coming
1:13:40 from? Total possible innovate provided
1:13:42 with the H. Just so I know what this is.
1:13:46 Let's copy this. Let's reset the name.
1:13:50 Macro
1:13:51 input
1:13:53 two. What happened on macro input
1:13:57 two? NFA lower roof lower vent.
1:14:03 Oh, the numbers changed. Look at
1:14:07 that.
1:14:09 Oops.
1:14:20 Okay. Okay. So, next
1:14:39 Let's fix this
1:14:41 lower. And it's going to be this whole
1:14:46 thing
1:14:54 minus this this whole thing.
1:14:59 -
1:15:01 2 -
1:15:03 3. It's
1:15:15 actually Yeah. So, we're subtracting two
1:15:19 ends and one potential error one because
1:15:22 you're not going to have an over well,
1:15:23 you might have an overhang of 36 in or
1:15:25 something,
1:15:28 but yeah. All
1:15:36 right. That's not going to change this
1:15:38 number because we are currently on
1:15:40 sophets. And this actually should be not
1:15:43 the full length. We should put like
1:15:45 minus a foot on either side. So minus
1:15:59 24. Yeah.
1:16:10 Then we almost get to copy a good part
1:16:12 of this code to do a new code going
1:16:15 NFA roof
1:16:21 um block
1:16:29 blocks. We're basically doing
1:16:40 If area to f is greater than zero, then
1:16:43 result equals I think
1:16:50 otherwise it just equals
1:16:56 this. But we're just looking
1:17:00 for
1:17:04 number. There you go. So if we said
1:17:07 let's to do this 2,00 or whatever 200
1:17:10 subtract three from a measurement of
1:17:12 length. Do F. We need to make sure I fix
1:17:15 that on the other one.
1:17:20 Um
1:17:22 salt just do around
1:17:25 here
1:17:27 cleaner cuz these are whole numbers or
1:17:29 just two
1:17:32 I work
1:17:34 15. That's the maximum number of
1:17:40 uh block vents you could put
1:17:41 in. That works.
1:17:56 should have still been
1:18:03 to and now I'll go
1:18:07 O and we are going
1:18:10 to info macro input one
1:18:18 NFA we've blocked
1:18:21 fence. Okay. And now this gets to do
1:18:25 macro input one add and
1:18:29 rename
1:18:40 possible
1:18:47 total. want that at the
1:18:54 end. Um, and this should be
1:18:57 NA, which that should have
1:19:09 been.
1:19:10 One,
1:19:14 two. Space out this
1:19:20 think I do that
1:19:24 right
1:19:34 showing. Yeah, it is
1:19:36 showing. Hey, NFA roof block
1:19:41 fence. Where do I put it?
1:19:47 Macro input
1:19:48 one. What is this? Oh, there it goes.
1:19:51 Now it's building.
1:20:25 Um, we could do one more which would
1:20:30 do same almost the same exact thing
1:20:54 Here would just
1:21:01 be this is going to be method.
1:21:35 Did I name I forget naming
1:21:38 this? I did I
1:21:41 didn't I didn't name it. Dang it.
1:21:55 Eve method.
1:22:33 Bam. I think this is a complete system.
1:22:36 I think that was it. You get into your
1:22:38 roof defaults. You change your custom
1:22:42 pattern angle. You change your second
1:22:45 custom pattern angle and you can change
1:22:47 your angle. And that will give you NFA
1:22:51 for blocks versus continuous. And then
1:22:54 it's just that's just whether or not you
1:22:56 have a set or not. And ridge
1:22:59 vent. Oh, I forgot something. I forgot
1:23:01 to switch the method. If ridge vent
1:23:06 is, there's no way to switch that
1:23:09 method. We have to have a boolean yes or
1:23:13 no
1:23:15 because even this is still going to be
1:23:18 using that method.
1:23:20 If we have a ridge vent here, this would
1:23:22 still be using that method. So, there
1:23:25 has to be a
1:23:28 trigger. Again, it'd be nice if it was
1:23:31 coming from the fill
1:23:32 style just to make it really
1:23:36 easy. So, something that's just
1:23:43 boolean. What would that be?
1:23:47 We've
1:23:48 gotah description, fill, color, fill,
1:23:51 line weight, floor number, whole area,
1:23:55 schedule. Let's
1:24:08 see. You do horizontal
1:24:11 spacing. I don't know if we can do
1:24:13 horizontal spacing. Can we do that? What
1:24:15 do we have here?
1:24:18 horizontal. Maybe they're
1:24:27 calling. Oh, we could do pattern line
1:24:30 weight would be real easy. One or two.
1:24:34 That'd be it. Method one or
1:24:37 two?
1:24:41 Yeah, because I think we get pattern
1:24:43 line weight for this.
1:24:52 pattern color from layer pattern
1:24:55 horizontal spacing pattern vertical
1:25:05 spacing. This is all we're getting from
1:25:08 pattern. So we could do
1:25:11 horizontal
1:25:28 spacing. See if we can get horizontal
1:25:31 spacing
1:25:34 here. Think I have to. All right, we're
1:25:36 going to make a copy of this. Bring this
1:25:38 over.
1:25:40 And let's go
1:25:43 hatch. I don't know what horizontal
1:25:46 spacing is. Where are they getting
1:25:50 that? That from library
1:25:53 again. Let's see that
1:25:59 option. That's got to be
1:26:03 offset. Let's try.
1:26:08 Well,
1:26:09 no. Where's this? Where's this
1:26:13 value
1:26:14 pattern? Horizontal spacing is 2 in.
1:26:18 Okay. That's
1:26:23 from
1:26:26 Yeah, that's from
1:26:29 this. Okay. So, we're going to set this
1:26:32 to
1:26:33 one. Set this back to library.
1:26:37 roof vent tool.
1:26:40 Bam. Dang
1:26:42 it. Custom X scale Y scale 43.3 and
1:26:47 18. And
1:26:52 then you know whatever for
1:26:59 this I think I drive fill style by layer
1:27:03 color.
1:27:14 So, what does this pick up
1:27:17 now? Horizontal
1:27:21 spacing still shows 2 in. Dang it. So,
1:27:26 that wasn't
1:27:28 it. Horizontal spacing pattern.
1:27:36 Where's that coming from? I wish I could
1:27:39 think of
1:27:40 this. There's no value to here.
1:27:49 So, if I change this here, is that that
1:27:52 giving me what I'm talking about?
1:28:01 Yeah. So, it doesn't retain. Doesn't
1:28:06 retain. Dang it.
1:28:09 Okay. So, we can't use
1:28:13 that. What else can we use? This is just
1:28:16 a flip from 150 to 300
1:28:22 method.
1:28:31 They're just making an
1:28:49 input. Oh, well.
1:29:00 If ridge vin is turned off, I don't know
1:29:02 if it there's a has ridge
1:29:06 vent. They should they should have an
1:29:08 MVP. That's Hazard
1:29:31 Vent. Pattern angle. Pattern color from
1:29:34 background. Pattern color from layer.
1:29:40 I have to think about this. I might just
1:29:43 have people punch it
1:29:46 in or I know what I could do. I could
1:29:49 put it in my global system. Here's what
1:29:51 it would look like. I already have this
1:29:53 system in place. So, it makes sense. So,
1:29:56 in project
1:29:59 designations, yeah, I just get to make a
1:30:03 new What would this even be?
1:30:09 Um, vent other. Oh, van ease. Look at
1:30:12 that. I actually have a call out for
1:30:14 venies already. So, we'll do
1:30:17 this and then we'll do
1:30:20 this. I'll just copy
1:30:23 this. This is going to be very
1:30:27 simple, very robust system. It's going
1:30:30 to
1:30:31 be method.
1:30:38 and method. And then label replacement
1:30:41 is going to be
1:30:50 um bridgement
1:30:53 versus let's see not even that just yes
1:30:56 and no or true and false. Let's do that.
1:31:08 Um, so it'll look like this. It'll look
1:31:11 like
1:31:29 uh or yeah
1:31:36 then equals
1:31:45 I think this
1:31:57 through I don't even need it to be Yeah.
1:32:01 I don't even need it to be.
1:32:14 What? How does this
1:32:16 go? Yeah, true has to be in
1:32:25 that method equals otherwise
1:32:33 I don't need this second part.
1:33:04 Think that's
1:33:12 it. One more percent sign.
1:33:33 I screwed it up. Dang
1:33:35 it. Dang it. And I have to go. That's
1:33:39 it. Sorry. I wish I could have shown you
1:33:41 the whole whole whole thing. Basically,
1:33:44 I'm going to have someone just flip a
1:33:45 switch and say, "Are you providing a
1:33:47 ridge vent or not?" and then that system
1:33:48 switches. So, I got a little bit more
1:33:50 scripting to go. Pretty cool. Thank you
1:33:53 for sticking with me through this. Um,
1:33:55 you can see the challenges I go through
1:33:57 coming up with some of the more advanced
1:33:59 systems. Um, I've wanted to do a good
1:34:03 vent system for a while and it's you
1:34:06 could see the complexities there.
1:34:07 There's no way to automatically tell if
1:34:09 something's going to be a ridge vent
1:34:11 method or not because as you can see,
1:34:13 sometimes you'll have a ridge vent, but
1:34:15 it's because we're not reporting
1:34:18 adjacent roof planes whether or not they
1:34:20 have ridge vents or not. So, there's no
1:34:22 way to tell that. And you can see also
1:34:24 that this is not 100% accurate because
1:34:27 we can't determine
1:34:29 um exactly the length
1:34:32 of basically where our roof um our seat
1:34:36 cut is or or our heel height as it may
1:34:38 be. And then yeah, but this is really
1:34:42 really close. It would be certainly good
1:34:44 enough for my jurisdiction. I know
1:34:45 that's within 1% or
1:34:48 less. Cool. And it's automatic. All you
1:34:52 have to do is set your preferred vents
1:34:54 in the pattern angles and and that's it.
1:35:00 You you just punch in the NFA there and
1:35:02 it does it for you. How cool is that?
1:35:04 So, I hope you got a kick out of this
1:35:06 one. Sweet.
1:35:17 [Music]
