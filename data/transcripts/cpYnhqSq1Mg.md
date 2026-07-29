---
videoId: cpYnhqSq1Mg
title: Faster Raytrace Renderings In Chief Architect X17
url: "https://www.youtube.com/watch?v=cpYnhqSq1Mg"
status: imported
---

# Transcript

0:03 What's going on, Chief Architect users?
0:05 I have a project here that I'm I'm
0:05 designing a golf simulator room for it.
0:10 And we're going to notice here, if we
0:10 take a look, that at the bottom of the
0:14 screen, we've got 6 million. Actually,
0:15 this project has about 7 million
0:15 surfaces. And so, that's a lot of
0:18 surfaces. So, what happens is when I go
0:21 to um kind of edit something on the fly,
0:29 we're just sitting here for seconds just
0:33 to redraw on something simple such as
0:33 changing the height of the cabinet. Add
0:37 in that this particular project, I'm
0:37 doing this live with the client so that
0:41 you know, not only are we wasting my
0:41 time, we're wasting their time, too. Um,
0:45 so how do we get around this? I've got a
0:48 really simple and elegant solution. But
0:50 before I get into that solution, I want
0:53 to stop and make a suggestion to you. I
0:55 would really love it if you took the
0:58 time to go to your chief architect
1:00 account and the same way we report
1:02 problems is the same way we get to
1:02 report suggestions. And I would love it
1:07 if you suggested the ability to do
1:08 object groups. And the dialogue for this
1:13 would be very similar to our current
1:13 light set um adjust lights parameters
1:16 where we get a listing of what the rooms
1:21 are and then maybe the objects in that
1:23 room meaning fixtures, furnishings,
1:23 cabinets so that we can create groups
1:27 based on the camera that is active. So
1:31 we can turn off objects that are in
1:33 rooms other than the room we're
1:33 designing in. And that would make a huge
1:37 difference. It would even be great if
1:38 somehow this was just kind of
1:38 incorporated into the adjust lights
1:40 parameter and it would just be a whole
1:45 set of basically saved camera options.
1:46 So you want to stop and go take the time
1:50 to do that. Maybe we get that into a
1:50 future version making this a lot easier
1:55 to work in a massive project like this.
1:56 Okay, tell you the truth, this isn't
1:56 even that large of a project. I think
2:00 this house is maybe like 5 or 6,000
2:00 square foot. This is pretty common for,
2:02 you know, something maybe down in Texas,
2:06 right? So, here we go. Let's get into
2:06 the solution, the temporary solution or
2:11 workaround, what have you. What I have
2:14 going on here is in my active layer
2:14 display options for my cameras, I have
2:17 architectural blocks turned off. Now, if
2:22 you're using architectural blocks for
2:22 some other reason, unfortunately, this
2:25 isn't going to work with that. You're
2:25 going to have to turn this off in these
2:27 display groups. Okay? Excuse me, in this
2:33 camera. So, next thing I want to do is I
2:36 want to save this camera. This camera is
2:37 going to save and be associated with
2:38 this room. And like I just discussed, it
2:43 has a light group associated with this.
2:45 Okay. So, I've got adjust lights. I've
2:45 got a new light set. Sorry, that's what
2:49 they're called. Light set, not light
2:49 group. And for this room, I've sorted
2:51 things by room and I've targeted my room
2:57 and just turned on the lights for that
2:57 room. So, I'm using a light set instead
3:01 of an automatic setting for lighting.
3:03 So, that works with this particular
3:03 camera. Then, next thing that I want to
3:08 do is pretty simple. I'm going to drop
3:12 in a custom schedule. Okay.
3:12 And so, there we go. Drop in a custom
3:17 schedule. Now, let's open up this
3:17 schedule. And we're going to do some
3:19 very specific things. Right off the bat,
3:22 we're just going to include objects from
3:25 all floors. That's fine. I want to
3:25 include the major things that can be
3:28 grouped in an architectural block. Okay.
3:34 And also we'll limit the amount of
3:34 surface count that we've got. So I've
3:39 got cabinet here, fixture, and
3:39 furnishings. All right. So furniture.
3:43 Now I want to uncheck include objects
3:46 from all floors. And I want to target
3:46 the room that I'm working in. Here's my
3:50 golf simulator room. So I'm going to
3:50 uncheck that. I do not want to include
3:52 objects from that room because those are
3:57 the objects I want to keep displayed.
3:58 The point of this is we're targeting
4:00 objects that are not in that room so
4:02 that we can group them as an
4:02 architectural block. The next thing, and
4:06 I mean you can stop there if you just
4:07 get where I'm going with this, but
4:07 there's a few tricks that I'm going to
4:11 still mention a little bit later. The
4:11 next thing I want to get into is I can
4:13 just remove everything from the columns
4:18 to include on the columns row panel.
4:21 Okay. Except for maybe quantity. All
4:21 right. And let's press okay. What this
4:28 does is it groups things by a singular
4:30 um category. And that makes it so that
4:32 we can target this. Now keep in mind
4:32 right now I have the schedule selected.
4:35 But if I click on this 228 number, now I
4:42 have the row selected. And so when I
4:42 have the schedule selected, this is what
4:46 my edit toolbar looks like. When I have
4:51 the row selected, this is what my edit
4:53 toolbar looks like. And we get this
4:53 little guy right here. Find object in
4:55 plan. Now, once I do that, it's going to
5:01 zoom out and it's going to show us all
5:01 of these objects and they will have been
5:08 selected. Isn't that pretty cool? Keep
5:10 in mind, even though everything is
5:10 selected, we are not getting the ability
5:15 to make an architectural block. And why
5:17 is that? Well, it might be that there's
5:20 already an architectural block in here.
5:22 What it's saying is something in our
5:24 schedule that we've got in these
5:24 parameters is not capable of becoming an
5:29 architectural block. So, let's go back
5:31 in and just make sure that we've got
5:31 everything set up the right way. So, in
5:33 the general panel, I've got cabinet. Oh,
5:38 look what I did. I accidentally clicked
5:40 electrical, which would let you know
5:41 electrical can't be blocked in
5:42 electrical. I mean, excuse me, in an
5:43 architectural block. So, let's try it
5:45 one more time. I've unchecked that. And
5:49 now when I select on the row, bind
5:49 objects in plan. What happens? We still
5:54 have a problem because we're still not
5:57 getting the make architectural block
5:59 tool. So, what's a way around this?
5:59 Well, I'm going to do something very
6:04 simple. I'm going to look at this. I
6:04 have an architectural block here. That's
6:09 actually what was causing the issue. But
6:10 I'm going to show you how to get around
6:12 that issue. Let's just say for instance
6:12 that this was an architectural block and
6:17 we couldn't find it. We couldn't see it.
6:19 We didn't know where it was in plan.
6:21 What we can do is take two other
6:21 objects, make an architectural block and
6:28 then use the select marquee select
6:28 similar and then marquee select all
6:31 similar. Okay, that targets this and we
6:36 don't even have to do anything beyond
6:38 just coming in here exploding the
6:40 architectural block. Now this is
6:43 ensuring that nothing is an
6:43 architectural block that lives in our
6:47 schedule. Let's target this one more
6:47 time. Find objects in plan. And here it
6:53 is. Make architectural block. That's
6:53 awesome. So we did that for this floor.
6:59 I'm going to copy paste this schedule
6:59 down a floor. We're going to open it up.
7:03 We're going to say we want to include
7:07 all items from floor one. Select all
7:07 rooms. We can leave everything the way
7:10 we've got it. Okay. And it might be that
7:14 there's an architectural block here as
7:17 well. We'll find out very shortly just
7:19 by selecting this. Let's do that. Find
7:22 object and plan. And sure enough,
7:22 something is an architectural block. So,
7:26 we know we can do that trick again,
7:28 right? Select two things, make an
7:28 architectural block out of them. Select
7:33 marquee similar. Select all similar.
7:34 Unblock.
7:34 And then let's go back to that schedule
7:43 One more thing, we can shift select this
7:45 schedule to make this really easy on
7:45 oursel and hit this resizing node. And
7:51 this just makes it even easier to work
7:51 from, right? Is we can keep this on the
7:56 screen. And this is going to be for our
7:58 design phase only. So I get to select
8:01 this find object in plan make that
8:01 architectural block. And what do we get
8:05 to do? Let's go back to my camera that
8:07 does not display architectural blocks.
8:07 And you're going to see that this tries
8:11 to rebuild the scene. And let's go take
8:13 a look in the status bar as this
8:13 rebuilds. And we have gone down to 1.2
8:19 million surfaces from 7 million
8:19 surfaces. How does that affect our
8:21 scene's redraw time? Let's go ahead and
8:27 punch in 4 in and then do a little
8:27 resize on this and see how much faster
8:30 this works. That's a lot faster for me.
8:34 Shaved maybe a second off of that redraw
8:38 of time, which is significant when we're
8:40 talking about editing multiple things
8:40 all the time. And also, not only that,
8:45 but my camera is just updating a lot
8:47 faster now. Less of a resource hog.
8:47 Let's try something else. Let's just try
8:51 painting this object.
8:51 Let's see how fast maybe that works. And
8:56 let me even try to click on my object
8:59 eyropper tool.
8:59 And I'm going to see if I can't get the
9:13 Yeah, this is just going just a little
9:13 bit faster. It's certainly enough to put
9:17 in that little bit of effort. Once you
9:18 have that schedule, okay, now this is a
9:23 utility, right? Once you've got that
9:25 schedule, what you get to do is you
9:25 could build that in your template plan
9:26 if you wanted to. Or you could come back
9:32 to this view, take this and guess what?
9:32 We get to add this to the library. Super
9:36 simple. You know, maybe you want to
9:36 rename it. Let's get into this and just
9:48 block creator. Why not?
9:48 There we go. This is a really simple
9:53 solution for this. So, I hope that
9:53 helped you out. Um, you know, drop a
9:56 like, please. I'm always looking for the
10:00 best solutions to some of these things.
