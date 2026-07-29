---
videoId: uwN0QHEy8yY
title: Template Tuesdays - Toolbar Tricks You Didnt Know In Chief Architect X18
url: "https://youtube.com/live/uwN0QHEy8yY?feature=share"
status: imported
---

# Transcript

0:01 template Tuesday action here.
0:06 I think I'm live.
0:09 That should just be That should just be
0:11 the thing I do is say I think I'm live
0:13 every live show.
0:17 Uh I I finally did it. I finally did it.
0:22 I went through being a really rough kid
0:25 all my life
0:28 without breaking a bone.
0:30 And then yesterday
0:31 I broke a bone.
0:33 I broke a bone and it reminded me that
0:35 life is short.
0:37 Broke my little I broke a little toe.
0:41 And that I shouldn't take all my tricks
0:42 with me. So here we are. We're going to
0:44 talk about tricks about toolbar hacking.
0:48 And
0:49 it's a video I've put off because, you
0:51 know, I don't want to
0:53 I don't want you know, the Chief
0:54 Architect um
0:57 samurais in the middle of the night to
0:58 come take off my head and or force me to
1:00 do seppuku.
1:03 And uh
1:05 and I'm very respectful of them usually
1:07 and uh because they're great folk. But
1:10 I've uh
1:11 I've had to come up with a workflow for
1:13 toolbars
1:14 that
1:15 you know, kind of circumvents the EULA,
1:18 I'm sure. And uh
1:21 And I take it upon myself and I will
1:23 never ever ever call them for tech
1:25 support for this because I know that
1:26 I'm, you know, intentionally
1:29 non-intentionally potentially breaking
1:31 the software when I mess around with
1:33 stuff in Chief Architect outside of
1:36 Chief Architect, you know, running on my
1:38 machine, you know, messing with some of
1:40 the core files. So
1:44 here we are. This is I'm going to show
1:46 you how to mess around with some of the
1:47 core files. And uh and if this if feed
1:51 self
1:51 explodes, you'll know
1:53 you'll know who to call.
1:56 And uh
1:58 so I want to preface by saying this, you
2:00 can break your software.
2:02 Maybe think about that before you embark
2:05 on what I'm going to do in this video.
2:07 But
2:08 um
2:09 it's pretty easy to correct. And so the
2:11 other thing that I would say is please,
2:13 please, please, please, please, if
2:15 you're going to do what I'm showing you
2:16 how to do here, don't call call Chief,
2:19 you know, call me. I don't want you to
2:21 call me, but I'd rather you call me than
2:23 you call them.
2:24 Um
2:26 And and so what I would say right off
2:28 the bat is before you start messing with
2:30 this, just make a backup.
2:33 It's as simple as that. You can make a
2:34 backup, you can restore from that
2:36 backup, and it's going to save all our
2:38 hides, and no one's going to have any
2:40 problems.
2:42 That's what I would say.
2:43 Uh because we're messing around with um
2:46 some config files for Chief Architect in
2:49 order to do a couple of really
2:52 kind of necessary things in some cases.
2:56 So what I'm talking about specifically
2:58 is that
3:00 for myself anyways, if I make a toolbar
3:02 configuration, and it has a specific
3:05 toolbar that I've spent time building
3:07 out, and I need to transfer it to
3:10 another toolbar,
3:12 there's no way to do that.
3:14 Especially now in project management
3:17 mode. Before you could do a little bit
3:18 of
3:19 hacky trick, and it would be easily
3:21 accessible. Nowadays, it's it's really
3:23 difficult to even get to, and and how do
3:25 you get to it? So, that's something
3:27 we're going to touch on.
3:28 Before I get too far into this feed, and
3:31 and I'll say good morning in just a
3:32 second, is that I would say if you do if
3:35 this is something that feels necessary
3:38 to you, then I would say go download a
3:41 couple programs that are free programs.
3:43 One of them is Notepad
3:46 plus plus. It's the plus plus symbol.
3:49 It's actually a great uh notepad editor
3:52 where
3:54 something that I I love about it in
3:56 particular is that if you change the
3:59 language settings here, they have all
4:01 the typical scripting languages, and so
4:04 it will color code things for you and
4:06 block things for you and make expandable
4:08 sections based on
4:11 that language's parameters. So, it's a
4:13 great utility for checking and testing
4:16 coding language. And And so, as we're
4:17 getting into these
4:20 in the the dawn of AI vibe coding where
4:24 you're using AI to do something that you
4:26 didn't otherwise know how to do with
4:28 coding languages,
4:30 then an editor like this is really
4:32 potentially going to help you learn,
4:33 okay? So, um this is a really great one
4:36 to have. So, notepad and then the plus
4:38 sign twice, okay? Notepad++.
4:42 The other utility I'm going to use for
4:43 this, which
4:45 is it
4:47 works great for the purpose that I need
4:49 it for today, but it also works great
4:52 for a a great number of other things.
4:55 Uh it's called TreeSize. TreeSize, okay?
4:59 TreeSize
5:01 free I'm going to use the free version
5:02 of this.
5:04 There's a paid version that I don't use.
5:07 And this allows you to scan directories.
5:10 And what's brilliant about this is it's
5:13 great for setting up and and freeing up
5:16 some space that might be on your hard
5:18 drive. I'm actually going to run this as
5:19 a in an administrator. So, I'm going to
5:22 look up that again. Uh
5:24 TreeSize free administrator. It's going
5:27 to ask
5:29 It just asked me my permissions.
5:32 And so, I can start scanning the my
5:34 Windows C drive.
5:38 And so, you can see here
5:41 it's quickly letting us know
5:43 And this is an active scan currently.
5:47 It's
5:47 it's us know what drives are storing all
5:51 all my data and where there might be
5:53 data here that hey, I could go look
5:55 through here and see what's going on
5:57 here and and see that maybe some of this
6:00 data is not data that I need. And so
6:03 this is a way that you can clear up some
6:05 space for yourself.
6:07 Um
6:08 maybe you follow around some of my posts
6:10 about optimizing Chief Architect on a
6:12 Windows PC where I discovered that
6:15 creating a raid
6:17 uh
6:18 raid zero configuration with my hard
6:20 drives was very very beneficial to
6:22 operating in Chief Architect and
6:25 and dropping down back uh
6:28 backup speeds.
6:30 All right, and trying to get it closer
6:31 to
6:32 uh what some of the Mac chips are doing
6:35 right now. Mac M5, Mac M4 where they do
6:38 much faster
6:40 um incremental rights, you know,
6:43 thousands of little write files, which
6:45 is what Chief Architect does. And yeah,
6:48 right now Mac does it faster.
6:51 And uh and so it's trying to get to that
6:53 speed. And so I was using this utility
6:55 to kind of discover where
6:58 uh some hard drive space was so that I
6:59 could recover it before I backed up my
7:02 hard drives so that I didn't need to go
7:04 buy a much bigger hard drive to back up
7:06 my hard drive in order to restore my
7:08 hard drive to a raid configuration. So
7:11 it's a great utility. I was just on a
7:12 training call the other day where um the
7:15 end user needed to free up some space,
7:17 put this on their machine, they were
7:18 able to find where they could free up
7:20 some space pretty quickly. So
7:22 uh this is a great utility. And and
7:23 we're going to use this today.
7:27 And so if you want to, go download those
7:30 those programs right now.
7:32 Do them on your side screen.
7:34 And then good morning, Victor. Good
7:36 morning, Mr. Pittman.
7:38 Anthony Reed. We got the The Anthony in
7:40 here, too? Not yet.
7:42 Aaron Rose over there in
7:44 Oh, Aaron, you're not in Monterey or did
7:46 you go back to Monterey?
7:48 Uh were you in Florida?
7:50 And then
7:52 Diane, how's it going?
7:54 Are you Diane, are you going to Chief
7:56 this year? In Coeur d'Alene?
7:59 And Mr. Cody Starr.
8:01 Um if if no one ever knew it, Cody is um
8:04 new to my admin team. He's been in in it
8:06 for actually several quite a few months
8:08 now, I think. Um for all the Facebook
8:10 groups.
8:12 Doing doing that tough dirty work for
8:14 me, helping me out on those.
8:17 And then Mr. Merlin Phillips.
8:20 My favorite.
8:21 And Tigger, I don't know that name. Have
8:24 you ever seen the error maximum number
8:26 of custom library buttons reached? Yeah,
8:29 stop making so many.
8:30 Uh I did a big lobby push. I think some
8:33 of you know this that every year I I
8:35 pick a handful of things that I'm going
8:37 to spend all my money and effort and
8:40 time going to go pressure Chief
8:42 Architect about
8:44 updating. That was one of them is I got
8:46 them to update from 200 custom library
8:48 objects to 400 custom library objects.
8:51 But that is the max, they told me. That
8:53 is no more. They said you get no more.
8:56 So,
8:57 if you're at 400, you might think about
8:59 limiting that down um cuz that's your
9:02 cap.
9:05 And
9:06 400 is a lot.
9:08 So,
9:09 choose wisely.
9:11 And uh yeah, I think I'm about at like
9:15 I think I'm at like three
9:16 300 or so.
9:20 Cool. Back in Carmel. Beautiful. Working
9:23 at Yosemite on a workcation. Very nice.
9:27 Very nice. So, the other thing that I
9:29 wanted to cover today was I'm going to
9:32 create a custom tool that is going to go
9:34 on a toolbar that then needs to go on my
9:37 other toolbars. So, that's kind of the
9:39 point. So, the custom tool
9:41 here is is also that is also a toolbar
9:44 tips you might not know.
9:46 And so, I'm going to do that. So, we've
9:48 got Chief Architect here. Let me get
9:50 this thing fired up. Um I oftentimes
9:53 just want to
9:54 make a copy of my template plan so I can
9:57 start working and testing a tool. So,
10:00 we'll open this up.
10:02 And you can see that this is just one of
10:04 my configurations.
10:07 I'd I'd love to show you right off the
10:09 bat that you can pin configurations,
10:13 other configurations as a tool to click
10:16 on
10:17 in your configurations. So, what you'll
10:19 see here is up at the top of the screen.
10:21 These are other configurations that I
10:23 have. And this is a built-in feature of
10:25 Chief Architect. So, you can
10:27 um click on these just on the fly and
10:30 it's going to change the active
10:31 configuration to whatever you need. All
10:33 right?
10:35 And so, I had a user request
10:38 coming from my Discord server.
10:40 And my Discord server serves as a
10:42 community technical support uh
10:45 area. And
10:48 and in there
10:50 there's a suggestions channel. And I try
10:52 to clear that suggestions channel out.
10:54 In fact, if you have my product and you
10:56 have a suggestion
10:57 I do in fact
10:59 go through those suggestions and work on
11:02 getting those in the software.
11:03 Um
11:05 in my pro plan template, which you know,
11:07 big part about this show is me
11:08 showcasing some of the products that I
11:10 have. I sell a template that comes with
11:12 these toolbar configurations that come
11:14 with the tools that they're linked to.
11:17 And so
11:18 um
11:19 in my template, there's a help and
11:21 information section.
11:24 And when we click on this
11:26 double click on these, it takes you to
11:28 these areas, okay? Um I just released an
11:31 update that updated the current PDF
11:33 manual. So, I could double-click that
11:35 and it just pops this up on the screen
11:38 so that you can go through and and
11:40 understand some of the more complex
11:42 systems that are in my
11:44 ProPlan template and how they work and
11:46 how to modify them and how to use them.
11:49 So,
11:50 um, something that's else is in there is
11:54 my Discord server,
11:56 which looks like this.
11:58 Uh, where you'll see uh, some of the
12:00 people that are on the chat right now,
12:02 um, just talking, asking questions of
12:04 each other. They're a great community of
12:07 experienced people that know what
12:08 they're doing in this business. It's
12:10 really fun to go see what they're
12:11 talking about cuz I learn things from
12:13 them. And then I go clear the
12:15 suggestions. So, something that was in
12:17 the suggestions was, "Hey,
12:19 on our main Revit Design toolbars, which
12:22 is where you get this whole like jet
12:25 engine cockpit level of of detail,
12:29 uh, they wanted a time tracker." Now,
12:32 I really try to minimize
12:34 or or I'm sorry, I said that wrong. I
12:37 really try to limit the number of icons
12:39 I have, believe it or not. But,
12:43 we don't have the capability of doing
12:45 like drop-down menus.
12:47 And every one of these tools are custom
12:48 tools.
12:50 These aren't tools built into the
12:51 software. I had someone comment on one
12:53 of my YouTube post that says, "You don't
12:55 need all these tools. What are you
12:57 doing?" And I would love it if I didn't
12:59 need all these tools and I just had hot
13:01 keys, but unfortunately, this is the
13:03 easiest way to get to some very specific
13:05 tools that save me a ton of time.
13:07 So, I do need these tools. They save me
13:10 a ton of time. In fact, I couldn't
13:12 imagine not having them and and you'll
13:14 find that a lot of the users that have
13:16 been using this for over a year now also
13:19 could not imagine not having them.
13:22 And And so, I do try to come back and
13:25 say, "Hey, do we really need that tool?
13:27 Can I get rid of it? Will I catch a lot
13:29 of flak if I get rid of a tool?"
13:31 And so, I'm I'm very hesitant to put
13:34 more tools on here.
13:37 So, another user wanted me to put the
13:39 time tracker tools on here. So, I'm
13:41 going to do that, but I'm going to keep
13:43 it as a hidden toolbar just so that they
13:45 could toggle it on when they need it.
13:47 And I'll show you how to do that right
13:49 now. It is we're going to right click
13:51 somewhere on the toolbars and go to
13:52 customize toolbars. Now, that's how I
13:54 have always gotten to the toolbars. I
13:57 just learned recently that you can get
13:58 to the toolbars in some other way,
14:01 and I don't even remember where it is.
14:02 Oh, it's in tools, toolbars and hot
14:04 keys, customize toolbars.
14:06 I've never gone through that menu, so I
14:08 didn't even know that was there, but
14:09 there we go. Customize toolbars.
14:12 And I'm just going to start by putting
14:14 the time tracker tools on here. And so,
14:16 this is just a simple little trick that
14:19 I feel like everybody should know, which
14:20 is
14:21 going to drag this start time logging,
14:24 and I'm going to drag it very
14:25 specifically, and this is hard to zoom
14:27 in on. Very specifically
14:30 just in a blank area. I do not want to
14:32 drag it on top of an existing tool.
14:35 If I wanted this coupled with other
14:37 tools, I would need to almost drag it on
14:39 top and to the right in order for it to
14:42 live in this toolbar. Okay, that's what
14:45 just happened. Now, if I drag this off
14:47 and bring it kind of over here, it's
14:49 just going to disappear, all right? So,
14:51 keep that in mind as well, cuz that's a
14:53 way you can lose a custom placed library
14:57 object, which if you don't know what
14:59 that is, that's a way that we can link a
15:01 library object to a tool, which is how
15:03 all these other tools are built. This is
15:05 linked to a tool
15:07 or some object in my library.
15:10 So, I'm going to drag this, bring it to
15:13 a blank space here, and that's going to
15:15 create a new toolbar.
15:17 And so, let me just do all three of
15:18 these. Stop logging,
15:20 view time log,
15:21 and there we go. The next thing I do is
15:25 I'm going to go to the toolbar panel.
15:28 I joke about this with Chief all the
15:29 time.
15:30 It's really ridiculous. I think that we
15:32 call this toolbar configurations with a
15:35 bunch of individual toolbars and then we
15:37 have a toolbar panel and we have a
15:39 configurations panel and then on top of
15:42 that we've got a drop down menu called
15:44 toolbar and toolbar configurations. It's
15:46 really redundant and confusing to train.
15:50 So, I'm going to get to the toolbar
15:51 panel.
15:53 And then I'm going to go find where it
15:55 says
15:57 custom start time logging toolbar and
16:00 I'm going to name this to what I want it
16:03 to be named, which is I'm just going to
16:05 say say this as time logging.
16:09 Okay?
16:10 And then note that it only shows up on
16:12 plan elevation 3D view. So, if we wanted
16:14 it on specific types of views, here's
16:18 where you put that check mark to make
16:20 sure that it shows up where you need it
16:21 to be because if we switch the view type
16:24 right now to elevation, you're going to
16:27 see that that toolbar configuration just
16:29 disappeared, got replaced with something
16:31 else, okay?
16:32 So, that's exactly what this view type
16:34 drop down menu is. Is it is forcing the
16:37 state of if we were to have an elevation
16:40 as our active tab, all right? So, I'm
16:43 going to switch that back to plan view
16:46 and now I'm actually going to toggle
16:48 this off. Now, I want to change the name
16:50 of this even more because what I want is
16:53 I want this in the beginning of my
16:55 available toolbars. I use this as a way
16:58 to give the end user a way to toggle
17:01 this very quickly. So, I'm going to put
17:02 a little
17:04 minus sign in front of that. I'm going
17:05 to uncheck this in plan and I'm going to
17:07 hit close.
17:09 So, how is that user then going to get
17:11 that toolbar up and working? Well, what
17:14 they would do is they're going to right
17:16 click here, and they're going to go to
17:20 tool bars, the drop down menu, and they
17:23 will see time logging, and they get to
17:25 just click that on. All right, and
17:27 that's a really easy way to implement
17:29 that.
17:30 Now, I have some other ones that I use
17:32 like that. I'll show you this. When I'm
17:33 working on terrain, I just get to come
17:35 in here and toggle my terrain tools, and
17:38 then I usually like to just undock these
17:40 things and get them on the middle of the
17:41 screen because this is not something I
17:42 have permanently turned on.
17:45 And so, it's really easy for me to
17:46 undock this, and then close it out if I
17:49 wanted to, or if I need to share it,
17:51 it's important that if you're going to
17:52 share
17:54 that you want to dock these things.
17:56 The reason why you want to dock these if
17:58 you're trying to share with another team
18:00 member, someone in your office, you're
18:02 trying to use the same configurations,
18:04 is they may not have the same scaling
18:07 settings, the same monitor, the same DPI
18:10 settings as you. They might have
18:12 multiple monitors, and so what can
18:14 happen is when you share the
18:15 configuration, they load it up, things
18:18 like this might be on um technically on
18:21 their second screen that might not even
18:23 exist, especially if they're on just a
18:25 laptop with no external monitor turned
18:27 on.
18:28 And so, this could just be floating out
18:30 there with no way to retrieve it. So,
18:32 it's important that if you're going to
18:33 share a configuration, that you dock it
18:36 again. All right, and then I'm going to
18:37 turn this off.
18:42 All right, let me let me look at the
18:43 comments here real quick.
18:45 Uh BP Drafting, love your template.
18:47 Thank you. Thank you. Um Imagine AI is
18:50 helping tremendously with you
18:51 documenting the PP, saves you a
18:53 Brazilian hours. Documenting the PP, um
18:57 uh building the building the uh manual.
19:01 Yes, absolutely. Documenting it, that's
19:04 just coming straight from me. I'm just
19:05 typing it. Um
19:08 and then
19:10 uh when time allows, I quite often drop
19:12 a few place library I J object place
19:15 library item icons on my toolbar. And
19:17 later, when I want to add something new,
19:19 I just double-click it. With the latest
19:21 version, icons for these buttons are
19:23 changing to random icons, making it hard
19:25 for me to pick them out. Uh, it would be
19:27 good if you just force the icons. What's
19:29 happening there is that we're getting
19:32 old custom icons, um, because I'm no
19:36 longer scripting my toolbars. I used to
19:38 script my toolbars so that they were all
19:40 in order, so that, um,
19:43 everything was in sequence. The way
19:45 Chief Architect numbers things in
19:48 toolbars it is they're in order. And I
19:50 used to group everything in order
19:52 because I was scripting my toolbar
19:54 configurations outside of Chief.
19:56 It's such a cumbersome process to do
19:58 that now that I stopped doing it.
20:00 And so, what's happening is if you use
20:02 the custom place library object tool, it
20:04 is just picking up a, um,
20:07 an icon from an old version. That's
20:10 what's happening.
20:13 Um, what can you do about that?
20:20 It's a tough question.
20:21 Cuz you'd have to know which
20:23 icons to delete in the toolbar config.
20:28 Be very, very difficult to figure out.
20:30 I'd have to actually go through and do a
20:32 census of all the configurations.
20:34 So, what we're talking about with custom
20:36 place library objects, for those of you
20:38 watching and don't know what that means,
20:40 is we're going to get to customize
20:42 toolbars.
20:43 And
20:45 I'm going to get to tools and pick up
20:47 place library object.
20:50 Okay? And actually, I need this tool
20:52 right now because I am going to link
20:55 some new tool.
20:56 The new tool that I'm going to link is
20:59 an extended style tool, a spray painter
21:02 just to extend styles on an object,
21:04 okay?
21:05 And so, I'm going to drag this
21:09 right here, right on top of an existing
21:11 one, so that it's in this toolbar.
21:15 All right, so there we go. That's a new
21:16 custom place library object. And when we
21:19 click on that,
21:20 that will link to
21:23 the library object. Now, what they're
21:24 saying is that there's an image here.
21:26 Um
21:28 you could just
21:29 you know, reset it back if you double
21:31 click this, reset it back to the button
21:33 button icon choices that are default
21:35 image, I believe that shows up.
21:37 Um SB, so
21:39 uh that might be something you can do.
21:41 And there's our other Anthony. Good
21:43 morning, Anthony Hayes.
21:45 And so, with this,
21:47 when I clicked on it the first time,
21:49 it's linked to something.
21:52 Or excuse me, it's not linked, so it
21:53 brings up this dialogue box. And so, now
21:55 I get to link it to something. And so,
21:57 I'm going to do
21:59 Extend it style.
22:05 So, Extend it style painter. Oh, I have
22:07 two of them cuz I'm a big dummy.
22:10 That's That was foolish. Let's see where
22:12 they live.
22:14 One of them is in the kitchen quick
22:17 tools folder. Okay. There we go.
22:22 And so, then it tries to build an icon.
22:25 All right? Put these little
22:27 That's what that is. Tries to build an
22:28 icon. Now, if you've noticed, my icons
22:31 look a lot like Chief Architect's icons,
22:34 and that's because I'm hand drawing
22:36 them.
22:38 Um if you want to try doing the same,
22:42 I'm going to bring up Photoshop. An
22:43 alternative to Photoshop would be
22:45 Photopea.
22:46 Okay? So, I'm going to bring up
22:48 Photoshop so I can mess around with this
22:50 a little bit.
22:51 Oops, it just disappeared. I don't know
22:53 what happened to it.
22:54 Oh, that's weird.
22:58 Okay, Photoshop just uh did something
23:00 I've never seen it do before, so maybe
23:02 we'll use Photopea instead.
23:05 Now, let me kick that back on.
23:07 As I like to use some existing icons and
23:09 I'm going to show you where the Chief
23:11 Architect icons live.
23:16 So, I'm going to go open up one of these
23:19 existing icons.
23:22 And for a Windows machine, this is going
23:24 to be in Program Files, Chief Architect,
23:28 and the version, and then resources, and
23:31 buttons. And it I can't tell you how how
23:34 much I like it that Chief exposes this
23:37 that we that we can touch these icons.
23:40 You know, they they could have encrypted
23:41 them. They could have hidden them from
23:43 us, right? Now, notice in X18, there's
23:45 dark and light.
23:47 I did a census of the icons in Chief
23:49 Architect and there's a big change in in
23:52 the way they did the icons. They got rid
23:54 of a a lot of their consumer icons, is
23:57 what they were called.
23:58 Um, but they also just they added about
24:01 17 icons, so that means, you know,
24:04 potentially 17 new tools. Um, most of
24:06 them are new tools. Some of them have to
24:08 do with like dialogues.
24:10 And then there's dark and light, which
24:13 is supposed to match your dark and light
24:15 modes.
24:16 Now, uh, for me, I'm in dark mode in my
24:20 Windows machine. And so, I really did
24:23 not like the light mode icons.
24:27 And so, what I did was I switched these
24:29 two folders.
24:31 It's the same number of icons. I didn't
24:33 break anything with that. Um, I've had
24:35 it like that for several weeks now and
24:38 nothing's been broken. They're just
24:39 straight image files, so I felt pretty
24:41 safe doing that. Do that on your own
24:43 risk. Make a backup. Make a backup.
24:46 Please make a backup.
24:47 Okay? Otherwise, you're going to have to
24:48 reinstall the program.
24:51 And so, I've got dark mode, light mode.
24:53 And so, I can get into the dark mode and
24:54 I I find something that might be similar
24:56 to the icon that I need so that I can
24:58 modify it and create a new icon.
25:01 So, I might come in here and find some
25:04 kind of cabinet icon.
25:06 And maybe just do a search for cabinet,
25:08 put that in the name so that maybe we
25:10 get some options for this. So, there's
25:11 cabinet parent icon.
25:13 And so, I could open this up in
25:15 Photoshop. Let's see if that expands
25:17 this time. It does.
25:19 And so, I did um in Photoshop you have
25:22 the ability to save things such as
25:24 colors. And so, I saved the default
25:28 Chief Architect icon colors in a palette
25:31 here. And so, I can just click on those
25:33 colors
25:34 very quickly and get to that. And so,
25:36 it's easy for me then to come in with
25:38 the brush tool or
25:40 the pen tool, which is you're just
25:42 hitting shift B to get to the pen tool
25:44 to get this really pixelated tool, and
25:46 then do something that might look like
25:49 an extended style, right? And they
25:51 typically
25:52 put their colors in red when it's
25:55 something that's like
25:57 going to um
25:59 a modification. Is the the red color
26:01 indicates what that modification is. So,
26:04 this would be my extended style tool,
26:07 right? Something like that.
26:09 And you know, I'm going to do a better
26:10 job if I'm off camera.
26:15 Do a little cleaner job. Make sure these
26:17 corners are all
26:18 nice and tight. And so, yeah, maybe that
26:20 looks like an extended style tool. Just
26:22 remember that the tool is going to be
26:24 this small. So, it has to make sense
26:26 like that, right? So, maybe for
26:28 something like this, you know, if you're
26:30 getting really clever,
26:33 um
26:35 you just
26:38 test it in different ways so that it
26:39 makes sense on the screen. So, maybe
26:42 that looks better when it's shrunk down
26:44 to itty itty itty itty bitty, right?
26:47 Maybe that looks a little bit
26:49 more informative. And then I'm going to
26:51 export this and you want to make sure
26:52 you're exporting it as a PNG with
26:54 transparency in the case that part of
26:56 this icon should be see-through. And so,
27:00 here we go. I'm just going to stick this
27:02 in my downloads folder because because
27:05 I'm not scripting it anymore, I don't
27:06 need to assign it a name that Chief
27:09 Architect is going to assign. All right.
27:12 So, I can just save it anywhere. Once I
27:15 attach it to that toolbar icon, Chief's
27:17 going to bring it into its config files
27:20 and name it according to which number of
27:23 custom tool that it's attached to.
27:27 That information's more for people that
27:28 might have experience with this.
27:30 Otherwise, it's not going to make any
27:31 sense to you.
27:33 So,
27:34 and that's okay. We'll get right through
27:36 this.
27:37 It won't mean anything to you, and it
27:38 doesn't need to mean anything to you.
27:41 And so,
27:42 I've got this
27:44 library object button that I placed into
27:46 the toolbar.
27:48 I've linked it to the extend style
27:50 painter. I have the opportunity to
27:52 change the name here. What that means is
27:54 when we hover over the tool, this is
27:56 what's going to show up. Okay?
27:59 And then the browse button allows me to
28:02 go find a new button icon. And so,
28:04 that's how I'm going to go find that
28:06 icon I just created.
28:11 There we go. And let me press okay, and
28:14 we'll see here. Bam.
28:16 And we're linked up. And notice that it
28:18 is in fact a spray tool that's going to
28:20 extend the styles on a cabinet. All
28:22 right.
28:24 So, that if I've got a cabinet here,
28:26 placed in plan,
28:28 and I spray this tool, it's actually
28:30 going to extend it on both sides.
28:32 And it will just disappear if I put a
28:35 cabinet next to it, right? Or if I put a
28:36 wall next to it.
28:38 Or maybe this cabinet's not quite
28:41 butted, and we're extending some kind of
28:43 scribe panel for some reason. That would
28:45 be a really silly workflow. We going to
28:47 put a filler in there for
28:49 that one. So, there we go. I've got that
28:51 button on
28:54 on that toolbar.
28:55 Now, here's the next trick
28:57 is
28:58 we can transfer these toolbars
29:02 to other configurations outside of
29:04 Chief.
29:05 We can.
29:08 I've got someone that's always in my
29:09 comments mentioning, "Why can't we do
29:11 this? Why can't we do this?" I keep
29:13 saying we can. He keeps saying, "Show
29:14 me."
29:15 And I keep saying I can't. So, here we
29:17 are. I'm showing you. And I'm going to
29:19 put it in my members area pretty
29:21 quickly.
29:25 What we need to do in order to transfer
29:27 something is that we need to at least
29:29 start the build on the other
29:31 configuration of that toolbar that we
29:34 want to transfer.
29:36 So, I'm going to switch to another
29:37 configuration right now.
29:39 Okay?
29:40 And I want that time tracker
29:43 uh configuration to be started.
29:45 And so, I'm going to get into customize
29:47 toolbars.
29:49 I'm just going to bring this solid tool
29:50 drop down here.
29:52 Drop it into a blank space. We know that
29:55 creates a new
29:56 toolbar.
29:58 I'm going to find that custom 3D solid
30:00 tools toolbar. I'm going to name it
30:03 time
30:06 tracker
30:07 toolbar, okay?
30:10 And
30:11 I'm going to leave plan checked just to
30:14 show you something. In fact, I'm going
30:15 to leave plan 3D view, CAD detail
30:17 checked for that time tracker toolbar
30:20 just to show you something when we get
30:22 to the scripting part of this, the way
30:24 that we would have to transfer this.
30:26 All right?
30:28 And let me press close.
30:31 Okay.
30:33 Now, here's
30:34 the big next one. This is where we need
30:36 tree size in order to export these
30:39 toolbars.
30:41 The only current way to export toolbars
30:43 if you were to right-click, customize
30:45 toolbars or toolbar configurations.
30:47 There is no way to like
30:49 take one of these configurations
30:52 and export. There's no export button.
30:54 There's no way to do it. The only way
30:56 you can do it is by
31:00 making a backup in managed mode.
31:05 All right. In unmanaged mode, it's
31:07 pretty easy. You just go to where your
31:09 where your folders are. You know, you
31:11 get into edit preferences.
31:14 You'd find the folders panel, and you'd
31:16 show all program paths, and you would
31:18 see here that there would be a toolbars
31:20 folder with
31:23 you know, an address on your machine
31:24 that you could go find.
31:26 In
31:27 um
31:27 managed mode, we don't have that option.
31:29 Those files are encrypted.
31:32 So, in in my testing about speeding up
31:34 Chief Architect, I found out that
31:37 the encrypted files
31:40 are
31:41 decrypted and put in a temp directory
31:44 and collected. So, they're written once
31:46 to temp directory.
31:47 And then once they're written to the
31:49 temp directory, then Chief Architect
31:51 compiles it as a backup and writes it
31:54 again as a zip file,
31:56 an archive file.
31:58 So, it's writing it twice.
32:01 Here's the trick. I want to just go
32:03 capture the toolbars while it's being
32:05 written to the temp directory. So, I
32:07 don't have to wait for my full backup
32:09 cuz that takes way too long for me to
32:11 wait just to do some little hacky thing
32:14 that I want to do with a configuration.
32:16 I don't want to sit here for that long.
32:18 Even though I sped up my backup to 8
32:20 minutes and I reduced my file sizes by a
32:22 bunch of different tricks, it still
32:24 takes way too long for me. So, here we
32:26 go.
32:28 Um
32:30 Oh, and let me let me just see what
32:31 comment we just got here.
32:33 Good morning, all. It's on null island.
32:36 You can use the AI to create those
32:37 icons. Yeah, you can. You can cheat and
32:39 do all my hard work and redo all my hard
32:41 work that I did by hand on airplanes and
32:44 such and just drawing on my pen tablet.
32:46 You can do that with AI. It would be
32:48 very easy. In fact, you could redo all
32:51 of Chief's icons if you really wanted
32:52 to. I once made kind of a fake um old
32:55 school Mac
32:57 uh
32:58 Macintosh
32:59 like icon style where I blew up
33:02 everything and and made everything drop
33:03 down menus and
33:05 it's pretty funny.
33:06 Um not very usable.
33:09 So,
33:10 let me shut down this this plan file and
33:12 I don't need to save it and let me
33:14 trigger a backup.
33:16 Now, before I do, I want to go pull up
33:19 TreeSize.
33:21 All right, and I'm going to kind of
33:22 shrink this down.
33:25 And what I'm looking for is I'm going to
33:29 be looking for something in my temp
33:30 directories that
33:33 kind of indicate that something's very
33:35 large in file size.
33:37 And so I have my temp directory stored.
33:40 Let me get this off on the screen a
33:41 little bit. I don't know if this is
33:42 being displayed. It is being displayed.
33:45 Okay, perfect.
33:46 Um so the temp directory I'm looking at
33:48 is appdata local temp.
33:51 And if you didn't know how to do that on
33:53 a Windows machine, I do not know how to
33:55 do this on a Mac, just so you know.
33:57 Is that if you open up a Windows
34:00 Explorer, and so for those of you on a
34:03 Mac, you have to kind of
34:05 address this by finding a similar
34:07 software that can scan all your drives
34:09 and show you where all of your data
34:11 lives. And you'd have to probably open
34:13 up security settings because Mac's
34:15 pretty serious about their security on
34:17 all applications you install. So, you'd
34:19 have to allow your Mac to scan for
34:22 files, all right?
34:24 And so what I'm looking for here or or
34:27 what I'm doing here is um there are some
34:29 shortcuts to get to certain parts of
34:31 your Windows operating system. One of
34:33 them is percentage sign app data
34:36 percentage sign is going to get you to
34:38 the app data roaming folder. Now, if you
34:42 drop this little carrot down to the
34:43 local folder, what you'll find here is
34:46 that these are temp directories and one
34:47 of them is going to be coming from um
34:51 Chief Architect um
34:53 Actually, these are some core
34:55 uh file directories. But, the other
34:57 thing that's in here in the local is
34:59 your temp directories coming from every
35:02 single application that needs to write
35:04 something to cache or pre-load
35:06 something. So, saving it saving some
35:09 amount of information short-term as it's
35:11 trying to do something, okay? And so,
35:14 there's a temp directory in here.
35:16 So, there we go. There's my temp
35:18 directory.
35:19 Now, this isn't very helpful.
35:21 What you do see is Chief Architect's
35:23 creating a billion little
35:25 temp files, right?
35:27 It's creating a ton of these.
35:30 Um it's not always clearing out its temp
35:32 directory, too. I think a reboot clears
35:34 that out. So, I've been doing a lot of
35:36 file operations, so that's why there's
35:37 so many Chief Chief temp directories.
35:40 So, trying to target the correct Chief
35:42 temp directory is pretty difficult
35:43 because you can see here
35:45 it's jumping from 89 to 119. What am I
35:48 doing, by the way, in case you were
35:50 wondering? I'm looking for a Chief temp
35:52 directory where it's going to start
35:53 loading up all the files that it's
35:55 decrypting as it starts up a backup, all
35:58 right? Because I don't want to work wait
36:00 20, 30, 40 hour
36:03 amount of time to get to that toolbars
36:06 configuration.
36:08 So,
36:09 what I'm doing instead here is
36:12 let me get the Chief. Let me do file
36:15 backup and restore, backup manage
36:17 resources.
36:18 I'm going to choose my typical backup
36:20 location.
36:22 What it's going to do right now, I don't
36:24 know. It's doing some amount of
36:25 processing before it starts, typically
36:28 my drives are just lightning lightning
36:30 fast, so that should have taken you a
36:32 lot longer if you're on a PC. I've got
36:34 the fastest drives on the market,
36:36 they're in a RAID configuration.
36:38 So, mine popped up super quick.
36:40 And so, I'm going to then scan this temp
36:43 directory.
36:45 And I can refresh this.
36:47 And once this thing starts writing,
36:50 we're going to see Here we go.
36:53 This is starting to build
36:58 these directories. It's starting to
36:59 write things to this, okay? Actively
37:02 writing right now. If I refresh again,
37:05 you're going to see it's just
37:07 continuously increasing in size. Once we
37:10 get this settings folder that just
37:12 popped up, notice, okay? Settings
37:15 folder. Now, I get to go open this
37:17 folder.
37:19 And look at this. This is my toolbar
37:21 configs.
37:23 Now, I'm going to wait till this
37:24 populates it's completely.
37:27 And
37:28 I just kind of know what's in my config
37:30 files to know when this populates
37:32 completely. Um but I would say you could
37:34 just wait, you know, maybe a couple
37:36 minutes for this to populate completely.
37:38 All I need to do here is wait until
37:41 uh the two configuration files that I'm
37:43 trying to swap toolbars show up. Now,
37:45 one of them kind of already has is um
37:50 the dot toolbar file extension will show
37:53 up right next to the image
37:55 that
37:56 that it's using for its toolbar icon.
38:00 And so, that's all I'm doing here is I'm
38:02 just waiting for this to show up. Now,
38:04 this is a temp directory. What's the
38:06 problem with the temp directory? Well,
38:08 once it builds all the assets and starts
38:11 writing, after it's done writing, this
38:13 temp directory disappears. All these
38:15 files disappear. So, that's something to
38:17 note here.
38:20 But, this does save me a good amount of
38:23 time because I'm not having to wait for
38:25 everything to build in order for me to
38:27 get to this. So, I'm still just going to
38:29 wait for a little bit for this to finish
38:31 what it's doing um before I can see
38:33 um this particular toolbar that I need.
38:36 And so, there you go. It's just writing.
38:40 Oh. Oh.
38:42 Oh.
38:43 Oh man, I forgot my toe is broken.
38:46 I was just trying to flex it.
38:51 All right. Let's see.
38:54 Seeing some bunny ears. That's what I'm
38:55 waiting for. What am I seeing in the
38:56 comments here?
39:04 Yeah.
39:05 Don't
39:06 Don't don't scream that one from the
39:07 rooftops. I did change that. Oh, it's
39:10 peanut. Okay. Nice. All right.
39:14 I'm talking to the chat right now.
39:20 Oh, it's still not giving me the config
39:22 that I want. I was hoping that was going
39:24 to be a little super fast.
39:26 This is still fat a lot faster than
39:28 waiting 30 minutes. There we go.
39:31 There's the start of what I want. I want
39:32 that neon green rabbit ears because I'm
39:34 going to take that and transfer
39:37 to the other one.
39:41 And
39:44 give it to me. Give it to me.
39:48 Okay, so here's one of the files I need.
39:49 Rabbit design toolbar full. So, I'm
39:51 going to just going to drag this file
39:53 into downloads and
39:55 I'm going to hold my control key
39:58 to copy it to downloads instead of
40:01 moving it to downloads, okay? That's
40:03 what I just did.
40:04 And then, let me see if I can capture
40:06 the other one. Here's the wide screen.
40:07 I'm going to hold control key, dropping
40:09 it into downloads.
40:11 Now, I don't need this backup to
40:12 continue.
40:14 And keep in mind again, my backup's way
40:17 faster than the than the norm because of
40:19 the drives that I have. So, I'm going to
40:21 just cancel this backup. I don't need it
40:23 because now I should get be able to get
40:25 into downloads.
40:27 And if I were to get into the toolbars
40:30 files,
40:33 you were right there they are. Here's
40:35 the two where I'm going to transfer
40:37 these two.
40:39 And so, I can open this in Notepad++
40:42 and let me get back here, open this in
40:43 Notepad++,
40:45 and if I remember how to do this, I'm
40:47 going to
40:50 let's see, open into
40:54 Pa pa pa pa. Move document, move to
40:57 other view. There we go. Now we have
40:59 these side by side.
41:01 And here's where we get to do some
41:03 modification.
41:04 Now, back in Chief, I stopped that
41:07 backup, so no file's being written. If
41:09 we were to go look at that temp
41:10 directory again,
41:12 um
41:13 like if I were to go back, a stage, look
41:15 at that. That folder's empty. Chief
41:18 cleared it out, okay?
41:20 And so now I'm coming back to Notepad++
41:23 and we're going to do a little
41:24 examination of what's here. And I can
41:27 just kind of
41:29 explode this. Now, we know a couple
41:31 things. We know that I named
41:34 that time tracker in the widescreen one,
41:37 I'm logging right here.
41:39 I want you to note something.
41:42 These might not mean anything to you,
41:44 but the 2000s are built-in tools.
41:48 Um the 24 series are
41:53 and 23 series, I believe, are um
41:57 are custom tools.
41:59 So, for the time logging one, these are
42:00 built-in tools.
42:02 Notice that there's a whole blank line
42:03 here. Line 23 is blanked out.
42:06 What does that mean? Let's go look at
42:08 this other one where I did not rename
42:10 this appropriately, right? I named it a
42:12 little bit different.
42:14 I named it time tracker. I didn't put
42:15 that hyphen in front. Now, here's what
42:17 I'd tell you.
42:18 Now is not the time to rename this. You
42:21 may be tempted to, but I would just
42:23 wouldn't do it. We're going to do some
42:24 edits that are minimizing the risk of
42:28 blowing these toolbars up and making
42:30 your toolbars not function.
42:32 Okay?
42:33 Um and so that's important. We're not
42:36 going to change the name here, not at
42:38 all.
42:40 We're not going to change line 140. Line
42:43 140
42:44 relates to
42:46 line 23, where this is blank. Why is
42:48 this blank? Because
42:50 we did not have this turned on
42:53 in any of the views.
42:55 So, there's no key coding here to show
42:58 us which views it's turned on in.
43:01 Again, this is not the opportunity to
43:03 make an edit there. You can easily blow
43:05 up your toolbars, all right?
43:08 Here's the only edit that I would say is
43:11 okay to make, that I've made a bunch of
43:13 times, and I've been doing it for years,
43:15 and it hasn't been any problem. They
43:17 introduced new toolbar configuration
43:19 format. This did not used to be in
43:21 alphabetical order. It is now, which now
43:24 means it's got some leading amount of
43:27 code to um
43:30 kind of communicate with the rest of
43:33 this body to understand how these
43:36 toolbars are configured.
43:38 I did at some point figure out what this
43:40 code means and how to edit it. I just
43:42 don't recommend it.
43:44 Okay?
43:45 And so, I'm going to get back to that
43:48 that section. Let's see. Here we go.
43:50 Time tracker toolbar.
43:53 I'm going to come over to time logging
43:55 over here. I'm going to copy this.
43:57 Those 2,000 numbers, or maybe they're
43:59 2,400 numbers,
44:01 or maybe they're 800 series numbers.
44:04 These are all just representing
44:05 different icons in the system. I'm going
44:08 to copy this.
44:10 I'm going to come over here to my time
44:12 tracker. I'm going to overwrite what's
44:14 here. Notice this 2183
44:18 is the solid tool.
44:21 And these are the time tracker tools.
44:23 So, I'm just going to overwrite this.
44:25 This is something that's seemingly okay
44:27 to do.
44:30 Chief Architect, if you're watching
44:31 this, this is the opportunity to give us
44:34 what we need.
44:35 Give us a way to export toolbars. Give
44:38 us a way to transfer toolbars from one
44:40 configuration to another. We would not
44:42 need to come up with this kind of stuff.
44:46 And also, please don't go break our
44:47 ability to do this.
44:49 I'm trying to give an end user the
44:51 safest way to possibly do this in a in
44:53 the case that they really need to share
44:55 this with their team.
44:56 So, there we go. I've pasted this into
44:59 my design toolbar full from the design
45:03 toolbar wide screen. Okay?
45:06 The next thing that I want to do is I
45:07 want to go find my kitchen base
45:09 cabinets. We made a modification. We
45:12 added a new custom tool to the kitchen
45:13 base cabinets.
45:15 And so, I'm going to go find kitchen
45:16 base cabinets
45:18 uh over here.
45:20 There we go. I'm going to grab this
45:21 whole line,
45:23 copy it,
45:25 going to overwrite my kitchen base
45:27 cabinets on this side,
45:29 and paste.
45:31 And then, save this.
45:33 Okay?
45:34 Now, I get to come back in the Chief.
45:36 Let's go ahead and open up a file here.
45:41 And then, customize toolbars.
45:45 Configurations.
45:47 I'm going to click on import.
45:49 I'm then going to go to my downloads
45:51 folder.
45:52 There's that design toolbar full.
45:55 What should we expect when I import
45:57 this? My expectation is that this solid
46:01 turns into the time Actually, yeah,
46:03 turns into the time tracker tools cuz it
46:05 is toggled on currently. All right. My
46:07 expectation is we get another icon right
46:10 next to this. All right, so customize
46:13 toolbars
46:15 and then import.
46:18 Let me do find that in my downloads.
46:21 Here's that toolbar full.
46:25 Here's what it's going to give me as
46:26 options.
46:27 I can it saying that there's a conflict.
46:29 Same name, same coding, blah blah blah.
46:31 Well, same name anyways.
46:33 Uh replace all is my function here. I'm
46:36 going to replace. All right. You press
46:38 okay. Now, the first time you're doing
46:40 this and you're testing things, you
46:41 might want to just try to import it and
46:43 not replace. Let it um save as a as a
46:46 duplicate. All right. That would be
46:48 another safety check. That would be
46:49 another level of buffer before you're
46:52 breaking toolbars.
46:54 So, maybe you do not choose replace all.
46:57 But, I'm going to choose replace all.
46:58 I'm pretty confident on what I'm doing
47:00 here.
47:01 And then
47:02 um typically, it will um it if it's part
47:06 of a system that you don't have, so for
47:08 another end user, it's going to then
47:10 import custom place library objects that
47:12 you've established. And so, you'll see
47:14 that on the other user's side if they
47:17 didn't have your configuration before.
47:19 And in that process, it might prompt you
47:21 to say, "Hey,
47:23 there's a difference between the custom
47:25 place library objects you have currently
47:27 and the custom place library objects
47:29 coming from this import. Would you like
47:31 to choose all existing to maintain or
47:34 choose new?" And often times if we're
47:36 importing toolbar, uh we want to choose
47:38 new. So, you're going to say select all
47:40 new. That's a dialogue box I can't fake
47:42 right now. All right.
47:44 And so, let me just
47:47 There we go. I imported that toolbar.
47:49 Let me hit close. We've switched to that
47:51 toolbar. And look what happens when it
47:53 loads up. I now have that same time
47:56 tracker toolbar that I had in the wide
47:58 screen configuration. I also now have
48:01 that same tool here. If we click on it,
48:03 does it work? It sure does.
48:05 There we go.
48:06 So, we've effectively transferred a
48:08 toolbar from one configuration to
48:10 another.
48:11 And that's how you do it.
48:15 How do we do on time? Oh, I got that in
48:16 under the hour, too. Pretty cool.
48:19 Um so, the last kind of cleanup here is
48:21 that I'm just going to get to customize
48:22 toolbars and turn that off and rename it
48:24 the way I wanted to rename it.
48:28 So, and back down here, we're going to
48:30 just put a little
48:32 minus sign in front of that. We're going
48:33 to turn that off in these views.
48:36 And close that out. And there we go.
48:39 Simple as that.
48:41 Pretty cool.
48:43 Now, I mentioned earlier that you can
48:45 put other configurations
48:47 on your current configurations. So,
48:49 buttons that link to other
48:50 configurations on your current
48:52 configurations.
48:53 Um this is kind of an easy process.
48:56 You're going to go to customize
48:57 toolbars.
48:59 You'll go to
49:01 tools, and you'll just search the name
49:04 of the configuration you created. Just
49:06 to show you how this works, I'm going to
49:07 make a copy of this place space planning
49:10 configuration. There we go. Where I can
49:12 modify it, what have you. Example
49:15 toolbar.
49:18 Right?
49:21 So, I just made that copy. There we go.
49:24 I'm going to switch back to
49:26 the configuration I was on. I'm going to
49:28 get into the tools section, and if I
49:31 were to type in example, there it is
49:34 right there. And so, I could drag this
49:36 onto the toolbars so that I was linking
49:39 to that toolbar configuration that I
49:41 just created, okay? Now, when we get to
49:44 configurations and you see the space
49:47 planning configuration right here, you
49:49 do have the ability to change the icon
49:52 that you're using here.
49:53 And so you can choose the choose icon
49:56 button there, and that's a way that you
49:58 can come in here and choose whatever
49:59 icon you want for that, like my broken
50:01 toe.
50:06 All right.
50:08 Anybody in the comments have any
50:09 questions about that whole process?
50:12 Bet you do.
50:19 And let me see. I was going to think
50:20 about some other
50:22 little
50:23 tips and tricks I could give about this.
50:27 Um in terms of these icons, keep them at
50:30 128 by 128. I don't know if you can
50:32 limit uh Chat GPT or some kind of AI to
50:35 do that. Um
50:38 I know that some things like uh Chat
50:39 GPT's Codex
50:41 or
50:42 um
50:44 uh it has a version of kind of Codex, uh
50:46 Cursor. Those those AIs can write files
50:50 on your machine. So you install them as
50:52 a desktop app,
50:53 and you can go get them to build you a
50:55 bunch of files uh according to your
50:57 parameters and get you build build you a
50:59 bunch of icons that you might like.
51:01 So,
51:02 that was a actually a a great point from
51:04 Victor in the comments section here. He
51:06 said, "Yeah, you could get these icons
51:08 built similarly to Chief Architect's
51:11 icons."
51:12 Um
51:13 again, I switched the dark icons for the
51:17 light icons because the light icons were
51:19 the old icons coming from X17, and I
51:23 really um liked the way those looked on
51:25 my machine, so I switched back to those.
51:28 Um if you didn't know it,
51:31 the current light and dark
51:33 configurations, if you have a custom
51:35 color profile
51:37 in your preferences for your interface
51:39 here,
51:40 like I do,
51:41 there is no real setting to change what
51:46 um
51:48 what certain menus look like, such as
51:52 if you get to an item in your library,
51:54 you get to tag section, look at how this
51:56 is white, right? That's not very
51:59 helpful.
52:00 So,
52:01 I wanted to change my color
52:02 configuration.
52:04 Um I'm also noticing that my color
52:06 configuration is not staying the way
52:08 that I had it changed. So, I'm not sure
52:10 what's going on with that, but it's uh
52:12 it's reverting back
52:14 um to a configuration that I had before.
52:16 So, I don't I don't particularly like
52:18 that either.
52:19 Um
52:22 so, what I would say is that the
52:24 table input background or table
52:26 alternate row, you might need to change
52:29 off of white if your
52:31 um machine is in dark mode. You might
52:34 need to add a little bit of contrast
52:36 here, some kind of color contrast here.
52:39 I'm just going to use this color.
52:42 So, you'll see what happens with this is
52:44 now when I right click this and get to
52:45 tags, oops, still wrong. Let me see if
52:48 I'm going to get this right.
52:51 Uh table input background then must be
52:54 it. Table input background, let's grab
52:57 this.
52:59 And table alternate row,
53:02 change to be a little lighter.
53:06 And so, now if I right click, yeah, now
53:09 I can see my tags because they are all
53:11 white text and they're not following
53:13 that that flip flop um
53:16 of white to dark in dark mode. So, uh
53:19 that was making it really challenging
53:21 for me to create tags. So, if you see
53:23 something like that, go report it. We're
53:24 still in beta, keep that in mind.
53:26 And then,
53:28 what do we have?
53:34 Seems like the text file you edited is
53:36 kind of a toolbar mapper. So, the text,
53:38 yes, that's exactly what it is. Is it's
53:40 the config file for Chief Architect's
53:42 toolbars.
53:44 Um
53:45 you know, you can you can maybe take
53:47 this in AI and figure out exactly how
53:49 it's working, what it's doing, and have
53:50 it explain it to you, but um I can just
53:53 tell you what it's doing is you know,
53:55 this is the name of Oops, let me get
53:58 that on the screen. This is the name of
54:00 the toolbar as you named it or as it was
54:02 automatically named. This next line
54:06 directly after the toolbar name is
54:09 which um types of views that toolbar is
54:12 turned on in.
54:14 So, the coding here is just the code for
54:19 uh the view name. That's it.
54:22 And so, if there is a code here, it
54:24 means that this toolbar is on in that
54:26 view type.
54:28 And then, these are the codes for the
54:30 individually placed library objects.
54:33 So, when someone was asking earlier, you
54:36 know, before when I um double-clicked
54:38 and did a custom-placed library object
54:41 that it um it had no icon and now it has
54:44 an icon. Before when it had no icon,
54:46 that's because I was coming in here and
54:49 scripting these numbers specific to
54:51 exactly uh the toolbar icon that I
54:54 wanted to use in the custom um toolbar
54:58 that I wanted to use.
54:59 To just explain that further, let me get
55:02 into where people download my toolbars
55:04 so that they can install them on their
55:06 systems and have linked toolbars is that
55:10 uh if you were to go look at this
55:12 file, this is all my toolbar settings.
55:15 One is that there's a configurations
55:16 button data folder. This is um contains
55:20 all the data for and I think it might be
55:22 um a sequel
55:24 um
55:25 type file, but this contains all the
55:27 data for your custom-placed library
55:28 objects. And then, um
55:32 Chief Library JSON has something to do
55:34 with that as well.
55:36 Um so, you know, these are things that
55:38 you could probably try to go open up in
55:40 in a database viewer. I wouldn't
55:42 necessarily
55:44 advise that, but you can certainly give
55:46 it a try. Get SQLite
55:49 and go look at Oh, no, that is not
55:52 database
55:53 database based.
55:55 Um, but the JSON might be.
55:58 And then you can see here as you link
56:02 these icons to something, Chief
56:03 Architect's putting it this custom
56:05 number, custom 56, custom 57.
56:08 So, for example, if we were to go find
56:11 some of my kitchen tools here, where we
56:14 see custom 137,
56:16 you'll see that this is actually um, is
56:19 probably the code 23 137.
56:23 If we were to go look at Notepad, get
56:26 into the base cabinets, kitchen
56:29 base cabinets, 23 137.
56:34 That's what that means. That's that
56:35 custom 137 icon. The 23 prefix is
56:39 indicating that it's we're in the um,
56:42 custom placed library objects, of which
56:44 we have 400.
56:46 Okay?
56:47 So, that's how this coding is happening.
56:49 And then the forward code here, if we
56:51 did some word wrap, this is a really,
56:53 really long set of code and it just um,
56:57 it's something about the data management
56:59 and and keying in and coding for how all
57:01 these things are loaded up. So, um,
57:03 again, I wouldn't touch any of that
57:07 except for what I showed
57:09 earlier on, which would just be
57:11 um, the second set of numbers after your
57:14 name. So,
57:15 name,
57:16 where it's turned on, don't touch that.
57:19 This is what you can replace. Just make
57:22 sure that your codes are valid or you
57:24 will have an invalid toolbar.
57:27 And that's that and you'll have to go
57:28 reset your toolbars.
57:31 In case you didn't know how to reset
57:33 your toolbars,
57:35 not sure what that setup file is about,
57:37 but okay.
57:38 Um is edit preferences,
57:42 and we've got reset options, and you're
57:44 going to have the option to reset
57:45 toolbars.
57:47 So, in the case that you brought in some
57:49 custom toolbar, and you forgot to dock
57:52 your edit menu, and it showed up on some
57:55 second screen, and you're on you're on
57:57 the road, and you're there's no way you
57:59 could get your edit toolbar back, that's
58:00 how you would get it back is you're
58:01 going to reset bars. Unfortunately,
58:03 you're going to lose your custom
58:04 configuration,
58:06 and I don't know how to script in how to
58:08 dock that edit toolbar.
58:10 I just don't, so that's part of that
58:12 forward code is is the docking side of
58:15 that.
58:16 Um
58:18 and let's see, did I miss
58:21 I missed something else here. See what
58:23 he's saying in the comment.
58:26 That's what I'm doing, creating shortcut
58:27 keys for Stream Deck and my mouse. Cool.
58:32 Okay.
58:33 Yeah, Stream Deck is pretty popular,
58:34 pretty popular setup.
58:37 And I know some people make some pretty
58:38 cool setups with that where you can In
58:40 case you didn't know, Stream Deck is a
58:42 way that you can have
58:43 um
58:45 hot keys
58:47 attached to a device, programmed to to a
58:50 device. So, if you didn't know this
58:51 product, it's pretty good. I use um
58:54 something that I like better than Stream
58:55 Deck, I use my 3D mouse with radial
58:57 menus, um but here you go. Not only can
59:00 you configure these buttons, but I
59:02 believe you get to swipe to load other
59:04 buttons because this is completely
59:06 digital, so you don't you're not just
59:08 restricted to this number of buttons,
59:09 you get to just
59:11 keep scrolling through buttons after
59:13 buttons after buttons to get to other
59:14 buttons, right? Um I just have a setup
59:17 that gets me way more hot keys in a in
59:21 fewer button clicks, um which is my
59:23 radial menus.
59:25 And so, there we go. I can get to these
59:27 buttons very quickly. So, it's just
59:29 taking a swipe action. So, here's my
59:30 base cabinet tool. If I hold the
59:33 modifier key on my right mouse, then I'm
59:36 going to dip make that same swipe, and
59:38 now it's full height cabinet. Hold some
59:40 modifier button, there's my wall
59:42 cabinets, etc. So, really easy for me to
59:46 just get to
59:48 a huge number of hot keys just by doing
59:50 some swipes. Oh, that's nice. Good job,
59:52 Revit.
59:55 Uh let's see.
59:57 Yeah, I think we about covered it. Boy,
59:59 I thought the show was going to run
1:00:00 long, and here we are. We're all
1:00:02 finished.
1:00:03 Um I am going to send this to my members
1:00:07 area pretty quickly. I don't think I'm
1:00:08 going to leave this
1:00:10 um over 24 hours. I don't want to get my
1:00:12 head chopped off.
1:00:14 Over there, Chief. I will be in Coeur
1:00:17 d'Alene in August over at uh at Chief
1:00:20 talking to all all the people at Chief.
1:00:22 I love those people over there. They're
1:00:25 awesome people. I love talking to all of
1:00:26 them. Um from the trainers to the
1:00:28 marketing team to you know, just anybody
1:00:33 and everybody in between. And then I
1:00:34 especially love talking to the devs, and
1:00:36 of course
1:00:38 um the CEO, president.
1:00:40 He's a great guy to talk to, hang out
1:00:42 with. He's very accessible, too, when
1:00:44 when you're at these things. So,
1:00:46 really, really cool that you get to go
1:00:48 talk to someone that's in charge of your
1:00:50 livelihood.
1:00:52 And uh
1:00:53 and then if you didn't know it, my pro
1:00:56 plan is uh feeling pretty stable
1:00:58 nowadays. Let me know in the comments
1:01:00 section if you feel like the pro plan's
1:01:01 pretty stable. Um the current version
1:01:04 right now is called um beta 260720. So,
1:01:09 if you don't have that, you want that,
1:01:11 you can go get that right now. That's
1:01:12 available to you in your links.
1:01:15 Um it's going to have a link to the new
1:01:18 manual. That's one of the major changes
1:01:20 in there. And then uh a few little um
1:01:24 patches and updates to some of the
1:01:25 layouts.
1:01:26 Um I got rid of some things that were
1:01:29 redundant.
1:01:30 And
1:01:31 um
1:01:32 I'm continuously working on some of the
1:01:35 um Pro Arch layouts that are full
1:01:38 architectural set layouts where um we're
1:01:40 using some layer base fill styles for
1:01:42 some changes for some um visual changes.
1:01:46 That's pretty cool. I'm starting to
1:01:47 implement that into some of the other
1:01:49 profiles um such as the Rexel
1:01:53 um architectural one where now the
1:01:55 sidebar can be changed by layer base
1:01:57 fill style as well.
1:02:00 Um
1:02:01 Yeah, and if you
1:02:03 find some glitches, go ahead and throw
1:02:05 it into our beta reporting. Thank you.
1:02:07 Thank you. Thank you.
1:02:11 Oh, Mr. Pittman, going to be there. You
1:02:13 registered. Very cool.
1:02:16 Well, I look forward to meeting you,
1:02:17 sir.
1:02:19 Yeah, I've been seeing you all through
1:02:20 Facebook and Chief Talk. Um
1:02:23 good contributor.
1:02:25 All right, that's it for this show.
1:02:27 Thank you all for watching.
1:02:29 I'll check you next time.
1:02:54 Oh, you know what? I got to address this
1:02:56 comment real quick. I'm back. I'm back.
1:02:57 I'm back. I'm back. Victor, I used to
1:02:59 say it's still showing 14 not 20. You're
1:03:02 correct. Uh 20 is my current um
1:03:04 development set. 14 is the current set.
1:03:07 So, um
1:03:10 now in the Discord server, something new
1:03:13 here is I do have a PPX 18 upcoming
1:03:18 channel. So, if you don't have that
1:03:19 turned on, you're not seeing that, um go
1:03:22 search channels, you'll find this. Um I
1:03:24 think you can edit your
1:03:26 um your preferences up here
1:03:29 to get into the drop-down menu and
1:03:32 it should say show all channels as an
1:03:34 option. Anyways, PPX 18 upcoming, that
1:03:37 just lists current unreleased
1:03:40 development is that 260720.
1:03:43 The current issue is 260714. So, I did
1:03:46 put that out yesterday. So, you were
1:03:47 correct. The current version right now
1:03:49 is 260714.
1:03:51 All right. And then, if you want to, you
1:03:53 can go look at what was changed um in
1:03:56 the latest version.
1:03:58 And so, um yeah, a couple things were
1:04:00 added to this.
1:04:02 Just wanted to make note of that. So,
1:04:04 one of the things that I did was
1:04:06 um in those big old McMansion plans
1:04:10 where you might be converting from a CAD
1:04:12 drawing or something like that, um I did
1:04:15 add
1:04:17 a new working view that I call light,
1:04:19 working light. And so, that just makes
1:04:22 everything but the walls basically a
1:04:25 very light gray. And that just helps me
1:04:27 in a really congested plan.
1:04:29 And so, that's that's one of the things
1:04:31 that I added there. Um
1:04:34 And let's see.
1:04:36 Uh there's more project information you
1:04:38 can input. So, setbacks, max height. In
1:04:40 case people don't know that, I'm using
1:04:43 basically a warehouse template plan
1:04:45 where that's where your spec and title
1:04:47 block information comes from.
1:04:49 And so, that builds out a bunch of these
1:04:51 info things that are dropped into
1:04:53 various different layout types. Um some
1:04:55 would be more extensive than others,
1:04:57 like the pro archer is going to have the
1:04:59 uh the project team. Um some of them
1:05:02 might have uh this compliance one where
1:05:04 it shows front and rear side setbacks
1:05:06 and max height and stories. And then, I
1:05:08 give you a way to override the automatic
1:05:10 applicable codes in the case that um
1:05:13 that's not working for your jurisdiction
1:05:15 or you have a custom applicable codes
1:05:17 that you need to write through. And so
1:05:19 all those are accessed in your toolbar
1:05:21 configs through the project information
1:05:23 input here. And so that's going to bring
1:05:25 up um this dialogue box where we have
1:05:27 the ability to change here's front
1:05:30 setback, side setback, etc. That's going
1:05:33 to report from there.
1:05:35 Then your designer information, your
1:05:37 client contact, design load criteria,
1:05:40 your project team, and applicable codes.
1:05:43 Um I personally uh got a Python script
1:05:47 to input my project team from just a
1:05:49 document so that it would just tab
1:05:51 through these. So that was the way that
1:05:52 I got to this.
1:05:54 Um
1:05:55 So there you go. That's uh some of the
1:05:56 big updates in this latest review. Uh
1:06:00 And I don't think there were many
1:06:01 patches that came out with this.
1:06:04 Um
1:06:05 There was a split of some text styles so
1:06:07 that I can control one from the other to
1:06:09 create that light working view.
1:06:12 And then
1:06:13 um
1:06:15 Oh, and then I added the tool to your
1:06:16 toolbars in the case that you're trying
1:06:19 to
1:06:20 um test or figure out why your area
1:06:22 analysis is not reporting the way that
1:06:24 you want it to report, okay? So I were
1:06:27 to go draw some walls here. I just This
1:06:30 is just a little bonus for the people
1:06:31 that have my
1:06:33 my stuff. If If I'm going to draw some
1:06:35 walls and some reason not getting it all
1:06:37 the way to this wall here.
1:06:39 And let's just designate these rooms
1:06:41 real quick.
1:06:48 Something different.
1:06:51 And let's go bath.
1:06:54 And let's make a little itty-bitty room.
1:06:55 Why not?
1:06:58 Another little itty-bitty room.
1:07:03 And one more.
1:07:04 Why not?
1:07:05 Now if I go look at
1:07:08 where this is reporting our totals, if
1:07:10 these totals are not making sense to me
1:07:14 in the library browser, now if you do
1:07:17 replace all of your library with the new
1:07:19 updated library that I just put out for
1:07:22 this version
1:07:23 in the pro plan tools folder, I believe,
1:07:26 or let's see.
1:07:29 Um
1:07:30 What am I What were we calling this?
1:07:32 We're calling this
1:07:34 I think it's architectural quick tools
1:07:36 then.
1:07:37 Mhm mhm mhm. Maybe not. Let me search.
1:07:41 Let's just type in an Now, oh, it's an
1:07:43 area analysis, duh.
1:07:45 Um breakdown schedule for
1:07:47 troubleshooting. And so, when you place
1:07:49 this in plan, it's going to break down
1:07:51 where these numbers are coming from.
1:07:54 Um and so, you can just
1:07:56 um
1:07:58 Those are ungrouped. You might just want
1:08:00 to add
1:08:02 room name
1:08:04 or room function, either one.
1:08:08 And so, this is just a quick and easy
1:08:09 way to understand what the breakdown of
1:08:11 your totals are coming from, okay?
1:08:14 That's it. Simple as that.
1:08:18 All right, that's it. Thanks again.
1:08:20 Appreciate it, guys.
