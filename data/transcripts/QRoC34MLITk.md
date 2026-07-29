---
videoId: QRoC34MLITk
title: Twinmotion 2020 Tutorial-PART 8-Vector Masks, Scene States, and Quixel Megascans and Bridge imports
url: "https://www.youtube.com/watch?v=QRoC34MLITk"
status: imported
---

# Transcript

0:18 well this is a cool looking scene
0:18 what do we have here this looks like
0:21 it's twin motion it
0:21 is twin motion look at this
0:25 fantastic this is renee rabbit of rabbit
0:29 design and what we're looking at here is
0:30 a little preview
0:30 of part nine of this tutorial series
0:34 just wanted to give you a teaser before
0:37 we jumped into part eight
0:37 we're gonna be going over how to create
0:42 this scene in twin motion in part nine
0:44 please stay tuned for that i've been
0:45 looking forward to this video as a
0:47 little bit of a challenge
0:47 from the community from back in part
0:50 three so
0:50 stay tuned for this part eight coming up
0:59 okay we're in we're in part eight of
1:02 twin motion 2020 tutorial series
1:02 and to start off we're going to go over
1:05 something called scene states and you
1:06 can see here i've got two
1:06 10 meter boxes sitting in front of us
1:09 and we've got
1:10 box 10 meter and we've got we're gonna
1:14 just rename this guy to box number two
1:17 for a little bit of clarity
1:17 okay you can see here underneath the
1:21 scene graph we've got something
1:21 where it says statistics down here and
1:24 we've got a right
1:24 carrot in fact should be an up carrot
1:27 and because it expands upwards and you
1:31 can see if i click this
1:31 down carrot it's going to minimize back
1:34 down so
1:34 click this and it expands upwards and
1:37 then
1:37 if we go to the section where it says
1:41 statistics and that down carrot
1:41 i'm going to click that and we're going
1:44 to get to scene states simple
1:44 simple process so what we've got in the
1:48 bottom hand corner here is this little
1:48 plus icon and yes you guessed it it adds
1:51 a state
1:51 to our scene states which i actually
1:53 would prefer if they were called scenes
1:57 it gets a little bit redundant to
1:59 explain to new people
1:59 or doing any kind of tutoring so we've
2:04 got one state that's been saved now
2:04 now what that does is it's saving the
2:07 state
2:08 of the scene graph more specifically
2:11 if we were to make this box number two
2:14 go invisible
2:14 and i want to return back to the state
2:18 that i had saved
2:18 i can click on this and there you go
2:20 it's going to return everything back to
2:24 the way it was when this was captured
2:25 now of course we can
2:25 hit this icon which i believe is the
2:29 recapture icon if we
2:29 take similar icons that are you know
2:33 built throughout twin motion
2:33 and that would recapture this state so
2:37 that if i turned off box number two
2:37 and hit this recapture turned it back on
2:42 just to illustrate the point and then
2:44 click on state it should in fact
2:44 disappear because it recaptured the
2:48 state of that scene graph
2:48 to further illustrate this let's go
2:51 ahead and
2:51 turn this box number two back on
2:54 which you know state would turn it back
2:57 off
2:57 and let's add another scene state now
3:01 we've got a state number one
3:01 if i click on the first one it's got
3:05 that box off
3:05 here's a new state of the scene graph
3:08 and it's got that back box turned back
3:11 on
3:11 so that's really quick easy way of
3:15 creating multiple different
3:15 options if you want for a particular
3:17 project it's pretty powerful when you
3:19 think about
3:20 you know the different uses you can
3:23 implement using this feature of the
3:24 scene states
3:24 so now that we've got that out of the
3:27 way i want to introduce to you guys
3:30 mega scans mega scans is a company
3:31 called quicksole
3:31 they actually go out and scan 3d
3:35 geometry in the real world
3:35 and translate it into things that we can
3:40 use in twin motion in fact if you do
3:41 have some kind of
3:42 any kind of unreal product like twin
3:45 motion i believe you have access to
3:46 qixel's
3:46 mega scans and so if you download their
3:49 desktop software particularly for pc and
3:52 in my case
3:52 we've got something called their qixel
3:57 bridge and the quiksil bridge
3:57 is a portal if you will to their online
4:00 platform
4:00 where we've got access to all their
4:03 different 3d
4:03 uh files as well as a bunch of their
4:07 decals and a few other things so
4:07 some powerful stuff in here some really
4:11 high quality things
4:11 you can see right here i'm tucked into
4:15 the downloading
4:15 sections excuse me download settings of
4:18 this section
4:18 where i can you know set my preferences
4:22 for downloads
4:22 namely lod lod stands for level of
4:26 detail
4:26 and it's a sliding scale zero to i
4:28 believe eight if you get really into
4:30 this
4:30 uh level detail zero is going to be the
4:34 best detail that they offer
4:34 in their scans all the way up to things
4:38 that
4:38 don't have any detail at all it seems
4:42 and then various different
4:42 maps that are going to come along with
4:45 those 3d scans that we'll
4:45 download for you and i'll start this off
4:49 by saying i already downloaded something
4:51 i already downloaded something and so
4:52 we're going to import it and see what
4:54 the difference is between a couple of
4:56 these different level of details
4:56 so we'll go ahead and open and i'm going
4:59 to navigate to that mega scans library
5:00 which is right here
5:00 and then they've got a downloaded
5:02 section if you're using the bridge
5:05 software
5:05 on your uh on your pc and
5:08 this particular thing i downloaded is a
5:11 plant that's how it's categorized it's
5:13 categorized the same way it is in the
5:13 bridge software so that's how you have
5:15 to
5:15 locate it the naming convention isn't
5:19 always easy
5:19 to discern from what you actually
5:20 downloaded because this particular item
5:23 was called something completely
5:25 different than plants 3d
5:25 rj something something so i've got
5:31 three different versions of that
5:31 particular item and then within the
5:33 versions we've got
5:34 different levels of detail so go ahead
5:38 and click on one of these levels of
5:38 detail
5:38 expand my option i'm going to collapse
5:41 all and
5:42 leave it as such in fact i could try to
5:45 do the y up because i happen to know
5:47 that this is turned on its side but
5:47 this is just another one of those gripes
5:51 i have with twin motion
5:51 as i zoom to this selection you're going
5:54 to see
5:54 that in fact this thing is turned upside
5:57 down so
5:57 it is nice that we can change the axis
6:01 axis
6:01 i should say as it imports but without
6:05 any flip option there's no way to
6:06 correct things
6:06 such as this which means we've got to do
6:11 some workarounds unfortunately
6:11 now as i plant this on the ground we
6:13 notice we could see something that was
6:15 underneath here
6:15 yeah from over here on this side but we
6:19 can't see it from this side so we know
6:20 right away if we were to click our
6:20 eyedropper tool that we should be able
6:23 to go into settings
6:23 and turn two-sided on so we could see
6:27 both sides of this thing
6:28 so there we go we've got a level of
6:32 detail for item from mega scans
6:32 and let's go ahead and import a couple
6:36 more here we're going to do a level
6:36 detail
6:36 let's say two and see what this thing
6:41 looks like
6:41 it should look exponentially more
6:44 detailed than that first one
6:44 we're gonna go ahead and use the scene
6:48 material because we're gonna to edit
6:48 all these scans use the same material
6:51 which is
6:51 really nice especially if you've got a
6:55 couple variations because
6:55 then you can go through and fix a few
7:00 things
7:00 on a global scale in terms of the
7:08 let's do one more import we're going to
7:09 get that level detail zero which is
7:12 really going to be the good one
7:12 and then twin motion please can you give
7:15 me a little setting
7:16 here that just says save my last setting
7:19 so i don't need to keep expanding
7:20 options
7:20 and doing all these unnecessary clicks
7:23 like this
7:23 just save the last scene state and i
7:28 would be very very happy
7:28 so there we go we've got a level detail
7:32 zero there level detail two and a level
7:33 detail four
7:33 you can see that level detail zero it's
7:37 got a few extra
7:37 bits of geometry that the other uh level
7:42 details do not have so
7:42 uh very clear you know they've done a
7:46 good job of scaling this
7:46 especially for someone that's going to
7:47 try to keep their scene as realistic as
7:50 possible
7:50 or as quick and fast as possible
7:53 so let's go ahead and get into this
7:55 material file now i already know that
7:58 there's a problem with this material
7:58 file and we'll show you this in just a
8:01 second before i get too far
8:01 i don't know why this is set to gray but
8:05 let's crank it back up to white
8:05 and then hit that more category and load
8:09 in a texture
8:09 i'm going to navigate back to that mega
8:12 scans library
8:12 and then find that same plant and get
8:17 into the textures folder
8:17 and then i'm going to get into the atlas
8:22 folder so in here is my albedo map
8:24 commonly called an albedo map it's
8:24 similar to a diffuse map or the main
8:26 texture that they you know built this
8:30 geometry from so there we go we can see
8:36 it looks looks pretty good so far
8:39 obviously that level detail
8:39 four is is lacking a little bit now the
8:43 main problem here is
8:43 even if we turn on this opacity mask
8:47 nothing happens
8:47 and that's because this main texture is
8:51 built as a jpeg
8:52 which jpegs just don't carry any kind of
8:55 transparency with them so
8:55 we're gonna have to create transparency
8:59 unfortunately i'm gonna need a separate
9:01 software to be able to utilize this
9:03 particular mega scans
9:03 that's not true of all mega scans but
9:06 this particular one
9:06 it is so i'm going to use photoshop for
9:10 this particular
9:10 task and you can see here i've already
9:12 done it once just illustrate what we're
9:15 looking for
9:15 we want to make it so that this check
9:18 checker section actually is
9:18 saying that there's no texture here at
9:22 all and to get there is
9:22 a little bit of a process but it's not
9:24 too bad i don't want to make this into a
9:27 photoshop tutorial but
9:27 all i did was take the albedo mask
9:33 bring in the opacity mask and then
9:40 let's see shift control z it's going to
9:41 be
9:42 i flipped the two i made layer zero that
9:47 albeit a mask of clipping mask onto
9:47 that opacity mask and then i inverted
9:51 the opacity mask
9:51 and then i deleted everything
9:55 outside of that it made a quick
9:58 selection mask if you will
9:58 or a clipping mask so i was able to clip
10:02 this out
10:02 and then the last bit of this is i want
10:06 to export this as a png file because
10:06 png file will carry that transparency
10:10 through and here you go right here
10:10 that's a png image that's the one that
10:14 we're going to need
10:14 so um plenty of tutorials online on how
10:20 to create this particular effect
10:20 the ultimate result is going to be that
10:23 we're going to upload
10:23 a different albedo mask which is this
10:28 guy right here and we're going to see
10:30 all of a sudden that clipping takes
10:30 place when we've got this opacity mask
10:35 option turned on in our material
10:36 properties
10:36 and you can already see this is starting
10:40 to look pretty good
10:40 so next thing is we've got
10:44 in our settings bump or normal mask
10:48 which
10:48 twin motion will automatically take a
10:52 normal mask as a normal mask
10:52 instead of say a black and white
10:55 gradient bump mask
10:55 so we'll load this normal mask up this
10:59 is going to make kind of a
10:59 big difference as it plays with
11:02 reflection
11:02 which we also did get a reflection mask
11:05 from qixel
11:05 as well or what's called a glossiness
11:10 mask
11:10 once we turn that reflection up we're
11:14 really going to see that bump max
11:14 mask take hold or that normal map take
11:18 hold here
11:18 you can start to see the texture in
11:21 these and i mean they start looking
11:21 really fantastic i mean this these quixo
11:25 skins
11:25 just look fantastic especially when
11:28 we've got it
11:28 double-sided so we can't see through the
11:32 underside of this
11:32 it looks nice that level detail for
11:36 probably gonna never use that
11:39 so i'm okay deleting him
11:39 maybe way off in the distance that might
11:43 be helpful but probably not for
11:43 for my general purposes this of course
11:46 is is pretty nice
11:46 you really have to weigh you know the
11:50 pros and cons of how detailed and
11:50 you know close up do you need to get
11:54 here this level of detail too would
11:54 probably work for me for most scenes
11:57 so i might want to say that to the
11:57 library and then that level detail for
12:02 excuse me level detail zero just looks
12:03 as good as it can
12:03 look of course you can download 4k
12:07 resolution
12:08 texture maps that gets to be pretty
12:10 heavy on your system these are in fact
12:13 2k
12:13 resolution maps i could probably
12:14 decrease that as well did something
12:17 uh as low as a thousand resolution or
12:22 even a 512. so
12:22 this is all part of downloading that
12:25 that quixo bridge
12:25 assets and getting them into twin motion
12:29 and of course saving them
12:29 into your library now before i save
12:32 these into my library
12:32 i want to touch on a trick that i went
12:35 over on part seven
12:35 of this uh twin motion tutorial series
12:39 and that is
12:39 i want to go in and get a positioning
12:43 node is what i like to call it
12:43 i'm going to go into my primitives and
12:47 pick something like this cylinder
12:47 which is maybe a little too big let's go
12:51 for a one meter
12:51 cylinder there and i'm gonna shrink him
12:54 down hit my number six key so i can get
12:56 to scale and scale this guy
13:01 and then i'm gonna apply something like
13:04 a dirt to him and position him right
13:05 where i need him to be
13:05 underneath this i'm going to get in
13:06 tight just make sure that's the right
13:10 location it is
13:10 and back out a little bit maybe i'll put
13:14 something like
13:14 dirt onto this there we go
13:18 i'll adjust that scale just a little bit
13:23 and now that i've got that called dirt
13:23 i can go ahead and rename this cylinder
13:27 something like
13:27 flower and drop
13:30 this guy right on top of him if i drop
13:33 it to
13:34 the so that there shows up a line in the
13:37 down carrot on the left side
13:37 it's going to just change the order of
13:40 the hierarchy in the scene graph
13:40 but if i drop it on top of flower flower
13:44 now is apparent
13:44 to this child here and so if i click
13:47 on the parent and move the gizmo it's
13:51 going to move that object
13:51 together which is a great thing
13:54 especially if i want to move it onto
13:55 some kind of oops didn't mean to rescale
13:59 it there
13:59 if i want to move it on to some kind of
14:02 off-angle geometry
14:02 makes it really more of a powerful setup
14:05 so
14:05 add that to my library the only negative
14:09 thing about that is if you're just
14:09 clicking on things such as this you're
14:13 catching
14:13 the child of this object and now it's
14:16 going to turn sideways
14:16 so you'd have to click this go to the
14:20 scene graph make sure you get that
14:20 parent object to be able to utilize this
14:25 in the way it was intended so twin
14:27 motion hope you guys fix that but
14:27 that is my workaround at the moment
14:33 okay so now we're gonna bring you back
14:34 into that main scene and let's just take
14:37 a look we've gone over seeing states you
14:38 can see here
14:38 just quickly how how how amazing is that
14:43 i've obviously got some walls i've
14:45 duplicated them applied different
14:46 materials to them
14:46 and then created scene states so that i
14:50 can quickly change finish options
14:50 and most importantly this vector mask
14:52 which we're going to talk about in just
14:54 a minute but before we do let's just
14:54 take a look at some of the other mega
14:57 scans that are in this scene
14:57 all these curves here this transition
15:02 piece curve here where it tapers down
15:02 the posts over here on this railing and
15:07 the railing itself
15:07 all from mega scans really a really
15:10 sharp way of bringing some high quality
15:14 stuff into the foreground of your shot
15:16 so please go take a look at that
15:18 fantastic stuff
15:18 um back to our vector masks we've gone
15:22 over scene states let's look at
15:22 what vector masks are even going to do
15:26 for this scene
15:26 and if you've never seen a movie with a
15:30 green screen i mean most people are
15:32 pretty familiar with that
15:32 and it's used so that's easily
15:35 selectable
15:35 and then you can do something well in
15:38 terms of movies do something like
15:40 rotoscoping
15:40 in this case we actually want to just be
15:44 able to edit certain materials
15:44 and so to do that you need to set up an
15:48 image and then duplicate that image
15:51 or just recapture that image in the
15:51 various
15:52 scene states now for the purpose of this
15:56 i actually want to do one thing
15:56 more which is if we go into this more
16:00 section under lighting
16:00 i ended up dragging this shadow all the
16:04 way down to 10 meters you can see
16:04 from a default it's somewhere in like
16:06 250 meters range or something like that
16:08 you can see the shadow from this tree as
16:10 it's cast
16:10 upon the gable here you can see that
16:14 this whole side is cast in shadow
16:14 i want to pull all those shadows out
16:18 because really i don't need to see
16:20 accuracy in this model in terms of
16:20 shadows what i really need to see is i
16:24 need to see this material nice and
16:26 bright and clean and clear
16:26 so i might go in after pulling the
16:30 shadows out
16:30 go ahead and capture that image again
16:35 recapture this
16:35 and then quit my media mode and do my
16:40 last edits to this material
16:40 make sure that it's just what i need it
16:43 to be
16:43 maybe throw an additional glow on it
16:47 something like that
16:47 and then get back into that image
16:50 property and export
16:50 out once we've got it exported we can
16:56 put it into a layer stack in some
16:57 software like
16:57 photoshop again i don't want to be tree
17:01 and training in photoshop but
17:01 just for the purpose of this video let's
17:05 take a look at what that mask can do
17:07 with tools like the magic wand in
17:08 photoshop it's
17:08 very easy to select exactly what i want
17:12 to select here which is that material
17:14 that that i wanted to edit out
17:14 right very simple for me to do that and
17:18 then the next thing to do is i'm just
17:18 going to turn off that vector mask and
17:22 look what happens underneath i can see
17:22 that i've selected that stucco and i can
17:25 do things like
17:26 delete that stucco if i'm on the right
17:29 layer there you go
17:29 to reveal a cat on my gable end here so
17:34 some funny things but you can see that
17:34 it's perfectly shaped within that gable
17:39 so there's the purpose of the vector
17:40 mask there's kind of a
17:40 way of creating a vector mask using
17:45 scene states and some new materials
17:45 and i hope that helps some of you if you
17:49 need to do some heavy post edits or show
17:49 some
17:50 additional options or even make more of
17:54 a realistic scene you could use
17:54 this same kind of setup to do things
17:59 like do a little editing just on
17:59 one particular material or duplicate and
18:04 bring in a whole shadow channel or
18:04 something like that or a clay rendering
18:06 on top
18:06 so a few different things you can do
18:10 with vector mass
18:10 that's going to be it for this video i
18:13 hope you enjoyed please
18:13 stay tuned for the next part we are
18:17 going to be going over that
18:17 the fun little challenge where we
18:20 recreate a scene so
18:20 stay tuned and and as always please
18:28 subscribe
