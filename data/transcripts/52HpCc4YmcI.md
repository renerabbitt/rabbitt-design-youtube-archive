---
videoId: 52HpCc4YmcI
title: Template Tuesdays #31 - Use Ai To Draw In Chief Architect Natively
url: "https://www.youtube.com/watch?v=52HpCc4YmcI"
status: imported
---

# Transcript

0:02 Oh, yeah.
0:04 Yeah, yeah, yeah.
0:07 It's a big day.
0:08 It's a big
0:09 day.
0:11 Uh, the time is here that we finally get
0:14 a little bit of AI in Chief Architect.
0:18 Little AI in Chief Architect. Actually,
0:20 we've had a little AI in Chief
0:21 Architect, but not like this.
0:24 We now have
0:27 what's called an MCP server integrated
0:30 into Chief Architect, and I'm going to
0:32 show you how to set that up.
0:34 And
0:37 I'm going to talk to you about what does
0:39 that even mean? Model context Model
0:42 context protocol.
0:45 So, it's a model context protocol
0:47 server.
0:48 AI runs on large langua- language
0:51 models.
0:53 So,
0:54 you know, just run that backwards and
0:56 through your head again, and you'll
0:57 understand that it's giving the large
1:00 language model AI some context, meaning
1:04 that the MCP server
1:06 think of it as like an instruction set,
1:09 if you will, of things that
1:11 Chief Architect can do. It can do a
1:14 bunch of things. So,
1:17 what's really cool about this is that
1:20 with an MCP server, unlike an agentic
1:24 workflow, if you know what agentic even
1:26 means, the heck is that term?
1:29 Agentic workflow means that we've got
1:31 Maybe we've got an AI acting on our
1:34 behalf
1:35 um and working on something for us,
1:38 okay? A lot of times um the agentic
1:42 workflow means that it's taking control
1:44 of your computer. You can't do anything.
1:46 With the MCP server, you can be doing
1:49 things on your computer while it's doing
1:52 things inside of Chief Architect for
1:55 you.
1:56 Um
1:58 I haven't prepped for this. I don't even
1:59 know how to like bring this up and tell
2:01 you it how this all works, really. Like
2:03 I'm just winging it right now. I don't
2:04 have a script, so.
2:06 Let me know in the comments, cuz there
2:08 I'm sure there'd be a lot of comments
2:10 that have questions about what the heck
2:13 are we doing here? What are we doing?
2:15 What is this?
2:17 I do want you to start somewhere
2:19 and I'm just going to bring this up
2:20 right away before we hit the good
2:22 mornings to the whole chat going off
2:24 right now.
2:26 And so, what I'm going to tell you to do
2:28 is go to my website.
2:31 rabbitdesign.net
2:33 r a b b i t t design.net.
2:38 Go to my website. Go to my website and
2:40 get over to the professionals drop down
2:43 menu.
2:44 And if you look right here, there is a
2:46 blog, okay?
2:48 Click on that blog.
2:50 So, again, rabbitdesign.net.
2:53 Oh.
2:54 There we go, okay?
2:56 Professionals drop down menu, click on
2:58 this blog.
3:00 Then once you've clicked on this blog,
3:03 there's going to be a little button
3:04 right here. Download the Chief Architect
3:06 X18 MCP installation kit. Here's what
3:10 that kit is. I'm trying to make life a
3:12 little bit easier on you.
3:14 Um
3:15 I take no benefit of this other than um
3:18 helping the community get this set up.
3:20 I'm fully on board with this.
3:22 Um could I have just kept this to myself
3:25 as long as possible and gone and charged
3:27 people to go get their plans done um
3:30 a lot easier without me have having to
3:32 actually do any work? Yes, I could have.
3:35 But no, let's get in this together.
3:38 Let's all get there together. Let's all
3:40 make some money. Let's bring the whole
3:41 community up and talk about it, all
3:44 right?
3:45 And hopefully this just drives us
3:46 forward and helps keep producing better
3:49 and better workflows.
3:50 So, you're going to download this
3:52 package. What this package is is it's
3:55 it's like an installation kit. It's an
3:57 instruction kit for your AI.
3:59 What you will need is some an an AI that
4:05 can communicate with an application on
4:08 your
4:09 on your machine.
4:11 Um
4:12 So, your Chat GPT, your Claude, those
4:15 are a couple AIs, those are frontier
4:17 model AIs.
4:19 Okay?
4:20 Those are to those level that they've
4:22 got some kind of an integration where
4:24 they have a desktop application version
4:27 and they can work on your machine. Chat
4:29 GPT would call that um work mode or
4:32 codex. Uh Claude,
4:35 heck, I don't remember what the heck
4:36 they call it. So, I'm stuck there. Um I
4:39 have Claude on my machine. I probably
4:40 could go look it up.
4:42 But, download this package and then just
4:46 save it in some place where you can tell
4:48 your desktop
4:50 frontier model AI that there is this
4:53 package.
4:55 Go open it up and go install the MCP
4:58 server for Chief Architect. And what you
5:00 could also tell it is if it's not clear
5:03 as day in this package, tell it that the
5:06 MCP server lives in on a PC side,
5:08 program files
5:10 uh Chief Architect
5:12 Chief Architect X18.
5:14 And so, once you have this package, once
5:17 you
5:18 have your AI desktop application
5:21 downloaded on the machine, it should
5:23 know what to do.
5:25 If you try to install it without this
5:26 package, yes, it might work. Okay? You
5:29 might just have to do some back and
5:31 forth and tell it to um install some
5:33 dependent other programs like Python and
5:37 a few other things. So, there's some
5:39 things that require some installation
5:41 here and it might take a little while.
5:43 Uh for me, because I had been using AI
5:46 to do a great number of things, I had
5:48 already had every um all the
5:51 dependencies installed already. So, it
5:54 took 1 minute to get this set up on my
5:56 machine my machine.
5:58 Uh for you, if you you haven't been
6:00 messing around with AI, you haven't been
6:02 doing a bunch of coding or um
6:04 Python scripting, that stuff,
6:06 you're going to need this package. Get
6:08 it installed.
6:09 All right. So, good morning to the chat.
6:10 Boy, I got to scroll up. You guys just
6:12 spattered in here. Very cool. So, uh
6:16 Aaron Liss
6:18 Aaron, you changed your name. Cool.
6:19 Good morning, Aaron.
6:21 Mr. Rose, I got your email. Thank you
6:22 for responding back to me.
6:25 I loved reading that. And then uh Keith,
6:27 morning from Southwest Louisiana.
6:30 Morning to Shane Pittman in Alabama.
6:33 And someone had their coffee. No, I
6:35 haven't had my coffee. I'm uh I'm
6:37 feigning enthusiasm for lack of coffee
6:40 right now.
6:42 I uh I did not quite make it to to make
6:45 one this morning.
6:46 And then
6:48 are we about to knock our socks off? I
6:49 think so. I think so. I'll tell you
6:53 you know, what successes I've had with
6:54 this. And some of those successes are
6:57 very exciting. Um some things I don't
6:59 think it does that well, and it's not
7:01 ready for prime time yet. But
7:03 uh let's stick to what its strengths
7:05 are. And I'd love to hear in the
7:06 comments cuz I know I've got some people
7:08 in here that have been using it as well.
7:10 So, if you have found some method that
7:13 work well for you, share it in the
7:14 comments. I want to hear about it. Um do
7:16 the old trick that uh
7:20 um oh, I'm I'm forgetting who does it,
7:22 but give me the you know, the finger up
7:24 emoji uh a bunch of times, and I'll see
7:27 the the comment in case I miss it.
7:30 Uh good morning, Sharon Mitchell.
7:33 My my my my
7:34 Sharona.
7:36 And then
7:38 Shane says morning again.
7:40 Shane, you don't get to keep saying good
7:41 morning over and over again everybody.
7:45 And Anthony Hayes, good day from
7:47 northern Virginia. Well, we got a lot of
7:49 people in here. Very cool. My first
7:51 Template Tuesdays, Amy Keller. Nice. I
7:54 know that name. I've seen you in the
7:56 Discord server. Cool.
7:58 Daniel Perez
8:00 Shane saying good morning again.
8:02 >> [laughter]
8:04 >> Uh Darian from Southern California. Cody
8:07 um Cody, uh you know, I want you to
8:09 chime in and please anytime you hear me
8:11 say something and you think you've got
8:13 something to add to it, please. I'm I'm
8:15 I'm leaning on you. I want to hear from
8:17 you. I wish I could have gotten it
8:18 together and got you in the show with me
8:20 because I know that you are
8:22 top of the class for this kind of stuff,
8:24 so.
8:25 And then Donnie Cross, good morning.
8:28 Darin, good morning from San Angelo.
8:30 That's right down the street for me.
8:31 Cool.
8:33 And then
8:35 order Canada. Wow, I got so many people
8:37 in here. So cool.
8:39 All right. Hopefully anybody that hasn't
8:41 gotten this set up already has this
8:43 package installed, has AI doing some
8:45 stuff for you. Like I said, just bring
8:47 up your AI.
8:49 Point it to that package, tell it to
8:50 install the MCP server. What does the
8:52 MCP server do? Well, from there we can
8:55 just get into a chat GPT chat. Um
8:59 I don't even like to get it to do things
9:02 like open a file because
9:06 I just know I can do that so
9:08 conveniently fast. If I want to set up
9:11 my
9:12 I'm working with chat GPT. I'm not going
9:14 to show you Claude today. I could show
9:15 you Claude as well. I'm just going to
9:17 stick with one platform. That's it. I
9:19 also have cursor. I'm just going to and
9:21 I also have uh for those of you that are
9:23 interested, you can also get this to run
9:26 on your own local LM something like LM
9:30 Studio where it takes advantage of your
9:32 graphics card and your hard drive space
9:35 where you're going to download something
9:38 like a 50 billion parameter thing. Well,
9:40 depends on your graphics card. You've
9:42 got a um prosumer level graphics card or
9:46 professional level graphics cards like
9:49 4090 series, 5090 series. Um maybe the
9:52 four uh 5080 series then yeah, you're
9:55 going to get up in those 50 billion
9:57 parameter marks. Um if you've got, you
10:00 know, 4070, 4060, um 5070, 5060, that
10:04 kind of stuff maybe you're getting into
10:06 like 24 billion parameters.
10:08 What does that even mean?
10:09 Uh the parameters is just that's the
10:12 amount of data that the large language
10:14 model is trained on. Think of it that
10:16 way.
10:17 I'm not going to give give you precise
10:19 descriptions of this stuff. It's more
10:21 complicated than that. I'm simp- over
10:23 simplifying it.
10:25 Um, so you can in fact install this on
10:27 your machine without having to take up
10:30 credits where you might have a really
10:32 expensive thing that you're purchasing.
10:35 Keep in mind with this MCP server, you
10:39 don't necessarily need some of the more
10:42 expensive models to be running on your
10:45 machine because it's getting into its
10:47 instruction set, so to speak, from the
10:49 MCP server. So, you can dumb it down a
10:52 little bit. You can take it down a few
10:54 models.
10:55 I personally have been keeping it on a
10:57 higher model cuz I just decided to up my
11:00 um
11:00 the payment structure in Chat GPT and
11:03 it's not burning credits that quickly
11:05 for me, so I'm okay with that. And also,
11:08 I find that it's doing a better job um
11:11 when I don't give it enough context.
11:14 So, in the case that I want to connect
11:16 my Chat GPT to my phone so that I'm
11:18 giving it instructions from my desktop
11:20 machine that is running on my computer
11:22 at all times, I mean, that is running at
11:25 all times.
11:26 Um it's just easier for me to keep it on
11:29 a uh a higher tier model. And
11:32 so, I've got a little chat that I've
11:34 pinned here,
11:35 MCP server, and I've got some skills
11:38 I've been developing, okay?
11:41 Now,
11:43 we're going to talk about
11:45 the some of the things that you can set
11:47 up to
11:49 um make this work better for you.
11:52 Because out of the box,
11:54 you'll see that things are happening on
11:56 the screen and you'll be surprised that
11:57 they're happening as quickly as they
11:59 are. I'm going to just start a little
12:00 project here
12:02 in my templates. And for so for those of
12:04 you that have my templates and you don't
12:06 know about this, um my template is here
12:09 pinned at the top of the screen.
12:11 Okay? I'm going to um open and expand
12:14 this. I'm going to expand the layouts
12:16 folder and I'm going to get to a layout
12:19 that I want to use for my next project.
12:21 So, I'm going to pick this layout and
12:23 I'm going to say make a copy with links
12:24 to project. And so, this is just really
12:27 specific to my Pro Plan template that I
12:29 sell. So, if you've purchased this and
12:31 you didn't know this is how I like to
12:32 start a project, this is how I like to
12:33 start a project. So, I just hit new
12:35 project. It brings forward the four plan
12:38 files that I need for this project and
12:40 I'm going to open up
12:42 my template plan file.
12:44 Now that I have this, I could get into
12:46 ChatGPT and tell it to just draw a
12:50 generic house and it will start drawing.
12:53 Um I'm going to do a little voice to
12:55 text.
13:00 I'd like you to draw just a modern
13:02 farmhouse,
13:05 two bedrooms on the right wing
13:07 with a shared bathroom
13:09 and one
13:11 primary bedroom on the left wing.
13:13 And there should be a great room
13:15 attached to a kitchen and then a formal
13:17 dining room
13:18 that projects
13:21 out towards the front of the house.
13:23 There should be an alcove that creates a
13:25 porch
13:27 where the dining room is on the left of
13:29 the alcove, garage is on the right of
13:31 the alcove.
13:33 And then that front door opens into the
13:35 entry. And so, as we walk in through the
13:37 entry, we know that the dining room is
13:39 on the left, great room's in front of
13:41 us, right wings of the house on the
13:43 right side, left wings of the house, and
13:46 then the primary bedroom should extend
13:48 past the back of the house where the
13:50 kitchen and the first bedroom are so
13:54 that it
13:55 um creates a little bit of a wing as
13:57 well and then there should be a deck off
13:59 of the back.
14:02 Uh the plan file's open right now, you
14:04 can just start drawing.
14:08 And so, we'll just let it do its thing.
14:11 And I'm going to minimize this and I'll
14:12 leave Chief Architect open on the screen
14:14 so we can see what happens.
14:16 Now, we're going to see this just start
14:17 drawing. And
14:19 um
14:21 you know, hopefully it follows that
14:22 instruction set. But there's many times
14:25 when we need to draw something far more
14:27 specific than this. Maybe we're not
14:29 doing new construction plans. Maybe
14:30 we're rebuilding something. Right? Maybe
14:33 we're converting um a lot of us in in
14:36 this chat might be uh interior design
14:38 scope or remodel scope, and you're
14:40 getting already complete plans from an
14:43 architect, and you're needing to
14:45 recreate it in Chief Architect because
14:47 they did not create it in Chief
14:48 Architect. And so that would be a a much
14:50 more specific workflow, right? So
14:53 there's a couple of things that you can
14:55 do with this setup once you've got it
14:56 set up.
14:58 Is
14:59 um
15:00 in most of these frontier model
15:03 services, you can create what might be
15:05 called a skill.
15:07 And so you are producing an instruction
15:10 set
15:11 that will be a persistent instruction
15:14 set for how you want this
15:17 software to be used.
15:19 So that you're creating rules such as
15:22 I know that I've already created some
15:24 rules, and I'm going to be sharing these
15:25 over time. I'm I am fully on board with
15:28 sharing my workflows and helping
15:31 everybody improve their workflows. So
15:33 um
15:34 something that I
15:38 I know that I want is
15:40 I know that I want it to be as uh fast
15:43 and efficient as possible. I want this
15:46 to run very quickly.
15:48 And so one of the things I've been
15:49 telling it to do as a skill that is to
15:52 train, meaning it
15:54 think of it as a memory, if you will.
15:55 It's creating a resource file that it's
15:58 going to utilize when it's drawing in
16:00 Chief.
16:01 Here's what I've been doing. I've been
16:02 telling it, "I want you to draw all of
16:05 your walls
16:06 at once, because it can do that. It can
16:08 send a bunch of instructions for a bunch
16:11 of walls at a time."
16:13 And then I'd say, "I don't want you to
16:15 confirm every wall.
16:17 I want you to just send the instruction
16:19 to send all walls and then once all
16:23 walls have been sent, then you can
16:25 confirm the placement of those walls and
16:28 adjust them from there.
16:30 The current version of this MCP this
16:33 this video is not going to last long
16:35 before it becomes outdated because
16:38 currently they have some functions
16:40 restricted. This isn't a fully
16:42 functioning software in terms of the
16:44 MCP, okay? There's some things that we
16:47 cannot do.
16:48 It It can't do much for navigating the
16:51 library browser. There's a few things
16:53 that it can do.
16:54 Um navigating the project browser can be
16:56 a little bit complicated as well. It
16:58 can't delete currently which, you know,
17:01 that's a big bummer for me.
17:04 There are ways around it and I can
17:06 explain those ways.
17:08 Uh we can see here it's starting to draw
17:09 the shape of this house, right? Um we
17:12 can also see here that at times it's
17:13 going to create some uh disconnected
17:16 walls. I want you to note something. I'm
17:18 going to put something else on top of
17:20 the screen here and just note that right
17:24 now
17:25 Chrome is what's in focus, okay? We can
17:28 see this.
17:29 This is what's um the focused program.
17:33 Typically when we're working on a PC or
17:35 a Mac, whatever is in focus is the only
17:37 thing that you can work on.
17:39 So, just know that Chrome's
17:42 the focused program right now. Chief
17:44 Architect still working. They just The
17:47 MCP just switched from an exterior wall
17:49 type to an interior wall and it's going
17:51 to start drawing with that interior
17:53 wall. So, while we are working in
17:56 um you know, maybe I'm going to our
17:58 Facebook group, right? Maybe I'm going
18:01 to my
18:02 my Facebook feed.
18:05 Something like that and I'm doing work
18:07 where I'm or what's even cooler than
18:09 this is
18:10 if you are brand new to doing a frontier
18:14 model in a desktop app application,
18:16 right? If you're brand new to this,
18:18 maybe you don't know. I can also go work
18:22 on something else.
18:23 In code X in this case, I can go, you
18:27 know, start another chat where I want to
18:29 go log in to some service and get it to
18:32 work on something else. I can work on
18:33 multiple things at once with the chat.
18:36 So you can use your AI to be doing work
18:38 while AI is doing work inside of Chief
18:41 Architect. That's what's so fascinating
18:43 about this.
18:47 Just let me get this back to where that
18:49 is. Let's get
18:51 this back up so you can see walls are
18:52 being drawn here. Now it's not perfect.
18:54 It's going to make some mistakes, you
18:56 know.
18:57 Um I've noticed that uh a lot of times
18:59 this is something I'm going to have to
19:00 correct for is when it starts drawing a
19:02 deck, it uh it tends to remove some
19:05 pieces.
19:06 Um
19:07 I usually have the instruction that uh I
19:09 don't need you to create the room types.
19:12 Leave that for me because I'm usually
19:14 thinking I'm going to do some redesign
19:15 anyways, so I don't want to start naming
19:17 rooms.
19:18 Um I've got some instruction sets about
19:21 um wall types to use or just ignore
19:24 trying to change wall types because I'll
19:27 do it for you or I'll bring in another
19:29 instruction set for that. So there's
19:31 these are some ideas for you.
19:33 Um
19:34 I got some instruction sets about
19:38 you know, how I want windows placed, to
19:40 ask me about what windows I want, etc.
19:44 Um so you can see, my hands are off. I'm
19:46 not controlling Chief. Chief is being
19:49 controlled by the AI.
19:51 So a few things
19:54 else that I want to mention.
19:56 If you if you want to do some more
19:58 complex actions, it's capable of doing
20:01 that.
20:02 You can
20:04 write you can get your chat to write
20:07 specific instruction sets
20:09 for Python to execute specific actions
20:13 for Chief Architect. So for instance,
20:16 um maybe a more complex one would be
20:19 that I want to
20:21 um save the process for
20:25 uh let's say accessing an item in my
20:27 library.
20:29 I can write a Python script for that.
20:32 And so, what that would do is I write a
20:33 Python script. I'm going to say, "Hey,
20:35 we're going to um
20:37 hit these set of modifier keys, these
20:38 set of hot keys. That's going to bring
20:41 my library into focus. I want you to
20:42 search this term. That's going to bring
20:44 some filtered items into focus.
20:47 I want you to click enter, hit tab three
20:49 times.
20:51 That's going to do something to that
20:52 library item. And then send it back to
20:54 the MCP server. You will have an object
20:58 that you're capable of placing at that
21:00 point with the MCP server. Why? Why
21:02 would I do that? Because
21:04 right now it might not be capable of
21:06 finding that library object because the
21:08 MCP server limits it in its instruction
21:11 capability set. So,
21:13 that's where we might write a script to
21:15 do things where the MCP has hit its
21:18 limit. So,
21:20 it's not that you can't have it control
21:22 the computer. You can.
21:24 I currently have it set up so that it's
21:26 using MCP server only.
21:29 Meaning that it's not going to control
21:30 the mouse
21:32 specifically to hover over things like
21:34 project browser and click on things in
21:35 project browser or click on things in my
21:38 toolbar. All right? It will It does have
21:41 the ability to move the mouse in our
21:44 sheet space, in our drawing area. It has
21:47 that built into the MCP server. Outside
21:50 of that, the bounds of that, it's not
21:52 going to do anything in terms of
21:53 clicking on menu objects and library
21:56 objects in project browser. So,
21:59 you can still get it to do some agentic
22:02 tasks where it controls the computer and
22:05 and is a full scope thing.
22:08 Just know that when you get into an
22:10 agentic mode that's not MCP, you're
22:14 you're potentially burning credits at a
22:16 much faster rate. And this is something
22:19 that's going to be important to us if
22:20 we're not just buying the most expensive
22:23 uh subscription plan, okay?
22:25 So, um
22:30 Yeah, look at it go. It's building us a
22:32 house. Isn't this cool?
22:35 Let me uh check in on the chat here.
22:41 Luna Someone's saying Luna works great.
22:43 I've had some success with Luna, and
22:45 I'll tell you when that success is.
22:47 We're going to stop this um drawing the
22:49 model pretty soon here, and I'm going to
22:51 show you, you know, when I need it to
22:53 draw from context, right? When I need it
22:56 to um draw a specific house, but that is
23:00 when I have um had difficulty with Luna,
23:03 except for when I do one thing. And the
23:06 one thing that I'll do, in fact, we can
23:08 stop this. This is proving that this is
23:10 working, right? This is This is that wow
23:12 factor, right? Now, let's get it to draw
23:14 something specific. I'm going to go look
23:16 up uh let's just look up some generic um
23:19 stock homes.
23:23 And
23:24 You know what? I don't want to promote
23:25 that because
23:27 Let me Let me go find a house I've done
23:29 before. Let's just go
23:31 find one in my old archives here. I'm
23:33 going to find this on a little side
23:35 screen.
23:38 So,
23:41 we're just going to get into some
23:43 archives of PDFs that I've done.
23:55 Example
24:01 And
24:06 Do this one. Why not?
24:12 Example example as built
24:17 Yeah, here we go.
24:19 Here we go.
24:21 Let's take this one.
24:26 So, I'm going to stop my AI.
24:31 Draws this.
24:38 And I'll throw this up on side screen.
24:41 We're just going to say okay to this.
24:42 That's okay.
24:44 And it's going to remember all these
24:46 rooms.
24:48 Maybe I'll do a brand new plan file.
24:51 We'll save this. We'll come back to
24:52 this.
24:55 We're going to come back to that model.
24:56 We're going to do a new model and the
24:59 uh plan file is open on the screen and
25:01 go ahead.
25:03 I want you to trace from the existing
25:04 PDF.
25:06 Oops, that didn't accept anything I just
25:08 said.
25:19 Here's what I'm going to do. As-built
25:21 redacted. There we go.
25:29 And so, this is when
25:31 those um less expensive models works
25:35 well for me, okay? It's when I give it
25:38 something to trace.
25:40 And so, I've got a PDF here. I'm going
25:42 to resize this PDF.
25:46 I'm going to resize it based on
25:50 a little point-to-point resize.
25:52 23 ft 9 and 3/8.
25:55 Get in here real tight.
26:03 Actually, looks like it's the right
26:04 size. I'm going to get this
26:06 in a place where it's going to draw this
26:09 um upstairs first. Why not?
26:13 I like to set this up ahead of time. I
26:15 know it's two stories. Let's build a
26:17 second blank story.
26:19 Okay?
26:20 This is That's what I like to do.
26:22 So,
26:24 that way I can take this PDF, drop it
26:26 upstairs.
26:29 It's just an old as-built report I did.
26:31 And then I don't need to confuse it. We
26:33 can just limit it to just the plan right
26:36 there, just like that. Okay?
26:39 And then
26:40 hey, might as well confirm something.
26:43 Let's just confirm that this overall
26:44 length is roughly
26:46 uh 23 ft. Yeah, perfect. So, this is
26:50 scaled appropriately. Bam.
26:58 I put that on project on hold. We'll get
27:00 back to that one. I've got a new one up
27:02 on the screen and it's ready to go.
27:05 Please just trace over the existing
27:07 image.
27:09 Draw your walls, windows, and doors.
27:13 Don't bother naming rooms.
27:19 So, I'm going to switch my model.
27:21 I'm going to show you how this is done.
27:23 I'm going to switch my model down here
27:24 at the bottom.
27:26 Okay? If you're using Chat GPT,
27:29 bam.
27:30 I'm going to click on this.
27:32 And we're going to try Luna.
27:33 Okay?
27:36 And then there we go.
27:38 Let's set that going.
27:41 And we'll see how it does. This is where
27:43 I I really feel like the AI does a great
27:46 job, pretty good job, I should say.
27:49 Um is that I I find that it does a lot
27:52 better just tracing over an image the
27:54 way it does screen capture to confirm.
27:57 Um it's going to screen capture first to
28:00 have it in its own
28:01 um
28:03 model context, and then on top of that
28:06 it will continue to screenshot after
28:08 it's done some things to confirm
28:10 placements of things.
28:12 Um it's
28:14 it's important to train skills on
28:17 correcting hinge side. It seems to have
28:19 a problem with that, hinge side and
28:21 swing side, okay, for doors.
28:24 And then uh it has a challenging time
28:27 placing side by side windows, I've
28:29 found, so
28:31 you know, there's a little bit of back
28:32 and forth with this. Uh what's fantastic
28:34 about this is you don't have to be at
28:36 your computer for this. I could go get a
28:37 coffee right now and just let you guys
28:39 watch this, right?
28:41 So,
28:42 um
28:44 let me uh let me get back to you guys.
28:46 What are we What are we all saying?
28:54 Alabama.
28:56 >> [laughter]
29:01 >> All right. Hey, we got Mike in here,
29:03 too. Cool.
29:05 Yeah, I know, Cody. I should have
29:06 invited you.
29:08 You know, I don't really set these
29:09 things up like I should.
29:11 >> [laughter]
29:12 >> Just
29:13 there's a lot of winging it on template
29:15 Tuesdays.
29:17 Morning, Ant.
29:21 Home run, dude. Who are you? I'd love to
29:23 get familiar with the uh the screen
29:25 name.
29:26 Reformed done, who are you?
29:29 Greetings from Maine.
29:31 Greg here. First template Tuesdays. Greg
29:33 who? Give me Give me your last name.
29:35 I love being familiar with who's in the
29:37 chat. Um just from our experience being
29:39 on all these different platforms and
29:41 everything, I try my best to keep up
29:43 with who all of you are
29:45 uh cuz I like uh getting to know you.
29:48 And hey, the hat's big pimpin. Thank
29:49 you. I haven't worn this thing in a
29:51 while. I know, I need to I need to re-up
29:53 my shop and throw some new hat models in
29:56 there.
29:58 In my area, this kind of like this five
30:01 panel is going out of style. They want
30:02 these new seven panel low profile hats,
30:04 so
30:05 uh but I wear it every once in a while.
30:09 Uh will there be a step-by-step on
30:10 actually how to set it up? So, in case
30:12 you missed it, I'm just going to repeat
30:14 this for the class.
30:16 In case you missed it, you can always go
30:18 back to the beginning of this video, but
30:20 um the setup is that um
30:23 first of all, start with whatever front
30:26 well, it doesn't need to be a frontier
30:27 model necessarily. It just needs to be
30:29 an AI that can
30:31 um
30:32 communicate with an MCP server on your
30:35 machine. So, we know chat GPT does that.
30:38 We know Claude does that. We know cursor
30:40 does that. We know Grok does that, okay?
30:44 So, you can use any of those different
30:45 AIs. There's some AIs that are like an
30:48 aggregator kind of thing where they
30:49 allow you to access those models.
30:52 There's There's too many AIs to list.
30:54 So,
30:55 um
30:56 and I'm just calling them AIs. That's
30:58 not even the correct term for them.
30:59 That's what we're just going to call
31:00 them.
31:01 And so, get that installed. Get it
31:04 installed on your machine. Follow
31:06 whatever their instructions are to get
31:07 that installed on your machine.
31:09 Uh for chat GPT, it's as simple as just
31:12 go look up chat GPT desktop application
31:15 and download it and get it installed and
31:18 let it um authorize some of the things
31:20 it needs to authorize to control some
31:22 things on your computer. And then you
31:24 can get into settings to limit how much
31:26 it has control of or you can change it
31:28 so that it has to ask for approval to
31:31 control things on your computer. It is
31:34 going to need to do certain things with
31:36 um some kind of a terminal. So, um
31:41 you know, Windows PowerShell if you're
31:43 on a PC. Um some kind of a um like a
31:46 command line thing. So, some kind of
31:48 terminal. It's going to need to get
31:49 access to that. Why? Because it has to
31:52 write in some Python. Um it has to
31:55 download some Python packages and a few
31:57 other things.
31:59 Once you've got your AI installed on
32:02 your machine, go look up on the blog on
32:04 my site. Professionals drop-down menu.
32:07 Check out this blog.
32:09 There's a download here, okay? It's
32:11 first button right here. Download this
32:13 stuff, okay?
32:14 Um
32:15 uh I'm not trying to give you any any
32:17 kind of viruses or anything like that.
32:19 Run it through your virus scan. Doesn't
32:20 matter. It This is just a basically a a
32:23 robust instruction set. Here, I'll
32:25 download it myself.
32:27 Downloads.
32:30 Here we go. In my downloads folder, I
32:32 have something that automatically unzips
32:34 things. So, if I just wait a couple of
32:36 seconds,
32:38 we should see this.
32:40 Uh
32:42 What was that even called? I'm not sure.
32:45 Here we go.
32:47 And so here it is. There's a markdown
32:49 file that's an installation guide.
32:52 There's a little readme markdown file.
32:55 Okay?
32:56 Um I have developed some skills. You can
32:59 install those skills. Maybe you like
33:02 those skills. You might have to adjust
33:04 them if you want. And then there's um
33:07 codex config file. Yeah. So there's some
33:10 files here for you to get this set up a
33:12 little bit easier than just having it um
33:14 done by chatting with your AI to ask it
33:16 to set it up for you is you just tell it
33:19 to go, you know, look at this folder.
33:22 Look in my downloads folder for the
33:23 Chief Architect X18 MCP Template Tuesday
33:27 file.
33:28 And then
33:30 install um the MCP server protocol
33:34 stuff
33:35 so that I can integrate with my chat
33:37 model.
33:40 Here we go. It's kicking off. It's going
33:42 away. You know, it's making some errors.
33:44 It's going to fix them over time.
33:46 Um
33:47 one of the things that my skill says,
33:49 and which I found is when it's dumping a
33:51 bunch of interior walls at once, it's
33:54 important that you get your at least
33:57 from my experience at this date, which
34:00 we're, you know, almost to Halloween.
34:02 It's the 27th of October 2026.
34:05 As of this date, I found that I needed
34:08 to get my AI to turn off object snaps.
34:13 Turning off object snaps made it so that
34:15 it would stop drawing these off-angle
34:17 walls cuz that was my experience. It was
34:19 drawing these off-angle walls. Okay?
34:22 Um so that's in my skills.
34:24 So something to keep in mind.
34:27 Um
34:28 one of the next things that I think is
34:30 just fantastic about this, and I used it
34:33 last night, is that
34:36 especially if you have my templates.
34:39 If you have my templates, you know that
34:40 there is a title block and spec plan.
34:44 That title block and spec plan has some
34:47 input that we could do for project
34:48 information.
34:52 While I'm talking, let me see what's
34:53 going on here. Yeah, it's still working.
34:55 Um
34:57 what I did last night was all I had was
35:00 an address
35:02 for a project and I wanted to and this
35:05 was for for a potential client.
35:08 And
35:10 I go to bed.
35:12 I I have
35:14 my AI start drafting some stuff and then
35:17 on top of that, all I did was I told it
35:20 the address. I said, "I need you to go
35:22 look up all of the information that we
35:24 need. We need assessor's parcel number,
35:27 okay? We want the book ID. We want the
35:31 um occupancy code. We want the Go ahead
35:33 and list the construction type as as VB.
35:36 I want you to get all the wind seismic
35:38 loads correct. I want you to get all my
35:40 front and side setbacks correct. I want
35:42 you to go look up the um it's public
35:45 record. Go look up the the last person
35:47 that purchased this property. Put that
35:49 as as the client. Put their information
35:51 in there.
35:52 I want you to and that's it.
35:55 I just had an address and this filled
35:58 out all the information I needed for my
36:00 title block.
36:02 And
36:02 >> [laughter]
36:02 >> I mean
36:03 that's
36:04 that kind of information, getting that
36:06 kind of information all together, not
36:09 only was that a stressful thing for my
36:11 majorly ADD brain, but
36:14 I mean, it took me it used to take me
36:15 hours.
36:16 And so now it's just doing it without me
36:18 even having to pay attention to it. Heck
36:20 yeah. I'm sleeping like a little baby.
36:23 I'm getting the best sleep of my life.
36:25 >> [laughter]
36:32 >> Um so SB5325, let me know if you um if
36:36 you have any more questions about this.
36:43 Key strokes, yes.
36:45 MCP server can send key strokes. Just
36:47 know that some key strokes will not be
36:50 accepted from the MCP server like
36:52 delete. Doesn't matter if you sign
36:54 delete to some new hotkey, it recognizes
36:57 what the delete action does and it
37:00 rejects it. So, there are some things
37:02 that it will reject. So, to delete, um I
37:05 will just tell you here's in my
37:07 instruction sets if some things need to
37:09 be deleted and it's stuck, you could
37:12 either tell it to stop, you know, using
37:15 MCP and instead,
37:17 um go send it to the delete key as an
37:21 agentic, um approach.
37:24 Or what I have it do is I just have it
37:27 move the objects that it needs to delete
37:32 2,000 in to the left. And so, when it's
37:35 done drawing, I just know look 2,000 in
37:38 to the left and there will be maybe a
37:39 puddle of things that need to be deleted
37:41 and that's really simple for me to do.
37:44 So, it um don't let that hang you up
37:46 that we can't get this to delete things
37:49 because it's going to make errors. It's
37:51 going to think it needs to delete
37:52 something and it can't.
37:54 And that's going to hang you up. So,
37:55 instead, just tell it to move things to
37:57 the left or to the right or what have
37:59 you. Just make a rule for it instead.
38:03 Uh did I import the PDF or an image
38:06 file? I imported a PDF, but you could do
38:08 either or, PDF or image file, up to you.
38:12 Um Victor,
38:14 you're the one that uses the finger
38:15 pointing
38:16 finger pointing emojis. That helps me to
38:19 look look at stuff in the chat.
38:24 Sarasota, Florida. Cool.
38:27 Nice, first template Tuesday. Who are
38:29 you, Ocean Builders? What's your name?
38:31 And Mr. Todd Beck,
38:33 Todd Beck, excuse me.
38:35 Mr. Todd Beck. Todd, still wanted to
38:37 thank Todd if you didn't see template
38:39 Tuesday what, 30 or 29 or something like
38:42 that. Um Todd was the one that pointed
38:45 me to the ability to um assign hot keys
38:49 to toolbar items that are custom placed
38:52 library objects.
38:53 Uh where we can get hot keys
38:55 to access things that are in our
38:58 library. It's very cool.
39:00 So, I'd go walk watch that template too.
39:02 If this is your first template Tuesday,
39:04 um know that the previous template
39:06 Tuesdays are in
39:09 the
39:10 VIP side of my YouTube, okay?
39:15 So,
39:16 um go spend 35 bucks.
39:19 Spend 35 bucks, then cancel it, and go
39:21 watch all the videos.
39:23 Because that one's a particularly good
39:24 one where anything that we place into
39:27 our toolbars has the ability to have a
39:29 hot key assigned to it. That's a really
39:31 good template Tuesday to go check out
39:33 for those of you that this is your first
39:35 one.
39:43 Been on Chief for a year or so.
39:45 Nice.
39:46 A relatively short time period. You
39:49 would be what we call a beginner.
39:51 Yeah. Um usually I always say
39:54 people are intermediate level for about,
39:56 you know, 5 6 years.
39:58 And then you get into that advanced
40:00 level. But nowadays,
40:02 with this as as a little helper, I think
40:05 everybody could be a little bit more
40:08 advanced.
40:09 Uh any killer a little ask Claude how to
40:12 set it up, and it walked me through it
40:13 including all the Python settings
40:15 through PowerShell. Nice. Yeah, it will
40:17 walk you through it. If you don't want
40:19 to be walked through it, and you want it
40:20 to just
40:22 do the setup for you, that's what the
40:24 that download package is for.
40:28 Um do I have nunchuck skills or bow
40:30 hunting skills?
40:32 Um it's been a while since I've used the
40:34 nunchucks, but yeah, I got a compound
40:37 bow downstairs.
40:39 I'm pretty good with it.
40:45 Johnny, it's exciting, but we all know
40:47 where this is going.
40:49 Yes and no. Yes and no. Um I'd like to
40:52 remind people that
40:55 when AI is successful
40:58 at doing things,
41:00 um it usually means that it has billions
41:03 of parameters.
41:05 I would like to remind everybody that we
41:09 don't have billions of homes. So, we
41:12 don't have billions of construction
41:14 documents. We certainly don't have them
41:18 publicly registered and in a huge um
41:22 online repository.
41:24 We only have thousands of homes online,
41:27 which makes it a really small subset of
41:30 data. So, I know you're all fearful that
41:34 this is going to take your jobs, but we
41:36 don't have the data.
41:38 And
41:40 when we hit a lack of data, then that's
41:43 when people take it upon themselves to
41:45 start programming limitations and
41:47 directions. And so, you could try to
41:50 program something to hey, when we want
41:53 to build um some kind of a modern
41:55 farmhouse, we are going to limit our
41:58 already limited subset of data down to
42:02 only things that are considered
42:03 farmhouse. Now we're down dealing with
42:06 maybe a thousand farmhouses. Are you
42:09 worried that AI is going to figure out
42:11 how to design the next best farmhouse
42:14 when all it can do is look up a thousand
42:17 farmhouses and get variations from
42:19 there?
42:20 No, it's not going to produce some
42:22 unique house that's going to suddenly
42:25 take away our value. So, just keep that
42:28 in mind. There is not enough data in our
42:30 field
42:31 for this to take over. It simply doesn't
42:33 exist. It would need to produce a whole
42:37 gang load of houses for it even to have
42:40 the data. Guess what? If AI is the one
42:42 producing all the gang load of houses,
42:46 is it going to give us anything unique?
42:48 No, it's not. It's not going to give us
42:50 anything unique. So, the context for our
42:53 industry is going to be lacking because
42:56 simply speaking, we just don't have
42:58 enough data.
42:59 So, I know you we want to say this this
43:02 kind of a I call it a little bit of doom
43:04 and gloom where we think that AI is
43:06 going to take over everything that we
43:08 do.
43:09 It's just it's not the case. It's um
43:12 we just don't have enough data. There's
43:14 certain things in this world where we
43:16 just don't have that much public online
43:18 data for it to be trained on.
43:20 And that's when people are really
43:21 getting in and doing programmatic
43:22 limitations and directions. And so, yes,
43:26 through programming, you can get some
43:28 things to look pretty good sometimes. Is
43:30 this going to become a thing where it's
43:33 exponentially increasing its
43:34 capabilities as we go as we've seen it?
43:38 No, I think we got that huge influx and
43:40 boom. We're going to continue to see
43:42 some growth, right? But, it's not going
43:45 to suddenly know how to design every
43:47 house that you run into. It's certainly
43:49 not going to know how to deal with
43:51 remodels in Oakland, which are just
43:53 crazy where we've got weird things
43:56 happening in every single house here cuz
43:58 we've got
43:59 five different um
44:02 construction booms where we remodeled in
44:06 five different decades here in my area,
44:09 and it's a mix match of styles and
44:11 there's no way you can train AI to deal
44:13 with all that stuff. So, I still have a
44:16 job. I'm still going to have a job. So,
44:18 it's it's great to think that, you know,
44:21 that this is the capabilities are going
44:22 to increase. This is a tool. Just keep
44:24 that in mind. Um
44:26 There you go. For those um out there
44:29 that really don't want to use AI cuz you
44:31 hurting it um you think it's hurting the
44:33 environment, um a few of you've heard me
44:36 say this live and in person or message
44:38 you directly, but I will uh propose a
44:41 different thought, which is
44:43 um
44:45 the
44:47 uh
44:48 we suddenly have funding to change the
44:51 way that we do computing.
44:53 It is suddenly a viable option to invest
44:56 in things that make it so that we are
44:58 not using all of our valuable resources.
45:03 Yes, we're going to still continue to
45:05 utilize those valuable resources. We're
45:07 still going to have a RAM shortage for a
45:09 while. Rare metals, you know, water, all
45:12 these things, silicon, all the stuff
45:14 that we're we're doing right now to just
45:16 keep on throwing
45:19 more of the same bad solutions on the
45:21 same bad problem, but because this is
45:24 suddenly such a big industry, billions
45:28 and billions of dollars going into this
45:29 industry, we suddenly make it viable and
45:33 the funding is there for us to explore
45:35 new things such as
45:38 um photonic computing, where we are
45:40 using photons instead of electrons to do
45:45 our computing, our processing power, all
45:47 that stuff. So, um bear in mind the fact
45:50 that we're going to keep utilizing this
45:52 the fact that AI is going to continue to
45:54 take off. It is producing
45:57 the need for us to go find alternative
46:00 means for computing that will not hurt
46:02 our environment as much. Um there are
46:05 just recently, just this last year, it
46:07 was $400 billion invested into photonic
46:10 computing, which means, you know, um if
46:13 we just think about it this way,
46:15 uh if you think about just electrons,
46:17 they're producing heat.
46:18 Most of the resource problems that we're
46:20 dealing with is um around the fact that
46:22 we're producing heat, right? We need to
46:25 dissipate that heat. Rare metals that
46:27 dissipate that heat faster. Um rare
46:30 um compounds that we're producing that
46:33 dissipates heat faster, you know,
46:35 cooling systems that dissipate heat,
46:37 water dissipate heat. It's all about
46:39 heat, really.
46:40 Um so, with photonic computing, we're
46:42 not producing that heat, so we don't
46:44 have that need anymore. We're also not
46:47 utilizing We're not having the same
46:49 power needs. Um lower power consumption.
46:52 So,
46:54 believe it or not, AI might actually
46:56 introduce um some huge huge innovation
47:00 in the industry. We've been building
47:01 computers the same way we've been
47:03 building computers since the first
47:04 computers ever built.
47:06 So, it'd be pretty cool if we all of a
47:07 sudden started innovating and built
47:10 computers in a new way.
47:11 So, food for thought for you out there.
47:14 Uh let's see.
47:19 Paying 35 forever you find a genius.
47:20 Hey, I appreciate that mindset. I love
47:24 that mindset. My community has made this
47:27 possible for me to do stuff like this
47:30 with you guys.
47:31 Um
47:32 that has never been lost on me. I spend
47:35 um a couple trips a year going and
47:38 thinking about what my community has
47:40 done for me and what this software has
47:42 done for me and what Yeah, I mean
47:45 I thank you guys, really.
47:47 Um
47:47 yeah, if you want to go
47:49 buy my YouTube subscription just to
47:51 support me, yeah, I couldn't thank you
47:54 enough for that. I I find that to be a
47:56 very beautiful approach to helping each
47:59 other learn.
48:01 Uh can this accomplish an AI enhancement
48:04 of a three-camera rendering with CA? So,
48:07 here's what's great. I do have an
48:08 instruction set in here for
48:11 um
48:12 for how I want my renderings on my main
48:14 screen. It's a watercolor rendering. So,
48:17 I'll just show you in I'll scroll scroll
48:20 up my chat.
48:23 Is
48:24 um I still took it to chat. I didn't
48:27 need to. I could have had it replace it
48:29 right in Chief. It just so happens to be
48:30 that I was in a hurry and I wanted it
48:33 done. But, here you go. I sent it a map,
48:36 okay? And I sent it um a real rough
48:40 rendering of the front of
48:43 the house that I was um
48:45 dealing with and then it came back and
48:48 did exactly what I needed, which is
48:50 these are my parameters for how I wanted
48:52 that map re-rendered. So, my parameters
48:54 on how I wanted the front of this house
48:57 re-rendered. So, it can do this um
48:59 hands-off, too. You can say pull a
49:02 camera view.
49:03 Um take a screenshot, replace this.
49:05 Actually, I don't even think it's a
49:07 screenshot necessarily.
49:09 Um
49:10 you can ask your AI to explain to you
49:14 what the capabilities of the MCP server
49:17 is, so that you get a list of of things
49:20 that it does, so that maybe that gives
49:22 you some ideas.
49:23 But, I happen to know that it will
49:26 um take a rendering right from Chief,
49:29 replace the image that's there.
49:31 Right right inside of Chief. So, you can
49:35 get it to take a rendering, send it to
49:37 layout, replace it with your AI
49:40 generated version, and it will do that.
49:45 Um I don't know what the server's hung
49:47 up on this. Now, we haven't seen it
49:48 doing anything in a while, I feel like.
49:55 Yeah, and it's still doing a really bad
49:56 job. Um yeah, this is where I I just
49:59 don't think that Luna model
50:01 does a great job. I think Luna does a
50:03 great job at just
50:05 um design, you know, but following
50:09 an existing setup, I don't think it does
50:11 as well at.
50:16 And I think it's performing really
50:18 slowly right now.
50:21 But, we'll let it keep going.
50:30 Yeah, open up a lot of possibilities for
50:32 the MCP with the pro plan. Yes, because
50:34 you can get the MCP to send hot keys.
50:37 You combine that with that previous
50:39 Template Tuesday video on how to set it
50:41 up, so that you are assigning hot keys
50:43 to custom place library objects. And
50:46 now, all of a sudden, you can build
50:47 custom toolbars that are serving your
50:50 needs, where you're sending the MCP
50:52 specific hot keys that trigger those
50:54 toolbar icons to place,
50:56 you know, your specific items. So, um
50:59 absolutely, these two videos go really
51:01 well with each other. Thank you for
51:02 mentioning that, Donnie.
51:07 Um I'm guessing the chat slowed down cuz
51:09 you guys are all messing around, aren't
51:11 you?
51:12 >> [laughter]
51:14 >> Perhaps so.
51:21 Yeah, I was hoping that this would kick
51:23 off a little faster. I should have stuck
51:25 with a faster model cuz we're burning
51:26 through our time, but let me stop it
51:28 real quick. I'm going to stop it and I'm
51:29 going to switch to just showing you how
51:31 I can input information about something.
51:34 So, um
51:35 if you've watched any amount of my
51:37 videos, you know that um my
51:40 my house is public knowledge. Um anyone
51:43 in the world could bomb my house. We
51:45 know exactly where it is.
51:47 Send me a care package. Uh so, I might
51:50 as well use my own info. Why not?
51:53 Um so, let's do this. I'm going to stop
51:55 this.
51:58 And I'll just shut this dialog box down.
52:01 I'm going to open up title block
52:02 inspect.
52:04 And I'm going to change gears and say
52:10 I'd like you to open up project
52:12 information and um I'm on a live stream
52:15 right now. We're doing a demonstration.
52:17 So, what we're going to do is I'm going
52:18 to have you input all the project
52:20 information for my own house. So, I want
52:22 you to put me as the client and I want
52:25 you to put any information that you
52:27 found about my house into the project
52:30 information fields including the
52:31 assessor's parcel map,
52:33 the book ID, all of the
52:36 um design criteria, and on top of that
52:40 any kind of front side setbacks,
52:43 uh zoning codes. Um don't touch my
52:46 climate zone cuz that's an automatic
52:48 lookup and then uh go ahead and put in
52:51 the occupancy group, etc.
52:54 And
52:55 do not touch any of the CRC
52:59 uh IRC NBC code criteria.
53:06 And let's see what it does. We'll see
53:08 how good it does. And that'll pretty
53:10 much take us to the end of the show. Um
53:12 this is your chance is if you want me to
53:14 pivot and give you some answers and you
53:16 got some questions, um this is your
53:18 chance to ask me those questions. I
53:21 imagine that next Template Tuesday will
53:23 we will do a little bit of continuation
53:26 of this Template Tuesday so that we can
53:28 answer anybody's questions that um
53:31 people might be running into.
53:34 I probably will show you some Python
53:36 scripts that I've scripted so that the
53:39 my
53:41 AI executes those Python scripts to do
53:43 specific tasks and then from there uh it
53:48 picks back to the MCP. So you can have
53:50 it doing things where it's like
53:52 you know, MCP only MCP only. Oh, execute
53:55 a Python script, come back to MCP, MCP,
53:57 MCP, bam.
53:59 Um
54:00 I'll tell you that um Cody and uh
54:03 Anthony Reed, for those of you that have
54:05 my full library and putting out library
54:08 updates, um
54:10 we know that Chief Architect does not
54:13 allow you to import a library file where
54:17 there are duplicates and have those
54:19 duplicates be overwritten by the
54:22 imported library file, right? Which
54:25 forces us to go delete the library and
54:28 then delete our trash library, which is
54:31 a very
54:33 very time-consuming set of actions.
54:37 Um yes, you can write a Python script
54:40 for it to get the MCP to go delete that
54:44 stuff and just walk away from it, not
54:46 worry about it.
54:48 But what they're working on and should
54:50 be easy enough to accomplish
54:53 is that you get a
54:55 um
54:57 get a Python script to analyze
55:00 a previous library
55:03 to the most updated library. You can get
55:05 it to compare it. You compare unique
55:07 IDs. You compare all of the context of
55:11 each unique idea of every object in the
55:13 library that's in that library file on
55:16 your machine before you install it in
55:19 Chief. So, you got two um library files,
55:22 an old version, a new version on your
55:24 machine downloaded.
55:26 You can get Python to um execute a
55:30 script to compare the two, then list all
55:33 of the things that have changed.
55:36 From there, of that list of things that
55:38 have changed, you can then get it to
55:42 take action in your library to go
55:44 through, find those things in the
55:46 library, just delete those things that
55:49 have changed, and import a custom new
55:53 library file that is just the objects
55:56 that were changed. So, here's the
55:59 action. Comparing two libraries,
56:01 you are then producing a new library of
56:04 just items that have changed.
56:06 Okay? Or new items.
56:09 Then, you have MCP, together with a
56:12 Python script, go target those items in
56:14 your active library, delete them, empty
56:17 the trash. Then, you get to install just
56:19 that package that's the difference,
56:22 right? So, that suddenly takes that
56:24 action from, you know, 30 minutes to an
56:26 hour on some slower machines to maybe it
56:29 only takes 15 minutes, and it's
56:31 hands-off.
56:32 So, it's just some of the things you can
56:34 do when you get into some of the more
56:36 advanced workflows with this. And so,
56:38 we'll keep going through and discovering
56:39 this.
56:40 Um uh-oh.
56:46 Oh, I didn't know my address. Haha.
56:50 That's why it's hung up.
56:59 All right, give me my address. Let's see
57:00 if it finishes before Oh, it's got 3
57:02 minutes. I don't think it's going to
57:03 finish that fast. So, maybe we're in
57:05 We'll run 5 minutes long.
57:18 >> Um Codex and Chat GPT, it's like, you
57:21 know, next week Claude's going to be
57:22 better than Chat GPT. Then the next week
57:25 Chat GPT will be better than Claude. I
57:27 think Claude's fine. I've just been
57:28 sticking with Chat GPT. Um
57:31 that's just the
57:34 for the conversations I've previously
57:36 had. I have a longer history with Chat
57:37 GPT than I do with Claude. Um
57:40 3 and 1/2 years ago is my first
57:43 code uh ever written in Chat GPT. So, I
57:46 have a lot of context that I can draw
57:49 from. And so, it knows
57:51 my stuff better. And so, that's why I
57:53 stick with Chat GPT. That's the only
57:55 reason.
57:56 Um I had a
57:58 a period of about
58:01 I don't know, 3/4 of a year where I used
58:03 Claude. Um I had a period of about a
58:06 year where I used Cursor. So,
58:08 you know, I have yet to combine all the
58:11 contexts together, which I should do.
58:14 Um that would be a good thing to do is
58:17 get these individual services to write a
58:19 markdown file to give all the context of
58:22 all the conversations I've ever had. So,
58:24 every one of them could be working from
58:25 the same playing field, right?
58:29 And then, can the AI do a review of
58:30 plans to find particular errors such as
58:32 our walls to mention? Absolutely.
58:35 Absolutely. That's I mean, that's
58:37 another big thing that you could be
58:38 doing with this just to give you more
58:41 ideas and pump you full of more ideas is
58:43 that
58:44 there's nothing keeping you from having
58:46 this do a plan check for you. Check all
58:49 your windows for egress. You know, my
58:52 pro plan does a pretty good job of of
58:55 finding if your windows meet egress or
58:58 not, but nothing keeping you from
59:01 getting the AI to check this as well.
59:03 So, that it checks parameters and
59:04 cross-checks codes online.
59:07 Um
59:08 you can get it to check your
59:09 construction document. Make sure you
59:11 haven't missed anything from your
59:12 jurisdiction.
59:13 Um especially if you start training it
59:15 with a skill where you are
59:18 um
59:19 you know, you can get it to train skills
59:21 just by giving it a images and text
59:24 context and voice to text and voice
59:26 memos and all that stuff. Keep in mind,
59:28 you can also record actions you doing
59:32 actions on a screen. Thank you to one of
59:34 our community members. I think that was
59:36 Anthony
59:37 um Reed who said, you know, get it to
59:39 record video of you doing an action so
59:42 that it understands what that action is.
59:44 You can get it to do that as well.
59:46 So, um but training your model is going
59:49 to be very important. Are you going to
59:51 get incredible results out of the box?
59:54 Maybe, maybe not. Are you going to get
59:56 better results if you start training
59:58 skills for these AIs? Yes, you're going
1:00:00 to get better results then.
1:00:09 Um all right, I forgot to kick this off
1:00:11 of Luna and something to a little bit
1:00:12 faster and better. So,
1:00:15 let me see if we can't get this
1:00:19 move a little faster, baby. We need you
1:00:21 to move quicker.
1:00:24 Um part about um parts of this getting
1:00:26 this to move quicker is about just how
1:00:30 how many things it has to confirm after
1:00:32 it does an action in Chief Architect. If
1:00:34 you can limit the amount of times it
1:00:36 needs to confirm actions, you might get
1:00:39 um
1:00:39 some faster output. If you can write
1:00:42 Python scripts to do actions for you, if
1:00:46 if you plan on being hands-off of your
1:00:47 computer and you got a second computer
1:00:49 to work from,
1:00:51 then those Python scripts are going to
1:00:52 speed up actions considerably.
1:00:54 Um I had a good long conversation with
1:00:56 Cody, uh who's just commenting right
1:00:58 now, and then with Anthony Reed who was
1:01:01 commenting. They're on my Discord
1:01:02 server. If you've never been on there,
1:01:04 it's a great um
1:01:06 it's a great little community. They're
1:01:08 usually specifically talking about
1:01:10 working with my products, but nothing to
1:01:12 keep you from going and joining that as
1:01:14 well.
1:01:15 Um
1:01:16 they've been talking about how they're
1:01:18 building out there
1:01:20 um MCP protocol integrations. So,
1:01:23 uh
1:01:24 one of the things to keep in mind is you
1:01:25 can you can get it to do
1:01:28 things that
1:01:30 are repeatable and and you know that,
1:01:32 you know, you can maybe like instruct it
1:01:34 on keystrokes. Hit tab three times, hit
1:01:36 enter, then hit this.
1:01:38 And to do that action, and the MCP
1:01:40 server just goes to that Python script
1:01:43 as opposed to
1:01:45 um trying to analyze instruction sets
1:01:48 and sending instructions back and forth
1:01:50 to the MCP.
1:01:52 It instead just knows to call upon that
1:01:54 Python script, and the Python script can
1:01:56 do instantaneous actions where it will
1:01:59 run as fast as your CPU can register uh
1:02:02 keystrokes,
1:02:04 which is very fast, mind you.
1:02:11 Here we go. Finally, we're getting some
1:02:12 info put in here.
1:02:14 See what it does.
1:02:18 See if we can expand this, too.
1:02:43 Yeah, you can export a script from
1:02:45 ChatGPT to any AI agent bringing in
1:02:48 information from one AI agent
1:02:51 to another. Yes.
1:02:53 Um like I said, there's a skills in that
1:02:55 download package. So, if you want to go
1:02:57 and take that skills as a
1:02:59 preliminary um skill to develop for your
1:03:03 AI,
1:03:04 yeah, by all means do that. There's
1:03:06 nothing keeping you even though it's
1:03:08 developed that skill is developed in
1:03:11 um
1:03:12 in
1:03:13 uh
1:03:14 Codex, ChatGPT, um it's just a markdown
1:03:18 file. Can be transferred to Claude, etc.
1:03:22 Now let's see. Home run dude. Builder
1:03:24 needs some room areas for flooring
1:03:26 on an older project. Use the MCP from my
1:03:29 phone to pull the data
1:03:31 while I was at the grocery store. Yeah.
1:03:34 Um some of these applications need uh
1:03:37 access.
1:03:39 So
1:03:41 let's see if I can get this a little
1:03:42 side by side going on here.
1:03:45 Oops.
1:03:47 What happened to it?
1:03:48 Um so you can get into settings
1:03:52 and at least in the desktop app for Chat
1:03:55 GPT
1:03:57 um I believe you get into connections,
1:04:00 I think.
1:04:02 Connections?
1:04:03 Yes, devices that can control this PC.
1:04:07 So my Pixel Fold phone
1:04:10 uh can control this from the phone, but
1:04:13 you need to authorize and add that.
1:04:15 Okay? So for Chat GPT, that's in you
1:04:18 click on your um profile icon bottom
1:04:21 left of the desktop app at least at this
1:04:23 time at this date, and then you uh click
1:04:26 on settings, and then you come down to
1:04:28 connections, open up connections, and
1:04:31 then you're going to click on the add
1:04:32 button for devices that can control this
1:04:35 PC. Add your uh phone. That way you can
1:04:38 communicate back and forth with the MCP.
1:04:41 What does this enable you to do? Well,
1:04:42 so long as you have a project in your
1:04:44 project browser, guess what you get to
1:04:45 do? Go open that project and give me um
1:04:49 the square foot area from my
1:04:53 area analysis
1:04:55 section.
1:04:56 Right?
1:04:57 Open up that project and give me the
1:04:58 partial number. I need it right now.
1:05:01 Open up that project and give me such
1:05:02 and such data. So that's really really
1:05:05 helpful for those of you that run
1:05:06 running out to the field and want to get
1:05:08 some information done.
1:05:10 Um I need square foot of this room. Can
1:05:12 you open that up and tell me what that
1:05:13 square foot is? Yeah, you no longer need
1:05:15 someone in the office to do that for
1:05:17 you. You You now just do that from this
1:05:20 setup.
1:05:28 Uh the important Cody is saying
1:05:30 something here.
1:05:31 The important thing is if you can keep
1:05:33 your context, your memory, your
1:05:35 connectors, and your skills all separate
1:05:37 from the model vendor that you're using,
1:05:39 then you can jump back in
1:05:42 and jump back and forth. Yes, so if you
1:05:44 are taking the time to do things such as
1:05:47 I mean give you some context of what
1:05:49 Cody's been doing recently. He's got a
1:05:51 180 stock plans that he sells on his
1:05:54 website. Um and so so these are all new
1:05:57 home designs, right? And he's trying to
1:06:00 bring some of the older stuff up to
1:06:03 um new standards and maybe new visual
1:06:06 standards, etc. or just new dimensions
1:06:09 standards, what what have you. And so
1:06:12 he's written a bunch of Python scripts
1:06:15 to do specific actions to make this
1:06:17 process go faster. Not only that, it's
1:06:20 just it's going to take far less
1:06:22 credits. You know, he went from um
1:06:24 frontier model at maybe the $200 a month
1:06:27 model to maybe he's down to the 100 or
1:06:30 even $20 a month model. Why? Because
1:06:32 um we're no longer having to um
1:06:35 understand context. You just get to
1:06:37 execute script that's already built to
1:06:39 do exactly what it needs to do. So, the
1:06:42 more you want to build out scripts to do
1:06:43 specific actions, that's going to make
1:06:45 it a lot easier for it to run through
1:06:47 and not burn uh credits. And also, if
1:06:50 those scripts are accessible on your
1:06:52 machine, it doesn't matter which
1:06:55 frontier model you have. You can always
1:06:57 just switch models and point it to this.
1:06:59 So, if some cheaper um newer model comes
1:07:03 in uh from some other surface uh
1:07:06 service, then you can just point it to
1:07:08 those Python scripts, give it the same
1:07:09 instruction set, export that from your
1:07:11 existing frontier model.
1:07:15 And then he says, "You can call the MCP
1:07:17 directly from Python.
1:07:19 It doesn't cost you tokens because
1:07:21 there's no agent involved." Oh, that's
1:07:23 interesting.
1:07:24 Like using standard API. But Cody, I'd
1:07:27 love to give you um
1:07:29 for you to give us more context about
1:07:31 that so I can share that next week.
1:07:34 And so, here we go.
1:07:35 Bam. All I get did was I just gave it my
1:07:39 address
1:07:40 and it pumped out all the information
1:07:42 including
1:07:43 um my APN number, my
1:07:46 um properties and stuff, blah blah blah.
1:07:48 And then all this gets sent if I go look
1:07:49 at my
1:07:50 title block on my layout, then
1:07:54 it's all here. Everything I need it to
1:07:56 have done, right?
1:07:59 The occupancy, R3.
1:08:02 Wind zones. Yeah, yeah, yeah.
1:08:06 Um
1:08:09 Oh, it's still going, I guess. What's it
1:08:11 doing here?
1:08:13 Bringing up the wrong thing.
1:08:17 Well, let's get back to it. Let's see.
1:08:19 Did it get my
1:08:21 setbacks?
1:08:22 Max height, cool.
1:08:25 Yeah.
1:08:26 Yeah, very cool.
1:08:28 5-ft interior, 5-ft street side, rear
1:08:31 20-ft.
1:08:33 Yeah, super cool.
1:08:37 Oh, I hated looking up that information
1:08:39 10 years ago. I just loathed it.
1:08:43 So,
1:08:45 yeah.
1:08:47 Well, I think I'll just see you next
1:08:48 week. We'll do a little bit more of
1:08:50 this. Why not? Um please come with your
1:08:52 questions. Go use it. Go check it out.
1:08:55 Go try it out. See what it does for you.
1:08:57 And then come back with your questions
1:08:59 next week.
1:09:00 Um just to let you know, for those of
1:09:02 you that have never done training with
1:09:04 me,
1:09:05 come do training with me. I love working
1:09:07 with people. I love doing training. My
1:09:09 schedule is almost wide open right now.
1:09:11 I don't know what's going on with that.
1:09:13 Um I just built in some new function to
1:09:16 my scheduling tools.
1:09:18 Um my scheduler now lets you know how
1:09:20 many schedule hours that you have left
1:09:22 if you're buying a a at a discounted
1:09:24 rate.
1:09:25 >> [snorts]
1:09:25 >> My discounted rate is at an industry low
1:09:28 right now. I'm a lot cheaper than any
1:09:30 other trainer you might find, including
1:09:32 Chief Architect's own training team.
1:09:34 I can certainly instruct you on things
1:09:36 that Chief Architect's training team
1:09:38 can't instruct you on. Sorry, Chief. It
1:09:40 is what it is.
1:09:42 And then, um not only that, I'm I'll
1:09:45 train at your pace. Most of my online
1:09:48 videos, um like this in Template
1:09:51 Tuesdays, fast-paced cuz we've got some
1:09:53 fast-paced people in here. You want to
1:09:55 go at a slower pace, you're a beginner,
1:09:56 you're a first-day learner, no problem.
1:09:59 We slow right on down and I'll show you
1:10:00 some really cool tricks that'll create a
1:10:03 foundation for you to start learning
1:10:05 this software and get ahead of the game,
1:10:07 okay?
1:10:08 So, we can slow it way way down if you
1:10:10 need to, or we could go as fast as you
1:10:12 could possibly want. Up to you.
1:10:15 >> [snorts]
1:10:15 >> And um it's real simple. You just get to
1:10:18 go on to my website, book a training
1:10:20 directly from there, check out my
1:10:22 scheduler. There's available slots
1:10:23 there, pick the slot you need. And you
1:10:25 could do 1 hour at a time or 2 hours at
1:10:27 a time. So, it's pretty flexible.
1:10:30 Uh
1:10:31 yeah, go check it out. Thanks again for
1:10:33 joining me. This goes into the
1:10:34 membership area, so
1:10:37 please
1:10:38 go pick up a membership for a little
1:10:39 bit, go check it out.
1:10:41 Check out the previous ones, too. We've
1:10:42 got some good content coming in here.
1:10:44 This is what I would call some of my
1:10:46 better content in these Template
1:10:48 Tuesdays, but it's free for you so long
1:10:49 as you're in the live show. So, make
1:10:51 sure you come back next Tuesday.
1:10:53 Thank you, everyone.
1:10:55 I'm going to go get some coffee.
