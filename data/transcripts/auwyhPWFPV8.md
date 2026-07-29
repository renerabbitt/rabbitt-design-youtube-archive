---
videoId: auwyhPWFPV8
title: Macro Emojis and Reading Client Info From CSV in Chief Architect
url: "https://www.youtube.com/watch?v=auwyhPWFPV8"
status: imported
---

# Transcript

0:01 a VIP. Where's my macro people at?
0:04 Because that's what we're going over
0:05 today. Um, and I'm going to review
0:07 something that I just built into the pro
0:09 plan as opposed to watching me struggle
0:13 in the process. I know some of you love
0:14 to watch me struggle through macros. Um,
0:17 this time around, I didn't struggle too
0:19 bad. It was actually pretty streamlined.
0:20 Uh, but I just forgot to record it. So,
0:23 let me get in and show you what we're
0:25 doing. Uh what I've done is I've set it
0:27 up so that out of the box when you open
0:30 up my new versions that are going to be
0:32 for X17, which you can um order right
0:34 now actually. They're they're out there.
0:36 Um is that the pro plan will now take
0:40 information, your client and designer
0:44 information from a CSV file, which would
0:48 be you could open that up with a text
0:49 editor or you could open that up with um
0:52 Excel or like Google Sheets or something
0:54 like that. can all do CSV files. I even
0:56 think a PDF editor might be able to open
0:58 them up as
0:59 well. What is nice about that? What's
1:02 nice about that is that you might have
1:05 someone in your office that needs to
1:07 plug in information and they don't have
1:08 access to Chief Architect and so they're
1:10 going to plug in your client information
1:12 anyways. So, we might as well give you a
1:15 way to do that so that they could plug
1:18 it in and you open up your project file
1:19 and bam, all that information is
1:21 populated. You didn't have to do that.
1:22 So, that's a really nice way of of doing
1:24 it. One, two, is that the the old method
1:27 was coming into tools and designer
1:29 client information. And maybe that's
1:31 efficient, but maybe not. Maybe that's a
1:33 really slow method, especially if you're
1:35 someone that's switching the designer
1:37 constantly or switching the client
1:39 constantly, but it's a static client,
1:40 like one that you use over and over
1:42 again. So, this would be a method where
1:44 we could easily just copy our CSV file
1:47 over from that same project where that
1:50 information is already plugged into the
1:52 CSV. So, I'm going to show you how this
1:54 works. It's um it's kind of cool. I've
1:56 done a lot of cool new things to my pro
1:58 plan and I'll show you a few of those
2:00 things in this because I don't really
2:02 have a goal in this video other than to
2:04 show you what I've been doing with
2:06 macros. Let's just give you a macro
2:08 update. So, here's what I've got is I've
2:11 got this project information call out
2:13 and it's a link to a CAD detail. We
2:15 double click it, it brings us to this
2:17 page. Now, I'm going to still work on
2:19 making this page look a little cleaner
2:21 and have fewer notes on them because
2:24 we're trying to drive notes towards a
2:27 manual that's being built for the pro
2:28 plan. But, in the meantime, here's what
2:31 this page looks like. Now, this is being
2:34 sent to to layout as a view. Okay. So
2:37 that's this is the lot analysis. That's
2:40 a different aspect. I you know probably
2:42 show that in some other videos where I'm
2:44 doing automatic lot analysis as soon as
2:46 you start drawing. But the project
2:48 information it was always being derived
2:51 from um just going into tools designer
2:54 client information and you can see here
2:56 I've got some stuff filled out already.
2:58 Right? So I've set stored my designer
3:01 information in this case and you can see
3:03 it's reporting here. All right. The next
3:06 thing is if I just go and save this
3:07 project and let's just save it as test.
3:10 Now we're going to see something over
3:11 here that just happened. This is telling
3:14 us that if hey we do in fact want to um
3:18 derive our designer and client
3:19 information from the CSV file then you
3:22 need to have that file in this location.
3:26 Now what happened when I suddenly saved
3:29 this was that it happens to be that I
3:30 have that designer CSV file and that
3:33 client info CSV file in the same
3:35 location that I just saved test. So that
3:39 if I need to only do one thing here is
3:42 open and close this detail. Here we go.
3:45 This is information derived from the CSV
3:48 as opposed to my client information
3:50 that's in Chief Architect. Now, if that
3:53 CSV doesn't exist or the values in that
3:56 CSV or nil are blank, then my macro,
4:00 what it's doing is then it's falling
4:02 back to the client information. And then
4:05 if the client information is blank, it's
4:06 just going to remain blank and you could
4:08 fill it in. What's really cool about
4:11 this is you can do a mix and match. You
4:13 don't actually need to have all your
4:15 information in the CSV file. Now, let's
4:17 just take a look at what the CSV file
4:19 even is. Let me see if I can't locate it
4:22 real quick. I'm going to get this on my
4:24 second screen. Here's my client info CSV
4:27 file. And so, because it's a CSV file,
4:31 we can't retain any special formatting.
4:33 So, I can't put bold headers on here. I
4:36 can't put a fill style in here,
4:38 unfortunately. That's all native to like
4:39 an Excel sheet versus a CSV. It's just
4:42 going to be plain text. So, it's not
4:44 even going to be formatted column widths
4:46 or anything like that. You could come in
4:47 here and and do that yourself. But here
4:49 you go. It's a simple input. You input
4:52 name, you input address, city, etc. You
4:55 get to put in your parcel number, scope
4:57 of work, and all this will populate in
5:00 Chief Architect. So, how does this all
5:02 work? Well, let me get into macro
5:04 management here. And I just have two
5:07 little macros. One I call CSV lookup
5:09 client, the other CSV lookup designer. I
5:13 want to point out that when you're
5:14 building systems, boy, a lot of this uh
5:18 times this stuff does not come naturally
5:20 where you're trying to come up with a
5:23 system that's going to stand the test of
5:24 time and that means considering
5:27 everything including your macro naming
5:30 conventions. It just so happened to be
5:32 that I have another CSV lookup system
5:36 within this setup that starts with CSV
5:39 as a prefix. So, I needed to make sure
5:41 that I wanted to gather all my CSV
5:44 lookup stuff into one location. Now, CSV
5:47 lookup is in the case that maybe we're
5:49 looking up information that we're
5:50 getting from a builder trend. So, that's
5:52 now built into my prop plane, even
5:54 though you would need a little bit of
5:55 info on how to use it. But the CSV
5:58 lookup client is very simple. It's
6:00 looking for, let's just go to edit this
6:02 so we can really see it. It's looking
6:04 for file read path. And what it's doing
6:07 is it's looking at a directory. Now this
6:09 directory the global sign directory in
6:11 this case is defined as the the short
6:16 URL of where our plan file exists. So
6:20 when we saved our plan file it defined
6:23 directory so that then it's looking in
6:26 that same directory for this specific
6:30 CSV name. Now, I could do a little bit
6:32 more of a dynamic thing here where I
6:35 could look for anything that might
6:37 include the name client info.csv, but
6:40 that gets a little bit more complex. And
6:42 I thought, you know what, bare minimum,
6:45 I figure people could just not rename
6:47 the CSV file. That'd be great. But in
6:50 the case that you really want to make
6:52 this foolproof, maybe that's something
6:54 that you script in is that you're
6:56 looking for anything that says client
6:57 info in that path or even a
7:00 subdirectory. if you could get that
7:02 specific. There are some security issues
7:05 within the execution of Ruby that's in
7:08 Chief Architect. And this is some kind
7:10 of info that I think I'm the only one
7:13 that really has this aside from a few
7:14 other people that write a lot of Ruby
7:16 scripting for Chief Architect, which is
7:18 that this is not something you're going
7:19 to find in the manual. You're going to
7:21 find it in videos like this. So, what
7:24 I'm telling you is this is when we're
7:26 writing up some kind of um script that
7:29 wants to parse info from a file, Chief
7:32 Architect has a bunch of security
7:34 measures where you can't do a bunch of
7:37 variable lookups because that ends up
7:40 being some kind of security parameter
7:43 which is saying, hey, we need something
7:46 to be a static lookup otherwise there's
7:49 a potential for screwing some things up
7:51 that you know in terms of Ruby that
7:54 becomes a security issue. That's why I
7:56 needed a I have a variable for directory
8:00 but I have a static lookup for that CSV
8:02 file because otherwise you might run
8:04 into some security issue errors within
8:06 the Ruby environment. So the first thing
8:08 then that I'm doing is hey if the file
8:12 is missing I want to clear these global
8:14 values because what we know about global
8:16 values with macros if you are somewhat
8:19 of an intermediate advanced user is that
8:22 globals work across all um all open
8:27 files within Chief Architect. It's not
8:30 just the file that you're working on
8:31 here. And so that's a huge um aspect of
8:36 this is that this system even though
8:39 it's pulling client information from
8:41 this CSV, it will define your client and
8:44 designer information even if you are
8:47 printing a file number two, but you're
8:50 working on file number one. So keep that
8:52 in mind. That's the kind of the caveat
8:55 of the system. Now, what I would say is
8:57 if whenever you're going to go print,
8:59 especially one of with one of my
9:00 systems, you close down everything else
9:02 but the thing that you're going to
9:04 print. That way, you know that your
9:06 globals are firing based on that file.
9:08 Do you one step better when you shut
9:11 CHEF down, it clears all global values.
9:14 So, if you were going to go print and
9:16 you've been working on multiple files,
9:18 it's just a good practice to shut down,
9:20 open it back up, open the file you want
9:22 to print, go print. It's going to work
9:24 better that way.
9:26 The other thing about globals and just
9:28 macros in general within Chief Architect
9:31 is a lot of times we might be driving um
9:34 one of these systems based on an object
9:36 in plan and that object might need to be
9:39 open or wherever that path is being
9:42 executed, it might need to be on the
9:45 screen and displayed which will really
9:48 change your approach on a lot of these
9:49 things until we get some updates within
9:51 the macro system with Chief Architect.
9:54 Now, we're going to notice something
9:55 here. All I had to do was zoom in here,
9:57 but we had an error there. We had an
9:59 error there, but all it took was zooming
10:00 in and it parsed that new info and it
10:02 fixed it. Now, I want kind of want to
10:05 backtrack just to what something I just
10:07 said, which is often times we're trying
10:10 to execute something and it needs to be
10:12 displayed on the screen for it to
10:14 execute. Now, in the case of this, this
10:17 didn't populate until we opened up this
10:19 polyline. This didn't populate until we
10:21 opened up this view. Otherwise, it would
10:22 have just been blank. If we had opened
10:24 up a layout, would have been blank
10:25 information regardless of the CSV being
10:28 present. Another thing about my newest
10:30 version of my pro plan is I do have a
10:33 section here called project project
10:35 designations. And what this does is it
10:37 designates all of the CAD details in
10:41 terms of their systems. Right? So all
10:43 these call outs are coming from this
10:45 designation page where I get to just
10:47 drag and drop this up to the number one
10:49 slot and it's going to change all the
10:50 details of my plan so that it shows 2x6
10:53 Doug fur at all the wall designations.
10:55 Okay, now this was a great system and I
10:58 keep trying to improve it and it does
11:00 keep getting better. But the next
11:02 version of this system which is my
11:04 current version of the system, this no
11:06 longer lives in the CAD detail that it
11:08 used to live in. it now lives on a plan
11:13 view. Now, there's a few reasons that I
11:15 did this. Um, one of the major reasons
11:19 that I did this was so that I could put
11:21 these user label options off to the
11:24 side. What do these user label options
11:26 do? Well, I have really advanced labels
11:28 for my cabinet labels, for my window and
11:30 door labels. They do a lot of awesome
11:32 things, which I'll kind of go over in
11:34 this video. But one of the things that
11:36 they do is they allow you to change just
11:40 a portion of that labeling convention so
11:42 that maybe you're matching some kind of
11:45 cabinet vendor's naming conventions so
11:48 that you're matching exactly. So you can
11:50 almost print an order sheet from a
11:52 schedule within the pro plan. So you get
11:55 to come in here and change some of these
11:57 designations. Now, it used to be that
12:01 you needed to have opened that up
12:03 because it's using a global. You had to
12:05 open that CAD detail up for it to
12:08 initiate those changes. What's the
12:11 problem with that approach? Well, let's
12:13 go. Say you finished your drafting
12:15 session for that day and you went to go
12:18 open your file back up. And what happens
12:20 is it reverts back to its default values
12:24 for your cabinet labels in this case
12:26 until you open that CAD detail again.
12:29 That was the problem with that approach.
12:31 The new approach is that this lives in a
12:34 plan view now and it's being its layer
12:38 is being displayed in the default
12:40 working plan view. It's actually right
12:42 off here to the side on a locked layer
12:45 that's set to white so that you don't
12:48 see it. If we just turn on the drawing
12:50 sheet, you can see it's right there. The
12:52 text is right there. What's great about
12:54 this is it's executing your changes
12:57 immediately. So that you don't need to
12:59 know macro scripting to go change these
13:01 things permanently and have them always
13:03 be correct. They're always going to be
13:05 driven from this working plan view.
13:07 They're always going to be correct out
13:08 of the box. That's an awesome approach.
13:11 So this was a fix and that's just taking
13:14 into account what Chief Architect has in
13:17 terms of limitation on how we can
13:18 execute
13:20 script. So that all that being said,
13:24 something that's cool that's built into
13:26 this system now is that I can place a
13:29 cabinet here and say it's a base 24
13:31 cabinet. And let's just say for instance
13:33 that and by the way one of my scripts
13:36 says hey if this is not in a room
13:38 because some of the part of this script
13:41 does look for what kind of room type
13:43 that it's in. It says if it's not in a
13:45 room just go back to a default label. So
13:47 that's something I've kind of fixed in
13:48 the newest versions. Now let's say I
13:50 drew some walls and I'm going to change
13:51 this to
13:54 bath. We're going to see that this
13:56 parses some information. It adds a
13:58 prefix V for some kind of base vanity.
14:01 then it keeps all the other labeling
14:03 conventions so that it's still going to
14:04 show some kind of three drawer base here
14:07 but with that V because we're in a
14:09 bathroom. But if we change this to
14:10 something like living room then it's
14:13 going to remove that V. Now what happens
14:16 with this three drawer base when I want
14:18 to change that designation or actually
14:20 more appropriately let's just change
14:21 this to a garbage pull out and let's
14:23 just say our cabinet vendor does not
14:25 call garbage pull out it's GBG they call
14:27 it something else. Let's just call it uh
14:30 BG for argument sake. I'm going to
14:32 switch to my project designations page.
14:35 I'm going to get into that cabinet label
14:38 setup here. I'm going to find wherever
14:40 that garbage cabinet is and I'm going to
14:42 change it to just BG instead. Right? And
14:46 so that when I come back to my working
14:48 plan view and we go pull off to the side
14:52 here, we're going to see that this has
14:54 been changed. Look at that. Isn't that
14:56 cool? So that works really well. What
14:59 was another consideration that I then
15:01 scripted in just talking about macro
15:03 scripting in general? And this is take
15:06 this video as like a systems approach to
15:10 creating macros. Okay, which is that
15:13 sometimes we might have a cabinet that
15:15 needs additional info. Well, I already
15:18 scripted something similar to this
15:21 inside of my scripts for my exterior
15:24 doors where you can change what this is
15:27 calling out in terms of type. But you
15:29 could also just come in here in object
15:32 information and in supplier go new type
15:37 and it's going to overwrite whatever was
15:39 there for type. So this is where we've
15:41 got some kind of oneoff door that
15:43 doesn't match our conventions, but it's
15:45 still picking up all the dynamics of
15:48 doing something like in window order
15:50 overview showing that it's um you know
15:53 just the window number or we're showing
15:54 that this is an existing one and it's
15:56 not applicable and it's so it's doing
15:59 all these other things that that it used
16:00 to be able to do before you know stack
16:02 the label that kind of thing. So what
16:05 else can we do with this? Well, now in
16:08 object information, let's just say
16:10 instead I've got a conditional check
16:12 that's looking for instead of overriding
16:14 the existing type. Let's add a plus sign
16:17 in front of our text and now it's adding
16:20 that to what was there before. Well, I
16:23 that's the same approach I'm now taking
16:25 to my cabinet labels. Okay, so when I
16:28 come to kitchen cabinet plan or working
16:30 kitchen cabinet plan, we see this label
16:33 BG24. I get to just open this up and I
16:36 can overwrite this convention. Now, I'm
16:38 still picking up the with denotion. I'm
16:41 thinking that this is just we're
16:42 changing some kind of acronym. So, we
16:44 can go back to that, you know, whatever
16:47 we want. Maybe that's the new name. And
16:49 there we go. It's picking it up. It's
16:51 replacing that old acronym, but it's
16:53 still taking in account that width. So,
16:55 it's still dynamic. Isn't that cool? The
16:59 nice thing about this is it does still
17:01 have that convention where we get to
17:02 just say the plus sign in front of it.
17:04 And so my macro is looking for that and
17:06 being able to add that this is going to
17:09 add some other text to the existing
17:12 coding logic that's also using the
17:14 coding logic from us user label options.
17:17 How dynamic is this? It's actually
17:20 really exciting. Something that we can
17:22 do with this then is that in some views
17:24 maybe I make it so that we're only
17:27 showing some um the schedule number as
17:30 opposed to the call out, right? And so
17:33 I'll put that in user options and I'll
17:36 say, "Hey, what layer set would you like
17:39 to have it where our cabinet labels will
17:42 only show a schedule number versus
17:45 showing the schedule number plus this
17:46 additional info?" So that's the dynamics
17:49 that I'm talking about about scripting
17:51 this stuff in. And it's a bunch of
17:52 conditional logic. So let's kind of
17:55 backtrack
17:56 again and go back to this project
17:59 information and see what it's even
18:01 doing. Now I kind of illustrate in
18:04 another video where I'm showing that we
18:07 could get information from builder trend
18:09 straight from CSV file straight into
18:12 this setup here. And what's nice about
18:14 that video is that I um just explained
18:16 that we can take some kind of Excel
18:19 sheet that's being exported from a
18:20 program and then we can get chat GPT to
18:23 write a Python code to automatically
18:26 conform whatever that export is to what
18:29 we need it to be in terms of a CSV by
18:31 just double clicking the Python code,
18:33 having it execute by looking up for any
18:36 Excel file within a folder and
18:38 immediately converting it to CSV with
18:40 our parameters. So that's what I did
18:42 with this builder trend setup. So that
18:45 brings us a lot of dynamics where
18:47 basically we can take any data
18:55 from having a lot of trouble with my mic
18:58 lately. Boy, I hope I didn't lose too
18:59 much of that. I just knocked the cable.
19:02 Hopefully we didn't have a bunch of
19:03 blank space. I'm just going to keep
19:06 talking. Hopefully that that gets
19:08 recorded right. So, here's what I've
19:11 got. I've got a polyline. In case you
19:14 didn't know, poly lines can execute and
19:18 store information from global macros
19:20 within Chief Architect that are not
19:23 accessible in any other way. What macros
19:26 are we talking about? Well, if we drop
19:29 down the macro, get into global contact
19:31 info, client info, and just go or
19:34 designer info in this case for company.
19:37 There we go. But how do we assign that
19:40 value to a
19:42 variable that we can use in a script
19:44 within text macro management? You can't.
19:47 You can't. But what you can assign it to
19:49 is a global variable. All right? And so
19:53 that's what I'm doing here with these
19:54 poly lines is I'm assigning a bunch of
19:56 values to a global variable variable
20:00 from the label of this polyline.
20:02 Polyline's one of those object types
20:04 that can do this very easily. And it
20:05 also just kind of helps in terms of
20:07 formatting. It looks nice on the page.
20:09 Looks better than just trying to drop a
20:11 cabinet in here. You can't drop a
20:13 cabinet in the CAD detail anyways. So,
20:15 if you're going to do this in a CAD
20:16 detail, polyline's probably the best
20:18 option. Now, I'm putting all this
20:20 information in the label. It's hard to
20:21 see this information in label. So, I
20:23 ended up scripting some of this in chat
20:26 GPT. And then I use the application
20:28 called
20:29 Notepad++ to kind of paste this in. And
20:32 then because chat GPT likes to screw
20:34 things up, I then went and fixed a bunch
20:36 of stuff here. Now, something to note
20:38 here is that in Notepad++, you can set
20:42 your language up. And maybe this helps
20:43 you kind of see your scripting as we can
20:45 set this to Ruby. And we'll see a few
20:48 things that are just getting formatted
20:50 automatically from Notepad++, which
20:52 makes it a little bit easier to
20:53 understand what's happening here. And so
20:56 this is what this polyline is doing is
20:59 it's saying all right here's some text
21:02 client information. Now we've got an
21:04 opening and closing percentage sign
21:06 which is a place marker call from some
21:09 for some script to be executed within
21:11 that those two percentage signs. So it's
21:13 an opening and closing of a script if
21:15 you will. So then I'm saying hey I have
21:18 this global client name. I'd like to
21:21 define it. I'm going to define it as hey
21:24 if client name is already nil or client
21:28 name to s is empty then client
21:31 name equals client name basically but
21:36 what I'm saying is it's actually what
21:38 this is saying is if these things are
21:41 blank if that global is already cleared
21:44 and it's zero it's nil there's nothing
21:46 there then we are going to define it by
21:49 saying quote unquote out percentage sign
21:53 client.name. Well, this should look
21:55 familiar to you. This is that global.
21:59 When you hit macro, the drop-own client,
22:02 the drop-own client name, this is what
22:05 it places. But we're putting this in the
22:07 quotes as kind of like a, hey, place
22:11 this text. But when we place this text
22:14 in a polyline label in quotes, it's
22:18 going to execute that client name macro.
22:21 And so we are now defining that global
22:24 as this. So we're pulling that
22:26 information basically from the polyline
22:30 that is capable of calling that global.
22:33 And so then we're storing it in that
22:35 global information. So if it's not nil,
22:38 if that information is not nil, it's
22:41 going to just put client name. Why would
22:43 it not be nil? Let me explain that. It
22:46 would not be nil if in the case that we
22:49 have that CSV file and that CSV file is
22:53 being read and defining things. So in
22:56 fact, right here at the beginning of
22:58 this script, it's immediately saying,
23:01 "Hey, let's just nail these out right
23:02 off the bat." Okay. Then it's going to
23:05 go try to read that CSV file. It's gonna
23:08 and this is all some stuff from chat GPT
23:10 that helped me script this, right? And
23:12 so it's finding rows. It's finding, you
23:14 know, exact fields and then it's finding
23:16 cell values. And here we go. We are
23:19 defining that row zero, row one, row
23:21 two. In fact, it's calling it row, but
23:23 those are actually columns. Okay? And so
23:26 what it's saying here is there's our
23:27 client name. Is that column
23:29 Z, column one, column two? And then it's
23:32 got a little note to explain what it is.
23:35 So then we want to return a hash of
23:37 these items. And that hash is going to
23:39 be here's our key. Here's our value. Our
23:42 key is a. Our value is this global. And
23:45 then else. So in case there is no CSV
23:49 file, in case we're not able to look
23:51 something up, in case we can't find
23:52 anything, let's just make sure that
23:54 these things are defined as nil. And we
23:57 know from what we just looked at, if
23:59 these values are defined as nil, what's
24:01 going to take over is those built-in
24:05 client name designer information coming
24:07 from Chief
24:09 Architect. What's our output then? It's
24:12 creating a hash. And a hash is a way for
24:15 us to we can always look up this
24:17 information pretty easily from some
24:20 other macro, believe it or not. In fact,
24:22 let's see if I can just do this from
24:23 memory. It's going to be a little bit
24:25 complicated for me, but data type hash
24:27 and our key value for A is what's being
24:31 reported from the CSV, which is this is
24:33 the text in that cell underneath my
24:37 designer or client's name in this case.
24:40 So, I can copy this macro
24:44 name. Let's create a new macro that I
24:47 will just call test or spell it all
24:50 kinds of wrong. And I can say well I
24:53 could type in that macroname or I could
24:55 come to this dropdown userdefined and
24:57 find that CSV lookup client. Okay so
25:01 this is doing this is placing that place
25:04 marker and when evaluated it's not
25:07 checked that works just fine right and
25:09 so then if we just did this if we just
25:11 put a bracket in here and then a and
25:15 bracket what's it going to do? Well it's
25:17 just going to create a place mark. It's
25:19 just basically um it's reporting text in
25:22 this case. But instead if we removed our
25:24 percentage sign and we said macros dot
25:28 now we are looking for that macro in the
25:30 system if it's evaluated. And you can
25:34 see here look at the output. We are
25:37 indexing that key from the hash. We're
25:40 grabbing that key from the hash. That
25:41 key is a. So we're looking up macros dot
25:45 and then which macro it is that CSV
25:48 lookup client and then we are taking
25:51 that key value A and that's what's being
25:53 reported. So we can use this in multiple
25:56 different
25:57 places. Here's the next really cool part
26:00 about this. because we're using a global
26:03 system, because we're grabbing this
26:05 information from either our CSV lookup
26:08 or from either our designer client
26:10 information and tools that when we open
26:12 up a file, um, excuse me. Let's see.
26:15 Let's just do control shift new. And I'm
26:17 going to open up some new layout file
26:20 here. And this actually does not look
26:22 like the correct layout file. Let me
26:24 open one up instead. Let's open this guy
26:26 up.
26:30 This one's been updated. So, what
26:33 happens is when I reassociate this file
26:38 with the file that I'm actively working
26:40 on, and let me just find that real
26:42 quick. File that I'm actively working on
26:45 is
26:46 test. All
26:48 right. Then we get back to our test and
26:52 project information and we make sure
26:54 that this is in fact looking up that
26:56 CSV. See that's been populated and this
26:59 has been populated. Now this is being
27:01 sent to view just like you would send
27:04 any view this portion. But keep in mind
27:08 we're still getting all this information
27:10 from globals and we know we can just
27:12 drop in some text using a global call to
27:15 any of these items. So that when we
27:17 reassociated this and populated this,
27:19 this is coming from those globals. This
27:22 is not a saved plan view. This is just
27:24 some text on my page zero. So, here we
27:27 go. Page zero. Bam. There's all those
27:29 globals being
27:31 reported. This makes it really nice. We
27:33 don't have to worry about a save plan
27:35 view for some reason getting who knows
27:38 what, screwed up in some way. This is
27:40 just all that's happening here is this
27:43 is getting pulled from our CSV, which
27:46 means that we might have an assistant
27:47 that's punching this information in for
27:49 us and it's just there and it's
27:50 populated. So, let's say we're at zero
27:53 hour and we've got no time, right? And
27:55 we've got a client that's like, "Hey,
27:57 can you just can you just send me an
28:00 update to this little thing real quick?"
28:01 Or, "Can you just get that on a page and
28:03 get it to me with, you know, your your
28:05 title block real quick?" And you don't
28:07 have to worry about it because maybe you
28:09 had someone ahead of time punch this in
28:11 and you get to open this up and send a
28:13 view to it and all your information's
28:15 there. It's
28:19 awesome. Feel like I've been rambling.
28:22 Not sure where to go from here.
28:26 I just built this, so you can tell that
28:28 I'm excited about it. Um, and I'm not
28:31 sure that I've considered everything
28:33 that we might run into, but you know,
28:36 the more you build these systems, the
28:39 more this stuff just kind of starts
28:40 making sense and and you learn from the
28:44 previous setups. And so hopefully you're
28:46 learning from my previous mistakes here.
28:49 And you can see here that we've got
28:50 automatic lot analysis. And now we're
28:52 just pulling this information from a
28:54 CSV. Um, in my case, the climate zones
28:57 automatically be populated from a zip
29:00 code. So that part's all automatic as
29:02 well. So where is the potential for user
29:05 error? It's if I can't plug in eight
29:08 cells in a CSV file. That's the only
29:11 time I'm plugging this information in.
29:14 It's the only time. And that's all I
29:16 need to know. I need to know that that
29:19 CSV file is there, which I probably
29:22 don't need to know that. I probably need
29:23 to just punch in one more thing that
29:26 just as a check here that very clearly
29:28 shows, hey, a CSV file is present just
29:32 so you know, you know, that would be a
29:34 nice little check for myself is that it
29:37 or maybe even put it in this text right
29:38 here. We're reading from the CSV versus
29:41 client information. Let's see if we
29:43 can't set that up. There's no reason why
29:44 we shouldn't be able to. And I'm going
29:46 to use chat GPD. I don't even want to
29:48 think about it. So, let's open up a
29:50 little browser
29:52 here. I like to have um I have a chat
29:56 GPT set to temp chat GPT. So, I can do a
30:00 um I can just click on this bookmark and
30:03 all that it's doing is you see that URL?
30:07 It's just chat GPT. And then I added
30:09 that end part on there for a temp chat
30:11 GPT. So, I have temp coding right here.
30:14 Temp coding. That just means it's not
30:15 going to store it in my chat GBT
30:18 history. It's going to get rid of it as
30:20 soon as we're done. So, this would be a
30:22 use case for that where I don't really
30:24 care if this gets deleted or not. So, I
30:27 want to
30:29 script something that
30:32 says whether we are reading from
30:39 CSV or not. And so, what would be the
30:42 conditional check for that?
30:45 Um I guess the conditional check would
30:47 be
30:49 [Music]
30:50 um and we will check this by see
30:58 by seeing if there is a hash reported
31:04 from
31:08 um macros.csv
31:15 CSV
31:16 lookup
31:19 point. This is for chief
31:22 architect
31:26 Ruby. Not sure that I did the right
31:28 approach for that. I bet there's a
31:30 better approach, but we'll see what it
31:31 comes up with.
31:49 interesting approach
31:51 here. And I bet you Let's just try to
31:54 I'm going to try to I am going to try to
31:56 struggle through this just a little bit.
31:59 So, I'm
32:01 thinking let's do a little macro.
32:05 Let's do a little new and let's go
32:09 CSV
32:13 lookup
32:15 check probably be client check but fine
32:18 we're going to put this in here evaluate
32:21 and a number of arguments so client 18
32:25 let's see client call into your CSV
32:30 lookup I don't know that I care about
32:32 the client ID portion of
32:34 call into the client data and then
32:38 client data is a
32:43 hash. I don't know what this UI message
32:45 box is. That's
32:49 interesting. And then it's saying client
32:52 ID. I don't need to do
32:54 that. I just could get rid of that
33:01 entirely. And I don't think I need you
33:04 message box. It's very curious that it
33:07 put some emojis in here. I'm wondering
33:09 if that's even possible. I didn't know I
33:12 could do that in Chief. That brings up a
33:14 whole new fun bit of stuff here. And
33:16 then let's get rid of this UI message
33:19 box as
33:22 well. And this part as
33:27 well. And can we just put this in
33:29 quotes?
33:35 What are we getting here? Client ID.
33:36 There's still some reference to client
33:38 ID. Oh, and client ID empty. I don't
33:41 need
33:44 that. Oh, there's still one more me
33:47 you're seeing. I'm looking at, you know,
33:49 new result client ID for object. There's
33:52 still some reference to this. Oh, here.
34:01 data. So accurate. Well, so basically we
34:04 get to just do this is bracket a bracket
34:12 bracket not reading from. How cool is
34:15 that? I did not know we could put emojis
34:18 in our
34:19 macros. I'm going to start using
34:22 that. I don't know what for, but like So
34:25 what happens here when we do this? Let's
34:28 bring up that check.
34:32 How cool is that? I had no idea. Oh,
34:39 that's CSV. And why is that? Let's see
34:43 if we can't see why that is. And so,
34:44 let's do another check here. So, let's
34:46 just um copy this. Let's copy this. And
34:50 in this case, let's just do um let's
34:53 just do this name from
34:56 CSV. And name from CSV is not nil. So
35:00 then
35:01 why? So we know that this is not nil. So
35:05 what did we do wrong here? If client
35:06 data is a
35:09 hash. Oh, cuz client we're we're
35:12 defining it as a key. So we need to take
35:14 away the
35:17 key. There we go. It's
35:20 working. I just like that. That's an
35:23 emoji. I have no I don't know why I
35:25 never knew that. That's really cool.
35:26 What other emojis can we get? Um, if you
35:28 didn't know this, uh, I think
35:30 in, um, a PC that you can
35:34 hit window key plus colon or or yeah,
35:40 semicolon. Window key plus colon or
35:42 semicolon. And let's just put this guy
35:44 in here. Can we get this big arm? No.
35:48 Okay. So, this must not be this not
35:51 emoji. This is some kind of chat GPT
35:54 what the heck this is and how they got
35:55 it. Uh, let's
35:57 see. How did you use what looks like an
36:03 emoji? And can you
36:06 please show me all
36:10 available
36:12 emojis so I can copy them and give them
36:17 to my
36:19 wonderful VIP YouTube
36:23 members? How about that?
36:30 Give me let me see these let me see
36:32 these glorious emoji that I'm going to
36:34 start sticking in my plans and piss off
36:37 my plan
36:40 checkers.
36:43 Uh there we
36:46 go. Is that
36:49 it? No. I want all. I want give me give
36:53 them all to
36:58 me. I want all of them. I want to copy
37:00 all of
37:08 them. There are over 3,800 of them.
37:12 Okay. But for some reason I couldn't um
37:15 parse that
37:17 from what is this one line requires no
37:21 extra
37:23 all open all emojis inline text. What
37:27 are you saying? If you'd rather have
37:28 them all in one long string
37:34 run.
37:35 Okay, let's copy this. This looks like a
37:38 command line thing.
37:44 What kind of Okay. No. Let's see. What
37:47 are they saying? Open all emojis text.
37:51 Where's all emojis text? Oh,
37:58 okay. So,
38:00 this Okay, it's pointing me to where
38:03 these exist. Cool. What do you
38:06 got? Look at those little beauties. How
38:10 fun is that? I'll paste this for you
38:14 guys.
38:16 So, where's my I want the bicep. That's
38:19 what I want
38:21 first. Or actually, I probably use these
38:24 um these hand gestures is probably
38:27 probably what I choose. So, let's grab
38:30 this guy and see if we can't use
38:33 it. I mean, it looks like it was there,
38:35 so I don't know what happened.
38:39 Let's
38:40 see. I'm not able to paste
38:44 this there. That one right there. That's
38:46 the one I want. So, why is that not Oh,
38:49 cuz I'm placing it on the wrong one.
38:50 Aha. That's why it's not showing up.
38:53 There we
38:54 go. Oh my goodness. This is so fun. So
38:57 it probably does work if I just did the
38:59 window key and colon
39:01 is although this says not rating from
39:05 and it doesn't have that
39:06 emoji. Try one more time
39:11 then maybe there's only certain
39:15 ones. Oh no this didn't get
39:18 updated. See if we look up
39:21 check must have had the second part of
39:24 this. Okay, so window key
39:26 colon buff dude. Same thing. No key
39:33 colon. Man, I love this. Um, let's just
39:37 try point. I think we could just search.
39:39 Yeah, look at this. Isn't that
39:45 cool? This is the best video I've ever
39:49 made. So, it's saying it's not reading
39:52 from and it shouldn't be. It should. Why
39:55 is it saying that? Why is it saying it's
39:56 not? Because we know that it
39:59 is. Oh, because we have this index part.
40:05 Okay, there we go. So, it's reading for
40:09 client. Boy, stuff just gets more and
40:12 more fun when you get into the scripting
40:15 stuff. I think that's it. I think we're
40:18 going to stop there. I think I'm going
40:19 to lean on you guys to come back with
40:22 some fun stuff about this and questions
40:24 you might have. So, um, definitely
40:27 getting into the weeds on on macro
40:29 scripting. But, you know, what a cool
40:31 system,
40:32 right? Check you later.
40:36 [Music]
