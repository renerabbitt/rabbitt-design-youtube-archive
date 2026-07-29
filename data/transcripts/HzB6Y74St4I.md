---
videoId: HzB6Y74St4I
title: Template Tuesdays - Managed Mode Tricks and Tips
url: "https://www.youtube.com/live/HzB6Y74St4I?si=QnGf7zQLCEJIu6Ro"
status: imported
---

# Transcript

0:02 What's going on everybody? Welcome to
0:03 Template Tuesdays.
0:06 Today, figured I'd go over managed mode.
0:10 I've got a couple videos on my channel
0:12 about managed mode, but I don't know, I
0:14 think I have some new thoughts, some new
0:16 tips and tricks, um and also give the
0:18 opportunity for anybody that's in the
0:20 live chat this time to ask me questions
0:23 about how to use managed mode and
0:25 um maybe run into some problems and I
0:28 can
0:29 solve those problems for you.
0:31 Um
0:32 yeah, that's kind of where I'm at with
0:33 today's episode. And it
0:36 there's not a whole lot to managed mode,
0:39 so you'd think we're not going to burn
0:40 up an hour. We're going to burn up an
0:42 hour cuz it takes a while to
0:44 uh do some of the things that I want to
0:46 show how to do in managed mode because
0:49 um
0:50 they hadn't quite optimized in this
0:52 version of Chief, they hadn't quite
0:53 optimized the file right cache and and
0:57 read write uh for managed mode. So, some
1:00 things take a while to do in managed
1:03 mode. Now, there's a lot of really cool
1:06 benefits to being in managed mode and I
1:08 want to showcase those and then uh the
1:11 thing that I run into quite often is
1:13 that people say that they can't work on
1:15 a cloud, they can't work on a team in
1:17 managed mode. And I will tell you that
1:19 managed mode is the best way to work on
1:22 a cloud. Managed mode is the best way to
1:25 work with a team. So, hopefully I'm
1:27 going to show you
1:29 why I say that. So,
1:32 welcome anybody that's in the chat. Um
1:35 chat hasn't started kicking off yet, so
1:37 we'll see what happens with that and
1:39 then
1:40 um let me just dive right in.
1:43 So, if you're not in managed mode and
1:45 you want to get in managed mode just to
1:47 try some things out, I want to note
1:49 something is that when you switch to
1:51 managed mode, Chief Architect does try
1:54 to migrate your existing um settings,
1:57 your existing files, etc., your
1:59 toolbars, etc., your user library.
2:03 Try to migrate that, and it stores it on
2:06 a place on your machine that typically
2:09 is not a
2:09 a place that we're going to access. If
2:11 you're on a PC, that's going to be in
2:14 your program data and your app data
2:16 folders, and that's where we're going to
2:17 store a bunch of managed files. And if
2:20 you go try to dig around and find those
2:22 files, they're actually encrypted files.
2:24 You can't really do anything with them.
2:26 Um so,
2:27 you can, if you feel like really
2:29 screwing Chief Architect up, you can go
2:32 save those encrypted files and load them
2:34 on another machine, and you will
2:37 uh
2:38 get a duplicate of your machine, believe
2:39 it or not. But,
2:41 um having had experience with
2:44 a write cache that uh was broken in
2:47 Chief Architect, I couldn't tell you if
2:49 that's because I did that particular
2:51 trick or not. And so, I did have to
2:54 reinstall Chief Architect not that long
2:56 ago um to get my write cache to be
2:58 working again.
2:59 So, I guess I'll start with some of the
3:01 more basic things, and then we might get
3:03 into some of the more advanced things
3:05 that I've discovered um from manage mode
3:08 later on in the hour. And then, there we
3:11 go. The chat's kicking off, so
3:14 uh hello. Hello, everybody. Hello,
3:15 Merlin. And good morning, Keith. And
3:19 uh YouTube Peak Kieran. Uh let's see.
3:21 Kieran sounds like a
3:23 recognizable name.
3:25 Good day.
3:26 So,
3:28 manage mode, just to start this off, you
3:30 know, I always kind of mention this
3:31 [clears throat] is Template Tuesdays is
3:33 about me sharing um it advanced
3:35 knowledge that I would typically have in
3:36 my members area.
3:38 This stays live for 24 hours, and then
3:40 this video goes and gets put into the
3:42 membership area of my YouTube.
3:44 And
3:46 I also take the opportunity to say,
3:48 "Hey, I have products that utilize
3:50 everything that I'm teaching you, and
3:51 they were already built and to put
3:53 together and in a way that you don't
3:55 have to rebuild them. So, if you want to
3:56 go check those out, you can go look in
3:58 the description on YouTube and uh you
4:00 can go check take a look at my shop. One
4:02 of those things that I have is my
4:03 templates. And my templates are built to
4:06 utilize manage mode in the best way
4:08 possible. And if I expand this and we
4:10 take a look right here, what's great
4:13 about manage mode, especially when
4:15 you're working with a team,
4:17 is that you can drop in additional files
4:20 here, such as a URL.
4:24 And this could be some kind of an
4:25 information for a team member, what have
4:28 you, all right?
4:30 So, for example, if I wanted to drop in
4:32 some kind of file for a team member,
4:35 I might just go, "Hey, import file."
4:38 And then it's going to bring up a dialog
4:39 box and I'll go find some file that I
4:41 want to
4:42 uh keep alongside of this. Here's a
4:43 screenshot, for instance. Maybe I've got
4:45 a markdown file,
4:47 what have you, all right?
4:49 So, that part's
4:51 really, really cool is that maybe along
4:53 the way, as you're
4:56 picking up information, as, you know,
4:58 you're just um compiling, you're doing
5:01 your edits for the work day, and you
5:02 want to be able to share what you have
5:04 back to the team member, and it's and
5:06 it's just you want it inside of the
5:08 project file because for whatever
5:10 reason,
5:11 um maybe you did not want it in your
5:13 shared Dropbox file or SharePoint file,
5:15 et cetera, Google Drive, et cetera.
5:18 So,
5:19 this is a really cool part of this.
5:21 The other really cool part about this is
5:24 that you can drop in files that might
5:27 not be for every team member. Maybe
5:30 they're just for you on your end,
5:32 and then you can
5:35 and maybe those files were just so that
5:37 you had quick access to them, you know,
5:39 you can come up with a number of
5:41 different scenarios, but if I were to go
5:43 and right click on this and click on
5:45 export, what happens here is we get an
5:48 export dialog box and this is our
5:50 opportunity to, if we wanted to, say
5:53 that we actually didn't want our team
5:54 member to have that screenshot. We get
5:55 to uncheck this.
5:57 And so, what happens when we export this
5:59 file? Let me go ahead and press okay and
6:02 I'm just going to save this
6:04 to my downloads folder for this case,
6:06 furniture fixtures fix fixes.
6:09 Let me save that real quick.
6:12 Now, I'm exporting this file. That means
6:14 it's now being compiled outside of Chief
6:17 Architect. Typically, in a previous
6:20 workflow, X16, etc., we would just be
6:23 saving a plan file, a layout file, and,
6:27 you know, if we're doing a bunch of
6:29 design things and we're utilizing
6:31 textures that didn't exist across all of
6:34 our team members' computers, we might
6:36 even be doing file export export a
6:40 backup. And that backup might be a zip
6:42 file and that zip file is going to
6:44 include a bunch of texture files and
6:46 that's necessary if we want our other
6:49 team member to be able to see all the
6:50 same materials that we put in the plan.
6:53 Because they won't have the source
6:55 texture files that make up those
6:57 materials. Meaning that we have a bunch
7:00 of JPEGs or PNG files that make a
7:03 material that makes something look like
7:05 metal. And so, maybe we created that or
7:07 maybe it was from a catalog that someone
7:09 else doesn't have. That's why you want
7:10 to include those files so that there's
7:13 no missing file dialog boxes.
7:15 Now, enter managed mode and we don't
7:18 have to worry about that anymore because
7:21 all of those files are included in that
7:23 export. I'll show you what I mean.
7:26 We get to just go open this up,
7:28 downloads. Here's that furner fic-
7:31 furniture fixtures CA proj file, okay?
7:35 Now, I'm going to come back here to
7:36 Chief and I'm going to delete my
7:38 furniture fixtures uh
7:41 Mind you, I don't think even have a
7:43 backup of this file yet. So, kind of
7:46 scary to delete this, right? But, I'm
7:48 fairly confident that Chief Architect's
7:51 export worked correctly. And even if it
7:54 had a little bit of a problem on its
7:56 export, I still have some ways of
7:58 extracting those files and finding those
8:01 files.
8:02 One is that we still have archives,
8:04 okay? And archives is going to be that
8:07 individual plan file, that individual
8:09 layout file. I can still find those, get
8:11 them back into Chief, link those back
8:14 together, and rebuild that project file.
8:17 In fact,
8:18 we could do that in just a minute.
8:21 But, for now, I want to show you that,
8:23 you know, you saw me just export the CA
8:25 proj file. I can double-click this, and
8:27 it's just going to install right back
8:28 into Chief. So, that's what I just did.
8:30 I just double-clicked it. The next thing
8:33 that I want to do is
8:34 in the case that you have multiple
8:36 different Chief Architect versions on
8:38 your machine, and maybe you even have
8:40 Home Designer on your machine, when you
8:43 open up those programs, those other
8:46 versions, they will prompt you to ask
8:48 you if you want to associate certain
8:50 file types with that program and make it
8:53 the default. In the case that that's
8:55 happening with you when you double-click
8:57 the CA proj file, it might be that it's
9:00 trying to open it in some other software
9:02 version. Just keep in mind, on a PC at
9:04 least, you can always go to open with,
9:07 and instead of choosing the correct
9:10 um program version here, you would say
9:13 choose another app. The reason you would
9:15 do that is then you would choose the
9:17 correct app and choose always, and that
9:20 will reassociate this with just X17.
9:24 That way, I know I could double-click
9:26 this, and it's going to install
9:27 correctly. Now, if we come back to Chief
9:29 Architect, we're going to see, there we
9:30 go. It's prompting me to say, "Hey, do
9:33 we want to open something from this
9:35 project file?" And I could just say
9:36 close,
9:37 and know that here it is over in my
9:39 project browser exactly as I exported
9:42 it. Notice that it's missing that extra
9:44 image file that I loaded at the
9:46 beginning of this session. All right.
9:49 And so the other thing that I want to
9:50 show you is that if you had a There
9:53 There is a trick where we can change the
9:55 extension of this to a .zip file,
9:58 but if you have a really good extractor
10:01 program such as 7-Zip, you could
10:05 right-click this and just say open with
10:08 and then I'm going to choose 7-Zip file
10:11 manager and we'll see this is what's
10:13 included in that project file.
10:16 Is inside of projects, there is the
10:18 folder for furniture fixtures
10:20 and here's all of those source files,
10:24 right?
10:25 We go up a couple levels. We can also
10:27 see here's all the source files for all
10:30 the materials that were used in this
10:32 project. All right, so they're all
10:34 bundled up in here.
10:36 This should also tell you why the file
10:38 size is so large and I want to cue you
10:41 in to something that's, you know,
10:42 glaring and obvious right now is
10:45 that's a big file size, man, right? And
10:50 so when we go look at this, if we go
10:52 right-click on this and
10:54 um and kind of see, you know, what the
10:57 details are about this, properties, etc.
11:00 190 megabytes, that's quite large. So
11:03 how do we share that with a team? Yeah,
11:04 you're going to need some kind of a
11:07 cloud-based service to a share a file
11:09 size that large. That file size is that
11:13 large because of those image files.
11:16 All right, so when we go look at this in
11:20 assets again, we can see, you know,
11:22 organized by size. Yeah, these are large
11:24 image files. If I wanted to be diligent
11:28 about keeping a really optimized system
11:31 at all times, then I could go in there
11:35 and reduce the image resolution of those
11:38 particular files. Now, that would be a
11:40 lot of work, and so that would be
11:41 something that I might, you know, stick
11:44 that on and associate some kind of
11:46 um
11:47 you know, someone that's that's new to
11:49 my company, etc. And and have them just
11:52 do some busy work because it would be
11:53 worth my time. Because overall, there's
11:56 there's a bit more on the managed side
11:59 of things when we start to see a
12:01 slowdown in programs, when we start to
12:04 lose space in our drives, etc.
12:07 File bloat,
12:08 this might be worth my time to go in
12:10 there and, you know, reduce the file
12:13 size of the top 10 items here. Now, you
12:15 can reduce file sizes by changing them
12:18 to um
12:19 a
12:20 um
12:22 a compressed
12:23 file type like a JPEG.
12:25 Just keep in mind that the graphic
12:27 fidelity inside a Chief Architect really
12:30 is reduced when we use JPEG. You really
12:33 see that compression in the image
12:35 quality.
12:37 So, if you're someone that relies on
12:39 renderings
12:41 from Chief Architect and you're not
12:42 utilizing AI, maybe that image fidelity
12:45 is really important to you. So, you want
12:46 to try to keep these as PNG file types.
12:50 Just keep in mind, PNG's a lossless file
12:52 type. So, they're going to be larger
12:53 size. So, what do you have to do then?
12:56 You have to reduce the resolution of
12:57 that image.
12:59 Now, if you're getting into much better
13:01 in in um
13:03 um maps, materials, where you're
13:05 utilizing the other
13:08 uh texture slots such as the bump map,
13:10 roughness map, AO maps, etc., opacity,
13:14 etc.
13:15 Um then
13:16 you might just reduce the resolution of
13:19 those secondary maps and keep the
13:22 resolution of the primary base color map
13:25 or texture map up to that 1024
13:28 resolution, I would say would be the
13:30 minimum.
13:31 And then
13:32 you could reduce the file size of your
13:35 secondary maps to like 768 or even 512
13:38 and just take a look and see if they
13:40 still look realistic enough for you.
13:42 The main one here that's 50 megabytes is
13:45 that's a
13:48 an HDRI backdrop. An HDRI has a radiance
13:52 channel, so it actually is emitting
13:54 light in the scene when we utilize that
13:57 in Chief Architect. So, I like to have
14:00 this, but you know, there's no way
14:02 around this. This is a large file size.
14:04 It's going to be a 4K or 8K texture with
14:07 a whole another channel embedded in it.
14:10 So,
14:11 um that's just kind of a breakdown of
14:13 where these file size problems might be
14:16 coming from, okay?
14:18 Now, something to note if you want to
14:19 try to
14:20 kind of like limit this in some ways,
14:22 I'll show you some tricks.
14:25 So, let me get into here and that I'm
14:28 going to say, "Hey, I've just got a I'm
14:30 going to make a copy of this furniture
14:32 plan, all right?" And let's just say for
14:35 argument's sake you're doing something
14:37 like what I do in my templates. And I'll
14:39 show you what I do in my templates
14:40 actually. I'm going to
14:42 I'm going to come in here.
14:44 I have my templates as soon as I start
14:47 drawing, what happens here is my plan
14:50 files go to all of these various
14:53 layouts. These layouts serve different
14:55 purposes. They're different title block
14:56 styles, they're different sheet sizes. I
14:59 get to go and pick which one I want to
15:00 use, okay? So, as soon as I start
15:02 drawing, those layouts start building a
15:05 construction document set for me.
15:07 Now, what I could do, I could utilize
15:09 something that's very cool about manage
15:11 mode, which is I'm going to choose a
15:13 title block style that I want and I'm
15:15 going to right-click and choose this
15:17 really
15:18 strangely named thing here, which is
15:21 make a copy with links to project.
15:24 What does this mean exactly? Well, I
15:26 just told you that my layout already has
15:29 views sent from my plan files to that
15:32 layout, okay?
15:34 And so, what this is saying is we want
15:36 to make a copy of this layout and retain
15:39 the links of anything that's a that has
15:43 some pre-established links, some views
15:45 sent. So, we want to maintain that,
15:47 right? So, we want to copy the layout,
15:49 we want to also
15:51 bring anything that's linked to that
15:53 layout with it, and we're going to put
15:55 this into a new project, all right?
15:59 So, this prompts this dialog box here. I
16:01 don't have a project set up already, so
16:04 I need to come down here and click on
16:05 new project.
16:07 And so, what this did was it it did not
16:10 bring in all this helping information
16:13 files that I have. I've got a bunch of
16:14 links here to help people out for
16:16 utilizing my templates. I've got some
16:18 utilities here um that are all linked.
16:21 All these things are in my
16:23 template project, okay? So, I'm
16:25 utilizing this project because it's
16:27 already got links. That's how I start a
16:29 new project is I make a copy of this.
16:32 Well, even
16:34 cooler than that is I just chose the
16:36 things that I need, and you can see it
16:38 did make a copy of that layout, and it
16:41 brought the three plan files that have
16:43 things being sent
16:45 to this layout.
16:46 Now, for argument's sake, let's say I
16:49 didn't have this logo and design
16:50 criteria option one plan, all right?
16:53 What this plan is doing specifically is
16:56 it's establishing all of my spec um IRC,
16:59 CBC,
17:01 all that stuff. It's establishing my
17:03 project information, it's establishing
17:05 my logo, it's establishing my stamp if
17:07 I've got one, it's it's establishing my
17:09 design load criteria. The reason I do
17:12 this and isolate this is so that I can
17:15 build several of these in the case that
17:18 I'm working different jurisdictions, in
17:20 the case that I'm working for different
17:22 builders, in the case that I need
17:23 different title blocks, okay? It's
17:26 really easy for me to make a copy of
17:29 this
17:30 design option two, all right? Open up my
17:35 layout,
17:37 and then I can change my reference plan
17:40 files by getting into tools, layout,
17:43 reference plan layouts, and you can see
17:45 logo and design criteria option one
17:47 plan.
17:49 I can replace that reference and replace
17:52 it with my design option two plan, where
17:55 I might have had a different logo,
17:58 different um design loads, etc. And so
18:01 there you go, it's going to just change
18:02 out all my spec that easily.
18:05 All right. Now, in the case that we're
18:07 building up a bunch of these different
18:09 um plan files, some of these plan files
18:13 might just be for information, but you
18:15 might have built them from something
18:17 that had a bunch of material files in
18:20 that plan file. And if that's the case,
18:23 my trick for reducing your file size is
18:26 getting into the 3D menu, materials,
18:29 plan materials, and select all of your
18:32 materials here,
18:34 and then merge them into one material.
18:37 Why would we do that? That's because
18:39 this Let's just pretend that this
18:41 particular plan file is just
18:43 establishing some criteria for my
18:45 layouts. We're not actually producing
18:47 any kind of a 3D view, but
18:50 it came with it a bunch of materials.
18:52 And so when we would go to export this
18:54 as a project, it's going to really pump
18:57 up the file bloat on this project. So
18:59 this would be my trick for getting
19:00 around that is you're going to want to
19:02 press okay, save this out. There we go,
19:04 we're all done.
19:07 Now,
19:08 let me just close down a couple things.
19:10 Don't save, save, what have you.
19:15 Let's say that I've got this fully built
19:18 out and I want to show you something.
19:20 I'm going to delete this plan option two
19:22 plan, okay? I'm actually going to delete
19:25 this as well. I'm going to make a copy
19:27 of it first, but I'm going to show you
19:28 what happens.
19:29 Made a copy of that and then I'm
19:31 deleting this one.
19:34 And I want you to show you what happens
19:36 when I do this cuz this is not the prop
19:38 proper process of doing things. Is when
19:41 I delete this, this action is permanent,
19:44 okay? This was already sent to Townsend.
19:47 This is already sent to my layout is
19:49 what it's telling me.
19:50 And so I ignored that. I didn't really
19:52 pay attention and then all of a sudden
19:55 we see that we've got a little question
19:56 mark here.
19:58 This means that we had a linked file
19:59 with this
20:00 file and now it's it's missing that
20:03 linked reference. Now, I'll show you
20:05 when I open this up and it's missing all
20:08 those files in the beginning there. I'm
20:10 going to go ahead and replace that
20:11 reference and I'm going to replace it
20:13 with the thing that I copied, okay? And
20:15 all of a sudden
20:17 there we go. We've got our views all
20:19 linked back up again. But I want you to
20:21 notice that that question mark still is
20:23 there. And so someone that might be
20:25 working through this and going, "Man,
20:27 you know, how the heck do I get rid of
20:28 that question mark? I thought I just
20:29 fixed it right there." All you have to
20:31 do is save your file and that's it.
20:34 You'll notice that that question mark
20:35 disappeared.
20:37 So that's it. It's just looking to be
20:38 updated there.
20:42 Now, while I'm still going on this,
20:44 let's say that my
20:46 floor plan {dash} N here is my design
20:49 one, okay?
20:51 And that
20:53 um in this case, I want to create
20:55 another design iteration to share with
20:58 my team. One we've got some kind of a
21:00 galley kitchen, the other one we might
21:01 have
21:02 um just a you know,
21:04 uh a a kitchen, something like that with
21:06 a peninsula.
21:08 So, what can I do? What would be the
21:09 proper way of doing this? It is not to
21:11 sit here and go make a copy. We don't
21:14 want to create a copy.
21:16 All right? That is an old methodology.
21:19 When we sit here and try to create a
21:20 copy,
21:21 what this is doing is this is how we
21:24 would work in X16. You'd have design
21:26 one,
21:27 you create a copy, you'd have design
21:28 two. You'd have to open up layout and
21:31 change the reference files to design two
21:33 if you wanted to present design two.
21:37 Not only that, but you would really be
21:38 worried about renaming things, such as
21:41 renaming this, because you know, in
21:44 previous versions, that would break the
21:46 links for its files. You all of a sudden
21:50 would not be able to find these files
21:51 because you just changed the name of
21:53 them. That's not a problem in managed
21:55 mode. That That is something that you
21:57 don't have to train your people on
21:59 anymore. You can rename them to your
22:01 heart's content.
22:03 So, if I want to come up with a design
22:05 two iteration one, it might be nice if I
22:08 just create a new folder inside of this
22:10 project. That might be a good thing. So,
22:12 this is going to be design one, okay?
22:15 And then I could take my files for
22:17 design one and throw them in here. And
22:20 then, if I wanted to create a design
22:21 two, I can right click,
22:25 make a copy with links to new folder. We
22:27 already know what that make a copy with
22:29 links part is, right? We'd said that
22:32 just a little bit ago, is that we have a
22:34 layout, it's got linked files there, we
22:36 want to retain those links, and we're
22:38 going to put them in a new folder within
22:41 this project, okay?
22:43 So,
22:45 there we go. Look at this, design two.
22:48 And I might do a little bit more work
22:50 and go ahead and name this, okay?
22:54 Now, there might be cases where you want
22:56 to have these separate in separate
22:59 projects, okay? And that's where you're
23:02 going to make a copy with a links to a
23:04 new project. And so let's just say for
23:07 argument's sake that we don't actually
23:09 want design two in here. We want it in a
23:11 separate project file, all right?
23:13 And so we could
23:15 come up here and just we could actually
23:18 do right click new project.
23:21 We don't need to include a plan. We
23:22 don't need to include a layout. We can
23:25 say that this is design two for now.
23:28 Oops, and I can misspell it. That's
23:29 fine.
23:31 Press okay.
23:32 Now I could just drag and drop this.
23:37 And so
23:38 there we go. It's going to take it just
23:40 a second here.
23:46 And what you will notice here is these
23:48 additional link items will be moved
23:50 design two, etc., etc. Yes, do we want
23:52 to continue? Yes, we do.
23:55 And so there we go. We have this split
23:58 up two separate projects. So if we
23:59 wanted to share this with the the team,
24:02 we'd have to export both this proj both
24:04 of these projects.
24:06 What might be nice about this approach
24:08 as opposed to having everything in one
24:11 project file is that we might be able to
24:14 take advantage of
24:16 uh what Chief calls folders, which I
24:18 think is
24:19 Sorry, Chief. I battled with you a lot
24:22 in beta when you were doing this, but
24:24 folders was not the right name for this.
24:25 These are tags.
24:27 Um they're or filters, if you will,
24:29 okay? And so I want to create a new
24:33 folder tag is what I'm going to call it.
24:35 All right?
24:36 And I might say that this is, you know,
24:39 I might want to start classifying some
24:41 of my stuff. You can see I already
24:42 created galley kitchens there. So
24:43 actually we'll just get rid of that. Um
24:45 and we'll just do corner kitchen.
24:49 Now, I'm going to give you some ideas
24:51 about tags that you might like is
24:54 active.
24:56 We might do
24:59 We've got hold there, inactive.
25:02 Right, archive, something like that,
25:05 okay?
25:06 And so and we can see here, I've got a
25:08 few of these tags were already here
25:09 before, just for my trainings.
25:12 What's great about this is we get to
25:14 just drag and drop the project right on
25:17 top of Cali Kitchens. We get to drag and
25:19 drop this design too right on top of
25:21 Corner Kitchens. That way when I choose
25:24 this tag or filter, it's going to filter
25:27 down to just those things that have that
25:30 tag, okay?
25:32 And so that makes it really easy to
25:33 manage a really long list of projects.
25:37 So, those tags will come with the
25:40 project and if your other team member
25:42 has those tags as well, they'll be able
25:44 to filter just like you filter. So, as a
25:47 team, if you create a system for
25:49 filtering that works across the whole
25:51 team, this will make it really easy for
25:53 you to manage what projects are on hold,
25:56 what projects are inactive, what
25:58 projects for what customer, etc. Just a
26:00 few different ways that you can filter
26:02 down and make it easy to see what's
26:04 going on here.
26:06 A couple of other things to note is
26:07 we've got a few buttons that are unique
26:09 here. Uh I like to drag this toolbar in
26:12 between the folder tags and the projects
26:16 and that just makes more sense to me.
26:18 And so something that I
26:20 I have here is I don't show the default
26:22 categories.
26:23 I don't need to see common documents. I
26:25 don't need to see planning and layout
26:26 templates. I have very few things in
26:28 here.
26:29 That's it. So, I like to uncheck this.
26:32 This guy right here will just show you
26:34 open projects. So, if you're confused
26:36 about where your tabs are coming from,
26:38 you can click on this and it will show
26:40 you just the projects that you have open
26:42 at that time.
26:43 Okay? So, those are a couple important
26:45 ones there.
26:46 And let me take a look at the comments
26:48 here before I keep going.
26:49 See.
26:52 Started using the project management a
26:53 couple months ago. I started so that I
26:55 could create a template project with
26:56 three layout sizes and as-built plan
26:59 file and proposed plan file.
27:01 All of my views are already linked and I
27:03 only need to manually tweak a few things
27:05 for each plan. Perfect. Yeah, that's I
27:08 mean that's exactly what I do here.
27:10 We'll just we'll show you right now. So,
27:12 I'm just going to come in here. I'm
27:14 going to draw a quick building real
27:16 quick.
27:18 Redundant quick building real quick.
27:20 I'm going to draw the same building I
27:21 draw every single time if you've ever
27:23 seen my videos for whatever reason stuck
27:25 on this shape.
27:27 >> [laughter]
27:28 >> And I throw a couple windows there just
27:30 to populate some schedules.
27:33 And a door and why not? Store.
27:36 Going to be a funny little house.
27:44 And so, when I go and open up my layout,
27:49 here we go. As it starts just building
27:51 this out already. I've got some views
27:53 established. I've got some things
27:54 happening. So, my construction document.
27:57 I need to um
27:58 I I choose in my templates
28:01 to not automatically update elevations.
28:04 Especially once you get into a large
28:06 number of wall elevations is that's
28:09 going to take a long time when you make
28:11 some changes. So, I like to
28:14 instead prompt my elevations to be
28:16 updated.
28:18 Um and so, that's what's happening right
28:19 there.
28:20 Go, it's updated. It's showing us our
28:22 building now.
28:24 So, there we go. This is exactly how I
28:26 have my templates. I usually have to
28:28 come in here and do a little build off
28:29 framing if I want my framing views to be
28:32 shown correctly.
28:33 And there we go.
28:37 As simple as that. This is just starting
28:38 to get built out as I go.
28:41 So, that's really a huge part about why
28:44 to use manage mode is that you can have
28:46 these views pre-linked, ready to go, and
28:49 populating schedules for you.
28:53 And views.
28:54 I do want to save. Sure, why not?
29:00 So, let's get back into how do we save
29:03 this to a team? Why is this method
29:05 better for saving to a team?
29:07 And again, this is because we have all
29:10 the established files that a team member
29:12 would need,
29:13 and it's compressed into one file.
29:17 Simple as that. And in case you didn't
29:20 know this, someone that does not have
29:23 managed mode turned on
29:25 can still utilize that single file type.
29:28 They would just double-click that file,
29:31 and Chief Architect would import those
29:32 assets for them, and would give them the
29:35 option to open that plan file and open
29:39 that layout file in the unmanaged mode.
29:42 So, even if you've got some team members
29:44 not utilizing this, it's still a better
29:46 workflow. It's still better for you for
29:49 saving these project files.
29:51 Unfortunately for them, it's not a great
29:53 workflow coming back to you. So, if that
29:56 was that person were to go edit those
29:58 files and try to save it back to you,
30:00 they'd be saving a backup, and then all
30:02 of a sudden you've got a ton of files on
30:04 your machine again. So, it really is
30:05 good if you kind of push the team to all
30:07 utilize this system.
30:10 There is nothing that this system can't
30:12 do that the old ways can do. You can do
30:16 everything that the old ways
30:20 worked. All right? The way we worked in
30:22 X16, saving a plan file, saving a layout
30:24 file, saving the assets,
30:26 everything you could do in the old
30:28 versions, you could do in managed mode.
30:30 It's just a new process. And once you
30:33 learn it, it's actually a much simpler
30:34 process, and it's a much cleaner
30:36 workflow.
30:37 So,
30:38 I would just right-click, export. Now,
30:42 I I've said this before in some of my
30:44 other videos that are produced to kind
30:45 of help people understand what I would
30:47 call a save as because we're all missing
30:49 that term, right? We're all missing that
30:52 workflow is how do I do a save as? That
30:54 makes so much more sense to me. And this
30:57 is the most ridiculous thing to me, but
31:00 the closest thing we have to a save as
31:02 is delete and export. And so I can
31:04 choose this new project. I can hit
31:06 delete. When I hit delete, it's going to
31:09 prompt me to export and delete. And that
31:12 sounds super crazy and super scary to
31:15 hit the delete button. So, yeah, it
31:18 seems odd. And that's what I'm going to
31:20 do. Export and delete. I'll find my
31:23 downloads folder, project. Let me save
31:25 that. Once it's done exporting, it will
31:28 delete that project from here. And then
31:30 just to show you that we do have methods
31:33 for kind of bringing this back together
31:34 if we need to is I'm going to rebuild
31:37 this furniture fixtures fixes file.
31:42 And so we'll let that finish its delete
31:44 process.
31:47 And I'm going to try to take a sip of
31:48 coffee.
31:54 All right.
31:55 So, I'm going to click on file new new
31:57 project and you know, out of the box
32:01 I don't load up any of my templates into
32:04 the new projects from template. I leave
32:06 this the out of the box templates.
32:08 That's because when I'm working, I'm
32:10 going to work from a pre-established
32:12 pinned project that's up here and make a
32:15 copy with links to project to new
32:17 project just like I showed you before.
32:20 So, since I'm utilizing an existing
32:24 project for my templates, I don't need
32:27 to load up
32:29 any of those um my template files into
32:32 the new project from template from
32:34 preferences, okay? And so what's here
32:37 instead is the out of the box
32:39 residential templates. And I utilize
32:42 that every once in a while just to make
32:44 sure that maybe there's a problem I'm
32:47 having with my templates and I want to
32:49 confirm that that problem does or does
32:51 not exist in the out of the box
32:52 templates. So, something to keep in
32:54 mind. If you're migrating from previous
32:57 versions and there still seems to be a
32:59 problem with the
33:02 out of the box templates coming from
33:04 Chief Architect, it might be that you're
33:05 migrating old versions of their out of
33:08 the box templates. If you really want to
33:09 find their true shipped with Chief
33:13 Architect out of the box templates and
33:15 you're on a Windows machine, you'd get
33:17 into program files, you'd get in Chief
33:19 Architect, you'd find your version and
33:22 inside of the templates folder would be
33:25 the templates that are shipped with the
33:27 program, okay? And that's how you could
33:29 do some testing in case you've got some
33:31 system problems.
33:33 All right, so now what I'm going to do
33:35 here is I'm going to rebuild furniture
33:39 fixes, rebuild in the case that I lost
33:42 this project file or it became corrupted
33:45 for some odd reason, right? A lot of um
33:49 stuff that's happening and and being
33:50 corrupted comes from people maybe
33:53 running Chief out of the cloud and not
33:54 in manage mode. What's really brilliant
33:56 about manage mode is that it's not
33:58 running from your documents folder. It's
34:01 running from the program data folder.
34:02 So, out of the box it's not running in
34:05 one drive when your PC ships with one
34:08 drive. So, you don't have that cloud
34:10 problem.
34:11 All right, so furniture fixes rebuild I
34:13 unchecked include plan, I unchecked
34:15 include layout. So, that just builds a
34:18 blank project file.
34:20 And so what am I going to do here? I'm
34:22 going to add a new plan. How am I going
34:23 to find this plan? Well,
34:26 it's not it it wants to look in common
34:28 documents, right? So, that's not a way
34:30 that I can do this. So, instead, I'm
34:33 going to say
34:34 file open plan layout, all right, and
34:37 I'm going to browse for an unmanaged
34:39 plan and layout file.
34:41 And so, what do I want to do? I want to
34:42 find my archives. And in this case, I
34:45 keep my stuff outside of the cloud
34:48 in a folder I call Chief Architect
34:50 non-sync, and find my archives here.
34:54 And so, I could look for that furniture
34:59 fixes. There we go. And so, here's, you
35:02 know, here's an archive file. And we can
35:04 see here, you know, by date, what's
35:06 going to be the most
35:07 uh current date. There we go. Now, when
35:10 I click on this, it prompts me and asks,
35:12 "Do we want to import this into a new
35:13 project or into an existing project or
35:16 do not import at all, just open the dang
35:17 thing?"
35:18 So, I'm going to import into existing
35:20 project. There we go.
35:23 And it picks up that there's some other
35:26 auto save file in that same folder, and
35:29 do you want to include it? And I would
35:31 say, "Go ahead and do yes." Because that
35:34 way, you can double-check that these uh
35:37 which one is the one that's was the most
35:39 current, okay?
35:41 And in this case, I don't think I had a
35:43 layout associated. Oh, it looks like I
35:44 did.
35:46 Um so, I could go try to find that
35:47 layout as well. This is why it's
35:49 important if you're using template plans
35:52 to rename your layout file because
35:57 this is my template name, okay?
36:00 And so, if I'm going to go look through
36:01 the archives to try to find this, it's
36:03 going to be a little bit more difficult
36:05 to find this because I did not rename
36:06 it. So, as you're working, I would
36:09 suggest that you rename this so you can
36:11 find it in archives if you need to.
36:17 Now, let's see. Now, I'm going to show
36:19 you just my naming convention once I get
36:22 things outside of Chief. Um while we're
36:25 doing this, I'm just going to delete
36:26 these two. The reason I keep offlining
36:29 my project files is it's really easy to
36:32 double-click them and install them again
36:33 as you need to.
36:35 But the other part about this is that if
36:37 you have automatic backups turned on,
36:39 which is coming from preferences,
36:43 and then our project management, and we
36:45 have a backup managed resources, and you
36:48 set a schedule, okay?
36:52 What happens here is the more project
36:54 files you have, and we noticed that one
36:56 project file was 190 [clears throat] MB.
36:58 That's the more space it's going to take
37:00 up. That's the longer that the backup is
37:03 going to take to complete. So, if you've
37:07 got like 30 projects in here, you can
37:09 easily take several hours to back up
37:12 those 30 projects, all right? And so,
37:14 that's going to take a long time. That's
37:16 why I export offline these files, get
37:19 them on my Dropbox, so that I can bring
37:21 them up as I need them.
37:24 So, I'm going to just delete these two.
37:26 We're going to have to close this file
37:27 down real quick.
37:30 Delete
37:32 item.
37:33 And then,
37:35 I'm going to come in and I'm just going
37:37 to show you
37:39 a build-out that is for one of my
37:41 clients,
37:42 and just give you an example of how
37:46 we name these things, okay?
37:51 And let's get this guy in kind of a list
37:52 view.
37:53 So, you can see here that my naming
37:56 convention
37:58 is
37:59 year year, month month, day day.
38:03 What version number is it?
38:05 You could add another sub-version, which
38:09 might be design review A, design review
38:11 B. If you've seen my videos in the past,
38:13 you you know this convention. I've been
38:15 using this convention for as long as
38:16 I've been doing this. And this came from
38:19 uh someone that I learned from, and so
38:21 this has been an architectural practice
38:23 for something like uh 60 years or
38:25 something like that. It's this this
38:27 naming convention.
38:28 So, it's year year month month day day
38:31 version number, the project name, and
38:33 the person's initials who saved the
38:35 file.
38:36 Right? This quickly lets me know who the
38:39 last person was that worked on this
38:41 file.
38:42 Okay?
38:43 Now, it just so happens to be I'm the
38:44 only one that's working on these files,
38:46 and you can see that things are
38:48 um
38:49 progressing just by its name itself.
38:52 Notice that the version disappeared
38:53 here. That's because the version
38:54 actually exists inside of the project
38:56 file here. Um so, that's why we're not
38:58 seeing it anymore. But, if I were to
39:00 double click and open it up, it would
39:02 show inside of the project file.
39:04 And so,
39:05 this just keeps a hierarchy. I know when
39:07 I come here, I can quickly and easily go
39:10 to this version and know that that's the
39:13 most current version. Okay?
39:15 The other great thing about this is if
39:17 you print this version number somewhere
39:20 on your PDF,
39:21 and a client comes to you and says,
39:23 "Hey,
39:24 we can no longer afford 260622."
39:28 Or maybe, you know, planning department
39:30 came back and says, "We're not going to
39:31 accept this. You have to do something
39:33 different."
39:34 And, you need to go revert back to some
39:36 previous version. All you have to do is
39:38 go, "Hey, mis-
39:40 uh client, what is the printed name on
39:43 your PDF that you're referring to that
39:45 you would like to revert back to?"
39:47 Instead of them trying to describe it,
39:49 they could just say, "Hey, it's uh we
39:51 want to revert back to 260526."
39:54 And so, it's really easy for me to come
39:55 in here,
39:56 open that up and work from there again,
39:58 and start a new iteration, and progress
40:00 that date. So, this is a very, very
40:03 simple way to teach a team
40:07 how to utilize this naming convention.
40:09 It doesn't take that long. It takes, I
40:11 don't know, in my experience, 2 to 3
40:12 weeks for people to get used to this
40:14 naming convention.
40:16 Once they've got it down, then it just
40:18 becomes really clear what you're going
40:19 to be working on. And then when you've
40:21 got enough project files, you can
40:25 come in here, create an archive folder,
40:27 take your previous iterations,
40:30 drop them in that archive,
40:32 just like that, okay? And if you want to
40:35 get really clever, you don't want this
40:37 taking up space on your hard drive, you
40:39 can right click on this and every cloud
40:42 service has some version of make online
40:45 only, okay?
40:48 And so that means that file um this
40:50 folder and all of its sub files are no
40:53 longer um being stored on my machine,
40:56 they're being stored on the cloud only,
40:59 all right?
41:01 >> [clears throat]
41:03 >> Let me see what we got going on in the
41:05 comments here.
41:13 I get a Townsend in 30 by 42
41:17 and 36 by 48 along with Arch D
41:20 and
41:22 and D. What's that last and and D? Anth-
41:25 Anthony. [laughter]
41:27 Let me know what that's about. Um
41:29 the way that I do my templates, I'll
41:31 just show you
41:33 I'll show you this real quick.
41:35 Why not? We got a question about my
41:37 templates, I'll show you my templates
41:38 real quick. So,
41:41 we've got layout, we're talking about
41:42 Townsend, they like this one. Uh
41:44 Townsend is one of my favorites, too.
41:46 Make a copy with links to the new
41:48 project.
41:50 Okay.
41:53 And so this is what I have to do to make
41:55 all these different sheet sizes. This is
41:57 a little bit of work. There's a few
41:59 things I like to do to make things
42:00 easier. So, we're going to get off of
42:02 manage mode just for a second. We're
42:03 going to do this little side side quest,
42:06 okay?
42:07 Is that if I wanted to do a 30 by 42,
42:11 what is that? 30 by 42.
42:14 Um so, first off,
42:16 a win there is a glitch in Chief
42:18 Architect if you're using multiple
42:21 template pages.
42:23 Okay?
42:24 You might not even know that we could do
42:26 multiple template pages in Chief
42:29 Architect. What does that even mean? If
42:32 I were to go, notice that my G1, which
42:34 is my very first sheet, starts on page
42:37 three.
42:38 Okay?
42:39 And so, why is it start on page three?
42:42 Well, page
42:43 two, one, and zero are all template
42:45 pages.
42:46 What I want you to notice about these
42:48 template pages is as as I scroll through
42:50 here is, look, no no graphic scale,
42:55 graphic scale, different graphic scale.
42:58 All right? So, I have different template
43:00 pages for different scales. Notice this
43:03 says scale per view, scale 1/4 in = 1
43:05 ft, scale 1/2 in = 1 ft. All right? Why
43:08 do I do that? I already have certain
43:10 pages that I know are going to be no
43:13 scale, and as I go through, I have
43:16 certain pages that I know are going to
43:17 be 1/4 in = 1 ft. All right?
43:22 And so, as I keep going through this,
43:26 there's going to be other pages
43:29 Oops, can't
43:31 get through any more that are 1/2 in.
43:33 And so, I want that graph scale to just
43:35 be there. All I'm doing then is in the
43:37 page information is I'm changing the
43:39 page template that I'm using. So, on the
43:41 fly, I could just say, "Hey, give me my
43:43 1/4 in graphic scale on this page and
43:45 that annotation." And that will change
43:47 this out. So, that's the reason that I
43:49 have multiple template pages.
43:51 Now, I opened up the wrong file here. I
43:53 needed to be in the new project file.
43:56 But, I'll show you how I can go change
43:59 and create a sheet size and some of the
44:00 nice things that I like to do in this
44:03 setup is
44:05 I'm going to start by drawing a big s-
44:09 a polyline the size of this sheet, all
44:12 right? And I'm going to cut that and
44:15 just bring this back to
44:17 Should have just done it on this page
44:19 zero. The next thing that I'm going to
44:21 do is I'm going to get in the file menu
44:23 and I'm going to change the drawing
44:25 sheet setup. So, for this
44:28 what were we asking for? What's that? 30
44:30 by 42 Arch E1. Okay. So, Arch E1, let me
44:34 press okay. And we see what happens to
44:36 the sheet size, right? Now, here's my
44:39 polyline.
44:40 Now, I want to note a couple things.
44:43 Some of these are polylines and some of
44:45 these are remnant sheet sizes from the
44:49 other template pages. It's very strange,
44:53 but if I click on this
44:56 let's just see if I can get this to work
44:58 right.
45:00 is
45:03 Um you know what? I drew that polyline
45:05 at the wrong time. I need to draw the
45:06 polyline now
45:08 to maintain that size. So, that when I
45:10 stretch this out
45:12 right click and stretch this to this
45:14 corner and this corner, that's the other
45:16 polyline. So, I can delete that.
45:18 One of these is the template page.
45:21 When I move it, it will glitch out. Let
45:24 me keep doing this until we see that
45:26 problem. There we go. See what happened
45:28 there?
45:29 Really strange. So, you have to have
45:31 that polyline to be able to snap to it
45:32 because this will happen. We effectively
45:37 changed the template sheet size of the
45:39 one of the other template pages. So,
45:41 it's a little glitch in chief. It hasn't
45:43 been fixed yet.
45:44 Do it one more time and there it is.
45:46 There's that glitch again.
45:48 But there we go. Finally changed all
45:50 those sheet sizes.
45:52 And I end up taking all my title block
45:54 information, sliding this over, getting
45:56 this in the right place. And then what
45:57 you'll notice here is I've got a few
45:59 things in here that are um callouts
46:03 those callouts have lines. The reason
46:05 that I do this, and I'll show you why
46:08 just now,
46:09 is that I want to make sure that I've
46:11 got all of my information lined up in
46:15 the same space on every page, okay?
46:18 So, what I'm going to do here is
46:22 let me first
46:26 I'm going to do a little place point.
46:28 I'll go to the next page. I'm going to
46:30 slide this into that place point.
46:33 Here we go, just like that. Now, we know
46:35 that's in the same exact spot,
46:37 right?
46:40 There we go.
46:41 Now, when I scroll through here, notice
46:43 that I can get this keynote schedule
46:45 slid over a little bit,
46:48 right?
46:49 Because of that, that's where I want to
46:50 center line all my keynotes across all
46:52 pages. So, I'll draw a little line, I'll
46:54 cut that line, I'll come back to my
46:56 template pages, I'll paste hold that
46:59 line, and I'll center this callout on
47:02 it, slide this up.
47:04 And then I can get rid of this line.
47:05 What does that do for me?
47:07 As I go through my pages, it's easy for
47:10 me to take these elements that
47:12 were over here, and then utilize that
47:15 callout. So, I need to come back to that
47:16 template page, grab this callout, copy
47:18 paste, get rid of this one, paste hold
47:21 position,
47:23 come forward a page, get rid of this
47:24 one, paste hold position. Now, when I
47:27 come in here and try to line these
47:28 things up, it's easy for me to just take
47:30 these and use the centering tool and
47:32 center those up on that. So, this just
47:35 keeps everything very uniform across
47:37 these sheets, right?
47:39 Really nice way of lining things.
47:42 So, I utilize these in a number of
47:43 different ways to just be able to snap
47:45 to them. So, like we could take this
47:48 right here and snap it to this and know
47:50 that it's going to be snapped in the
47:51 same place on every page. So, this would
47:54 be how I'd build out one of these.
47:56 Um, I'm not going to finish this, so
47:59 not at this time.
48:01 I just wanted to show you a couple
48:02 things on how I create different sheet
48:03 sizes and how I organize them and
48:06 keep them going like that.
48:09 All right, we got another 12 minutes. We
48:10 have any more questions about the
48:12 project browser and how to use it, how
48:14 to utilize these tags, how to organize
48:17 your folders, how to create some
48:19 pre-linked stuff.
48:20 Um, the pre-linking is very challenging.
48:23 I'll show you a couple tricks for that.
48:25 When I want to create some new features
48:27 in my template plan, um,
48:30 the way I do this is I almost never draw
48:34 an enclosed room in my template plan
48:37 file. Why? Because Chief Architect does
48:40 have some kind of a memory for rooms.
48:43 I've never been able to describe exactly
48:45 how that works. So, I will not draw
48:48 walls in here. So, what I do instead is
48:51 you can open up your template plan file
48:53 and you can draw some things, just so
48:55 that you can establish some things.
48:59 Maybe it's that you want to save a wall
49:01 elevation in your template plan file.
49:03 Okay. So, I double-click that.
49:06 There we go. I'm going to do this.
49:09 Okay, so now I've got a wall elevation.
49:11 Now, what I'm going to do is
49:13 I'm going to make a copy of this.
49:17 All right? So, I'm going to make a copy.
49:20 Bam.
49:21 Etcetera. And then, I'm going to close
49:23 this down.
49:25 And don't save it.
49:27 When I open up my template plan, it's
49:28 still blank. When I open up the copy, it
49:31 is not blank.
49:33 Okay? Now, if I had saved that wall
49:35 elevation, which would have been a good
49:37 idea,
49:38 let's just save it real quick so we have
49:40 it.
49:41 What I could do is I might be able to
49:43 copy paste this back into the template
49:45 plan. Well,
49:47 it's not going to let us do that. It's
49:48 going to create a typical elevation, so
49:50 that if we open this up, we're going to
49:52 see that it's um not actually set to
49:54 clip to room. So, just keep that in
49:56 mind. But, I was able to bring that
50:00 elevation into this
50:02 plan and and utilize it that way.
50:04 All right?
50:09 So, you can always make a copy if if
50:12 you've made some changes in the um in
50:14 the layer sets here
50:17 because you've been testing it with
50:19 project file you can always import that
50:22 by opening up your template plan,
50:24 getting into the file menu, import, and
50:26 then import those settings from plan
50:28 layout and target that copied file that
50:31 you've been working on and adjusting
50:32 layer sets for.
50:34 You just have to be really diligent
50:36 about what you're copying and make sure
50:38 you're not bringing any in anything that
50:40 will then influence the way that that
50:42 plan file works because you've drawn,
50:45 you know, rooms or you turned off auto
50:47 build roofs or something like that.
50:50 Another difficult thing about creating
50:52 template plans is just understanding um
50:55 some of the settings, especially in like
50:57 dimensions where
50:59 you know, my dimensions are set to auto
51:01 refresh and they utilize a dimension set
51:04 that's set up for remodels. So, if I
51:06 want to set this up instead for new
51:08 construction, I have to come into this
51:10 remodel and turn off auto refresh just
51:13 so that I can switch to
51:16 maybe my new construction dimension
51:19 default and then come into this and come
51:22 into set up automatic and turn on auto
51:24 refresh.
51:26 So, that when I start drawing here, this
51:28 is going to be my new construction
51:32 dimension defaults.
51:35 Okay?
51:38 Now, I mentioned at the very beginning
51:41 of the show that
51:42 um Chief Architect in managed mode
51:46 caches your files, all right?
51:49 And what that means is somewhere on your
51:52 machine, let me see if I can grab this
51:54 real quick. I'm going to see if I
51:55 There's a program called TreeSize
51:58 um free.
52:01 And so, I'm going to turn on TreeSize
52:03 Free and
52:05 um this allows me to scan my hard
52:08 drives. And so, I want to scan my temp
52:10 directory in this case. And what we're
52:12 going to see here is that there in fact
52:15 is a Chief Architect temp directory
52:18 here. And what is this? If we load this
52:21 up, it's 1.6 GB. Now, at times, this
52:24 file is quite a bit larger than this,
52:27 all right? What this is is this is Chief
52:29 Architect caching your files so that the
52:32 software loads a little bit faster. So,
52:35 there's a temporary directory that will
52:36 always be overwritten over time if those
52:39 files change, okay?
52:42 So, if we were to go open up this temp
52:44 directory, we can see in here that it's
52:47 pre-caching my user library. It's
52:50 loading up my user library beforehand.
52:52 And my user library is um
52:55 you know, in a compressed state is
52:57 4 GB. I mean, that's just my library.
53:00 That it does not include the assets
53:03 associated with that library.
53:05 So, it's caching a pretty large file
53:08 type in this case, and then it's zipping
53:10 it on top of that. And so, what's
53:12 happening when Chief Architect loads?
53:13 It's unzipping that file and then
53:15 loading up my user library.
53:17 The other thing that's happening here,
53:18 if we were to go select a different
53:20 directory and see if I could find this
53:21 on the fly
53:22 in a short amount of time here, is that
53:26 um let's see, program data,
53:28 Chief Architect,
53:31 let's see if we find X17.
53:34 Seems to be very small.
53:37 Smaller than I expected. This is because
53:40 I haven't downloaded many of the
53:41 libraries. I don't have many of the
53:43 manufacturer libraries. That's all to
53:44 keep my backup really, really small. is
53:48 if you're someone that's downloading all
53:50 the catalogs
53:52 and you're in manage mode, please note
53:54 that will, again, slow down your backup.
53:58 Um
54:01 So,
54:03 So, that's in
54:05 program data on
54:09 on a Windows machine,
54:11 app data,
54:14 which should just be in the C drive.
54:18 See, where does app data live?
54:21 Yeah, here we go.
54:23 Under my name and I think it's going to
54:25 be
54:27 in local,
54:29 Chief Architect X17 data.
54:32 This is where all those encrypted files
54:34 live.
54:36 So, we've got a ton of files in here.
54:38 Something in here is 1.6 GB. Yeah, it's
54:41 very large.
54:43 This is going to be all those encrypted
54:44 files from Chief Architect.
54:47 So,
54:48 that's just to let you know these things
54:50 take up space. Another thing to note is
54:53 if you're someone that does training,
54:54 like I do,
54:56 and I'm opening up other people's files,
54:59 or if we're just um
55:02 we do a large volume of files across the
55:04 team, every time you bring in a project,
55:08 it's bringing in all those assets that
55:10 you don't have. Those assets live in
55:13 asset management, okay?
55:16 And so, if I were to change all assets
55:18 to assets owned by me, this is the list
55:21 of all images that have been imported
55:23 into my machine. Now, I have a very
55:26 large library, but also many of these
55:28 items are from projects that are no
55:30 longer active and I'm no longer working
55:33 on and aren't part of something that's
55:35 in my library, and so they're just files
55:38 that got imported at some time.
55:40 There is no current method coming from
55:43 Chief Architect to be able to purge
55:46 those assets that you're no longer
55:48 utilizing because those projects have
55:50 been offlined.
55:51 So, what's difficult about this is being
55:53 able to choose files that you no longer
55:55 want to have in here and get rid of
55:57 them.
55:58 And so, you could try to take, you know,
56:00 some image like this and click on delete
56:03 and see what happens, and you're going
56:04 to see this. Unable to delete because
56:06 it's still referenced by the following
56:08 resources. It's in the user library,
56:10 okay? So, it's not going to let me
56:11 delete that.
56:12 Now, if I were to just group select a
56:14 bunch of things and try to delete it
56:16 that way, it's not going to let us
56:18 delete everything.
56:20 Let me go try to get into some part of
56:22 this library that might have some stuff
56:24 that I don't um
56:26 don't have anymore.
56:29 Just
56:33 get out of the rabs section.
56:35 So, we've got some unnamed files. So, if
56:37 I were to like shift select these items
56:40 and then
56:41 hit delete, what's going to happen?
56:45 We see the number of items here.
56:48 All right, I could have screenshot this
56:49 just to get an idea.
56:52 And it's going to say, "Hey, we're
56:53 unable to delete this one because it's
56:55 still referenced." And press okay.
56:57 And so, did anything happen at all? No.
57:00 Because it came up with an error, it
57:02 didn't delete anything.
57:04 Which is unfortunate because how do you
57:06 discover which things are in your
57:08 libraries, which things are in a
57:11 project. Unfortunately, there's no real
57:14 way to do it.
57:15 The sad part about this is if you really
57:17 want to purge this, which I would
57:18 encourage you to do, you know, maybe a
57:20 couple times a year. This is the one
57:22 real big drawback to me about the manage
57:24 mode
57:25 is that I'm going to end up exporting my
57:28 library, right clicking, exporting my
57:30 library. Once I've done that, I'm going
57:32 to export all my project files.
57:34 What am I going to do after that? I'm
57:35 going to delete both library project
57:37 files.
57:38 Then I'm going to come into the asset
57:39 manager, select everything here, delete
57:42 everything.
57:43 Then I'll re-import my library and I'll
57:46 re-import my projects. How long is that
57:48 going to take me? Couple hours.
57:50 It'll take me a couple hours, but it
57:52 will purge all of my unused materials.
57:55 It will speed up my program load times.
57:58 It'll speed up my backups.
58:00 Okay? So, it's worth it to me to do
58:02 that, but it's a pain in the butt. So,
58:04 if you'd like to put this in as a
58:06 suggestion to Chief Architect, I'd
58:08 really appreciate it if you did that
58:09 because it's going to help us all out.
58:11 Just give us a little purge button would
58:12 be really, really awesome.
58:16 All right, taking a look at the comments
58:17 here.
58:20 You guys are pretty quiet today. You
58:22 might You maybe you know all this stuff
58:24 already. That's good.
58:28 Think I've covered everything that I'd
58:30 want to cover in the management. Let's
58:32 take a look at these.
58:34 Plan references. Um plan references are
58:37 going to show you um anytime that you
58:39 might have
58:40 a link to another plan. So, one plan
58:43 inside of another. Um in case you didn't
58:46 know how that works, we'll just I'll
58:48 I'll show you that real quick cuz I'm
58:49 going to open up this.
58:53 Okay, I'm going to draw a little house.
58:59 This is going to be my as-built. All
59:01 right? So, let's just say I've finished
59:02 drawing this. Notice that I drew it in
59:04 my
59:05 -n file, which is proposed for me.
59:08 Now, I'm finished with my as-built.
59:10 That's done.
59:11 I'm going to right click on my as-built
59:13 file, which is already sent to layout,
59:16 and I'm going to utilize this replace
59:18 with.
59:19 All right? This maintains the links that
59:21 are in layout already. In fact, it even
59:22 tells me, "Hey, this is linked to
59:24 layout. You sure you you to do that? You
59:25 sure you want to replace it? Yes, I do.
59:27 I want to replace it with my open file
59:29 right now.
59:31 Floor plan - N. I'm going to hit select.
59:33 It's saying, "Do you want to delete that
59:35 source file?" No, I do not. I want to
59:37 keep it. Okay?
59:39 That just injected the as-built into
59:41 this.
59:42 Now, what I could do in the as-built
59:44 file
59:48 Here's our as-built file, right? Here's
59:50 our new. Let's just say instead we've
59:52 got some kind of an addition here.
59:57 And let's just say instead that I'm
59:59 going to remove this wall for whatever
1:00:01 reason. It's a really strange addition,
1:00:04 okay?
1:00:05 What I get to do is I can just turn on a
1:00:07 reference
1:00:09 and I can go choose my as-built.
1:00:13 And I'm going to change my layer set to
1:00:15 one that I created called existing floor
1:00:17 plan, and I'm going to move this down.
1:00:19 Okay?
1:00:20 What that's showing is the as-built
1:00:23 underlaid.
1:00:25 And so we could see my demo walls in
1:00:27 this case.
1:00:28 So, what happens when we save this and
1:00:30 close it
1:00:31 and save it and close it
1:00:33 is that if we right-click on this
1:00:38 we should have seen reference. How did I
1:00:40 see that before? Plan references. Plan
1:00:43 references. Guess we have to open it.
1:00:45 See.
1:00:46 See if this works. There we go. Plan
1:00:48 references.
1:00:49 And we can see here there's that
1:00:50 as-built. And we can replace it with
1:00:52 something else.
1:00:53 Okay?
1:00:54 >> [snorts]
1:00:54 >> How do we replace it with something
1:00:55 else? We could easily make a copy of
1:00:57 this guy. Make a copy.
1:01:00 Name it whatever you want.
1:01:04 Plan references.
1:01:06 Replace that reference. Replace it with
1:01:08 that goofy name.
1:01:11 There we go. Now it's linked to some
1:01:13 other file.
1:01:15 So, a lot of really cool tips and tricks
1:01:17 you can get out of just messing around
1:01:19 with some of the stuff in here.
1:01:21 You can export a plan by itself and make
1:01:23 it disconnected.
1:01:25 Yeah.
1:01:29 Placement is something I've never seen
1:01:31 or used. Yeah, absolutely.
1:01:34 Um that makes it I actually just had to
1:01:37 repair someone's project files and
1:01:40 I utilized all those tools to repair it.
1:01:43 What they had done is they had used to
1:01:44 make a copy, but they didn't use make a
1:01:46 copy with links. So, it broke all their
1:01:49 links just like we used to break all the
1:01:50 links in X16, right? And so, I had to go
1:01:54 in there,
1:01:55 trade some things out, change some
1:01:58 references, rebuild it, build it into
1:02:00 two folders. They had two design
1:02:02 iterations and just show them how to put
1:02:03 it all back together.
1:02:05 Um
1:02:06 a really organized setup here. Um just
1:02:09 makes a huge difference in in just
1:02:12 utilizing the correct tools from from
1:02:14 making design iterations. Makes a huge
1:02:16 difference. The other thing that I would
1:02:18 say is when you make a new design
1:02:20 iteration, take the time to go in here
1:02:23 and do with new thumbnail because uh for
1:02:26 instance, we could just open the sub
1:02:28 real quick
1:02:30 and I'll show you. We're just a little
1:02:31 bit over time, but you can open this up
1:02:33 real quick and I can get to something
1:02:35 that's going to be recognizable like
1:02:36 this shot right here.
1:02:38 Okay? And then I can get into the file
1:02:40 menu and choose save thumbnail image and
1:02:44 then save this file, close it out.
1:02:48 Um across all Windows machines, control
1:02:51 W is close your current tab. Control
1:02:54 shift W would be close all tabs. So,
1:02:56 that's what I have my hotkey set up for
1:02:58 there.
1:02:59 And so, now when I go and click on this,
1:03:01 notice that the preview down here at the
1:03:03 bottom is that thumbnail image that I
1:03:06 just saved. So, this will make a big
1:03:08 difference for me when I have a design
1:03:10 one, design two and I'm trying to share
1:03:11 it to a team is go ahead and take a
1:03:14 screenshot of that um not a screenshot,
1:03:16 but save the thumbnail image of that
1:03:18 kitchen. Save the thumbnail image of the
1:03:20 exterior so that your other person can
1:03:23 come in here and understand which one's
1:03:25 which very easily just from a visual
1:03:26 standpoint. You can see here I obviously
1:03:29 did some stuff where, you know, my
1:03:31 thumbnail image is just
1:03:33 I put my branding.
1:03:35 Oh, my face is covering this.
1:03:38 How about that? There we go. Is there is
1:03:40 this saved thumbnail image.
1:03:50 All right.
1:03:51 That's it for today. I hope you got some
1:03:53 good stuff out of this. Um,
1:03:55 and I really
1:03:56 really hope people start utilizing this
1:03:58 project management. I know it's a
1:04:00 frustrating thing to learn at first, but
1:04:03 when you get it going and you get a
1:04:04 system together, it really works quite
1:04:07 well. Um, you know that I'm going to go
1:04:10 uh delete those new projects to get them
1:04:12 out of there so that my backup files
1:04:15 um, don't have any issues. Just to show
1:04:17 you the backups.
1:04:19 And then we're going to end the show is
1:04:21 that
1:04:22 I've got a location here somewhere.
1:04:24 Project backups. There we go. We've got
1:04:26 a bunch of backups in here. I think the
1:04:28 last one maybe didn't finish. You can
1:04:30 see here over time that I've purged some
1:04:32 things. They can use backups much
1:04:35 smaller. These used to be 25 GB. Now
1:04:38 they're 12 GB. You open up this and it's
1:04:41 a zip archive. Assets are going to be
1:04:43 all your image assets, PDFs. Database
1:04:46 libraries are going to be
1:04:47 user catalog. Uh, projects are anything
1:04:49 that's in projects. Settings are coming
1:04:51 from preferences, etc.
1:04:54 Um, so all this stuff is inside your
1:04:56 backups. It's not going to be project
1:04:58 files. So, keep that in mind. You can
1:05:01 see the last backup I did had a bunch of
1:05:03 project files in here.
1:05:05 Um, if you've got a bunch of things in
1:05:07 common documents and you're not
1:05:08 utilizing them, get rid of them cuz it
1:05:10 also slows down
1:05:12 what you've got going on here and then
1:05:14 we can see in here here is the build out
1:05:16 of the project file. So you could
1:05:18 recreate it from this backup if you
1:05:20 needed to just by extracting these
1:05:22 things and rebuilding a project. But the
1:05:25 other thing that you could do always
1:05:27 from those is just go into the file
1:05:28 menu, backup and restore, and restore
1:05:31 from backup, all right?
1:05:33 And so if you're someone where your
1:05:35 backup is taking, you know, more than 30
1:05:37 minutes of time, go rewatch this and
1:05:39 you'll see some tips and tricks about
1:05:40 reducing that time.
1:05:43 And thank you as always for joining me
1:05:45 on this. I appreciate it and see you
1:05:48 next Tuesday.
