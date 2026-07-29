---
videoId: Vf5zVIZR0-s
title: Building a dynamic Post Footing Tool In Chief Architect
url: "https://www.youtube.com/watch?v=Vf5zVIZR0-s"
status: imported
---

# Transcript

0:00 What's going on, VIP? I'm going to show
0:02 you how to make a tool that will do post
0:05 footings kind of dynamically, a little
0:06 bit more dynamic than just using the
0:08 post and footing tool. And so, I've just
0:12 raised, excuse me, lowered my
0:14 foundation, made it taller. And then I'm
0:17 going to get up to our next level here.
0:20 And I drew out just a little railing to
0:23 start with. And then what I'm going to
0:24 do is, well, we're going to be building
0:26 this out of a railing cuz that's a
0:28 pretty dynamic tool. It has a lot of
0:30 benefits once we've got into X16, X17.
0:33 So, the next thing I'll do is I'll draw
0:36 a little solid here. And I want to
0:38 specify that this solid is going to be
0:39 the size of the footing that I want to
0:41 use. And so, maybe I want to do
0:45 let's go 30 24. There we go. That's
0:49 going to be my footing size. And then I
0:51 can copy this and kind of shrink it down
0:53 and then edit this where we're going to
0:56 raise this up 30. And so the height of
0:59 this being 30 is okay. Width and depth
1:02 is going to be the size of my post in
1:04 this case. Maybe I'll do um a 4x4. And
1:07 so I might make a couple of these for
1:09 different scenarios. So there we go.
1:12 Bam. That's sent right on top of this
1:14 other footing. And we might want to take
1:17 it and do one more thing which is in the
1:19 materials tab. Change this to our
1:23 framing. Reframing.
1:26 Oops. Lost it. There we go. So, there's
1:29 our fur framing. We're just going to
1:32 call this post.
1:35 I can click on that. Sometimes it lets
1:37 me. Single click. No, it's not going to
1:39 let me. All right.
1:42 So, now we can take the two of these
1:43 together and convert the selected to
1:46 symbol. This is from our edit toolbar.
1:49 So, convert the selected to symbol. If I
1:52 did this correctly, that framing member
1:54 should be stacked right on top of that
1:56 post. And we want to choose the symbol
1:58 category of mill work because that's
2:01 what newles made with. So mill work,
2:04 show advanced options. We're going to
2:06 add it to the library. And here's what
2:09 we've got going on. And I did in fact
2:10 draw that correctly. Very cool.
2:13 So the next thing that I want is do I
2:16 want to size this based on the framing
2:19 member or do I want to size this based
2:21 on the footing in the case that I want
2:24 to use the directive of the railing to
2:27 resize this. And so it could be that I
2:29 get into advanced sizing and we take a
2:32 look at what our bounding box is by
2:34 clicking on this. All right. And I want
2:37 to adjust this so that I don't want to
2:40 change the geometry. I just want to
2:42 change the bounding box to represent
2:45 this object. And so what I want this to
2:48 be is my width to be three and a half
2:52 and that
2:54 to be three and a half. All right. So
2:56 that's what just happened is this is
2:58 going to be the size of this object.
3:01 Okay. And we can see where the bounding
3:04 box is represented here. So we might
3:06 actually have to shift this object. Um,
3:10 we'll test that first because maybe it's
3:13 not offset. I can't remember, but
3:16 looks like the bounding box is offset
3:18 from what you can tell. So, it might be
3:21 that our front to back. You see what
3:22 happened here? Our front and back got
3:24 changed here. So, could be instead go
3:27 -10 and a quarter and then do the math
3:31 over here. 10 and a quarter or rather -
3:35 10 and a quarter again. There we go. Now
3:38 our bounding box is in the right spot
3:42 thankfully. Okay. So the next thing I
3:46 want to do is when this stretches
3:48 upward, I don't want to change the
3:50 height of this concrete. I only want to
3:52 change the height of that post. Okay. So
3:56 I'm going to set this to be just above
3:58 that footing. So I've got it universal
4:01 cutting plane. That means that as this
4:03 symbol raises in height, it will
4:05 continue to create geometry
4:08 just in the um profile of where it's
4:11 that cutting plane is. Okay.
4:14 So,
4:16 all that being said,
4:19 um let's see.
4:22 When we stretch this object
4:26 is going to stretch uniformly. It's
4:29 going to resize uniformly. So, it does
4:30 end up
4:32 changing that the footing base. Might
4:36 have to do multiple of these to make it
4:38 really dynamic. So, let's just keep this
4:41 added to it. The library, I'm going to
4:43 change the name of this. This is going
4:45 to be my 4x4
4:47 on 24x 24x30
4:52 footing.
4:53 And then in parentheses, I love to put
4:56 the symbol category when it's not
4:57 straightforward. Let me take caps lock
5:00 off. See four on.
5:12 So it should look something like that.
5:15 And it's a mill work symbol. Now what do
5:18 we get to do? Well, let's come in here.
5:20 Let's open up this railing. And we're
5:22 probably going to draw this on the floor
5:23 below, but we're going to set up a
5:25 couple things. So in the rail style,
5:26 this is going to be an open railing with
5:28 no top and bottom rail. And we do not
5:31 want a full post at the end. We want no
5:33 posts at the end. So no posts at the
5:36 end. No top and bottom rail. No rags
5:39 lower. Get to the new ballasters. And
5:42 let's find my new.
5:52 And there we go.
5:54 Now use wall width. No problem there. We
5:58 should be able to do that.
6:00 Max spacing. You can set this up to be
6:04 the spacing that you need in between
6:06 your footings. So, you know, maybe you
6:08 need less than 8t, maybe you need 4
6:11 foot. So, this would be an opportunity
6:12 to change that. Okay, 4 foot in between
6:15 footings would be a little bit tight
6:17 because we just have footing this right
6:18 stack next to each other, right? So, for
6:21 your use case, whatever you need there.
6:23 And then um in terms of height now it
6:28 should be that we get to change this
6:32 to be that the post is going to go to
6:35 the ceiling.
6:37 Okay. Not only that, but if you really
6:40 want to get clever, maybe this is for a
6:42 girder system. So you would do post to
6:45 beam. Isn't that clever? Right. So let's
6:49 just press okay. See what we've got
6:50 going on here. Now check out what
6:53 happens. Let me just cut this. I'm going
6:54 to take it to the floor below. Paste.
6:56 Hold.
6:59 And let's see what happens as I span
7:01 this out. Look at that. I'm getting
7:02 these footings at these intervals,
7:05 right? Isn't that cool? And so what you
7:08 can do is you can select your railing
7:10 and then you can always tab. If you're
7:13 close to one of these nules, you can tab
7:15 to one of those new posts. Now notice
7:19 that there's an offset in the new post
7:20 and that's my fault. We need to get back
7:22 into our symbol real quick. Let's open
7:25 this object. And so we do need to get
7:27 this so that it's -10 and a quarter in
7:30 the y delta which is right here. Y
7:34 position. So actually it's positive.
7:35 This is our positive leg right here.
7:37 Okay, that's our positive leg. We need
7:39 to move this so that post is sitting
7:41 right on that positive leg. Right. So
7:44 this is going to go 10.25.
7:47 I got a zero. There we go. Okay, let's
7:52 press okay. And can we kind of toggle
7:54 and replace? I don't think so. It's not
7:56 going to let us toggle and replace. Not
7:58 unless we're in a camera view, which we
8:00 could do.
8:03 So, let's just do a little toggle and
8:05 replace. Now, select the library. There
8:07 we go. So, you can see all those just
8:09 shifted. So, now when I tab into this,
8:14 it still shows that they're offset.
8:17 That's because we did not update the CAD
8:19 block. All these little details, right?
8:22 2D symbol generate block.
8:27 And I'm going to have to replace this
8:28 one more time.
8:32 Hopefully this time around.
8:38 Seems that they still might be offset.
8:40 Interestingly enough, they're still
8:43 showing that they are offset by some
8:46 amount.
8:48 I'm not sure why.
8:52 So, if I select them here,
8:57 there's where they're represented. You
8:59 can see that the highlights off.
9:02 So, it must be center of the post is
9:04 what's happening here. So, one more time
9:07 here. So, let's get to this 3D menu. We
9:10 can kind of take a look here. We can see
9:12 where this is cutting through. This is
9:14 just buted right to the post. So, we
9:16 need to add one more thing here. We need
9:20 to add half of the distance of what is
9:24 half the distance of three and a half. I
9:26 don't even want to think. 1.75.
9:28 So, plus 1.75.
9:32 Let's see if this finally gets me to
9:34 where I need to be.
9:37 Now, if I tab to this, I am off
9:41 the full
9:44 length of that framing member.
9:48 Boy, I'm getting as confused as maybe
9:49 you are. I'm not sure what's happening
9:52 here.
9:57 Let's try that.
10:01 That seems to be close, even though it's
10:02 not 100% on.
10:05 I'm not sure why. I don't know what
10:08 that's coming from.
10:21 Interesting.
10:23 Boy, this video is going really well up
10:25 until we got to this point where the
10:28 math isn't making sense. I do know there
10:30 is some still some problems in negative
10:35 bounding box spacing,
10:41 but I might just be overlooking
10:42 something and not thinking clearly cuz 8
10:45 in seems to have done it. Why is that?
10:48 What would make this 8 in
10:54 peculiar? It might be because of the
10:56 railing size that we're getting some
10:58 problems here. So, let's open up this
11:01 railing. Let's say that instead of this
11:03 4 and 1/2 in that it is
11:09 see do we have a framing only?
11:13 We do not have a framing only wall type.
11:15 So, let's just make a copy of this
11:20 framing only.
11:26 And now we're at three and a half
11:28 inches. And do I is that location
11:31 correct? Aha. So there is a problem.
11:34 It's a long-standing problem in Chief.
11:37 I've been telling them about it for
11:38 years.
11:41 And that problem is that when you have a
11:43 negative bounding box spacing and you've
11:46 got some offsets that it stretches in
11:48 the incorrect way. So this should now be
11:52 aligned.
11:54 So this will not be dynamic. You don't
11:56 get to dynamically resize the railing
11:58 and have it be correct. So you're going
12:00 to have to build one of these for each
12:01 scenario that you need. But that
12:03 shouldn't be that many scenarios. You
12:05 can do, you know, a 6x6 beam or what
12:08 have you. So maybe it'll do different
12:12 sizes. But now I should be able to tab
12:13 in and get my center line. For some
12:17 reason, this is not working very well
12:19 either. Tab in and get my center line.
12:21 Tab in and get my center line. I cannot
12:25 seem to tab it. There is an alternate
12:28 way of doing this and that is this move
12:30 nules tool, but you should be able to
12:33 tab it. So, I'm not There it is. And we
12:36 can see how far this offset is here.
12:44 Could not tell you why.
12:46 Maybe it's still the generate block.
12:50 Try one more time.
12:56 Yeah, I do not know why the center line
12:59 is here. Boy, take a good idea and a
13:02 great implementation and a good video
13:05 and come to find out that
13:08 you got problems the whole way through.
13:14 That's the center line. Huh?
13:19 Very strange.
13:23 What is the length of this?
13:28 It's basically 10 and a quarter over. So
13:31 here when we tab in
13:34 in the wrong location by 10 and a
13:35 quarter but here when we tab in
13:40 the correct location.
13:45 So what should take precedence? Well the
13:48 one on top.
13:51 Too bad. Look at that. Be able to just
13:54 slide this over real easy.
13:59 In that case, let's do something
14:01 different.
14:03 Let's instead
14:05 get rid of these bounding box things.
14:08 Make this a lot easier.
14:16 Zero all this out.
14:18 This is going to get rid of that glitch
14:20 that is there.
14:29 Now to apply this, they're going to get
14:31 stretched funny. That's okay. We'll open
14:33 up the railing. And in rail uh newles
14:38 ballasters, we are going to set this to
14:39 be the size of the footing instead. And
14:42 that's okay.
14:48 Now
14:49 we should have it so that if we get rid
14:53 of any offset
14:56 in the 3D panel. Zero this out again.
15:03 There we go. You've got the correct
15:05 location. There we go. Got the correct
15:07 location. All right.
15:11 And I'm going to send this video into
15:12 Chief Architect because they still have
15:15 symbol offset stretching problems. So
15:20 cool, man. Cool, cool, cool. Now we're
15:24 able to slide these over as you need to
15:26 kind of dynamically. Um, let's just
15:29 check our plan view on this. Instead of
15:32 use defaults, we want to see
15:36 the rails as well.
15:39 But but we don't have rails, so it's not
15:41 going to show us that beam,
15:44 which you might be drawing a line for.
15:46 But if you wanted to show that beam,
15:48 what we could do instead is
15:50 um
15:53 we could add
15:56 could add a rail. We would do post rail.
15:59 It's just not going to go all the way.
16:01 Okay. post to ceiling include top rail
16:08 and then top rail is determined by
16:12 the overall height.
16:14 So that's not helpful.
16:18 You might be able to make that rail
16:20 invisible so that it's not shown
16:24 in certain views. I don't think so. I
16:26 think instead you just draw a line on
16:28 top and that's going to make this a lot
16:30 easier. But we still have the ability to
16:32 get some dynamic stuff here. And then um
16:34 manual dimension tool. You can set this
16:36 to centers so that you're picking this
16:37 up automatically. And this just makes
16:39 this whole setup a lot easier.
16:44 Yeah. Cool. There should be a way to
16:46 reset all the new spacing. Reset newles.
16:49 There we go. And once you've got this
16:51 all set up, now we get to just add this
16:53 to the library. And this becomes
16:59 our let's see um 4x4
17:04 on 24x 24x30
17:08 footing and then railing.
17:13 And so what do I get to do with that?
17:16 Bam. I just get to draw this across. And
17:17 I might even put this in my toolbarss
17:19 because that's a pretty nice tool. I
17:21 just slide these things over and get
17:23 them to where I need them to be. Pretty
17:25 pretty cool and efficient. What does
17:29 this look like in this view? Looks like
17:32 this. If we built all the framing, what
17:35 would this look like?
17:37 That would look like that. Doesn't that
17:39 look good? Right.
17:42 Um the last part of this, as you can
17:44 see, is what we can do one more thing
17:48 here. We could change this so that
17:54 um in rail style follow terrain. Follow
17:58 terrain. And so if you had some sloping
18:01 terrain under the house,
18:04 that might be cool. Um
18:09 that just made it disappear because the
18:11 terrain's low. Oh, that's funny.
18:15 Okay, so maybe not the best move there.
18:18 I was thinking we could get rid of that
18:20 framing skirt happening here.
18:24 And let's see what would be another way
18:25 to get rid of that.
18:32 We could set that wall type to just be
18:38 no framing this case.
18:45 And what happens?
18:47 still get this material. So maybe we
18:50 need to set it to insulation air gap
19:01 air
19:04 gap
19:07 and that makes it disappear. Perfect.
19:11 And so what does this look like in a
19:13 little
19:15 back clipped cross-section?
19:22 Look at that. Isn't that nice?
19:25 Pretty slick. The only problem with this
19:29 is
19:31 what's the height derived from, right?
19:35 This is essentially sitting on a floor
19:37 of this level. So the only way you
19:40 adjust this is by adjusting that
19:42 relative height of this room.
19:46 So this this footing is actually going
19:48 to be sitting on the floor. What else
19:50 can we do about that? Um we can do this.
19:53 We can open up our
19:56 new
19:58 and let's just say it's got a negative
20:00 height in the 3D for the Z position. So
20:02 I want this to actually go down. Let's
20:05 go -29 in.
20:08 That's almost sitting in the ground,
20:10 right? And so if I replace that now,
20:14 that's what that looks like.
20:19 Why is that not stretched to the one
20:21 above?
20:24 Not sure. Oh, because we need to adjust
20:26 where the stretch plane is as well. See,
20:29 the stretch plane is above the post.
20:35 So, this is going to be set at like two
20:37 inches.
20:41 And
20:43 still not doing what I want it to do.
20:46 This is a tough video.
20:51 This should have stretched that symbol
21:00 all the way up.
21:05 Isn't
21:38 instead. We probably could have done a
21:39 bottom offset.
21:42 Let's try that. Let's do that instead.
22:07 So, a bottom offset of -4.
22:12 There we go.
22:15 There it is. That's the money right
22:17 there. Well, I hope you learned
22:19 something. I don't often publish stuff
22:20 that's got this many little problems
22:22 along the way, but I know that I've
22:24 gotten requests to do that and let it
22:26 ride. So, hope you got something out of
22:28 this. This is me just working through
22:29 some problems, huh? Um, yeah. I think
22:34 this ends up being a pretty dynamic
22:36 tool, though. So, I want to
22:41 find original in library finds that. I
22:45 wish we can update from, you know, that
22:47 would be really nice,
22:50 right? But doesn't look like we can do
22:53 that. So, I'm just going to add this to
22:54 the library again. Copy this little bit
22:57 of info.
23:02 Throw that in there like that.
23:06 Now you got to remember which one's
23:07 which.
23:09 And let's go draw this out and just test
23:11 it real quick.
23:17 Bam. Bam. Bam.
23:19 And there we go. Cool tool.
23:23 Cool tool. Go ahead and make one
23:24 yourself. Let us know how it goes. Thank
23:27 you for watching.
