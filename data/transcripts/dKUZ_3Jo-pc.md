---
videoId: dKUZ_3Jo-pc
title: Build an RSMeans-Style Estimating System in Chief Architect X17 (Step-By-Step Guide)
url: "https://www.youtube.com/watch?v=dKUZ_3Jo-pc"
status: imported
---

# Transcript

0:00 What's going on VIP? Bet some of you are
0:03 going to really like this video. Let's
0:04 see if we can't make an RS means style
0:07 system for estimating costs on
0:11 installing things,
0:13 doors, windows, what have you. I've got
0:16 kind of a rudimentary system in place
0:18 and I'm only going to improve that
0:19 throughout this video. And so here's
0:21 what we're looking at. Let me just open
0:22 up this door real quick and we're going
0:25 to get to the components panel and we're
0:27 going to see a couple things here.
0:30 one is I've got some kind of labor cost
0:32 here. Let's instead just assume this
0:34 labor cost is not coming from a macro
0:36 that I had established. And we're going
0:38 to say that the uh labor in this case
0:40 for one window is just going to be um
0:43 something like 200. Okay.
0:46 And so what we're looking at here is a
0:49 final output. I've put in the price.
0:52 Now, mind you, if you want to retain
0:53 these things, you'd have to save this
0:56 door back to it being your default door
0:59 or save it back to your library in the
1:01 case that you change these individual
1:03 pieces here, such as setting a price for
1:06 this particular door. Keep that in mind
1:08 if you weren't aware of that. That's
1:10 something that you'd have to do.
1:11 Otherwise, this is just going to be all
1:12 zeroed out when you place a default
1:14 door. Okay. So, I've input these prices
1:18 and if these were my prices that I'm
1:19 going to use for this particular door,
1:21 for my default exterior door, I would
1:23 set this door as default. So, what's
1:26 happening here is we've got a price per
1:29 the door. So, this is the m, you know,
1:31 the actual um procurement price of that
1:34 door. So, I'm going to go buy it from
1:35 Home Depot, what have you. And by the
1:38 time that it's procured, this is the
1:40 price that I'm paying delivered, right?
1:43 And then there's a markup. And now
1:44 markup to me this is you know a standard
1:47 might be 20 25% something like that and
1:50 that's for that's a procurement cost
1:52 that's an ordering cost this is going to
1:54 cover the overhead of you know
1:57 purchasing this store doing the research
1:59 on this store picking this store and it
2:01 also covers and um you know has a base
2:04 amount of information about uh what my
2:07 relationships are with my vendors. This
2:09 is, you know, taking into account that
2:11 I've got years of experience with my
2:13 particular vendor and I've got
2:14 preferential pricing maybe set out
2:16 there. And then on top of that, in case
2:18 something is wrong with that door and I
2:20 have to replace it, that is also
2:23 encompassed into this markup cost. Okay,
2:25 so 20% might be a standard number. So
2:28 I've got a 20% markup. Then I've got
2:30 labor. Now labor, it doesn't include any
2:33 kind of markup, which it should. It
2:35 should have some kind of overhead. Now,
2:36 you could just kind of bake that into
2:38 this number just by doing, you know,
2:40 times 1.25, something like that. And
2:43 that's going to give you something new.
2:46 Although, 200 times what? 100.
2:51 That was interesting. 1.25. I'm doing my
2:54 math wrong. Not even worried about it.
2:55 I'm just going to leave it at 200. And
2:57 so then maybe you have an equipment cost
2:59 as well. So then the total cost output
3:01 is the count. Okay, in this case, it's
3:04 just a one count thing. So count plus
3:06 extra. This is in the case that you need
3:08 to buy um some extra depending on what
3:12 the unit of measurement is. So the unit
3:14 of measurement of a door is each, right?
3:17 Versus something that might be linear
3:19 foot. And so extra linear foot might be
3:21 an extra two linear foot in the case
3:24 that it's an 8ft plank, something like
3:25 that. So it's going to do count plus
3:28 extra times the price. And then it's
3:31 going to do times that markup. And in
3:33 the case of this markup, it is taking
3:35 this as just the number 20, the integer
3:38 20. So it is saying 1 + 20 divided by
3:42 100. So that's going to be that 1.2. So
3:45 it's the price times that 1.2 plus count
3:50 * labor plus count time equipment and it
3:54 gives us a final price. Okay. So, how do
3:57 we establish something that is more set
3:58 up like an RS means setup where we have
4:01 a crew one, crew two, crew three, and
4:05 crew one is our journeyman one and our
4:07 apprentice level one and they cost, you
4:10 know, $45 and $20, making them cost $65
4:14 total for crew one, right? Versus maybe
4:17 we've got a crew two that's $72 per
4:21 hour. Okay? And so that's another piece
4:25 of this puzzle, right? Is that we need
4:26 to have crew prices. Now based on the
4:29 crew price, we should have a value
4:32 that's associated with the type of thing
4:35 that we are installing so that it's a
4:37 modifier. And so well, not modifier,
4:40 it's a multiplier really, which is, hey,
4:43 it's going to take crew one 1.2 hours
4:49 for a door, right, to install that door.
4:52 And so then we're going to get a labor
4:53 cost. And on top of that, we should have
4:55 a markup included in this. Now, I'll
4:57 tell you, I'm just going to share with
4:59 you the preliminary uh macro that I've
5:02 created. And I'm going to come in here
5:04 and actually change this labor cost back
5:06 to that macro. And you're going to see
5:08 here, if I just double click to
5:09 overwrite this text input, I get to
5:11 click on the down arrow here on this
5:14 macro and go userdefined. And in this
5:16 case, I have a macro that I called crew.
5:19 Okay. So, there we go. And we're going
5:21 to see here it's reporting some kind of
5:23 value. And I'm going to show you how
5:25 this is working. So, let me with my door
5:29 selected, I'm going to get into that CAD
5:31 menu text macro management. If you're on
5:34 my pro plan, we have this in the Rabbit
5:36 Design full. And that's this guy right
5:39 here. So, we're going to get into this.
5:40 We're going to find that crew and we're
5:42 going to see how this is working out.
5:44 Now, this is not a perfect macro yet. I
5:46 actually think this could get, you know,
5:48 improved. And I would send this into
5:50 some AI to kind of help me write this.
5:52 But I like to put my uh variable values,
5:57 if it's an internal system, right in the
6:00 front of the macro itself. If this is a
6:03 system that I am um publishing to an
6:06 office environment, maybe I do this in
6:09 some other way, in some way that's even
6:11 more accessible. might even pull in
6:13 something like access from a CSV file
6:16 that can be, you know, imported values
6:18 from our actual uh bidding software, but
6:21 we're just going to keep everything
6:22 internal to Chief Architect in this
6:24 case. And so we're going to put our
6:25 variables in the front of this. And so
6:27 what are our variables? Well, got a
6:29 window multiplier. That means some crew,
6:31 it's going to take them eight hours.
6:33 Door multiplier. Some crew, it's going
6:35 to take them 1.5 hours, etc. Now,
6:38 there's a fault in this logic, but we're
6:41 going to get to that in a little bit.
6:43 Okay. The next thing I have here is my
6:45 crew rates. I've got journeyman one,
6:48 apprentice one, journeyman 2, apprentice
6:50 one, journeyman 3, apprentice one,
6:51 journeyman one, apprentice 2, and
6:53 there's some rates. That means that
6:55 that's
6:57 that um per hour cost. Okay, in this
7:00 case, these numbers are pretty low, but
7:02 here we go. This would be an example of
7:03 this. So, how you how do you calculate
7:05 these numbers? In fact, right, how do we
7:08 even come up with these numbers? I mean,
7:10 truly, if you wanted to do this
7:11 correctly, you might take a journeyman's
7:14 number and then calculate an overhead
7:16 specific to that journeyman and there
7:18 gives you your number and then you do
7:19 the same thing for your apprentice and
7:21 there gives you your number and you add
7:22 the two and you divide it by two and you
7:24 get a number, right? So maybe that would
7:26 be something. Um, or actually, I'm
7:28 sorry, you don't add by two. You just uh
7:30 you add them together and that's it and
7:32 that's your final number. So, I'm going
7:34 to leave that up to you how you're
7:35 calculating these numbers. But what this
7:38 is doing is we've got a pound sign. This
7:41 pound sign indicates that what's behind
7:43 this pound sign on this line only is not
7:47 an executable piece of code. Right?
7:50 That's what's happening here too. So,
7:51 you can use these to generate notes,
7:54 right? And so, then this is an
7:56 executable piece of code. Window
7:58 multiplier equals 8.0. Why do we have
8:00 the 0 Z there as opposed to just eight?
8:03 Well, this lets Ruby know that this is a
8:06 float value. It's not an integer. An
8:09 integer can be problematic. An integer
8:11 is a class value so that if we were
8:14 trying to multiply times something else
8:17 if it it won't necessarily see that
8:19 there's fractions there and it will just
8:21 pick a whole number. Okay? So, it's
8:23 important that you make sure that your
8:25 values are a float number. All right?
8:28 And so then here we go. Here's the next
8:30 part about this is I've got some new
8:32 input which is markup percentage. Now I
8:34 could have put this at the very top.
8:35 That might have been helpful. Who knows?
8:37 But I'm saying my markup percentage is
8:39 25. That makes it easy for an end user
8:41 to just understand that. And then it's
8:44 calculating what this markup is based on
8:46 that markup percentage, which is that
8:48 same kind of math that we did before.
8:50 One plus markup percentage. We're making
8:52 sure it's a float and we're dividing it
8:54 by 100. Otherwise, I would have had to
8:56 put 25.0 in here. And that's maybe
8:59 confusing to someone putting in a
9:01 percentage, right? So, we wanted to make
9:02 sure that 2F is in there. This converts
9:05 this value to a float. It's converting
9:08 this 25 to a float. It's making sure
9:10 it's not an in integer, right? Because
9:13 otherwise, this value would come out to
9:14 one and that wouldn't be helpful.
9:18 Next, we are beginning a code. So, this
9:21 is a, you know, conditional effect,
9:23 cause and effect. We're if this and then
9:25 that, etc. We're executing a line of
9:27 code here by creating a begin statement.
9:30 So, uh, and then this raise part is this
9:33 is going to look for any false, right?
9:36 So, if component code is nil or that's
9:41 what these two vertical bars are or
9:43 component code is empty, that is going
9:46 to raise a problem and it's going to
9:49 skip to the end of this immediately to
9:51 where there's a rescue. Okay? Okay. And
9:53 that's going to put in a statement that
9:55 hey, we know need a key name in the code
9:57 field. What am I doing with this? What
9:59 is component code? Well, component code
10:02 is the code value in the object
10:06 information panel of the object that we
10:08 are selecting right now. Okay. So, we're
10:11 selecting a door right now. In the
10:12 object information panel, there is a
10:15 code input. In that code input is some
10:18 text. Okay.
10:20 And so then here's the next part is base
10:23 rate is
10:25 true.
10:27 So we're defining something. We're
10:29 fetching component code and converting
10:31 that to a float. All right. So what is
10:35 that doing? Well, it's matching. Here's
10:38 our crew. Define crew. So crew fetch
10:41 component code. What do I have? I have
10:45 some code in there that matches these.
10:48 If it does not match these, then we're
10:51 going to kick to the error. Well, guess
10:52 what? I actually didn't have that in my
10:54 error checking. So, I should have done
10:56 that, right? Should have done that in
10:58 case that it didn't match something in
11:00 my error checking. All right. So, I
11:02 could put a second rescue and a second
11:05 raise where it says, hey, if this if
11:08 this crew code doesn't match our
11:11 definition of crew, then print something
11:14 that says it doesn't match. That would
11:16 be something that we should do. Okay. So
11:18 it's saying base rate is crew fetch
11:20 component code and convert that to a
11:22 float value. So it's going to take this
11:24 45 and it's going to convert that to a
11:27 float value. Right? If it finds that J1
11:30 A1 is in the uh code input of my object.
11:36 Next what are we doing? Uh we're
11:38 defining some variable DESC and that's
11:41 automatic description. And we're going
11:44 to convert this to a string in case it's
11:45 not one. it is, but that's okay. And
11:48 then we're going to downcase it and
11:49 we're going to G sub. And so this
11:51 particular G sub, what it's looking for,
11:53 and I had help with with this, getting
11:56 this to be written out, is it's removing
11:58 any kind of um it's doing like what's
12:00 called a fuzzy match. It's removing any
12:03 kind of punctuation or hyphenation so
12:05 that we're potentially matching some
12:08 part of the keyword. Okay. So then
12:11 deescription
12:15 and whatever that value is, we're
12:17 removing or replacing any kind of
12:20 hyphenation and we're replacing it with
12:22 a character space. That's what this last
12:25 part here is. That's denoted by this
12:28 comma followed by quote space. Quote is
12:32 saying, hey, we're going to we're going
12:33 to look for any of these funny
12:34 characters and replace it with a blank
12:36 space. All right. from the automatic
12:38 description. Next, we're looking for
12:42 those automatic descriptions. We're
12:44 saying, hey, we're looking for if
12:46 automatic description includes sliding,
12:49 apron, hung, casement, fixed. If it
12:51 includes any of these, which is that
12:54 DESC, which we defined here, includes,
12:57 and then this K. Well, I don't I'm not
12:59 good enough to know exactly what this
13:01 means, but this is basically saying,
13:03 hey, we're looking through this um
13:08 it's not an index in this case. It's a
13:10 uh an array. We're looking through this
13:13 array of terms for any kind of matching
13:16 in a down case scenario. All right, so
13:19 there we go. And then we're doing the
13:21 same thing for doors, walls, joists.
13:23 These are just examples. And so then
13:25 finally we're doing our base rate times
13:28 our markup times our type mod uh
13:31 multiplier and then otherwise we're
13:33 rescuing and putting this statement as a
13:35 final output. Now, here's where this
13:38 system is not perfect and we should
13:40 improve it, which is that right now
13:43 these are static multipliers
13:46 times our static numbers. But it might
13:50 be that J1 A1
13:53 takes longer to install the door versus
13:58 J1 A2. Okay, J1 A2, well, in this case,
14:02 it' be the inverse. J1 A2 may take
14:05 longer to install a door than J1A1.
14:08 All right, that would be a true RS means
14:11 setup. So, I'm actually going to take
14:12 this and build this in. Let's go ahead
14:14 and fix a couple of the issues that we
14:16 had with this. All right, so I'm going
14:17 to take this. I'm going to copy it. This
14:19 time, instead of using my typical cursor
14:22 AI, I'm actually using chat GBT. I don't
14:25 know why I'm doing that. I think because
14:27 I wasn't ready to build this into cursor
14:28 just yet because the macros that are in
14:30 cursor are stuff that I'm, you know,
14:32 bringing into my pro plan. But um here
14:34 we go. Here's what I'm going to do is
14:37 I'm going to post this in
14:40 here is the current code and I want to
14:42 make a few changes.
14:49 The changes I want to make are I want to
14:52 add an additional rescue and rescue
14:54 statement for in the case that
14:57 component code is not nil and component
15:00 code is not blank but the code in
15:04 component code does not match and then
15:06 the rescue would be that there is no
15:10 matching code to the component code
15:12 input field from the object information
15:14 panel.
15:18 Next, I want to add multipliers for our
15:23 different crews for the different type
15:26 of object they are installing since they
15:30 don't all install each object at the
15:33 same rate. And so, we need to add
15:36 multipliers
15:38 based on which crew is installing which
15:40 object. And so we can do this by setting
15:43 up an array for each crew alongside of
15:48 their
15:50 price.
15:55 I think I was pretty clear there. So my
15:57 big trick with learning how to code with
15:59 AI is overexplaining. And not only do
16:03 you overexlain this time, but if you
16:06 need to make another edit, you should
16:09 then go reexlain what you had explained
16:12 before because guess what? This is a
16:14 complete new set of instructions. There
16:16 is no true memory in this. I can go over
16:20 this in detail, but I'd rather point you
16:21 to another video, and I think I'm going
16:23 to do that in another video where I
16:25 explain, hey, let's go look at exactly
16:28 how AI works so you can better
16:30 understand how to use it and not be
16:32 frustrated by the output results. Okay,
16:35 so here we go. Is it's done a thing.
16:38 Let's see what it's done. Let's go ahead
16:39 and review it. It's nice to review it in
16:41 chat GBT because it's colorcoded. And so
16:44 some of these some of this color coding
16:46 has to do with exactly how this is all
16:48 running. Okay.
16:51 And one second because I am getting my
16:55 little preview here on the page. So I'm
16:57 making sure when I zoom in it's actually
16:58 on the screen. So when we zoom in, are
17:01 we still on the screen? We are. Cool. So
17:04 here we go. Window keys. And then these
17:07 are those key values to look for those
17:10 search parameters. Okay. So that's
17:12 what's going on there. Now,
17:15 the next part about this is we're
17:18 setting our modifiers with the crew
17:20 itself. So I could actually switch these
17:22 two because I would almost want this to
17:24 be at the very top. So J1 A1, there's
17:27 our base value. There's our multiplier.
17:30 So this is really clean code. This is
17:32 really easy to understand. Markups 25%.
17:37 We've got an argument error for that
17:39 component code.
17:42 I'm going to have to splice this video
17:44 by the way. Uh I just my computer just
17:47 crashed out right in the middle of that,
17:48 but I think I've picked up right where
17:49 we've left off. So back to this is that
17:52 we're looking at this raise argument
17:54 error. Uh this is going to be, you know,
17:56 creating that raise argument case about
17:59 the component code being empty,
18:01 component code being nil, and where it
18:04 kicks off to some kind of rescue at the
18:06 bottom of the screen right here. So
18:08 there we go. So this is the rescue for
18:10 argument error. This is the rescue for
18:12 key error. So argument error is if
18:14 component code is blank, right? And then
18:18 right after that we have a base rate per
18:20 type crew fetch.component code. So we're
18:22 going to fetch that component code.
18:24 Hopefully it matches one of our
18:26 component codes uh which we've you know
18:28 created an array in this case or a hash
18:31 in this case.
18:33 And then we could see you know we're
18:35 checking to see what category something
18:36 is. um the case of those categories,
18:41 you know, how how that stuff is worked
18:43 out. So, you can see here I've got
18:45 something in here that says when it's a
18:47 wall, so when something is defined as a
18:49 wall, then pro that type of wall, we're
18:53 going to define the length and we're
18:55 going to, you know, multiply our
18:57 multiplier times the length of that
18:59 wall. So, this would be a per foot cost
19:01 in that case. So, you can do kind of
19:04 establish these kind of setups. Again,
19:06 we're trying to get really close to that
19:07 RS means style of estimating. Okay. And
19:12 so I'm going to take this and copy it.
19:14 Now note I just kind of hover over here
19:16 and hit that copy button. This is chat
19:18 GBT the desktop version. And then I'm
19:21 going to slide that over to the left.
19:22 I'm going to select my door. I want to
19:25 open this up. First of all, I can look
19:27 at the object properties which is built
19:28 into Chief Architect. And so we could
19:30 take a look at the values here and just
19:33 take a look at some of the things that
19:34 are happening here. We can see here
19:36 under component code there is in fact a
19:38 code there J1 A1. All right. And then I
19:41 want to get to my macro. Let me just go
19:44 ahead and control or command A control
19:46 or commandV. And so I'm just pasting
19:48 these values back in. Notice that the
19:51 output is the same in this case. And
19:53 that's because my modifier for
19:57 this was our base value anyway. So
20:00 instead, if we use the J2A1,
20:03 not only would we get a, you know, $50,
20:06 so we get an increase in cost, but maybe
20:09 it takes them a little bit less time to
20:12 install that door. So, how do we check
20:14 this out? Well, we just press okay.
20:17 Press okay again. Let's get into the
20:18 door itself.
20:20 And let's get into that object
20:22 information panel. And I'm going to say
20:24 J. Well, first of all, let's go look at,
20:26 you know, what this all works out to be.
20:28 So, in the components, our total price
20:31 is 3.8438.
20:33 So, what's this doing? It's picking up
20:36 our labor, which is8438 per door. Okay.
20:40 It's got this price here, $250 each, 20%
20:43 markup on that, you know, procurement
20:46 and everything else. All right. And
20:48 there we go. So 8438 what happens when
20:52 we come in here and change this to a J2
20:55 A1 right and come back here is 38750.
21:01 So that does in fact change just like
21:04 that. And so when we then go calculate
21:08 materials for this that's what's
21:10 happening here. We're going to have to
21:12 include some other categories here to be
21:14 able to see our total cost. So we're
21:15 going to want to edit this active view.
21:18 And in the edit the active view, we're
21:20 not getting into column categories here.
21:22 We're getting into columns. And so in
21:24 this case, we want to see the markup
21:26 labor. And our total cost is going to
21:28 reflect those. All right? Because now
21:30 it's it's an inclusion, if you will. All
21:33 right. So let me press okay. And we can
21:36 see bam, we've got this. Now this total
21:40 rows is reflecting our calculations. So
21:42 this is all calc.
21:45 So, what happens when we improve this
21:47 count to something like three? Just like
21:49 that, it's updating. This is working
21:51 great. Bust out your calculator, double
21:53 check those calculations, make sure that
21:55 this is working. Now, not only can we do
21:58 this system as it is right now, right?
22:02 But we might even be able to do some
22:04 conditional statements based on object
22:06 information supplier where you add
22:08 another multiplier based on the
22:10 supplier. And so the supplier would then
22:14 do something like affect your overall
22:17 price. Okay? So, you know, let's just
22:20 say you'd have a conditional statement
22:23 that says, hey, if Home Depot, you know,
22:25 multiply the price times 75, right?
22:28 Because we get it cheaper at Home Depot
22:29 than we get it at our local lumber yard
22:31 or something like that. So, that would
22:33 be um, you know, even a more advanced
22:36 system and robust system. Now, what's
22:39 great about using those object
22:41 information panel inputs here is that
22:44 every one of these can be saved as an
22:46 individual component of a style pallet.
22:49 Well, an individual attribute that we
22:51 can apply with a style pallet tool.
22:54 Custom fields are a little bit
22:56 different. You can only apply all custom
22:58 fields. So, if you have some other
23:00 systems like I do in the custom fields,
23:03 we're not going to want to create a
23:04 system based on custom fields because it
23:07 will override other systems in terms of
23:09 utilizing a style pallet. What the heck
23:12 is a style pallet? Hopefully, you know
23:13 that already, but let's just go ahead
23:15 and build one. And so, what I'm going to
23:17 build is I'm going to start with the J1
23:20 A1 style pallet tool. So, I've put in
23:23 there my code J1 A1. Let me press okay.
23:27 And now in my edit toolbar, I'm going to
23:29 use add object to style pallet. So let
23:32 me add this. We're going to create a
23:34 new.
23:36 I'm just going to call this through A1.
23:40 Excuse me. J1 A1.
23:46 See J1 A1. There we go. And I want to
23:50 make sure I'm setting the properties on
23:52 this. And I'm going to clear all. And
23:54 really the only property I want is that
23:57 component code. And so that is only
23:59 applying that to whatever I spray this
24:02 on because a style pallet is a sprayer.
24:04 It's going to spray some object
24:06 attributes. All right. Now, I want you
24:08 to notice the setting at the bottom
24:09 here. Only apply properties to doors of
24:12 same type. That does not mean exterior v
24:16 versus interior. In fact, quite the
24:18 opposite. It means type in terms of
24:22 hinge or biffold or pocket. So, we want
24:26 this to be able to apply to all door
24:28 types. Do keep in mind that your system
24:31 only gets more robust if you're going
24:33 to, you know, create an index based on
24:36 the type of door you're installing and
24:38 how long it takes to install that door.
24:40 That's just adding another level of
24:42 complexity. We could do that pretty
24:44 quickly, believe it or not. In fact,
24:46 what I would probably do is create an
24:49 overall hash of values where we're just
24:52 going to make a huge hash of all the J1
24:54 A1 costs um and modifiers or multipliers
24:58 rather where it's taking a look at the
25:00 door type and putting a number to it.
25:02 And so you're just building that out of
25:04 you know your your particular pricing
25:06 model. Okay. So, I want to uncheck this
25:10 in this case because I want it always to
25:14 apply to all door types that this is a
25:16 J1A1 crew that I'm trying to get a
25:18 pricing model. Okay. So, I'm going to
25:20 press okay. This is going to add it to
25:22 my library. Right there it is right
25:24 there. It's added to my library. Now, if
25:26 you want to take this another step for
25:28 forward, I would, you know, add some
25:30 tags to this. I have a particular
25:31 stacked tag system. I have videos about
25:33 that somewhere else. So this might be a
25:36 utility special tool or it might be a
25:38 painter in this case. And in this case
25:40 it's some kind of material costing. So I
25:42 might even put material as the tag and
25:45 utility special tools. Yeah, there we
25:47 go. That's fine. So what does that mean?
25:50 I'll show you. Let's go ahead and open
25:52 this up. And let's just say that this
25:54 was actually set to
25:56 A1 J3 A1. All right. And so when I use
25:59 the crew J A1 deal here, I'm going to
26:03 apply some of our key mode. Swipe this
26:05 whole thing. What's that going to do?
26:07 Well, it's going to bring this window
26:09 into J1 A1, and it's going to bring this
26:12 door into J1 A1. I've effectively
26:15 changed the crew that's going to be
26:17 installing these two objects. Okay, so
26:20 when we put this side by side, I believe
26:22 material lists are active and actively
26:26 updating. Let's just go take a look real
26:27 quick. is let's open these two up. Oh,
26:30 we can't open them at the same time.
26:32 That's okay.
26:34 Let's put this at J3 A1
26:37 for instance. Let's go take a look. Does
26:40 price reflect that change? And we'll
26:43 take this back down to just one.
26:46 Right. So that's at 420. We use our J1
26:50 A1 back in this view. Swipe this. Let's
26:54 look at the There it goes on the fly.
26:56 It's updating. So if I go back a level
27:00 and look, I'm just going to make a new
27:01 style pallet here. And this is going to
27:03 be a create a new as well. And it's
27:05 going to be through J3 A1. And we're
27:10 going to do that same thing. Only
27:12 properties. Uncheck that. Clear all
27:14 component code. Press okay. Press okay
27:18 again. Now we've got that crew J3A1.
27:22 Now, it would be nice if at the same
27:26 time you added the window as well to
27:28 that existing tool. So, we're going to
27:30 add this to the style palette. This
27:31 time, we're going to choose add to
27:33 existing. And I'm going to find that J1
27:38 A1 in this case. Enter. And there we go.
27:42 And so, I've now added a window to this
27:45 sprayer. All right. So, same thing.
27:48 Clear all component code.
27:51 Press okay.
27:54 Now, if these both were J3 A1,
27:58 we can just swipe across these with our
28:01 J1 A1, and it's going to apply that to
28:03 both the window and the door.
28:06 Boom.
28:08 So, just as easy as that, you could
28:10 determine what your job costing is going
28:13 to be if you build out those indexes of
28:15 modifier values and you build out your
28:18 objects. Now, keep in mind I would have
28:21 to set this as my default door, right?
28:24 Exterior door defaults have been
28:25 updated. Why is that important? Because
28:28 we've set our price up for this already.
28:29 So, when I place this hinged door again,
28:33 now I'm coming in here to the components
28:36 panel and we see a price. Keep in mind,
28:39 you can create an index of prices that
28:41 is a separate macro. Let's go ahead and
28:43 do that right now. Let's make that you
28:45 know kind of the final step of this is
28:52 I need to revise this existing macro to
28:56 reference
28:58 macros dot
29:01 actually type this out. I'm going to say
29:03 macros dot um what are we going to say
29:06 here? We're going to say unit pricing
29:08 unit pricing
29:15 which will become a
29:19 hash output
29:23 and that's going to reference
29:26 our various
29:28 pricing modifiers per cruise and our
29:31 crews themselves. So the definition of
29:34 crew is going to come from that separate
29:36 macro.
29:38 And so that's how you access that
29:40 separate macro is you're going to have
29:42 to access the macro and then analyze the
29:45 macro to gather the values coming from
29:49 it from their name, value, pairs, etc.
29:52 And so then I want you to make that
29:54 second macro and it's going to be all
29:56 the crew values, but we're going to
29:59 expand on things such as door. We're
30:03 going to put different unit pricing for
30:06 door by type as well as different unit
30:10 pricing for window by type.
30:14 So for instance, we will have a triple
30:16 casement window and a price. We will
30:18 have a hinge door and a price. We will
30:20 have a biffold door and a price. We have
30:21 a sliding door enterprise. Go ahead and
30:24 make up some numbers for this and build
30:26 this out so that we can test that symbol
30:29 system.
30:34 So robust instructions and I know that
30:38 it helps that I know a little bit about
30:39 scripting to know what exactly to say,
30:42 but hopefully you just picked up some a
30:44 few key things about how I'm even
30:46 describing my need there, right? And
30:49 let's see what it comes up with.
30:52 So the the thought process here is we're
30:54 going to have a separate macro that we
30:55 can maintain separately from this main
30:57 code because it's going to start
30:59 becoming more and more robust, right?
31:00 And that separate macro is going to take
31:02 into account the type of door that it is
31:04 and we'll have individual modifiers
31:06 based on those types of doors, right?
31:08 Because you know it's going to take us
31:09 longer to install a slider. Then on top
31:12 of that, as you get to this system more
31:15 and more refined, you're going to come
31:16 up with a unit price for a sliding door
31:19 per foot of sliding door or per foot of
31:22 sliding door past 8 ft, right? Or past
31:25 5t where the cost incrementally changes
31:28 because it's just more work to install.
31:31 Okay, so what do we have now? This is
31:40 default multiplier is 1.0. No. Okay.
31:45 And so this is
31:49 this is our main crew one. Let's see
31:51 what happens with this. Very curious to
31:53 see how this works out.
31:58 So immediately it's going to throw an
32:00 error because it's looking for another
32:02 macro that doesn't exist yet.
32:05 Right there it is. Unit pricing doesn't
32:07 exist. Okay. So that's the first part.
32:10 Now, we do need to create unit pricing,
32:14 right? If I just put one in here and
32:16 evaluate an owner object,
32:19 then the crew
32:22 one
32:24 shouldn't necessarily of a string into
32:27 an integer, right? It's looking for a
32:29 hash. So, that's that's kind of the
32:31 problem there.
32:33 So, let's get you back to unit pricing
32:35 and let's see what they've got here.
32:38 Okay, we're going to copy this.
32:41 Paste this in. It's creating its hash.
32:44 You can see in this hash crew base
32:45 rates. Okay.
32:49 Multipliers
32:52 and then
33:00 interesting.
33:02 It's almost like it's setting pricing
33:04 here. But we'll just see that this
33:05 system works even though it needs some
33:07 refinement.
33:11 Uh unexpected return local jump area.
33:14 Let's give that back to So I like to
33:17 just copy this and say what it's coming
33:19 from. Right? So
33:22 first macro has this error.
33:28 And actually before that it might be
33:31 useful
33:35 Oops.
33:39 Did not mean to do voice to text.
33:42 Okay.
33:43 So, we're also going to put the output
33:46 from
33:48 unit pricing so it has an opportunity to
33:50 see.
34:00 Therefore, you know, now it has full
34:02 context. It sees what the output is from
34:05 its other macros so that it can
34:06 understand what the error is coming from
34:08 and address it that way.
34:22 So, it seems to be recognizing the
34:24 problem. And you know, this is where I
34:26 start to the first time I get an error,
34:28 that's when I start to go, "Oh boy,
34:31 fingers crossed. I don't want to battle
34:33 this thing for hours." And you know,
34:36 more often than not, I need to Oh, boy.
34:38 What just happened here? You're not
34:40 doing a voice chat. I didn't want to do
34:43 a voice chat, my friend.
34:51 Okay. Well, let's just repost these two.
35:07 I mean yeah, this is where I start to
35:08 go, "Oh, please don't don't make me
35:10 battle this thing."
35:12 Then more often than not, it's good to
35:15 just throw this into a separate AI as a
35:17 kind of a, you know, check for potential
35:20 errors because you think about this, the
35:22 approach to this is like building
35:23 blocks. You're building, you're
35:24 building, you're building. And when you
35:26 finally come to a conclusive system,
35:28 it's not necessarily the best system
35:31 that you could have made because it was
35:32 approached in a linear way. This is also
35:35 why I love cursor is cursor doesn't
35:38 quite approach in such a linear way when
35:41 we have multi-art systems like this.
35:43 It's a little bit better at figuring out
35:45 how to improve a system
35:48 coming from the standpoint of it not
35:51 being, you know, put together piece by
35:53 piece.
35:55 Copy this. Let's see what happens when
35:57 we kick this out. And there we go. Got a
36:00 value. So now we have modifiers based on
36:02 the type of door. Let's test that out.
36:04 There's 256.25.
36:07 Okay. Let's take this door. Um, let's do
36:11 a little material calc based on this.
36:13 So, we could just send it side by side
36:15 so we could see this. Do that same
36:17 thing. Edit the active view include our
36:20 labor and equipment or excuse me, markup
36:22 and labor.
36:24 But take a look at this value
36:27 384. Now, what happens when we change
36:30 this to a different type,
36:32 right? So, we're going to change this to
36:34 instead a slider instance 356. So that
36:39 did in fact change the price. Isn't that
36:42 cool? Based on type. And then like I
36:44 said, you can add on some kind of
36:46 conditional statement based on length.
36:49 So what does this mean? Well, this is a
36:52 little bit more difficult to set default
36:54 as. You just got to be careful. Some of
36:56 these don't distinguish between interior
36:58 and exterior. It might be easier to set
37:00 up your defaults in your default
37:02 settings here. Okay,
37:05 there you go. And then your unit
37:07 pricing, you should come up with a macro
37:10 specific for that. So, and it's um if
37:13 it's an exterior hinged door, it's this
37:16 price. You know, you use that same uh
37:18 macro setup. So, interior door, it's
37:21 this price. Slider, it's this price per
37:24 unit. You know, you can do a conditional
37:26 statement like that. I'd love to hear
37:28 any questions that you might have. This
37:30 is building off of um a series that I'm
37:32 starting to develop which is you know
37:34 I'm able to now communicate two ways. I
37:37 can communicate from job tread into
37:40 chief architect. I can communicate from
37:42 chief architect back into draw job
37:45 tread. Right? So now that means we could
37:47 take material lists from chief architect
37:51 import them into job tread which would
37:53 make it very helpful if we had an rs
37:55 means style reporting like this. So, if
37:59 you're following the series and you're
38:00 getting into material quantities,
38:02 takeoffs, you know that I don't build
38:04 accurate models, so I don't pay much
38:06 attention to material takeoffs and
38:08 quantities. That doesn't mean that I
38:10 can't build you systems that do, right?
38:12 Um, so it's capable of doing that,
38:14 especially if you're doing, you know, in
38:16 the remodel game, a lot of times we're
38:17 just looking for partial assemblies.
38:19 We're just looking for unit pricing of
38:21 something, right? We want to know how
38:23 much it, you know, costs to install
38:24 those windows cuz that's a lot of long
38:26 form estimating or something like that.
38:29 So,
38:31 let me know if you have any questions.
38:32 Thanks.
38:46 [Music]
