---
videoId: RmBx5PnXaDM
title: Updating My Fastest Detail Cross Section System For Better Automation In Chief Architect X17
url: "https://www.youtube.com/watch?v=RmBx5PnXaDM"
status: imported
---

# Transcript

0:18 Oh, I guess I'm streaming.
0:21 I'm still getting used to this.
0:26 Oh, dang it. I got to double check I'm
0:28 streaming every time otherwise.
0:31 I'm nervous that I'm not
0:34 streaming right now.
0:37 Yeah. Okay. I'm streaming right now,
0:40 man. I'll figure it out one of these
0:42 days. Anyways, if you're
0:48 I just I just created a stream and said,
0:51 "Hey, what the heck? Let's start
0:52 streaming." So, there's no no one in
0:54 here talking to me. I'm talking to a
0:56 wall. Um, so here's what I'm doing. I I
1:00 have a a cross-section system that
1:05 does a lot with a little bit of input.
1:07 But a big part of, you know, moving
1:10 forward with my systems is I'm I'm
1:13 adding things that that save you time
1:16 that are complicated things. And then
1:20 the process for getting you to that is
1:23 typically pretty complicated to get it
1:25 to automate the way I need it to be
1:27 automated.
1:29 But then I've got to go back and look at
1:31 it from a new lens and think, hey, this
1:34 isn't that intuitive to an end user and
1:38 how can I scale it back and make it more
1:40 simple and make it easy for an end user
1:43 to see? And I mean, this is case in
1:45 point. We're showing my layout template
1:48 and right off the bat, this is
1:50 overwhelming. You know, it has too much
1:53 stuff in it. But these things do
1:55 something and and even though they do
1:59 something, they require instructions.
2:01 And so, how do you how do you kind of
2:03 build in instructions? And that's tough.
2:07 And since Chief isn't an open APK, you
2:10 can't just build in some tool that'll,
2:13 you know, give someone some highlighted
2:15 instructions as they hover over
2:17 something. So then how do you approach
2:19 it? Do you build this, you know, some
2:21 side project where it's, I don't know,
2:25 some other helper outside of chief
2:27 architect? You never know. So, a lot of
2:30 these things are really complex and and
2:32 then you think you got to go back and
2:35 revisit it and see if you can't simplify
2:37 it. So, one of the things that's complex
2:41 and I've simplified it as much as I
2:44 could up until X16 was my detail system,
2:47 which is it drives all the annotations
2:50 on this sheet from some central place in
2:53 my plan template. And then it makes it
2:55 so that we've got details that can be
2:58 traded out and represent cross-sections.
3:01 And so you can build them really
3:02 quickly. Now, I could build this
3:03 cross-section in a matter of minutes,
3:05 but the setup for this is a little bit
3:09 of work. And the setup page for this is
3:12 immediately complex.
3:14 And so beginning user to my templates
3:18 always looks at this and and thinks,
3:21 "Wow, that's a lot." And it is. It's a
3:23 lot.
3:24 And
3:26 so I'm wondering if I can't simplify
3:29 this system. And I think I've come up
3:32 with a way of doing that. And it's
3:34 specific to X17.
3:37 So the way that this current system
3:38 works, and I'm just sharing this
3:41 publicly, by the way, because it takes
3:43 so much work to build this that not
3:46 really worried that someone's going to
3:47 steal these ideas. More power to you if
3:50 you go and put in the work to do this.
3:52 um it it takes many many hours to build
3:55 this. So I'm happy to share the
3:57 information on how it was done. And so
4:00 these are schedules and these schedules
4:04 come from notes and those notes dictate
4:07 an annotation. So we have an annotation
4:09 in the note itself and then it sees if
4:12 that note is schedule number one. So if
4:16 I slide this 2 by8 Doug fur up to
4:18 schedule number one, what we get is that
4:22 this has been updated immediately and
4:24 it's been updated across all 75 80
4:27 details that I have. So that we just get
4:30 the drive annotations from one central
4:32 place.
4:34 But let's back up again and say, hey,
4:37 this is still an overwhelming screen.
4:41 And what if we can make it so that we
4:43 never had to have a novice end user look
4:48 at this screen?
4:50 Now, for one, the model is not
4:53 communicating with this. It couldn't
4:56 before. Not without a lot of steps, a
5:00 lot of manual steps and complex steps
5:03 that was even more complex than just
5:05 sending someone to this page.
5:08 But now, I think we can. And that's
5:10 because we got an object information
5:12 panel in framing members. We have new
5:15 framing member defaults in X17. So if I
5:18 come into default settings, framing, we
5:21 have a framing members section here and
5:25 I can start
5:27 setting up
5:30 framing member specifications.
5:33 I'll show you how this kind of works and
5:34 I'll and I'll and I've got to kind of
5:36 try to think through this system as I'm
5:38 as I'm building it live um in my
5:42 membership area and in my forums and in
5:45 my Discord server and in and in our you
5:49 know just comments in YouTube. I do see
5:52 often enough that people love to see me
5:55 struggle. They like to see me, you know,
5:58 kind of fight through these things and
5:59 and see my process for creating systems.
6:03 And you're going to see me struggle on
6:04 this cuz this is not a straightforward
6:06 thing. And I'm and I haven't even
6:09 thought about how to do this beyond just
6:12 about 5 minutes of of concentrating on
6:15 it and and I haven't tried anything. So
6:18 here's the thought.
6:20 The existing system I want to remain.
6:23 It's a fallback system in case we want
6:25 to override from something that's coming
6:28 from the model that's not correct. So
6:30 the end goal is driving these
6:32 annotations from the model. That's
6:34 awesome.
6:35 But we still want to be able to override
6:38 those. So I think what I need is I need
6:41 an option and I'm going to use floor
6:43 framing as my test. I need an option to
6:45 say, hey, we're going to drive this from
6:48 the model.
6:49 And so this is going to be a unique
6:52 process. It's going to be different from
6:56 any previous process here. So here's my
6:58 floor framing annotations. They're built
7:00 from notes. And so I'm going to copy a
7:02 note over. And this is going to be my
7:04 test note.
7:06 And what it's doing here is it's so it's
7:09 picking up schedule number from object
7:12 information this field value. And
7:18 so I think I can just say
7:21 I think I can just do this. Um
7:29 so opening closing percentage signs is
7:32 basically a call to um do a text
7:35 replacement using our our macro systems.
7:38 And if we're going to do it in an inline
7:40 code, we need a global. And so the way
7:44 my system works is if schedule number if
7:48 this note is schedule number one, we're
7:50 just going to grab this field value. So
7:53 we typically would not put a macro in
7:55 here, we'd just put text. And so it's
7:57 just going to define
8:00 a global macro, which keep in mind that
8:02 works across all open plans, all open
8:04 layouts. We were going to define a
8:06 global macro in this system that then is
8:09 you that that same macro.
8:13 This is really complex is used in an
8:15 index that is then being referenced in
8:18 all details.
8:20 The full system is very very complex. So
8:23 adding to it is supposed to be scalable
8:27 since it's all built now. So what I'm
8:29 doing, if I can try to talk this out in
8:32 a way that's an end user, a viewer can
8:35 understand, is I'm creating a potential
8:39 new index value. And that value is going
8:42 to be a global where I'm saying, hey,
8:45 floor
8:47 framing
8:48 from
8:50 model. And I need to remember this. So
8:53 I'm going to copy this. And I have
8:54 clipboard history turned on. So even if
8:57 I copy other things, I'll I'll be able
8:58 to access this. So floor framing from
9:02 model
9:06 and so this becomes an option now in my
9:09 schedule or floor framing.
9:12 Get it right.
9:15 Framing framing
9:24 and I don't see it.
9:28 I do wrong. See, you're going to see me
9:30 struggle. Oh, it's right here. It's this
9:32 blank.
9:34 Okay. So, the reason it's blank is
9:36 because that input was a a macro call
9:39 and the macro call doesn't exist. So, I
9:43 need to change
9:45 um
9:47 the the text that's being reported to
9:49 the schedule is being reported from text
9:51 above line. So I can just say
9:55 from model
9:58 I think
10:03 and no that's not true.
10:07 So
10:10 columns to include reset this is coming
10:14 from text. Okay.
10:18 So this is coming from. So I'm just
10:21 going to undo once. Okay. Open this up.
10:25 And this text is driving
10:29 a name, but we can just add outside of
10:31 this percentage column from model.
10:39 There we go. So it's got some blank and
10:43 then it has from model, which is why it
10:45 looks like a double line.
10:48 Not sure that I could delete the first
10:50 line. Anyways, just drag this up a
10:54 little bit.
10:58 So, if I drive this to the top here
11:04 and then as a test, we just did
11:10 framing from model equals test.
11:16 Sure.
11:18 Then
11:24 that did not open and that might because
11:26 be because we're doing a macro call
11:29 within a schedule that is producing a
11:31 macro call. So that usually means we
11:33 have to open a schedule and close it to
11:36 initiate it.
11:39 Oh, and test doesn't mean anything
11:42 unless we put it in quotes.
11:52 And there we go. Okay, so that's
11:54 working.
11:55 The main problem here is that we're
11:57 doing a macro call inside of a macro
11:59 call. So even if we made this come from
12:01 the model,
12:03 somehow we have to get this to
12:05 initialize
12:07 because otherwise someone has to come in
12:09 here and open up a bunch of schedules.
12:13 That might not be something I solve in
12:15 this live video. So now I want to do the
12:18 true test which is let me get back to a
12:22 plan view
12:25 where we've got framing
12:29 and I'm going to regenerate this
12:30 framing. But first I want to get into
12:35 our framing. Oops, not manual framing
12:37 framing members. get into
12:42 joists.
12:47 Okay.
12:49 And then in object information panel
12:56 and I think just in label replacement
13:02 and we want to know what a joist even
13:05 reports. So we're missing some details
13:07 here. Hold on. going to select a joist.
13:09 Let's get some information about this.
13:15 I think that we want Yeah, we want
13:17 nominal size.
13:22 We want this.
13:27 And then there is no
13:31 indication of spacing
13:35 unfortunately.
13:39 And we wish we had that
13:47 normal size and maybe we want material
13:49 but maybe not.
13:52 So really we're just getting the size.
13:54 Okay.
13:57 So back to our default to show how this
14:00 kind of works is framing
14:04 framing members joists
14:10 table replacement means that we're going
14:12 to do
14:14 floor framing from model equals
14:18 nominal size
14:25 and in
14:27 I think I have to say plus
14:33 text
14:35 um at 16 in
14:40 and we're going to do a little
14:43 escape character. The escape character
14:45 says that you know this is this uh
14:47 quotation mark is not um calling text.
14:51 So we're we're we're you know ignoring
14:55 that this is a character that could be
14:57 indicating we're calling text within a
14:58 macro so that it just is a string that
15:02 is a quotation mark the 16 in O period C
15:06 period.
15:08 Um and we'll probably get a little
15:10 fancier than this because I have a
15:12 global system that drives the species of
15:14 wood and we'll probably add that but
15:15 right now I just want to test this real
15:17 quick. So there we go. Press okay.
15:21 That's joists. Press done. And now
15:26 go up a floor and rebuild that framing.
15:36 Maybe that worked.
15:40 And it still says test from model.
15:45 Oh, but I didn't open and close this.
15:48 And it still says test from
15:51 Okay,
15:53 there we go. This is the start of my
15:55 struggle.
15:58 So, first of all, let's see if these
15:59 actually carried with them that object
16:01 information. They did. And um
16:05 and so why didn't that generate
16:07 something?
16:14 Probably because it's not a valid macro
16:16 for some reason. So, let's do a little
16:19 copy and
16:21 let's do a little test.
16:24 Um, equals
16:31 owner nominal size
16:34 16
16:38 and
16:39 it's not doing this correctly. Okay,
16:43 so I need an inline script. I'm going to
16:45 go ahead and use a little chat GB teach.
16:47 Um, something people don't know is I'm
16:49 really good at uh troubleshooting
16:52 problems with macros. I am not good at
16:54 writing macros. That is a misconception.
17:02 Let's see
17:05 this inline cut generator.
17:22 They didn't give me that in a little
17:23 code block. Let's just test this real
17:25 quick. We won't even define anything
17:27 yet. Let's do
17:30 Okay, so that worked.
17:43 You can't see this.
17:50 Okay,
17:52 so that's correct.
17:56 What did I do wrong there in my version?
18:01 I don't really see what I did wrong.
18:03 Mine looked like almost identical to
18:06 that. That was close.
18:13 By the way, I have no idea if my mic
18:16 works or anybody's even watching this.
18:18 someone is watching this, throw me a
18:20 little message in the active chat and
18:22 that way see
18:27 that was close.
18:33 By the way, I have no idea if my
18:49 Okay, there's that.
18:53 Okay,
18:54 level
19:00 it. Should
19:08 be able to do a little
19:11 this.
19:20 Okay, I think that's working.
19:27 Holy cow. All right. So, this is cool.
19:32 And I didn't have to update the
19:34 schedule. Okay.
19:42 So, I want to open up
19:48 and double click this heading. It's
19:50 going to give me a little side by side.
20:04 So, here's what we're looking at. This
20:05 guy right here. So, here's here's what I
20:08 should be able to do. Change my floor
20:11 defaults
20:14 to
20:18 seven and a half.
20:27 Interesting. What happened here?
20:34 Why did that just change?
20:38 I'm not sure. Okay, reframe this,
20:46 which didn't frame anything for some
20:48 reason.
20:49 All right. Working.
21:03 That's okay. That says 2x8.
21:13 Okay. So, I think I do need to open up.
21:17 Yeah. to open that up, but it is being
21:20 driven from the model.
21:25 That's it. That's the end of the That's
21:27 the end of the live show. Glad you could
21:29 join me. There's no one in here anyways.
21:34 All right. At what point do you just
21:35 examine, you know, the psychosis of a
21:38 streamer that has to just talk to a a
21:40 window in a monitor and pretend like
21:43 people are there.
21:48 All right. Well, that's very cool. So,
21:52 now I got to think about this.
21:55 I'm curious about with the little um
21:57 16inch back slash thing. What happened
22:00 there?
22:22 There there is no backslash there.
22:39 How is it translating that backslash?
22:50 That's the ano tool saying that
23:09 We're defining a macro inside of a
23:12 macro.
23:17 Do I even need to do this? I take away
23:21 the percentage.
23:22 Oh,
23:25 well, that's really confusing.
23:30 and build off.
24:04 I think I need to escape. Need I do need
24:07 to have an escape.
24:14 Yeah, if I really knew my stuff like Joe
24:17 Carrick or Michael
24:20 be up in Alaska, they'd know exactly
24:22 what I'm running into, right?
24:32 I'd have to like really write this down
24:34 and map this out to understand
24:39 my full system which is saying okay
24:42 we've got
24:46 the start of it is the framing member
24:49 and it's got a percentage called
24:50 defining
24:53 a global and then that goes to a note
24:57 that is saying, "Hey, let's look at a
24:59 custom field macro." And within that,
25:02 that's what we're going to report. And
25:03 within that is this other macro that's
25:06 defining a global. And if it's schedule
25:09 number one, then that's
25:12 going to define a new global.
25:16 Or I can just fuss around and try things
25:21 like this.
25:30 And still does not produce
25:35 correct escape.
25:47 I mean, I could
25:50 I could G sub
25:54 I'm getting clever. Let's see here.
26:02 Put something conditional in
26:12 or or
26:15 a different idea.
26:28 It's just going to be a test, but this
26:30 is going to be a like a hash index. So,
26:33 here's the thought. If you if you define
26:36 a macro within text macro management,
26:39 then it will be formatted differently
26:40 than if we access direct from custom
26:43 fields. Custom fields is very unique in
26:46 that you can
26:51 you can act custom fields is what? It's
26:54 an array. Yeah, custom fields is an
26:56 array. And so you're basically accessing
27:00 a particular custom field as an array
27:02 because it's an array. We're not
27:06 we don't need the same we don't have the
27:07 same rules for executing the script.
27:10 It's really hard to explain that. Um,
27:13 but so if I if I generate my global
27:19 within a a macro and then I put that
27:22 macro in the custom field, it's going to
27:25 execute differently. So I might be able
27:27 to just do
27:31 this,
27:33 which is
27:34 basically doing like a pass through, if
27:37 you will.
27:43 And
27:45 with this logic, I can do something
27:47 conditional, which would say, hey, we're
27:50 only going to report nominal size if the
27:53 the source object is, you know, of an
27:56 object type joist. So I could put all
28:00 the conditions for all different framing
28:01 members in one macro. be put in a custom
28:04 field of all framing members, making it
28:07 a lot easier to manage, especially
28:11 scalability down the line.
29:13 evaluation here.
29:22 I approached this like cross my fingers
29:25 across. Well, I don't know why it has an
29:27 eval error cuz here it does not.
29:44 Oh, look. I got someone in here. Again,
29:47 you probably you probably rewind and
29:50 just caught up to the part where I said,
29:51 "Hey, is anyone in here?
29:59 Okay. Label replacement gives an eval
30:03 error. Why?
30:05 Why?
30:08 Why is that giving?
30:11 Oh, it's not there.
30:14 Okay, there we go. Fix the formatting.
30:16 That theory was correct. Okay, we're
30:19 getting somewhere.
30:34 Gill again, it looks like you might be
30:36 at up at the live portion. Thank you.
30:38 Thank you for for responding. It's nice
30:39 to know that it's it's not just me in
30:41 here.
30:44 Okay, so recap.
30:47 I explain this whole system.
30:51 So I have a note. Within the note in the
30:55 object information panel is a custom
30:57 field. We do that because it's much
30:59 easier. Um someone can put in just text.
31:03 They don't need to understand coding. So
31:05 they can put in whatever annotation they
31:07 want. For example, I can come in here
31:12 and I can in this label replacement put
31:17 anything I want.
31:20 And what will happen is that becomes
31:24 an option. And then the way this works
31:27 is the note itself says, hey, if I am
31:30 schedule line number one, then we're
31:32 going to define a global macro that goes
31:36 across all our details that's pointed to
31:38 the floor framing in this case. So it's
31:41 a way we can add additional annotations
31:44 that we're using commonly
31:46 and then on a project by project basis
31:48 set up your project.
31:50 So,
31:53 Enter X17 and
31:56 framing members have defaults and they
31:59 have an object information panel which
32:01 makes them immensely more powerful
32:04 because you can put in conditional
32:06 scripts to say, you know, the next part
32:09 of this is say, hey, if I'm, you know,
32:12 2x8 or I could say, hey, if my material
32:16 states that it's um or if it includ
32:20 includes the word fur, then we're going
32:22 to put the term DF in front of us.
32:26 Now, in this case, I still want to use
32:28 my global species setup here. And you
32:31 can see here, I'm saying that dollar
32:33 sign SBC is my global species sign.
32:36 What's really great about me just
32:38 putting
32:40 an indexed and conditional macro inside
32:44 of my framing member one is that I could
32:47 do this and come in. I can come into
32:49 defaults
32:53 framing framing members and I can select
32:56 everything here edit them and in the
32:59 object information panel just put this
33:02 script and now I am managing this from
33:06 one location
33:08 meaning I don't have to ever go to those
33:10 defaults again now I can edit something
33:12 in my framing index macro but I need to
33:16 put a conditional check for what kind of
33:18 frame remember it is. So then the next
33:21 part of this is I want to say it's
33:25 nominal size SBC.
33:31 Oh, let's see. I think I have to say
33:33 plus SBC
33:40 maybe
33:43 plus and then I need a space before the
33:45 at this case.
33:50 Let me see what that does.
33:52 When I build all framing again, which I
33:54 think if I build all framing from this
33:56 screen, it updates.
34:08 Oh, didn't.
34:12 So, I probably have
34:14 an eval error again because of how I
34:17 formatted that. Let me just fix that.
34:50 Something about the plus sign.
34:58 Isn't that exactly what I wrote?
35:18 See
35:20 what I
35:25 did?
35:32 So, it's going to show me an error
35:33 because I don't have premium member
35:35 selected, which I should.
35:38 Now, I get a proper error.
35:44 Oh, and I don't have an
35:47 firing correctly.
35:50 So, but it needs a space
35:57 unexpected keyword and
36:01 Here we go.
36:08 All right.
36:20 There we go.
36:23 So that means if I do this
36:28 and
36:31 changes all the species to SPF.
36:35 It did not change the framing member
36:37 because the framing member
36:39 probably needs to be rebuilt.
37:08 Delete.
37:13 Oh, delete
37:15 all framing.
37:38 So that's not updating.
37:46 Okay. So, we don't like that method.
37:51 Curious why that's not updating.
38:06 Okay. When I finally get into here.
38:10 Yeah. This is showing correct.
38:19 Interesting.
38:23 A little sec.
38:29 There it is. Oh, I bet I know what I
38:32 needed to do. All right, let's try this.
38:36 Take this dug for a backup here.
38:40 This is something I used to have to do
38:41 before and I'm going to have to figure
38:42 out a fix for this. Um, this still shows
38:45 SPF.
38:47 I don't know if we need to rebuild the
38:49 framing. I don't think we do, but I
38:51 think I do need to open the row object.
38:58 No, that still shows.
39:03 So, it wants me to reorder this.
39:07 That's still not it.
39:10 Did not rebuild. So, let's try
39:12 rebuilding.
39:16 I'll try. Oh,
39:25 I don't know.
39:28 I'll have to sit down and think about
39:30 that one. That's complicated.
39:34 Some combination of opening the right
39:36 things gets us there.
39:44 So far, none of it worked. How did I do
39:47 that just a second ago? All I did was
39:50 reorder this, right?
39:53 That changed.
39:56 It did not change this
40:00 is interesting.
40:10 Wait a minute.
40:15 That's interesting. Now my whole
40:17 system's not working,
40:19 which I found that if I get into the
40:21 weeds with this
40:26 that sometimes I need to shut it all
40:28 down.
40:29 might have caused some kind of loop.
40:43 Oh, well, here's a problem. That's not
40:46 schedule number one.
40:48 Oh, cuz I deleted
40:51 I deleted an object that was in schedule
40:53 number one. All right. So, I need to
40:55 renumber the schedule.
40:59 Yes. And that fixed that issue. Okay.
41:02 And here's the from model,
41:05 but it's still the old species.
41:08 When row object doesn't do it,
41:13 opening a framing member,
41:16 does it? Opening a framing member.
41:21 Okay.
41:25 If all we ever needed to do is opening a
41:27 framing member as opposed to coming back
41:29 and opening these schedules, that would
41:31 be very nice.
41:33 That would be a simple way of
41:36 for an end user a little small
41:38 instruction for them. All right,
41:43 this is working. We're building floor
41:45 framing from the model. Let's test it
41:47 again. So, first floor floor framing
41:52 pick up that this is
41:56 11 and a half and also now we have to
41:59 like
42:03 you know construction eye joist we could
42:05 drive information like that from it I
42:07 think let's just try it real quick let's
42:10 go uh
42:13 instruction is joist
42:17 oh but the
42:19 the type is driven from
42:23 default
42:25 So, let's go 11 and 78 instead.
42:32 See what craziness this does.
42:50 Isn't that cool?
43:00 That's so interesting. Okay.
43:15 This is This is exciting stuff for me.
43:19 If I could get an enduser just,
43:22 you know, 80 details and the ability to
43:25 build out 500 more from those same
43:29 details because they're driven from the
43:30 model. And then on top of that, you're
43:33 building out sections in just a few
43:36 minutes. Now, instead of even 20
43:38 minutes, it's just like two minutes.
43:40 That is pretty compelling.
43:44 Okay. So, let's see what we got in
43:48 our framing defaults now.
43:55 So, this is where we set up that this is
43:57 going to be roll blah blah blah roll is
44:00 automatic type is lumber type is I
44:02 joistic
44:04 in this case
44:08 and build the framing.
44:13 And let's go pick up this is
44:17 so some well actually let me just do my
44:20 search.
44:29 So
44:31 somewhere in here is type object type
44:34 type name I joist.
44:39 So now we're going to do
44:42 a little script
44:44 and I'm going to use my cursor AI for
44:47 this.
44:49 I think I also have any type
44:55 as a pre-done thing that I've got here.
44:57 Floor joist
44:59 is any type
45:02 but we want type name.
45:07 So, Cursor AI, if you're not a member on
45:09 my channel, um, VIP member anyways, you
45:13 might not know about this, but cursor AI
45:15 is what I use nowadays to create really
45:17 complex systems with my Ruby scripting.
45:20 And need to export
45:27 framing index macro.
45:46 cursor should be able to see framing
45:47 index. Yes.
45:51 Get in here.
46:05 I want you to create a new macro
46:09 that is named
46:13 any type name so that it sits along type
46:18 the any type macro that we already have.
46:23 What that's going to do is just going to
46:25 be
46:27 owner context
46:29 and then the NVP
46:35 type underscore name
46:38 as an output.
46:46 For those of you that don't know, NVP
46:48 stands for name value pair Ruby.
46:54 Then in my framing index macro,
47:05 unless
47:07 any type
47:09 equals
47:11 down
47:13 quote unquote framing,
47:16 then we will add
47:23 our macros dot any underscore type name
47:29 to our output
47:35 and see what it does. So the thought
47:37 here is that we're going to reference
47:39 the reason I made a separate macro for
47:41 the any type name portion of this is
47:43 because we'll use it somewhere else.
47:45 We'll use it in some other macro system.
47:47 It's a way of just saying first of all
47:50 any type looks at um chief architect
47:53 calls different objects um a variety of
47:57 different types. They don't you just use
47:58 the type MVP. They they call it object
48:02 type, they call it name type instead of
48:04 just consolidating all that. Who knows
48:07 why? Um probably some internal thing and
48:10 also the code's 30 years old. Probably
48:12 something having to do with that. So
48:14 it's just it's not we're not just
48:15 inheriting from a type property, which I
48:18 wish we were because now we're getting
48:20 into SQL database type stuff.
48:24 So I'm I use any type in many different
48:27 macros to just report a type of an
48:29 object.
48:31 You know, basically consolidating all
48:33 those various NVPs that are called type
48:36 so that it just reports, you know, one
48:38 thing from it. and then referencing that
48:42 type I can do conditional statements.
48:44 Hey, if any type reports that this is a
48:46 framing member then we want to do this
48:49 for example. So in this case we're
48:51 saying hey unless type name is lumber
48:54 well rather if type name's lumber do
48:57 nothing but if it's not lumber then
49:00 let's report what that is. In this case,
49:02 what we're doing is if it's not lumber,
49:04 then it's assumed to be some other
49:06 member like an eyejist. And we actually
49:08 want to see that. So that in our case of
49:11 our nominal size inch and 1/2 by 11 and
49:14 78, it should then say eyejoice.
49:18 And then also we're going to have to put
49:20 some conditional check in there to say,
49:22 hey,
49:23 if any type name is lumber, then we want
49:28 to include that species global, the
49:32 dollar sign SBC that I put in there
49:34 earlier.
49:38 And meanwhile,
49:41 chat's really slow because I'm on a slow
49:43 requesting because I burned all my
49:46 credits for this service. So, I'm just
49:49 in here filling air.
49:54 I imagine people that are on this one
49:56 just has this honest background noise.
49:58 Um, so it makes me want to go play
50:01 something from Dumb and Dumber where he
50:03 just screams in the car. The most
50:05 annoying noise in the world.
50:22 Meanwhile, while that's taking its sweet
50:25 time,
50:27 get in
51:03 Main problem with the system right now
51:04 is this guy right here. There's no way
51:06 for us to determine this. I don't think
51:10 this 16 on center. I don't think there's
51:12 any MVPs across the entire model that
51:18 state that specific detail what the
51:22 spacing is of your framing of a room.
51:26 Oh, maybe of a room.
51:30 Sometimes you just got to talk out loud
51:31 to get some ideas.
51:34 So,
51:38 yeah.
51:49 Smolding ceiling. Finish layers.
52:06 floor platform layers. Let's take a
52:08 close look at this
52:11 lumber first package. That's our
52:14 subfloor.
52:17 Here's our framing.
52:24 area.
52:28 Yeah. No mention of spacing.
52:33 Why wouldn't have that been
52:36 good idea?
52:55 Yeah, there's nothing that I know of
52:58 that will tell you
53:01 spacing. surprised
53:04 no one's ever requested that or not that
53:07 I know of anyway.
53:12 All right. What do we get here?
53:17 All right. Well, I wanted it to create a
53:18 brand new standalone macro, but it
53:21 packaged it together with my framing
53:22 index, which that's okay.
53:28 Or no, it just updated the framing
53:29 index. Okay, that part's good. Where do
53:33 we see
53:37 any type name? I don't see that.
53:45 What did it do?
53:52 Oh, yeah. It packaged it together. And
53:54 then the value is type name. Okay. Okay.
53:58 See what this got here. I just get to
54:00 import this. This is what's really cool
54:02 about cursor AI. I don't I don't need to
54:05 um
54:07 create things per se. I just get to come
54:09 in here and import this new JSON file
54:13 which is framing index
54:16 place the existing.
54:18 So that brought in any type name
54:22 unspecified because what are we doing?
54:24 We're not selecting it. We're selecting
54:25 a room. Let's just check check this out.
54:29 Okay. Any type name is ijist. Perfect.
54:32 And then framing index
54:36 did not work. So what did we do?
54:40 If macros any type down case no any type
54:43 name down case it.
54:51 Now what do we get? Anything? No.
54:56 Aim down case not equals includes
55:01 includes
55:06 include.
55:12 Ha. So we got the eye joist in there. Uh
55:16 it's just the wrong order.
55:19 Then we're going to do this.
55:25 We need species gone.
55:40 What?
55:52 going to do here.
56:09 There we go. Look at this output. And
56:12 half 11 78 I joint at 16 on center.
56:20 Okay, we got the start of something.
56:29 Sure
56:36 by exporting this to framing index. Yes.
56:40 And exporting
56:42 any type name and any
57:01 spelling spelling. You can do this.
57:12 So exporting this puts this back into
57:15 the programming for this right here.
57:18 We're just going to hit accept. There we
57:22 go. In fact, word wrapping so we
57:24 understand that. And then we do have any
57:27 type and any type name in here as well.
57:33 Very cool.
57:35 It's the start of something good. So
57:37 let's go test this.
57:42 So framing members,
57:52 change this to an LVL.
57:55 There anything else that includes just
57:58 lumber? No. So that
58:01 method is solid. Anything else will show
58:05 these reported amounts. First, we're
58:08 going to have to put something in here
58:09 that if it says solid concrete, that's
58:10 not going to be right.
58:14 And then we also have to distinguish
58:16 first floor from second floor. So, we're
58:17 going to have to put a conditional
58:18 statement in there.
58:27 So, all right, switch it to LVL.
58:32 Build all framing again.
58:38 Let's open a framing member.
58:40 And that did update Lvl.
58:44 Cool. This is cool.
58:49 Okay. Next,
59:00 I updated and created separate JSON
59:04 files for the any type and any type name
59:06 as well as the framing index. So, you
59:09 can see that those are separate. Now,
59:11 you're going to have to edit those
59:12 individually. Now, for the framing
59:14 index, we want to check what the floor
59:16 number is.
59:20 And
59:22 in this case, we only want to define
59:35 floor framing from model.
59:39 If the floor number is equal to zero
59:51 and then also add in a condition that
59:57 if the any type name
1:00:00 includes concrete
1:00:02 then we want to define
1:00:06 floor framing name
1:00:08 as
1:00:11 grade beam
1:00:13 which is a text string.
1:00:19 This is where we really get to see a
1:00:20 system sing where we get to just kind of
1:00:22 add these cool things and test it out
1:00:25 and not do any work. Just work the work
1:00:29 is kind of up here.
1:00:32 I'm like feel like I'm just a director
1:00:34 producer I suppose.
1:00:38 I wish I could script because then this
1:00:40 would just be like no problem. And then
1:00:44 the the biggest problem is once you get
1:00:46 a complex enough script, it would be
1:00:50 prudent of you to go back and say, "Hey,
1:00:52 could we improve this?" Because we're
1:00:53 just stacking features right now. We're
1:00:55 not necessarily building a great system.
1:01:03 Meantime, while that's doing its thing,
1:01:04 I'm just going to cross reference
1:01:07 our output
1:01:09 with chat GBT. See?
1:01:48 Now what's different about um
1:01:53 cursor from chat GPT is cursor
1:01:56 contextually can see
1:01:58 um other variables whereas chat GPT I
1:02:02 need to give it those variables because
1:02:04 I'm about to paste from cursor to chat
1:02:07 GPT to see if this does a better job or
1:02:09 or what or what approach it takes. Um
1:02:12 but it doesn't know for instance
1:02:18 any type name and it doesn't know
1:02:22 l number
1:02:27 MVPs.
1:02:42 See what it does.
1:02:48 It's asking me to classify it. Any type
1:02:50 name and floor number might be an
1:02:53 integer. It's a great question actually.
1:03:09 It is an integer. Good job.
1:03:17 Oh, and look, it's even built to put my
1:03:19 little copyright in front of it.
1:03:24 Okay, this a shot.
1:03:44 What did it do?
1:03:55 problem here.
1:03:58 Find
1:04:15 Oh, oops. Macro stop.
1:04:18 We're referencing a different
1:04:25 Um so I can just define this in the
1:04:27 beginning. I can say any type name
1:04:32 equals macro.
1:04:40 There we go.
1:04:48 All right. So that handles that LVL
1:04:50 condition.
1:04:53 Now let's go and make it solid concrete
1:04:55 and see what happens.
1:05:22 That's so cool.
1:05:25 Oh, I love it when things go right. I'm
1:05:26 not, you know, sometimes I'll be at this
1:05:29 for hours trying to figure out a
1:05:31 problem. I think maybe I maybe I should
1:05:33 pat myself on the back. I'm getting a
1:05:34 little better.
1:05:37 H so many hours wasted trying to figure
1:05:40 out stuff sometimes.
1:05:42 Um, and so I should just open the
1:05:44 framing member, close it down, and that
1:05:46 changes to a gray beam. That's so cool.
1:05:56 So, like if you were to set up your
1:05:58 automatic framing for this floor look
1:06:01 like grade beams, I don't actually know
1:06:03 that that's what you would ever do or
1:06:06 why or how that even works,
1:06:09 but
1:06:12 let's just argument sake call this 24 in
1:06:18 joist construction. So that's being
1:06:20 built from automatically.
1:06:24 Where are we setting spacing up? I guess
1:06:26 we're not.
1:06:28 We're not here. It's interesting that
1:06:30 they don't let you set up spacing there.
1:06:33 So what you get into build framing
1:06:35 dialogue?
1:06:37 No. Right. Framing defaults.
1:06:41 So spacing is here. Just say this is
1:06:44 like 8 foot on center.
1:06:48 Sure.
1:06:57 No, I suppose I could have just turned
1:06:59 on automatic rebuilding for floor.
1:07:05 That is not the width, huh?
1:07:15 The rim joist with spacing
1:07:21 or structure is 16
1:07:38 doesn't show width here. Oh, here it is.
1:07:42 It's a 12 inch.
1:07:44 Okay. insulation.
1:07:50 There's my grade beams.
1:07:56 Well, that's pretty cool.
1:08:00 Now, I have to make this
1:08:04 intensely more complex if I want the
1:08:06 rest of the system to drive the same
1:08:09 way.
1:08:18 I feel very successful. Does anyone want
1:08:20 me to do a little sidebar and show how
1:08:21 we can do something else in Chief
1:08:23 Architect? You got a problem you want me
1:08:24 to handle? Maybe we'll just do a little
1:08:27 little side quest.
1:08:30 Feel like there was something in the
1:08:31 Facebook groups. Let's go take a look.
1:08:36 Since I thought I was going to be at
1:08:37 this for two hours just to get that
1:08:38 concept in motion.
1:08:47 I love this group. It's a really active
1:08:50 group. It's fun. It's like a coming in
1:08:52 and just getting a little news feed.
1:08:54 Users of Chief Architect group. How to
1:08:57 do this roof gutter in Chief Architect.
1:09:00 Well, you're going to have to draw that
1:09:01 molding profile, my friend.
1:09:06 Simple. Look at that ugly face.
1:09:10 Uh,
1:09:12 still have to get rid of Evanbot doing
1:09:15 things that are outside of the scope of
1:09:17 our group.
1:09:19 Evans, if you're seeing this, your bot
1:09:22 is acting up in my Facebook group.
1:09:33 Hill question. Skirtboard question.
1:09:38 Maybe this is not where I was trying to
1:09:40 find this.
1:09:47 Anyone using that Max M4? That was a
1:09:49 question here.
1:09:52 Thing's pretty impressive.
1:09:57 Oh, here's one. Completed a kitchen
1:09:59 design and I like to crown molding to
1:10:01 it. Is there way to do it in default
1:10:02 settings? I was actually quite surprised
1:10:05 at the comments. To me, the the methods
1:10:08 mentioned in the comments were not the
1:10:10 fastest methods.
1:10:12 Um,
1:10:18 you can marquee select similar, but
1:10:19 that's only going to get you wall
1:10:20 cabinets. It's not going to get you full
1:10:22 height cabinets, which, you know, would
1:10:24 be simple enough. And then
1:10:34 I'd probably just do a restrictive
1:10:37 selection. Let's open something up. So,
1:10:39 let's get in my Let's do it.
1:10:43 Well, actually, I don't care if I screw
1:10:45 this plan up. Think
1:10:50 plan. Let's go up a level. Drop in some
1:10:54 cabinets.
1:11:00 Let's call this kitchen
1:11:03 or let's just
1:11:23 Oh, I don't know what I'm doing. Let's
1:11:24 do this in 3D view. This is my new
1:11:26 favorite thing. Man, did they make this
1:11:29 a lot more intuitive.
1:11:32 I don't want the floor overview camera.
1:11:35 I want something the floor camera.
1:11:41 Wait a minute. I thought floor camera
1:11:44 ceilings turned off. Let me try that
1:11:46 again.
1:11:48 What other cameras we have?
1:11:51 Overview.
1:11:55 for review, but I'm going to switch my
1:12:05 dimensions 3D
1:12:08 overview.
1:12:13 the text size that I switched on
1:12:17 made it so that it's really easy to see
1:12:20 dimensions in this view, but make sure
1:12:23 I'm using the correct dimension default.
1:12:25 Oh, 3D favorite. There it is.
1:12:29 Just got to switch this to
1:12:32 3D favorite. 3D workflow. There we go.
1:12:35 Cool. Had to remember that. All right.
1:12:38 So yeah, this is a dream come true.
1:12:42 Working in this in 3D is so much faster
1:12:45 than it used to be.
1:12:50 Still got to get used to placing things
1:12:52 accurately.
1:12:54 Yeah, that placed accurately.
1:12:58 Yeah, just get to drag this and then
1:13:01 click that zero. Yeah, this is so sweet.
1:13:06 H love it. Still can do tap enter if you
1:13:09 want to.
1:13:13 It's just so cool.
1:13:18 Yeah. Amazing.
1:13:35 This makes life easy. That's really,
1:13:37 really neat. I love it.
1:13:58 Cycle through tools, but wasn't getting
1:14:01 it.
1:14:07 And what?
1:14:10 Not not that they needed stack next to a
1:14:12 range, but sure. Oh, actually, let's do
1:14:16 this instead.
1:14:18 Two drawer base. Two drawer base.
1:14:22 Ice
1:14:24 garbage.
1:14:26 Three drawer.
1:14:29 And
1:14:32 why not? Let's make this a little drawer
1:14:33 pack.
1:14:35 We're going to put a sink in.
1:14:47 Shift. Move this over. Let the go.
1:14:49 Shift.
1:14:56 I do a video on just tips for doing this
1:14:58 in 3D so that
1:15:02 people kind of learn what buttons I'm
1:15:05 interesting. Why is that referencing
1:15:07 there?
1:15:09 See, I don't need to do that anymore.
1:15:11 Just use the temp dimensions, which I
1:15:13 should have done.
1:15:17 Yeah, it's still difficult to place a
1:15:18 little filler in 3D, which is dumb.
1:15:22 But I think I should be able to just
1:15:24 click this back side. Yeah. And say
1:15:26 zero.
1:15:28 Yeah, that's so much better.
1:15:36 Let's flush the toe out.
1:15:42 Yeah, liking it. I'm liking it.
1:15:49 So, still difficult to do that. Should
1:15:51 be able to select next side.
1:15:55 Yeah,
1:15:58 I wish they had an angle rotation in
1:16:00 temp dimensions there, but should still
1:16:03 be able to do
1:16:05 select next side. Next side, next side.
1:16:11 Interesting that 10 dimensions don't
1:16:13 show up here. Oh jeez,
1:16:20 they did what for a second there. I got
1:16:22 to figure this out. Is it just selecting
1:16:28 the top the top line? All right.
1:16:33 Good. That's in my memory banks now.
1:16:43 That's an end panel, but it doesn't have
1:16:49 I do the wrong face side of this.
1:16:53 Looks like it.
1:17:01 Yeah, I'm on the wrong face of this.
1:17:04 There we go.
1:17:07 All right. Come up with some easier
1:17:09 methods for that. That's got to get
1:17:11 better than that.
1:17:25 Okay.
1:17:47 You click inside it. So you can't you
1:17:49 can yeah you can fill this but you can't
1:17:52 get it to resize
1:17:55 would be nice.
1:18:15 Automatic blind corners turned on.
1:18:18 Doesn't look like it.
1:18:20 Nope.
1:18:22 Do not
1:18:26 fores.
1:18:39 Anyways,
1:18:59 okay. So, here is the thought. We've got
1:19:03 a kitchen.
1:19:11 Actually, let's make it a pretty
1:19:12 kitchen. Since we're here showcasing
1:19:17 kitchen style palette, let's just throw
1:19:19 a little backsplash in here.
1:19:27 Oh, that's weird. Backsplash cut to
1:19:30 That's really weird. Never seen that
1:19:32 before.
1:19:34 Error
1:19:36 ignore
1:19:51 export my macro in case that error comes
1:19:53 back and crashes me and then I don't get
1:19:55 this back
1:19:57 index.
1:20:00 There we go.
1:20:08 side tune. Oh, another error.
1:20:12 Oh,
1:20:13 don't break me.
1:20:18 Uh, let's see what else do we have here.
1:20:20 Ashford Kitchen.
1:20:28 Yeah, we'll take that.
1:20:31 And this is something common I'll do.
1:20:34 Base cabinets convert to custom
1:20:37 countertop. That'll be nice. Even though
1:20:40 it's got some weird brakes.
1:20:45 We'll get to pull this out.
1:20:47 Inches or 18 in. New KBA standards are
1:20:51 18 in recommended.
1:20:54 Honey
1:20:56 big old numbers. Let's throw some little
1:20:59 pendant lights in here.
1:21:03 Not throw my brand new LED
1:21:07 recessed can in here for some realism.
1:21:12 And these are cool that you get to do
1:21:14 spacing and everything in 3D. Now you've
1:21:17 got your dimensions set up correctly.
1:21:29 A little fishing.
1:21:43 [Music]
1:21:48 Good.
1:21:50 Bam. Cool.
1:21:55 And then what? Little sliding door right
1:21:58 here. Why not? That's a pocket door.
1:22:21 A pretty little kitchen.
1:22:38 Okay, so we've got no molding.
1:22:41 We're finally to the question that we're
1:22:43 supposed to be answering. We got no
1:22:45 molding and how do you add a molding to
1:22:47 everything. There's so many ways. Um,
1:22:52 but probably one of the easier ways to
1:22:54 do this is you just get to a plan view.
1:22:57 So, here's one way. Get to a plan view.
1:23:01 Choose the full height cabinet tool.
1:23:04 Shift select your full height cabinets.
1:23:07 Shift very carefully contain selection
1:23:09 your wall cabinets like so. Okay, now
1:23:14 you got all those cabinets. You get to
1:23:16 open them up and we get to add a molding
1:23:18 to it.
1:23:21 CML3.
1:23:27 There we go. And then do a little
1:23:29 vertical offset.
1:23:32 You do auto offset. Pick that up
1:23:35 automatically for you.
1:23:37 Maybe you want to put in a flat stock
1:23:39 here as well and account for the face
1:23:41 item. But there we go. Just added a
1:23:44 molding to the plan that easily. Bam. So
1:23:49 that's a really fast way.
1:23:53 Wait, what would be another way? You
1:23:56 could build a style palette, but that
1:23:57 takes time to build it the first time.
1:23:59 But you could do a style palette that
1:24:01 just says
1:24:04 the only one thing that it's just
1:24:06 copying moldings. So, and then you could
1:24:09 apply it to um all the wall cabinets and
1:24:12 then all the full high cabinets.
1:24:14 Honestly, I think what I just showed is
1:24:16 the fastest way.
1:24:18 Just go back a little.
1:24:23 The other thing that might be nice is
1:24:25 that you before you did this, you picked
1:24:28 up that this is um cabinet white.
1:24:33 It's the definition here. And if you
1:24:35 went into
1:24:37 your default materials
1:24:41 or what
1:24:43 trim
1:24:46 I would think it should pick up.
1:24:49 What is What is crown molding set to?
1:24:52 Let's see. Let's see. CMO one or 03.
1:25:01 CMO3. If we
1:25:07 copy it to the user catalog just so we
1:25:09 can see what it's doing.
1:25:13 Its materials are
1:25:16 default room moldings. Interesting.
1:25:22 So, it'd be cool if you
1:25:25 took the time to set up your crown
1:25:28 moldings that you're going to use in a
1:25:30 kitchen, which is just giving me more
1:25:32 ideas from my own library. And that way,
1:25:35 it defaults to the cabinet material when
1:25:37 you apply it. That would be a very nice
1:25:39 setup. So, here's what you would do. You
1:25:42 would say this is kitchen
1:25:45 kitchen
1:25:47 round molding. Maybe we'll put KC CMO3.
1:25:53 Okay. KCMO3.
1:25:55 Open the object.
1:25:58 Select the material. Go to
1:26:02 uh material defaults.
1:26:05 Cabinet.
1:26:08 Yeah. Cabinet.
1:26:11 And now
1:26:13 what we would do is
1:26:16 go full hide cabinet selection, shift
1:26:20 restrictive, select all your wall
1:26:22 cabinets, open them up,
1:26:27 add new ACM3,
1:26:32 press okay.
1:26:34 Um, auto offset. And there's still a
1:26:37 wrong material.
1:26:41 probably because this material is not
1:26:43 truly the
1:26:45 correct one.
1:26:52 But if we changed
1:26:54 for our base material for cabinets
1:26:58 to that other cabinet white grade,
1:27:01 that's the dark one. Cabinet white. This
1:27:03 one. There we go.
1:27:05 Now they should all match.
1:27:10 And voila.
1:27:13 Cool.
1:27:23 Oh, hey Doug.
1:27:27 Doug is in the house. Hey, Doug.
1:27:30 Doug, you want me to show you anything?
1:27:31 Because I'm going to end the stream here
1:27:32 pretty soon. Um because I did what I
1:27:36 came here to do and now I just have a
1:27:38 bunch of busy work that I'm going to be
1:27:39 doing.
1:27:43 Thought I'd throw in a little sidebar.
1:27:46 The other thing someone wants me to do
1:27:48 that I'm interested in maybe checking
1:27:50 out is they want me to build I have my
1:27:53 closet tools and I have my shelf tools.
1:27:55 They want me to build a tool that will
1:27:56 work for creating walk-in pantry item,
1:28:01 you know, shelf stuff.
1:28:04 But I need some ideas for that before I
1:28:06 start messing around with it.
1:28:18 Oh, here's something new that's in my
1:28:20 template that I love. And we'll try this
1:28:22 out.
1:28:25 Rope light. Made my own
1:28:28 special custom
1:28:33 See how it performs
1:28:46 in. Let's throw a little switch in here
1:28:49 where we can manage it.
1:29:09 Okay.
1:29:15 do the same thing. Let's throw another
1:29:17 switch in here.
1:29:41 So, we should be able to turn all these
1:29:43 off.
1:29:46 I just have my under counter lights
1:29:48 going. They are
1:29:52 angled diffused light.
1:30:00 Now, the sun
1:30:06 set these to like 20%.
1:30:20 the oven off.
1:30:25 Yeah. Doesn't that look nice?
1:30:27 Pretty good.
1:30:32 And down.
1:30:36 Suppose you don't need to turn both down
1:30:38 to a certain amount. But look at that. I
1:30:40 mean, that looks like a night shot.
1:30:56 Pretty dang cool.
1:31:02 Mhm.
1:31:32 See,
1:31:44 if you start putting in what's inside of
1:31:46 the cabinets
1:31:54 up in here, what is this little guy?
1:31:57 Oh, I managed to put a crown molding on
1:31:58 my
1:32:01 put a crown molding on my pillar over
1:32:03 here.
1:32:05 Do have a tool that is just a style
1:32:08 pallet tool to delete molding from
1:32:11 something.
1:32:15 It's funny.
1:32:18 All right.
1:32:20 Well, then I'm going to go get back to
1:32:22 work. Thank you for joining me, those of
1:32:25 you that did. I think um you know you're
1:32:28 obviously going to see an update at some
1:32:30 point where I showcase that full system,
1:32:32 but man am I excited about that. Let me
1:32:35 just get back to this and double check
1:32:36 again. Get our floor framing double
1:32:39 checked. Framing floor plan. There's our
1:32:41 great beams.
1:32:45 Let's fix this. Put this back to normal.
1:32:52 So
1:32:56 go back to that 11 78
1:33:04 and
1:33:07 auto build framing menu.
1:33:12 A B. Yeah.
1:33:16 B.
1:33:17 No.
1:33:20 Ring.
1:33:30 or structure. Oh, so you could define it
1:33:32 here, too. That's kind of clever.
1:33:35 I didn't realize that, I guess.
1:33:38 Framing, choice, choice, trust details,
1:33:40 insulation inch and half.
1:33:44 Keep forgetting where the spacing is.
1:33:46 There it is.
1:33:50 There we go.
1:33:52 And open one of these.
1:33:56 And then, oh,
1:34:00 guess we could cancel maybe. We'll see
1:34:03 if cancel works. And then if I open up
1:34:06 the project browser,
1:34:08 see what if details were changed at all.
1:34:18 What do you say?
1:34:26 See if something is called out for
1:34:28 framing. Where would be?
1:34:33 I don't think I even show
1:34:36 I don't even show a detail that's uh
1:34:39 falling out floor frame. That's funny.
1:34:44 Yeah, this isn't even pulling up.
1:34:49 Okay, trade this up
1:34:59 foundations.
1:35:07 Yeah, there's a stem wall
1:35:10 detail, but that's a
1:35:13 framing over rafters entes. No walls
1:35:17 framing between floors.
1:35:20 Oh, I don't have a typical stem wall
1:35:21 detail. That's funny. In my stackables,
1:35:26 that seems like a big oversight.
1:35:36 I suppose we could build one.
1:35:51 That's very interesting.
1:35:56 I think that this should have plugged
1:35:59 in.
1:36:12 New error. Dang it. All right, let's
1:36:15 bring this down here. Don't think this
1:36:17 auto picks up
1:36:20 floor framing. does not
1:36:25 an inside joke to myself
1:36:30 never without humor. Okay.
1:36:40 Yeah, there it is.
1:36:43 Very cool.
1:36:48 Very cool.
1:37:00 We go back to the model
1:37:03 build framing and enter
1:37:07 auto.
1:37:09 And
1:37:12 this is what would be great if we could
1:37:14 set this to be
1:37:16 macros are not accepted in
1:37:19 numerical inputs.
1:37:22 For example,
1:37:29 pretty sure this doesn't work.
1:37:41 Pretty sure
1:37:56 Even if you were just to say
1:38:11 sure that
1:38:14 Yeah. So there's no way to send this
1:38:18 value. That's so that's so unfortunate.
1:38:25 All right, but let's change this.
1:38:28 So, we're back to
1:38:32 framing joist joist define joist edit.
1:38:36 This is Oh, this is still set to solid
1:38:38 concrete, which is incorrect.
1:38:41 That should have shown solid concrete.
1:38:45 Back
1:38:55 to eye joist
1:39:04 structure for floor one builds it.
1:39:14 We're still showing grade beam because
1:39:16 we need to open this.
1:39:24 I would never have automatic framing on
1:39:26 anyways. So that's okay.
1:39:30 And then that didly update that
1:39:34 neck did correctly update this.
1:39:38 Oh, this is going to be so nice for an
1:39:41 intermediate end user that they don't
1:39:44 have to go into that dialogue. All I
1:39:46 have to do is open a framing member.
1:39:49 I wonder if I could get it to do that
1:39:52 some other way.
1:39:59 I think not. I'll go talk to the macro
1:40:02 gods and see what's happening.
1:40:04 Um, very cool everybody. Thank you for
1:40:08 joining me. If you're watching this as a
1:40:10 recording,
1:40:12 um, you're not missing anything in the
1:40:13 chat window because no one's talking.
1:40:17 Leave me some feedback if you're
1:40:19 wondering, you know, what the heck is
1:40:21 all this? If you're new to the channel,
1:40:24 if you're trying to figure out what I'm
1:40:25 even doing. Basically,
1:40:28 I build templates. Um
1:40:31 and and then you know of course I go use
1:40:34 them myself but they end up producing
1:40:36 things like this which is kind of
1:40:39 automatic templates where we're saving a
1:40:42 lot of time because we're automating
1:40:45 process as we go. So you can see here I
1:40:49 didn't send these views. They're already
1:40:50 present to view. So I just get to expand
1:40:53 some little window a little bit.
1:40:58 So, and center this up
1:41:05 and just do little minor incremental
1:41:08 things to get full condoc.
1:41:13 So, that's really fun. I think I added a
1:41:16 new tool in here, a new arrow. Yeah, I
1:41:18 did. Look at this. This is my default
1:41:21 arrow in layout.
1:41:24 Look at that. Creates a a match line.
1:41:27 Isn't that fun?
1:41:31 Do it over here too.
1:41:33 Bam.
1:41:35 Fast. That's so cool. You just change
1:41:39 the size of the arrow. You need that
1:41:41 match line to be a different size.
1:41:46 Order overview. There's plan.
1:41:50 Yeah, looking cool.
1:41:52 All right, I'm out of here. Thank you
1:41:54 very much for watching. Appreciate you.
1:42:09 [Music]
