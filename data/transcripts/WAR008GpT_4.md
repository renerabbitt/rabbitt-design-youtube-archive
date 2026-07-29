---
videoId: WAR008GpT_4
title: Twinmotion 2020 Tutorial-PART 4-Decals
url: "https://www.youtube.com/watch?v=WAR008GpT_4"
status: imported
---

# Transcript

0:13 okay I think we're on video number four
0:15 for twin motion so if you haven't
0:15 watched the previous videos please go
0:19 check them out on my channel in this
0:19 playlist for twin motion and what we've
0:23 done here is we've taken a model from
0:23 chief architect we've imported into twin
0:27 motion and we're slowly working through
0:29 it and trying to make it look realistic
0:32 so what we're gonna be focused on today
0:34 is this driveway I just want to spend a
0:36 real short amount of time on this
0:36 driveway and kind of detail this guy out
0:40 the first thing I want to do is let's
0:42 just take a look at some of the
0:42 materials that are available to us and
0:47 I'm gonna go into ground and our
0:47 man-made section here and we've got a
0:51 couple different like cobblestones
0:51 we've got this concrete road let's check
0:56 out the old cobblestone smooth
0:56 cobblestone yeah we've got the wave
0:59 cobblestone all pretty cool maybe we'll
1:04 stick with you know kind of this older
1:04 looking or I don't know let's check out
1:09 all these I like the smooth cobblestone
1:12 so already off the bat we can see one
1:14 thing is that the scale of this
1:14 cobblestone is a little off so I mean we
1:20 have a submenu here for this material we
1:23 can increase the scale exponentially
1:26 just immediately with just a drag of
1:26 this obviously if you just click on the
1:28 number itself you can designate your own
1:32 scale if you know what you're looking
1:32 for at this scale we're starting to see
1:36 some detail that I really like some
1:36 breaks on this here yeah it looks pretty
1:42 good so a bigger part of this video is
1:44 that we're gonna look at some of twin
1:47 motions decals which is an awesome
1:50 awesome feature so under materials
1:50 excuse me under ooh objects there we go
1:56 it's under objects we've got this right
1:59 here which is decals and you'll can see
1:59 as I bring this out into the model space
2:04 it's creating look at that zebra
2:04 crossing us-style crossing you can get
2:10 these layered on top of each other you
2:12 can scale them you can do a couple
2:13 different things to them
2:13 um so first thing I'm going to do is
2:15 well I will put some cracking in this
2:21 driveway and we're just gonna work
2:21 through this until it starts looking
2:24 good so I'm gonna scroll way down
2:24 because I know that I've got road damage
2:28 way down here and I'm gonna kind of put
2:32 it next to I don't know kind of the end
2:34 here and you see one thing that's
2:34 happening right away and we'll address
2:39 this right now is that this road
2:39 cracking is not bound to the item that
2:43 we've seemed to have isolated right and
2:48 so let's first thought would be what if
2:50 we isolate the selection can we get rid
2:51 of it then let's go over to a scene
2:51 graph and if you're unfamiliar chief
2:54 architect any other software it always
2:56 has some version of this some version of
3:03 a graph or a hierarchy or you know just
3:07 it's a project browser some version of
3:09 your project that you can go in and
3:09 isolate selections so I'm gonna delete
3:12 this guy right here and the first thing
3:15 I'm going to do is I'm going to select
3:15 this roadway and I'm gonna isolate that
3:22 selection now we've got an isolated
3:22 let's see what happens if we bring the
3:25 road damage in now let's see if it
3:25 changes anything here so go back to the
3:31 scene graph and exit isolate selection
3:31 look what happen it's still carried over
3:36 to this so it's not a true isolate
3:39 selection what a shame twin motion
3:39 please feature request so to get around
3:42 this I'm gonna do what this offset right
3:48 here and I'm not going to get into the
3:48 minutiae of what exactly this does it's
3:53 basically changing oh it's not really
3:53 changing the bounds for the purpose of
3:55 this video let's just say it's changing
3:59 the bounds of that decal so if I change
4:02 it to one you can see immediately that
4:02 it's essentially like changing the grip
4:09 at what it's um at what's being dropped
4:10 on to so there we go
4:10 we've seem to have isolated that
4:12 cracking just to where we want it to be
4:17 next thing is we've got a bunch of
4:17 different patches and leaking water etc
4:20 that we can do we can do this along this
4:25 area here and
4:25 along this area here and and then Oh
4:28 what if I wanted to have four more or
4:29 five more times well let's think about
4:34 that why can't we do it four or five
4:36 more times so let's go over to the
4:36 Seaton graph I'm going to select this
4:38 first one here and I had to hit a bunch
4:42 of buttons to figure this out and I
4:42 believe it was well it's not alt because
4:54 as I hit alt it doesn't do anything so
4:56 hit shift we drag it over to where we
4:58 want it to be and it gives us this
4:58 option instance copy number spacing and
5:05 to understand this you really need to
5:08 understand what an instance is if you
5:10 were familiar with sketchup you know
5:10 that if you create a component and then
5:14 duplicate that component any edit to
5:17 either component carries over to its
5:19 duplicate component because it is an
5:19 instance same thing goes here this is an
5:25 instance of this first decal that we
5:25 created if we edit the first decal it is
5:31 going to edit the second decal as well
5:33 so long as it is an instance and not a
5:33 copy for the purpose of this let's just
5:39 make this guy a copy and we're gonna
5:39 make oh I don't know like five of these
5:45 sure and we're gonna see what happens
5:46 what it's gonna do is it's gonna
5:46 duplicate it along this line now granted
5:51 art draw distance right now you know in
5:53 my settings in two in motion my
5:53 preference is letter quality I've got it
6:00 set to ultra it's as far of a draws
6:02 distance as I can get so as we get
6:02 closer to these decals they should show
6:09 up right wrong the reason being is that
6:09 we are not quite in plane we've got this
6:15 terrain is actually sloping up so what
6:18 happened there was that an instance to
6:21 along and access and now they've all
6:22 disappeared
6:22 so not a perfect tool it'd be nice to be
6:29 bound towards this road markers so that
6:31 you didn't have to go through and place
6:33 these one by one so let's get back to
6:33 this first one here and I want to just
6:36 show what I'm doing
6:36 to this first guy this first instance of
6:40 this and sometimes it's very difficult
6:43 to select these decals so please don't
6:45 forget you've got your scene graph and
6:45 you need to organize your scene graph to
6:49 be able to understand how to locate
6:49 these items so here you go and one thing
6:53 I'm going to do right off the bat is I'm
6:56 just gonna set the opacity to barely be
6:57 visible same thing with this other
6:57 leaking water or maybe I crank it all
7:02 the way up who knows but just gonna
7:02 barely put it on there and let's get
7:04 back into our objects and decals take a
7:11 look at some of the other decals we've
7:13 got here we've got some various stains
7:17 we can do you know just kind of try to
7:17 make this roadway feel a little bit more
7:22 realistic this stain you know I know I
7:22 want to have a little bit more of pasty
7:23 almost looks like we've got some kind of
7:28 a road leak going on let's change to our
7:31 scale tool which i think is number six
7:36 on the keyboard it is and actually we
7:36 don't use the scale tool we use the size
7:40 tool on these decals so long crease that
7:42 up it's kind of just like creating a big
7:46 shadow if you will and so now we're
7:46 starting to get a little bit of realism
7:50 in this let's take a look back and use
7:50 this eyedropper tool and select this and
7:57 see if we can't mess around with this if
7:58 you will we're gonna tint this a little
7:58 bit I want to get a little more depth in
8:04 there maybe a darker color now we're
8:06 starting to really see things and so
8:06 this is a nice segue into the next video
8:11 which is we're gonna be looking at all
8:14 the weather and lighting tools to get
8:16 this scene to look where we want it
8:16 because I want to establish lighting
8:19 before I go any further so that I have a
8:25 better understanding of how it how these
8:28 tools interact with what is gonna be my
8:31 final shot so there we go
8:31 that's the end of this video appreciate
