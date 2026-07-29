---
videoId: KKC5vgl3L9U
title: Material ID Masks in Chief Architect X15
url: "https://www.youtube.com/watch?v=KKC5vgl3L9U"
status: imported
---

# Transcript

0:00 this video is for VIP and Photoshop Club
0:03 I hope this just introduces one to the
0:05 other in a sense but also I think that
0:08 it's applicable to both we are going to
0:09 be using Photoshop with this uh image
0:12 that I'm about to put on the screen
0:14 right now and this is just a project I
0:17 put together real quick as a test
0:20 project and what we're looking at here
0:22 is creating material ID masks and what
0:26 that is in layman terms without me
0:27 actually going through step by step and
0:29 getting into this I'm going to just show
0:31 you when I switch to a vector rendering
0:34 mode you notice here that there are
0:36 colors associated with my materials and
0:38 what this is is that I'm taking a
0:41 material that has a texture in its
0:46 texture source so it needs to have a
0:48 texture in its texture source and then
0:50 I'm taking the pattern color or the
0:53 material color if you will and I'm
0:56 changing this to something that's bright
0:59 and vibrant and the purpose of that is
1:01 that we're going to export this image
1:04 and you have to use the export option
1:06 you can't just use a screen clip so
1:08 export this image and then export the
1:11 ray traced image as well and then we
1:14 bring these into Photoshop and what can
1:16 you do with that well you can make easy
1:19 selections and I'll show you how that
1:21 works so I've got at the bottom right
1:24 hand corner of the screen is my layer
1:26 stack here's my texture image and then
1:29 the vector vector image is below okay
1:32 now if I click on the vector image and I
1:34 use a tool such as this magic wand tool
1:38 it's going to be easy for me to make a
1:39 selection based on that color blocking
1:42 because I am selecting from the vector
1:45 image not the um PNG image the layer
1:49 that's on top of it so you see there it
1:51 was really easy for me to select the
1:54 underside of these EES I can shift
1:56 select the underside of these EES
1:58 because what they are selecting is this
2:02 pink color right shift select bam I've
2:05 got this pink color now keep in mind I
2:08 put on a depth of field in my render so
2:11 it's going to be a little bit more
2:13 challenging to select I would encourage
2:15 you to do a fake depth of field within
2:18 Photoshop using their neural filters as
2:20 opposed to doing it within Chief where
2:22 you're going to be battling some
2:24 selection issues okay but here we go
2:27 really easy for me to pick the underside
2:30 these Eaves and then what can I do with
2:31 that well we'll come back to our main
2:33 layer and maybe we add on an exposure
2:36 adjustment layer and what does this do
2:37 well it masks to that area that we've
2:41 had selected so that I can just change
2:43 the exposure on the underside of the
2:45 eaves only and then I'd have to do some
2:46 fixes because we didn't render this out
2:49 high enough but there we go very quickly
2:51 we can just edit one part of this
2:53 building and I'll show you another
2:55 example of that you can see the siding
2:57 material back here well I've got
3:00 a hue saturation adjustment layer where
3:03 I can change the color of the siding or
3:06 the intensity or the darkness what have
3:09 you so can obviously pump that up to a
3:11 bright purple that wouldn't look very
3:13 good and then change the lightness ETC
3:16 and mess around with some of these
3:17 settings and so all we're doing is
3:18 getting a really clear and concise mask
3:21 the other thing you can do with these
3:22 selections is do something like use your
3:25 generative fill to very accurately fill
3:28 in one portion of your rendering so that
3:30 might be helpful as well now this
3:33 tutorial kind of led me to another idea
3:35 or another tutorial and that is that
3:37 when I went and selected the siding and
3:39 tried to do a gen fill for that siding
3:42 um to make it a ston wall well it just
3:44 doesn't work all that well so I'm going
3:46 to control click on the masks that I
3:49 have for my sighting
3:53 okay oops let's see if I can get the
3:56 right
3:58 one there's my exciting right there so
4:01 now that I have control clicked on this
4:03 okay I'm going to do a gen fill and
4:05 we're just going to say stone wall using
4:09 round stones and see what it comes up
4:13 with okay so it just populated and you
4:16 can see here it's just kind of if we
4:18 look real tight here it's kind of just
4:21 matching my existing siding and so that
4:24 doesn't look like stone at all does it
4:26 no so it's not doing a very good job and
4:28 I've run into this a couple times
4:30 with Adobe Firefly or the Gen fill so
4:33 something that we can do instead is we
4:35 might need to make a texture so that we
4:37 can go in there and give a
4:38 representation of that ston wall so how
4:41 do we even do that well I'm going to
4:43 come in here I'm going to do a new
4:44 document all right and I'm just going to
4:46 make it a 1024 Actually I don't even
4:48 need to do a new document I'm going to
4:50 open and I'm going to go into my own
4:52 material store now you can make your own
4:54 material that's more for the Photoshop
4:56 Club go join that if you want to know
4:58 about making your own material what I'm
5:00 going to do instead is I'm going to come
5:01 in here and look for a material I might
5:02 already have so I'm going to come in and
5:04 look for my
5:06 concrete and then I'm looking for just
5:10 well I'm looking for a stone
5:14 wall okay so I've got a cinder block
5:16 texture here there we go now this is a
5:19 repeating texture so what do I get to do
5:21 with this well I'm going to control a to
5:23 select all I'm going to get into my edit
5:25 menu and then I'm going to define a
5:28 pattern cinder block
5:32 Stone and press
5:35 okay now what do I get to do with that
5:37 well this is pretty simple I can just
5:39 come in
5:40 here and I can take this selection that
5:43 I've got here or I can select new but
5:46 let's just take this selection we can
5:48 see here if I control click there's my
5:51 section of wall that I need to edit
5:53 right I'm going to do a
5:56 new layer actually that was not that was
5:59 the Gen fill let's
6:02 go contrl D and control
6:06 SCT there we go I'm going to do a new
6:09 layer that is a new fill layer and
6:13 that's going to be a pattern layer okay
6:15 just going to press okay on that and
6:17 then I got to click this down arrow and
6:18 find my new ston wall look at
6:21 that now we're going to have to edit
6:23 this right but let's just say our scale
6:26 is let's go
6:28 35% let's go less let's go 15 let's go a
6:32 little bit less still 14 and then I get
6:35 to change the
6:38 angle it's going to be something like
6:44 -25 how about that it's getting closer
6:48 -6 and kind of the last trick with this
6:51 is you know it needs to be tweaked right
6:53 it needs to be kind of tilted a little
6:55 bit so that's part of it as well but I'm
6:57 going to go ahead and control J
7:00 a and then double click into this again
7:04 and we'll go positive six this time so
7:06 that's for the other direction let's go
7:08 positive maybe
7:10 eight maybe 10 how about that and then
7:14 from here and even though this is a
7:16 skewed and doesn't look appropriate I'm
7:18 going to come in and I'm going to get
7:20 into this mask and paint this out right
7:23 at the
7:26 corner right so now we've got the stone
7:29 going both way let's control click into
7:31 this one more time and now let's try
7:35 stone
7:40 wall okay so it did generate a stone
7:44 wall it's an ugly one so you might want
7:46 to then go on top of
7:49 this and as tedious as that
7:52 is do it one more time
8:00 and so finally we get to something
8:03 that's
8:05 viable there's still one section of this
8:08 that didn't quite make it but for the
8:09 whole I've did a pretty good job so very
8:12 quickly we're changing out textures
8:14 where we've got ston wall here we've got
8:16 maybe a little bit more realistic
8:19 columns uh which need some touching up
8:22 and then you know you can come in here
8:24 and and fix a few things very easily
8:27 utilizing that Vector mask and so
8:31 another thing I can do is I can control
8:33 click into that ston wall again and I
8:35 can add another adjustment layer on top
8:37 of this to kind of change that exposure
8:39 of this layer if I want to Etc and of
8:43 course I can come in and just click on
8:45 my existing masks to do those
8:48 adjustments as well so with the Gen fill
8:51 it's a little bit different it's a
8:52 little bit hard to um select once you've
8:54 done a gen fill then the selection
8:56 changes so it's a little bit harder to
8:58 do some of these edits and that's when
9:00 you're going to have to get into some of
9:02 the more advanced things that we teach
9:03 in the Photoshop Club so uh there you go
9:06 hopefully that was a fun
9:08 little dive into Photoshop and and Chief
9:12 Architect and using Vector masks um it's
9:14 changing the way I'm rendering I am let
9:16 me actually get back to the main screen
9:18 here real quick I'm ignoring little
9:20 details like this and little problem
9:23 areas like this when I'm rendering out
9:24 now because I can just fix those in post
9:29 edit within Photoshop so a lot easier
9:32 for me to just fix those in post edit
9:33 and not care about them if they're not
9:35 bugging me in terms of an elevation or
9:37 something like that if it's a hard fix
9:39 to do then it's just easy to fix these
9:41 out into um like your Photoshop or your
9:44 delete Vector Lines within Chief
9:46 Architect on an
9:49 elevation take care
9:53 [Music]
