---
videoId: bF8KM9E_hno
title: Flush Base With Reglet in Chief Architect
url: "https://www.youtube.com/watch?v=bF8KM9E_hno"
status: imported
---

# Transcript

0:02 Guess
0:03 what?
0:03 I got a cool thing for you to check out.
0:07 Um, you ever had to do a flush base with
0:09 a little reglet detail here?
0:10 Um,
0:10 that's a tough one, right? So, we got a
0:13 couple of suggestions here. This is the
0:15 Chief Architect forums and we got tea
0:15 time who's really knowledgeable user and
0:19 they are suggesting maybe use a pony
0:19 wall. That works. So, you're creating a
0:23 pony wall and wall type where the wall
0:25 type is we're making that drywall a
0:27 thickness of 0 in
0:27 and that way the base automatically
0:29 pushes to that wall type. Only problem
0:34 is is that this can create some issues
0:34 in terms of vector lines and elevations
0:38 or it can also make it so that you're
0:40 building framing from that pony wall
0:41 now. So, it's a you know, kind of
0:41 messing with your framing. So, maybe you
0:44 don't want that. And then some other
0:44 suggestions use a wall material region,
0:48 but you have to do that on a wall by
0:48 wall basis. So, what happens when you
0:49 got a 3,000 square foot home with a ton
0:54 of rooms? You're not going to spend all
0:55 that time doing that. What a pain,
0:55 right? And then so someone's kind of
0:57 chiming in and saying, "Hey developers,
1:00 let's fix this. We want to, you know,
1:00 get in a a new approach for this, a tool
1:05 for this." But, guess what? I've got a
1:05 method for you and it's a pretty simple
1:07 method. So, let's start from a brand new
1:10 plan. Now, when we're finished setting
1:10 up this method, you should save this as
1:15 a template for any kind of flush base
1:16 projects you're going to do because
1:16 guess what? You won't have to do any
1:18 other setup. It'll just be automated.
1:21 So,
1:21 first thing I want to do is get into my
1:23 floor defaults and change my first floor
1:27 molding. And so, I'm going to replace
1:29 this molding
1:29 and I'm probably just going to do a BM03
1:34 for a 3 and 1/2 in square molding, okay?
1:36 And the one thing I'm making sure to do
1:38 is in our horizontal offset, I'm going
1:41 to take that width right here, 5/8 in,
1:44 and I'm going to minus that 5/8 in,
1:45 okay?
1:45 Once I've got that set, let me press
1:47 okay. Let's hit done. And then I want to
1:52 do a couple things. I'm going to change
1:55 my exterior wall defaults. Now, in In
1:56 case, I'm just going to go ahead and
1:56 grab, you know, these walls and I can
2:00 edit them right in place, but
2:00 usually I would just change my exterior
2:05 wall default. So, let me hit define. In
2:05 the interior layers, I'm going to insert
2:10 above and I'm going to set that to 0 in.
2:12 So, that's going to have drywall on its
2:14 surface. Next, I want to change that
2:14 exterior surface, okay? So, I'm going to
2:19 change that exterior material and I'm
2:22 going to change it to insulation air
2:23 gap.
2:23 There we go. Press okay and I'm done.
2:27 Now, let me go ahead and change my
2:30 default interior wall. So, let me
2:30 define. Same thing. I'm going to insert
2:34 below in this case for that exterior
2:35 side. Set this to 0 in. Go ahead and set
2:39 up this
2:39 grabs drywall to be insulation air gap
2:49 There we go. And now I can insert below
2:51 again and then move this down to the
2:55 exterior side and then set this
2:55 grabs drywall to 0 in. Hopefully, you
2:59 followed all that, okay? So, I've got
2:59 insulation air gap on the outside. It's
3:02 half inch.
3:02 Let me press okay. All right. Now, let's
3:07 start drawing out some rooms. Now, the
3:07 next step of this would be going through
3:10 all your room types and adding a wall
3:10 covering, but I'm not going to do that
3:13 in this video. Instead, I'm just going
3:15 to select a room, select marquee
3:15 similar, select all similar. Let's open
3:18 it up and we're going to get to the wall
3:21 panel
3:21 uh wall covering panel. And so, we're
3:25 going to add a new and I bet you can
3:27 guess what we're going to add. We're
3:30 going to add grabs drywall.
3:30 So, we're going to add a wall covering
3:35 over the top of an insulation air gap,
3:35 which is see-through, invisible. And so,
3:40 we need it to cover everything but that
3:43 base plus that reglet, right? So, I've
3:45 got a 95 and 5/8 in finished ceiling
3:45 height and I'm going to minus 3.75 and
3:49 then I'm going to set my top to ceiling
3:52 to zero.
3:52 What that mean? It's leaving a relief of
3:57 3.75. So, if I did this correctly in all
4:00 these rooms, when I pull a view here,
4:00 and let's just change it to a vector so
4:04 we can really clearly see this,
4:06 it should be
4:06 that I do in fact have a reglet with a
4:09 flush base.
4:09 Look at that.
4:11 In every room.
4:13 So, if you set this as all of your rooms
4:17 having a wall covering by default, that
4:20 means everything that you drew would
4:20 have a flush base. Pretty slick, right?
4:25 Anyways, have some fun trying to set
4:25 that up. Make sure to save it as your
4:26 template, so that that way when you go
