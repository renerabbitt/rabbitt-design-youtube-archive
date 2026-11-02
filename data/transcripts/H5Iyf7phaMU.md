---
videoId: H5Iyf7phaMU
title: What's New in Chief Architect X16 - PART 4 - Designers Show #131
url: "https://www.youtube.com/watch?v=H5Iyf7phaMU"
status: imported
---

# Transcript

0:00 going to make a cup of coffee so give me
0:01 a minute wait I know Robin you're
0:04 supposed to say
0:05 hi we're live now
0:10 hi everybody sorry I was getting my cup
0:13 of coffee welcome everybody I am
0:16 thrilled you're here today we're going
0:17 to be talking about what's the last of
0:20 the list hopefully depending upon how
0:24 far we go in the weeds of what's new in
0:26 Chief X um
0:28 x16 and most it's on rendering so Renee
0:31 is going to be our fearless leader
0:34 course it's about renderings
0:39 that's we all know that Rene can tend to
0:43 um explain things that he knows very
0:45 well with the proper terms and things
0:47 like that but we basically have no idea
0:50 what he's talking yeah so it's aene
0:53 bring it back down if he says something
0:56 you need more clarification or a
0:58 definition of a word or something like
1:01 that I will try to ask them because I am
1:04 in the dark as as much as anybody on the
1:08 things that he says so but if you have a
1:11 question about that make sure you put it
1:12 in the chat and we'll we'll try to work
1:15 it in and get it get it asked yeah hi
1:17 Richard hi Kenny welcome Todd who's new
1:20 and hi Anthony hello everybody not new
1:23 but he's a he's um he's subscribed to my
1:27 VIP section on my YouTube and I you guys
1:30 and say hello and say thank you thank
1:32 you very
1:33 much hi
1:35 everyone cool so I'm looking forward to
1:37 a great day today
1:39 Renee yeah give it to
1:42 us John's just gonna be roasting me
1:45 today it's gonna be great when was
1:48 that somebody has to do
1:51 it we left off on number 31 uh which was
1:55 HDR
1:56 backdrops
1:58 and uh
2:01 actually rich I'm gonna give a little
2:03 backstory I have my backs of Grands
2:05 ready let's just put on screen real
2:07 quick here's the let's do it Margaret
2:11 the backstory is that I made a post like
2:13 three or four years ago on the chief
2:15 talk forums Chief Architects forums and
2:18 it was a list of things that um a
2:21 professional rendering artist would want
2:23 in the software and the the lead uh
2:28 developer of the rendering
2:30 um and also um another guy in the
2:33 department Dan they reached out to me
2:36 and wanted more of an explanation about
2:38 what I'm even asking about um and we had
2:41 a big back and forth and then I ended up
2:44 seeing them in Idaho and doing a little
2:46 bit more of a back and forth and just
2:47 talk and Shop um because the complexity
2:50 of building the rendering engine to what
2:52 it is now is exactly what you're talking
2:55 about John is is we have to we want to
2:58 give you the tools but they they end up
3:00 really confusing the end user and which
3:03 ends up you know Chief is kind of built
3:06 around this SSA right there's software
3:08 Assurance there you get to call them you
3:10 get to ask them questions so they are
3:12 trying to mitigate the number of calls
3:14 that they're receiving so it's really
3:15 complicated to build a complex rendering
3:18 engine and still make it user friendly I
3:21 think they did a really great job um one
3:24 of the items that they did was HDR
3:27 backdrops and um HDR backdrops High
3:30 dynamic
3:31 range are old backdrops in X15 and prior
3:36 that was regular PNG based images if
3:40 you've ever seen that before um PNG is
3:43 an extension file extension and that
3:45 extension type is what we would call
3:47 lossless there's no
3:50 compression on the image you won't see
3:53 many artifacts in a PNG file type jpeg
3:57 or wa what do you mean by artifacts what
3:59 do you mean by artifacts we wouldn't see
4:02 let me see if I can I don't know that I
4:03 can um fake that on the fly but
4:06 artifacts would be and this is this is
4:08 not what we're seeing now this is they
4:09 fixed not what we're seeing now right
4:12 and so um just know that J jpeg is
4:16 inferior to PNG if you had the ability
4:20 to get a material that was a PNG based
4:23 material that would be a better material
4:25 to use um especially in the bump map
4:29 Maps within Chief Architect the bump map
4:32 simulates height in your material if you
4:35 use a JPEG you will see some things that
4:38 don't look sharp or crisp or exactly the
4:40 way that you want them to look okay all
4:43 I have to say is that before we used PNG
4:45 based backdrops and we're limited to 155
4:49 colors where zero is is um white or
4:54 black I'm gonna get this backwards all
4:56 of a sudden zero is black 155 is white
4:59 right got it um so 155 155 155 RGB is
5:04 true white 0000 Z true black now HDR
5:09 image has I don't someone could look it
5:11 up but it's more than millions of
5:13 different color values that you can use
5:15 okay and so that can bring in a lot of
5:18 natural tone into your shot now I'm in
5:21 my um I'm in my uh template right now
5:25 and in my template I have one of these
5:28 HDR images
5:30 and so when I pull a 3D view it defaults
5:34 the using this HDR image right out of
5:36 the bat so like as soon as I start
5:38 pulling a view it's already using the
5:41 HDR um for its basically for its color
5:44 grading color quality um it's ambient
5:47 lighting everything and in case you're
5:51 not aware of this how you even set this
5:53 up is and our rendering technique
5:56 options and know hopefully you'd be able
5:58 to look up some of these terms but
5:59 rendering technique options we can set
6:02 it up so that in our um when we're using
6:05 our physically based Ray Trace
6:08 okay we have this option now use only
6:11 backdrop for lighting if we uncheck this
6:15 you're going to see immediately that
6:16 this scene changes pretty drastically
6:19 right suddenly this is being lit by Sun
6:23 so now my sun settings are taking over
6:26 the backdrop is still lighting the backs
6:29 side of this house it's providing
6:31 ambient light to the back side of this
6:32 house but now the sunlight I'm I have
6:35 control over that in terms of you know
6:38 um the direct glare on the house the
6:40 direction of the sun is very pronounced
6:43 right and starting in X15 we were able
6:46 to use What's called the move Sun tool
6:49 and we could click somewhere on the
6:51 screen and move the sun around just like
6:54 this so I'm just clicking and dragging I
6:57 mean so this is still a very viable
7:00 technique option we're have we have the
7:02 back side of this house being lit by the
7:03 backdrop and then we have the front side
7:05 of this house being lit by the sun we
7:08 also have What's called the move excuse
7:11 me rotate spherical
7:13 backdrop so when I use this tool same
7:16 kind of thing I can click and drag and
7:18 you're going to see that I'm rotating
7:20 the backdrop
7:21 itself amazing so this really helps for
7:25 you know setting up a composition on
7:26 your exterior shots and interior mind
7:29 you a second Renee Rebecca if you can
7:32 hear us yes it's started the video is
7:34 going I don't know if you can hear us or
7:36 not but everything is working good on
7:38 our end okay did you double check that
7:41 we are um streaming
7:43 feed I didn't but yeah someone said his
7:46 Pike's Peak behind your head so there
7:48 you
7:49 go that was Nikki hi Nikki hi
7:52 [Laughter]
7:54 Nikki so something that's really
7:57 compelling about the HDR backdrops for
8:00 me is that um with a photo editor you
8:04 can come in and fake a sun location
8:08 which is kind of an interesting thought
8:09 I show how to do this in my membership
8:11 area on YouTube um I'm gon to go back to
8:15 my rendering technique options and and
8:17 check that box again for use only
8:18 backdrop for lighting right for lighting
8:21 for lighting now I want you to notice
8:22 something as I pan this shot around this
8:25 right here I put this here this was a
8:28 big spherical image
8:30 um looked like it was cut up and wrapped
8:32 around an orange and then unwrapped
8:34 right is what a backdrop essentially
8:36 looks like and so I took this into a
8:39 photo editor and I put this big Splat of
8:41 sun and then we all know what exposure
8:45 is I lowered the exposure on the overall
8:47 shot put this Splat of Sun so what
8:50 happens with this is this is actually
8:52 faking a directional sunlight with this
8:54 technique option you can see here on the
8:56 left hand side especially if I turn uh
8:58 the exposure up a little bit more you
9:00 can see on the left hand side that this
9:02 is picking up the sun right here right
9:05 it's being projected against this
9:06 surface if I rotate this backdrop with
9:08 the rotate backdrop tool to the back
9:10 side of this house you're going to see
9:12 that we've got a little bit of shadowing
9:14 on the ground now as I rotate this
9:16 around wow so this is actually
9:18 directional in a way now I've lit the
9:20 this right side rotated some more now
9:22 I've lit the whole front side so kind of
9:25 an interesting technique
9:27 and another thing to keep in mind is
9:30 when we pull a exterior shot and then we
9:33 move our camera into the interior shot
9:36 well Chief has what's called automatic
9:39 exposure adjustment it's working very
9:41 similar to the way if you were a
9:43 photographer or the way that metering is
9:46 working is we're sampling light and then
9:48 based on that light we're adjusting our
9:50 exposure automatically if for some
9:53 reason you move from an exterior camera
9:56 and move that camera into interior and
9:58 you're
10:00 underexposed it might be that you need
10:02 to rebuild the scam which would be in
10:04 the 3D
10:06 menu rebuild 3D and then it's going to
10:09 basically Remer this scene and readjust
10:12 its exposure um it was working correctly
10:15 for me but sometimes it's not always
10:16 working correctly the other way to
10:18 rebuild the scene is just draw anything
10:20 you could pop a cabinet in here and it
10:21 would suddenly rebuild as
10:24 well so something that goes back through
10:28 the previous vers versions too is
10:30 sometimes people would have a bunch of
10:31 lights in their scene and some of those
10:33 lights would be turned off and um part
10:36 of what that is is in the active view
10:39 itself you might have a setting that
10:41 says maximum lights here so that if I
10:43 had say two maximum lights and I popped
10:47 in three different lights in this
10:51 scene look one's not going to turn on
10:54 right oh now on top of that if I had
10:58 let's just say another room here
11:00 involved and I move that third light or
11:03 I copy this third light to that other
11:05 room we still only have a maximum of
11:08 three lights well it's rebuilding based
11:10 on what room the camera's in so it's not
11:13 necessarily predictable which lights are
11:15 going to be turned on watch what happens
11:17 when I place a cabinet in this room
11:20 suddenly this light turned on right
11:23 that's because it's rebuilding the scene
11:25 based on where the camera is so keep in
11:28 mind we can make lighting sets that we
11:31 can save to a camera so you could save
11:33 your kitchen camera and make sure that
11:36 all of your kitchen lights are turned on
11:38 in that view wow that's not that's not
11:40 nud x16 but that's good information if
11:42 we're talking about rendering and we're
11:44 kind of troubleshooting what's happening
11:46 with lighting
11:48 wow question so far yeah Margaret had a
11:51 question okay how does this work with
11:54 just regular picture of someone's
11:56 backyard well you have to do a 3D image
11:58 right it will work with some caveats you
12:02 won't have correct reflection in your
12:04 window you can see right now we're
12:06 getting a reflection in my window if I I
12:09 rotate this view it should rotate that
12:12 reflection um it doesn't that won't work
12:15 with a still image because of the way
12:18 Chief is processing that still image
12:19 they're basically repeating it in a way
12:21 and doing the best that they can to
12:24 create you know a backdrop image for you
12:27 so um doesn't quite work the way you
12:29 would want it to you'd have to get into
12:31 an editor and and create a spherical
12:34 rendering and you could probably find an
12:36 online tool to kind of fake that um yeah
12:40 depends and then Jeffrey had a question
12:42 that rebuild the scene button was again
12:44 yeah that's in the 3D menu down at the
12:47 bottom rebuild 3D and you could drop
12:49 this into your toolbars of course or
12:53 um we know this is a new thing is you
12:55 could drop the tool search into your
12:57 toolbars and we would just type in
12:59 rebuild and there you
13:01 go wow you're doing it a lot you can put
13:03 a hot key on
13:05 it um what's that you could put a hotkey
13:08 on it if you do it a lot you do a hotkey
13:11 or like I said if you just drop an
13:13 object in the scene it will rebuild as
13:15 well um nice yeah let's see so you can
13:19 rotate any regular photo not spherical
13:21 photo that's a good question I don't use
13:23 any regular photos so let me see if I
13:25 can't find one in the browser real quick
13:30 I do believe Chief has just some still
13:32 image backdrops um something to keep in
13:35 mind sh your head I mean I swear to God
13:37 it's like I just shake my head I still
13:38 don't understand half the things you're
13:39 talking about oh well ask me questions
13:42 no no you're fine it's just this is it's
13:45 it's just very um detailed right I mean
13:48 this is part of the program that you're
13:51 an expert in I don't use as much not to
13:53 the extent that you do I mean I use it
13:55 but it's not to this extent so it's
13:58 amazing always a shock I'm always I I'm
14:01 always amazed okay um what's awesome
14:04 about the rendering engine is you could
14:06 go at it not knowing what you're doing
14:08 and get some okay results out of it
14:11 right so that part's kind of fun I think
14:13 that's what brings everybody into it a
14:15 little bit absolutely um I want to note
14:19 that backdrops inherently are very large
14:22 image files my own backdrops um equate
14:26 to 13 gigabyt of data that's a large
14:29 chunk of data so when you're searching
14:32 for backdrops in your library
14:34 and chief I did do believe has some kind
14:38 of a cache
14:40 CA where once it's loaded something once
14:43 it will load it faster it keeps it in
14:45 some kind of um memory but if you
14:48 haven't built the cache if you haven't
14:50 been working in the software for a
14:51 minute and you try to search backdrops
14:53 it may take a long time might even seem
14:55 like it's freezing your computer like I
14:57 just searched for it right now and it's
14:58 it's taking Tak a really long time to
15:00 load
15:01 so yeah there's a little advertising for
15:03 you
15:05 Renee what's that oh cool yeah every
15:08 wants to be a subscriber to Rene's VIP
15:10 page yeah I go over some some detailed
15:12 stuff in there I just did one on symbol
15:15 modification and Ray tracing in the new
15:17 engine because they changed to some
15:18 other things that affected some of my
15:20 symbols so I got to go fix them okay so
15:23 let me see if I can find a still image
15:25 in the chief Library so in case you
15:28 didn't know this um I searched backdrop
15:31 in the
15:32 library and then if I want to limit my
15:35 search to just Chiefs backdrops I can
15:38 come in here and click this folder and
15:39 now we are filtering just by Chiefs
15:42 backdrops and I think some of these are
15:46 just still images just try this Farm
15:50 Overlook yeah that's just a still image
15:53 so you can't rotate the backdrop you can
15:57 rotate your scene in the backdrop will
15:59 stay static is what Chief's doing there
16:02 got it and in terms of the
16:06 reflection all right I see houses in the
16:09 reflection here if we look out this way
16:11 H we don't really know where that's
16:12 picking up from right and it's not it
16:15 you really have to position your camera
16:18 in a way that's going to be make sense
16:20 for your shot with these static back Tru
16:23 so a little more
16:26 challenging so marget got a question
16:28 here should should you just put in a
16:30 large number for lights to cover any and
16:32 all
16:33 lights um that just has the potential of
16:37 slowing your machine down a great deal
16:40 um I would say maybe a better workflow
16:43 for that would be to I'm going to open
16:45 up this room I'm going to name it
16:47 kitchen which by the way when you first
16:50 open up a room dialogue box notice that
16:53 this is already highlighted you don't
16:55 actually have to Pi your mouse and click
16:57 here you could just type in kit and hit
17:01 enter I don't actually have to move my
17:04 mouse at all so that's all I did I'll
17:06 show that again I'm just going to open
17:07 up this room and I'm just going to start
17:10 typing livv for living room and hit
17:14 enter and there we go it's that quickly
17:17 right so if all you're doing is naming a
17:19 room it's very quick so now we've got we
17:23 know what lights are associated with
17:25 what room if we open up and this is on
17:28 the default tool bars let me switch to
17:29 those I believe in the drop down menu
17:33 adjust lights that's this right here so
17:36 if we hit adjust lights this is where we
17:38 can make a light set to be associated
17:41 with a camera so right now we've got a
17:44 default light set I'm going to say new
17:47 set now by default this new set will
17:50 have all lights turned off all right so
17:53 I'm going to call this kitchen
17:56 lights so there we go it unchecked
17:59 all lights now I
18:02 can sort just by clicking on this
18:05 heading doesn't seem like that click
18:07 does anything but it will sort once you
18:09 click on any one of these headings and
18:11 any subsequent click will be a
18:13 subsequent sort okay so if I had a bunch
18:17 of on floor two and I wanted to organize
18:19 by floor two then I wanted to organize
18:22 by floor on floor two I believe you
18:24 could still just click on room next and
18:26 it would do that so here's my kitchen
18:28 lights I can click I can shift click and
18:32 then I can click to on and now I have a
18:35 kitchen lights light set where all the
18:37 kitchen lights are turned on now the
18:40 next thing I want to do is I want to
18:42 come into this camera and I want to set
18:45 this up so that it's using the kitchen
18:47 light set how do we do that we go into
18:50 edit the active
18:52 view that's this guy right here paper
18:54 with a pencil on it and down here at the
18:59 bottom lighting section we're going to
19:02 choose light set and we get to drop down
19:04 and choose kitchen lights and then you
19:07 would want to save this camera so we'd
19:08 want to save this camera that's this guy
19:11 right here or maybe save as right save
19:14 active view as kitchen
19:17 camera there we go so now every time I
19:20 open this up my kitchen lights are going
19:22 to be turned
19:23 on so in my project browser that now
19:26 saved underneath my projects heading in
19:29 the camera's folder under first
19:32 floor uh or it didn't oh this was an
19:35 overview camera oops so there we go
19:38 there's my kitchen
19:41 camera any questions on that
19:44 part um you you mentioned that you we we
19:48 hear a lot of things about or from
19:51 people that their computers running slow
19:53 and stuff like that you mentioned that
19:54 having a bunch of lights on will slow it
19:56 down yes is that possibly some of the
19:59 things that's going on with them when
20:00 they're having a slow
20:01 computer yeah possibly um there's a
20:04 number of things that can slow it down
20:06 if you have the line over technique
20:09 option or any kind of vector based um
20:12 rendering technique option that can slow
20:14 it down considerably it takes a lot to
20:16 try to convert Vector lines to raster
20:19 based lines basically that can slow it
20:22 down um if so especially if you've done
20:25 some kind of custom pattern from the
20:28 texture I encourage people to not do
20:30 that especially do not save that to your
20:32 library that causes a bunch of slowdowns
20:34 saving pattern from texture yeah so like
20:37 if I were to go in and use the rainbow
20:40 bacon tool to adjust the material here
20:43 and you see that we have a grid pattern
20:45 here but if instead I clicked on this
20:47 button which this was an elegant
20:50 solution but Chief is not optimized for
20:52 its output so we can see here this is
20:55 creating thousands of mini Vector lines
20:58 and um to recreate this in a shot ends
21:02 up really slowing your computer down I
21:04 used to have a bunch of textures save
21:06 that had this um this custom pattern
21:09 saved with it and I couldn't even access
21:11 my library after a while um and took a
21:14 while to troubleshooting figure out what
21:15 was going on so enourage you but then
21:17 when you're just doing a vector image
21:19 when then when you're doing just a
21:20 vector image a black and white image
21:23 you're not going to see any pattern
21:24 you're not going to see any patterns but
21:26 they did in X15 give us the new pattern
21:28 P tool um it's a I would say that it's a
21:32 little complex to learn but once you've
21:34 got it it's pretty easy to make your own
21:36 patterns that's you know it's a way of
21:39 doing it anyways so that can slow down
21:42 and the pattern tool is what you would
21:44 use to fill in the space then that's
21:46 essentially what you're doing you would
21:48 like spray that on essentially uh the
21:50 pattern tool is to literally build your
21:52 own um what's called a pat file um it's
21:57 a vector-based image it's going to be
21:59 Associated you know with the raster
22:01 based image so okay so you can draw your
22:03 own with that tool and we could probably
22:05 burn up half a show talking about that
22:07 um because I think that should be
22:08 something gra around yeah okay I've had
22:11 an issue with that one in the yeah in
22:13 the future that would be a good one to
22:14 talk about okay so some other things
22:17 that can slow um a scene down keep in
22:20 mind that that when Chief is rendering
22:22 it's rendering anything that is
22:24 displayed on okay so if you have a huge
22:27 house with items in every room it's
22:31 going to process every item it's going
22:34 to do its light bounces and traces on
22:37 every item even if it's not in your
22:39 active shot we've talked about possibly
22:42 either you know creating layer groups so
22:45 we can turn those off without having to
22:47 move things to individual layers or not
22:49 so that we're you know managing really
22:52 large files like that um at the end of
22:54 the day you might just have to put
22:56 things on custom layers or you might
22:57 have to have a file that is your
23:00 rendering only file if it's a huge
23:02 project so if you if you had that if
23:05 that was the case and you had if you put
23:07 all your fixtures or and furniture for
23:09 the living room on one layer and turned
23:12 them off when you're doing your camera
23:13 your kitchen camera yeah turn that layer
23:16 off when you're doing your kitchen
23:17 camera that would speed up your
23:18 processing yeah I'll give you an example
23:20 let me pull up a I'm G to pull up a
23:23 project if I could find it quickly yeah
23:25 I think I can
23:30 this is a very large file it's got a um
23:33 huge poly count by the way if you um
23:35 don't know where your poly count is when
23:37 you rebuild the scene you're going to
23:39 see um if if in your preferences you
23:42 have information displayed at the bottom
23:44 you're going to see here I've got
23:47 27,000 once the scene is rebuilt it will
23:49 show me that number otherwise it's going
23:51 to show me the active tool if I move
23:53 this around a little bit you can see
23:55 here just for a second it says 27,000
23:57 surfaces if your surface count is
24:00 getting above um let's call it 1.3
24:04 million and you have a 360 card you're
24:07 going to start seeing
24:09 slowdowns um if you if your surface
24:12 Count's getting up at 1.8 million and
24:15 you have a 4070 card you're going to
24:17 start seeing slowdowns if you've got a
24:20 4090 card or 7,800 AMD card and you get
24:24 up around 2.3 you're going to start
24:26 seeing slowdowns so
24:29 um just be aware of the surface count
24:31 and that's just the surface count of the
24:33 scene so if you need to limit that you
24:35 can go and try to Target items that have
24:37 a really high surface count something
24:40 that
24:41 clene we need to clarify the scene it's
24:43 not just what the camera seeing but it's
24:46 everything that's turned on in that all
24:48 the layers that are turned on in that in
24:50 that yeah that
24:51 camera so we know if I'm rebuilding the
24:55 scene and I'm just looking at I've got
24:56 someone's going to have to do some math
24:58 for me I've got
25:13 27,600 th000 surfaces okay you added
25:17 40,000 you added 40,000 Sur quickly
25:20 right just adding that sink in yeah yeah
25:22 so if I delete this cabinet now now I'm
25:24 back down to 25,000 which would let you
25:27 know just the blank cabinet which just a
25:28 couple thousand yeah it was only 3,000
25:31 yeah so it's okay so if you're curious
25:34 about the surface count of something you
25:36 could always place that item and open
25:40 that item up especially if it's an item
25:42 that inserts into something else you
25:43 could place it independently open this
25:46 item up and it's going to show you in
25:48 the 3D panel its surface count so there
25:50 you go it's
25:52 38,000 poly count now Chief
25:55 Architect um tries to keep their simp to
25:58 10,000
26:00 poly um giving you a point of reference
26:04 that's extremely low it's impressive
26:07 that they get away with making anything
26:09 look realistic at that low of a poly
26:11 count they will go up to around 100 at
26:15 times very infrequently um they I think
26:18 their in their internal cap that they
26:21 give towards manufacturers is right
26:23 around the 50,000 Mark so if you're
26:25 bringing an object from SketchUp 3D
26:27 Warehouse something like that and it's
26:29 400,000 poly yeah that's going to slow
26:32 your scene down considerably so um wow
26:36 if you are going to 3D Warehouse they do
26:38 have the ability to limit your searches
26:41 based on poly count and megabytes so you
26:44 might want to do that filter your
26:46 searches if you need to go Source
26:47 something from 3D Warehouse so let me
26:49 clarify this information is really more
26:53 applies to um physically base rendering
26:56 not just putting it in for vect image uh
26:59 no it would be any any shot if you're
27:01 seeing slowdowns these might be the
27:03 solutions for those slowdowns right got
27:05 it okay um I'm gonna continue on that
27:08 I'm gonna give you a little bit more
27:09 info on that so yeah John let me just
27:12 make make sure you're aware of some
27:14 questions here and then you can answer
27:15 them as you feel like you want to
27:18 Margaret's asking has a question about
27:21 um actually she had another question
27:24 about no that one we answered already
27:28 have a new set have a new camera set for
27:31 every
27:32 project as you add lights do you have to
27:34 go back in and check off the new
27:36 lights
27:37 [Music]
27:40 um yeah you would have to you'd have to
27:43 manage that that set a little bit um I
27:46 believe by default in whatever active
27:49 camera you have set and you add a new
27:51 light I think by default it turns it
27:53 on um if you're in the camera if you're
27:57 doing it from a plan View I don't
27:58 necessarily know that it turns it on you
27:59 have to try that out I'm not sure
28:01 actually um I will tell
28:05 you I'll say that most of my renderings
28:09 I try to have almost no lights turned on
28:13 I believe that the used backdrop only
28:16 for lighting with no lights turned on is
28:19 the best rendering I could produce well
28:21 and the reality is is the lights that
28:24 you put in the light fixtures and the
28:25 light source that you put on the
28:27 interior of the home is not ever going
28:28 to be real it's going it's never going
28:31 to be what it would be if you actually
28:33 know how to do a lighting plan because
28:35 you can't get the Lumen output you can't
28:37 get well you get the Lumen output but
28:39 you can't get the delivered candle power
28:41 you can't get you can't get certain
28:43 things so you're never going to get real
28:46 lighting for the interior of your house
28:48 so be aware of that yeah liting designer
28:50 is never going to love it
28:53 yeah um so for this particular project
28:57 because the account is so high I do I
29:00 did split this up in fact I I saved it
29:03 as a new plan file name and I called it
29:05 rendering only and so I actually have
29:08 this two layers here right in the front
29:10 of the stack and I put a space a
29:12 character space in front of the layer so
29:14 that it sorts to the front of the stack
29:17 and you can see here I could turn on and
29:19 off the front yard I could you know turn
29:21 on and off something in 3D so if I just
29:23 uncheck this because I want to do
29:25 interior rendering I'm picking things
29:27 that wouldn't be seen from the interior
29:30 side right and so that drastically
29:33 reduces the poly count so that I can
29:35 come in here and maybe do a new shot in
29:37 here and rebuild the
29:39 3D I think that's one of the biggest
29:41 things I've learned so far today is to
29:43 to turn those layers off of things that
29:45 aren't going to be in the camera view if
29:47 I'm having trouble yeah so that it's not
29:50 rendering them even though they're not
29:51 in the picture you know I never realized
29:54 that before so I'm on my 4090 machine
30:00 and we're streaming live which means the
30:03 encoder is is fighting the rendering
30:06 okay and you can see that I'm kind of
30:08 glitching out a little bit um so this is
30:11 just an example I also have a high
30:13 sample rate in this scene and now it
30:15 finally finished the sample rate and it
30:17 did a den noise at the end okay looks
30:20 good so 4090 card and we're at 2 million
30:23 surfaces so yeah some of the higher-end
30:26 cards can handle this stuff
30:28 um the 7800 I have can handle this scene
30:30 as well but if you're on a 3060 card or
30:33 especially if you're on you know one of
30:35 the um now the Mac SK rate trace this is
30:38 this scene on a Mac is going to take in
30:41 a couple hours to to resolve itself um
30:44 depending on which chip you have so just
30:46 keep that in mind it's going to be it's
30:49 going to be way more impactful to kind
30:51 of manage the scene if you're on a Mac
30:52 and trying to do the new R Trace
30:55 options wow so kind of slipping back to
30:58 one more thing that we could do if you
31:00 are on a lower-end machine and you would
31:03 um if you like me love to always be Ray
31:06 tracing even when I'm designing uh Chief
31:09 did give us something in the edit the
31:12 active view so I'm going to edit the
31:14 active View and they gave us AMD
31:16 Fidelity FX okay um I I don't have
31:20 background information on this so I
31:22 can't speak to it but what I do know is
31:23 that when you click this down through
31:25 quality balanced and performance um
31:28 especially if you're on a much slower
31:29 machine if you click on performance it's
31:31 going to make this scene look a little
31:33 bit muddy and it's also potentially
31:35 going to be a little bit
31:36 underexposed um so you see now the scene
31:39 looks very muddy around the casing and
31:42 everything like that but it is giving us
31:45 the lighting quality of the shot right
31:47 so if you want to design in Ray trace
31:49 and have it um resolve and D noise very
31:52 quickly you could set your sample rate
31:55 to something very low which would be
31:57 like 100 samples and turn on that AMD
32:01 Fidelity if you're on like an Mac M2
32:05 Chip and you want to you know get a
32:07 better idea of the scene you might even
32:09 turn down your opaque bounces and your
32:12 transmissive
32:14 bounces so now we're getting in like we
32:16 have save plan views we might have a
32:18 working plan save plan view we're doing
32:20 the same we could do the same thing with
32:22 cameras now we could have a working
32:23 camera we could have a finished camera
32:25 exactly so build a custom layer set
32:28 where you know things are turned on and
32:30 off the problem is that you're going to
32:32 be managing if you're putting objects
32:34 like on a room by room basis you're
32:36 going to be managing that um if you're
32:38 in Idaho this next month at Chief
32:42 headquarters at their training events I
32:45 would tell you please come with me let's
32:47 do a show of force because the thing
32:49 that I would like to suggest to them is
32:51 that we get layer groups layer groups
32:54 would be something where we can group
32:56 things into something that we could turn
32:58 off without needing to put objects on
33:01 separate layers meaning you wouldn't
33:03 have to change anything about the way
33:06 your template works right now you just
33:07 get to pick things to put into a group
33:09 the turn on its display or turn off so
33:12 are you talking about layer groups are
33:13 you talking about object groups well
33:15 object groups would be a good definition
33:18 maybe a better term because you can you
33:20 can already group layers and turn them
33:22 on and off together right so you want
33:24 object groups yeah kind of grouping of
33:27 those of you know yeah object groups is
33:29 a better definition yeah so that makes
33:31 sense if you wanted to this to be
33:33 performance-wise and also just the look
33:36 and feel of what it was before in X15
33:38 and prior you could set this opaque
33:40 bounces down to one you could set this
33:42 down to one as well and so um the only
33:46 thing about this is that that phenomenon
33:49 where you see light leaking sometimes at
33:51 the top of your
33:53 building um because we've limited the
33:55 number of Trace paths now the number
33:57 bounces we're tracing that light leaking
33:59 might show up so if you're if you've
34:01 ever seen that before that's essentially
34:04 what we're fixing by increasing the
34:06 number of bounces but if we set this
34:09 number to one and one we set AMD
34:11 Fidelity to two this scene and we set
34:14 our sample rate really low the scene's
34:15 going to resolve itself very very
34:18 quickly it's about as fast as you can
34:19 get your Mac to do it that's not bad
34:23 looking I mean a client would totally
34:24 understand what you're doing in that
34:26 space yeah it kind of looks like a
34:28 really nice water painting you know it's
34:31 not bad yeah it's not bad but this is a
34:33 great way to get to the point where
34:35 you're composing a shot and then maybe
34:38 you go leave it overnight to render out
34:40 with all the settings kicked back on
34:43 right um so Richard wondering where to
34:45 find that preference in preferences the
34:47 poly count setting oh the display of
34:50 this um if you don't have the display of
34:52 the of all this information at the
34:55 bottom of your screen I know it's in
34:57 preferences I don't know where but if
34:59 you never really edited your preferences
35:01 that should be there
35:04 um yeah I'm not sure where that
35:09 is John you want to see if you can find
35:11 that I I'll find it okay
35:14 um uh and then uh Christopher was
35:17 wondering where you can find Dynamic
35:20 backdrops um you can find HDR images
35:23 online there's um if you just search
35:25 free HDR uh h HDR or
35:29 hdri or aridan maps online you should be
35:33 able to find some repositories that have
35:35 free hdrs that you could download and
35:38 then install into Chief um I would
35:41 suggest that you download something that
35:43 is 8k resolution or less because at 16k
35:48 resolution Chief will slow down when
35:50 it's trying to load those back drops
35:54 up W Robin we made it 36 minutes and we
35:57 only got through one line item I know
35:59 it's amazing we're gonna be on this
36:01 forever I think that's okay we're
36:03 learning lots of good stuff we are I
36:05 think that's the best part about this is
36:07 we're definitely learning um a lot so
36:10 that's great okay HDR image export is
36:14 the next line um so when we go to file
36:19 export and then export a
36:24 picture I don't know that I see this
36:27 option maybe it's not in the export
36:29 picture dialogue but let me just see
36:31 what file types we have here yeah we
36:33 have a new file type here so if you
36:36 clicked on the drop down and dropped it
36:37 down to HDR it would export with that so
36:40 that's going to be it's going to
36:41 increase your you know your color map
36:43 your color numbers um I actually haven't
36:45 used that yet I should be using that on
36:46 my rendering
36:48 jobs that's GNA you know come up with a
36:50 much better quality image so maybe I'll
36:53 post an example of that when when we're
36:55 done
36:56 here wow
36:58 path traced renderings is the next line
37:01 yeah Robin oh no I just said you've done
37:03 two things now you said past renderings
37:06 what did you say what did you say we're
37:08 on
37:08 now um we are on path traced renderings
37:12 oh got it so Pat what was that that we
37:16 just flashed on the screen John uh just
37:18 that you include a bunch of stuff in
37:20 your Pro Plan oh I have um I have let's
37:24 see my user
37:26 catalog yeah I give you this kind of
37:29 setup here it's my favorite all around
37:32 um some that you know the Interiors I
37:36 tell you what your um um your backdrop
37:40 intensity numbers should be for these
37:42 right so I'm giving you an example of
37:44 maybe what you do there strong
37:45 directional Sun backdrops this is just
37:48 how I organize it um close in
37:51 environments something that's you know
37:53 really close to the window if you put it
37:55 outside um I've got scenes where if all
37:57 you're doing is doing you know an
37:59 example of a of a model that you're
38:01 creating I've got some in there and then
38:04 got some snow scenes and some Urban
38:05 scenes so include in my my
38:10 templates um path Trace renderings is is
38:13 what we just went over um I don't know
38:15 that I need to explain the whole of what
38:17 that is but when we're looking at a
38:19 scene um what Chief in very layman's
38:23 terms and by the way I am guessing I
38:25 don't know this for for certain the
38:28 developer could tell you more than I
38:29 could but essentially we're mapping
38:33 pixels so every pixel on your screen so
38:35 if you've got a 4K resolution monitor
38:39 that represents 4,000 pixels um
38:42 horizontally right so we're mapping
38:45 every pixel to some kind of quality of
38:48 of color of of what have you what we're
38:51 doing is we're um taking the distance
38:54 from the camera position to what that
38:57 pixel is supposed to be represented from
38:59 in this case we got a faucet right here
39:02 right and then we're looking at the mesh
39:04 of that faucet and we're saying okay
39:07 it's round it's you know it's going to
39:08 bounce a light off the front of it then
39:11 we're looking at the material that's
39:12 being applied to it is it a metal
39:14 material does it have roughness Etc and
39:16 it's going to create a quality based on
39:19 that and then we're also tracing now the
39:23 path of light now before we had a single
39:26 light bounc Trace meaning that we have a
39:29 light right here right there's a light
39:31 it's producing it's emitting light while
39:34 this light does actually bring light
39:37 towards this faucet right so what we
39:40 were doing was we were saying okay we're
39:41 going to trace the path of this light to
39:43 this faucet and based on what this
39:47 material is we're going to basically
39:49 guess at what this pixel should look
39:52 like okay so that's what we're doing
39:54 when we're um we're tracing the path of
39:57 light to this kind of um occluded
40:00 section up here where there's a lot of
40:01 Shadow all right and so when um when we
40:05 were getting light leaking what was
40:07 happening was we were getting light from
40:09 Windows we were getting light from
40:10 lights we were getting lights that were
40:12 bouncing off of other materials and then
40:14 Chiefs having to guess what that pixel
40:16 looks like sometimes it was guessing
40:19 that it's an overly lit pixel and that's
40:22 why it was creating light leaking so now
40:25 to improve the quality of this we we are
40:27 tracing the path of light several times
40:30 it's like we're fact checking or
40:32 something we're double-checking that
40:33 this is actually doing what we expect it
40:35 to do so and the program's doing that
40:38 for us we don't do anything about that
40:40 yeah and we have the ability to change
40:42 the settings here right um you could
40:44 increase this exponentially but you're
40:47 really only going to get an effect from
40:49 tracing the path of light up to three or
40:51 four bounces or something like that if
40:54 for some reason you're not getting glass
40:56 to resolve in a certain way maybe you
40:59 increase the number of bounces but three
41:01 or four is typically good enough to get
41:04 a a more accurate scene so this is
41:07 something more of when you're setting up
41:08 a piece of material then you're going to
41:10 be using that more often when you're
41:12 setting something up you're bringing in
41:13 a a material is that what you're you're
41:15 going You're probably never going to
41:17 touch that setting to be truthful unless
41:19 you have a problem that you're working
41:21 with right or like I said if you're on a
41:24 um like a Mac and you want to optimize
41:27 your workflow you want to set those
41:29 numbers low and then increase them when
41:30 you need them so that would be another
41:33 reason you might mess around with those
41:35 settings and then the sample rate is the
41:39 number of times from our camera position
41:41 that we are sampling the pixel meaning
41:43 we're we're knocking on it checking on
41:45 it hey have you updated did you change
41:47 from the last time that we sampled you
41:49 so the sample rate we're just we're
41:52 trying to figure out what exactly that
41:54 pixel should be comprised of right in
41:56 terms of like light bouncing material
41:58 Etc so if we increase our sample rate
42:02 that's going to continuously resample a
42:05 pixels so if I jump this up to 12,000
42:07 which is a really high number and and
42:09 that's extraordinarily high and we don't
42:11 need that number um and I move the
42:13 camera what you see here are what I call
42:15 fireflies and these fireflies are UND
42:18 sampled
42:19 pixels oh we haven't figured out what
42:22 this pixel is supposed to be we're
42:24 continuously sampling it right and if we
42:26 just let this go hopefully eventually it
42:30 will figure this out now Intel built a
42:34 system that is called a d noiser so this
42:37 is called noise essentially and the D
42:40 noiser works on your CPU not your
42:42 graphics card and the d noiser looks at
42:44 an undersample pixel it looks at the
42:46 pixels next to it and it guesses what
42:49 that pixel is supposed to be and it does
42:51 a really good job um so if you're
42:54 wondering what sample rate you should
42:56 you should set your scene what I would
42:59 suggest you do is come in here set your
43:01 sample rate really high get to the point
43:04 where the scene is maybe 5050 where it's
43:08 sampled pixels and under sampled pixels
43:11 and then take a look at the sample rate
43:13 as it's ringing up its number here at
43:15 the bottom and maybe set it based on
43:17 that got it so a number around 500 400
43:23 that's typically good enough but if you
43:25 are in a scene that that is
43:28 underlit substantially underlit you
43:30 might need to improve the sample rate or
43:33 if you have a scene that has a lot of
43:35 transparent materials um or has you know
43:38 trans translucent materials something
43:41 like that maybe you need to increase
43:42 your sample rate
43:46 perfect I think we may have time for one
43:48 more all right I have an answer for that
43:51 question
43:53 about finally finally it's the status
43:57 bar you you turn the status bar on and
43:59 off from The
44:03 View go to view oh it's not oh it's in
44:05 the it's in the view menu you just
44:07 toggle it on and off oh view wait is in
44:10 the view menu or
44:12 preferences it's in the Under The View
44:15 and then up right about the middle of
44:17 the sheet there oh there it is Aha and
44:21 then sa so also might what be might what
44:24 might be happening is the status bar
44:26 only shows up when you're doing
44:27 something that it pertains to yeah
44:31 right order to get the get the surfaces
44:35 have to move move your camera or rebuild
44:37 the scene in order for you to see those
44:38 numbers start or select something got it
44:41 that makes sense y okay all right what
44:45 do we got next emissive area lighting
44:47 this is a big
44:48 one oh this is the one that you allows
44:51 you to have lighting actually put get
44:54 light make I know what we're talking
44:56 about it
44:57 when you translucency I can speak
45:00 English and I can actually speak English
45:02 you were get I thought you were getting
45:04 there well it's putting light on a
45:05 Surface right actually light on a
45:07 Surface taking that thing so it has
45:09 light on it's giving off light that's
45:11 what I just said it's putting light on a
45:14 Surface that's why that's why I knew
45:16 what he said Robin because that's what
45:18 you said because I said it thank you I
45:20 appreciate that I'm gonna um just do
45:24 light picker here I'm gonna take this
45:26 excuse me um material eye dropper and I
45:30 just sampled the the the light here from
45:33 my recess light here and I'm going to
45:35 spray it on this solid now we know that
45:37 this solid is is a solid it's not an
45:40 object that's a classification of an
45:42 electrical symbol right but it is now
45:45 producing light that is being path
45:47 traced okay and because of that it
45:53 also can be turned off in 3D and it also
45:56 shows up in your list of
45:58 lights no kid very cool right so if you
46:01 wanted to adjust this material you could
46:03 of course adjust the quality of um the
46:05 light the intensity of the light from
46:07 using the rainbow baking tool the adjust
46:10 materials tool or you could come in here
46:12 into your adjust light section and
46:14 you're going to see here it's listed
46:16 look at that 3D solid and so if I expand
46:19 this carrot to a down Carro we're going
46:21 to see here's my intensity so I could
46:23 come in here and change the intensity
46:25 now this menu pops up this a new menu
46:28 for us so we create a copy of the
46:31 material we could edit the source
46:33 material across the entire plan you
46:36 select a different material and this is
46:38 saying apply missive and color from
46:40 lights so the the reason it's doing that
46:43 is
46:44 because I grabbed that light material
46:48 from an electrical item that is
46:50 specified as a light okay and so the
46:53 light itself the intensity from the
46:55 light is specif
46:57 the emissive quality of this material
47:00 because I used it to ey drop it over to
47:02 the solid but I could uncheck this and
47:05 set my own intensity level let me just
47:07 set this to a th and just to show what
47:10 this is even doing we'll kick it on the
47:11 red press
47:14 okay so I've adjusted wow but is it
47:18 already on an electrical layer or it's
47:20 still on a 3D solid layer you still have
47:22 change solid no still a 3D solid on a
47:25 solid layer so and notice that this will
47:28 be amazing once we get to oleds that are
47:31 that you can put into paint or anything
47:32 like that then you can illuminate your
47:34 whole wall that makes sense way in the
47:36 future but cool notice that I didn't
47:37 adjust this light when I adjusted the
47:39 materials and properties of this light
47:41 so they adjusted independently of each
47:43 other and all you did was just use your
47:46 material eye dropper essentially and
47:48 grab it from yeah that's all you did you
47:51 grabbed the light from the wallcon and
47:53 just placed it on 3D that 3D solid yeah
47:57 in fact I'll I'll do something that I
47:59 know you will do at some point is I'm
48:01 just going to throw a wall cabinet in
48:02 here and we'll just turn this wall
48:06 cabinet if I can see my own screen glass
48:10 do a glass front and then put yeah just
48:12 you can illuminate the sides or
48:13 something so this is probably my
48:16 preferred method for this I feel like
48:17 it's pretty quick I can take a solid I
48:20 can move my camera and I'm using a 3D
48:22 mouse so it's easy for me to move my
48:23 camera and I can start drawing down here
48:26 right mhm and so I'll draw a little
48:28 solid here oh God you're doing oh right
48:33 this is freaking brilliant and now
48:35 you're turning that into a light s
48:36 here's a really nice thing about us um
48:38 the solid I'm gonna bring this back face
48:42 off of the cabinet just a little bit and
48:44 then what I'm going to do is I'm going
48:46 to explode this entire shape actually
48:48 I'm going to bring the front face back a
48:51 little bit there we go I'm going to
48:52 explode this shape that's this guy right
48:55 here
48:56 I'll explode the 3D solid what happens
48:59 is the entire assembly is still selected
49:02 this exploded into individual
49:04 faces all these faces are still selected
49:08 if I hold control and just select this
49:10 front face now I've deselected that one
49:15 face I can delete all the rest that left
49:17 me with one face left over this is very
49:20 quick when you practice it and then it's
49:22 super simple for me to just take that ey
49:25 dropper grab this this come back over
49:28 here and populate right and so now when
49:32 we kick on the rate Trace there we go
49:35 and I need to adjust this and you can
49:38 turn that into a light source and then
49:40 you can put it on your cabinet schedule
49:41 now because that's where it's going to
49:43 go well it's a solid and solids report
49:45 to schedules and so you could report
49:48 that solid to a custom schedule any
49:50 schedule you'd like so yeah name it a
49:52 light and have it report to a schedule
49:54 as some kind of vertical rope lighting
49:58 that was so easy okay right there I'm
50:00 all I'm like with Margaret oh my
50:03 God oh my God that's fabulous yeah so
50:07 drop that around now I will say I
50:10 noticed something about this that was
50:12 funny the other day and and I'm going to
50:13 try it live right now and see if it does
50:15 the same thing um when I copy paste and
50:19 reflect about this cabinet which should
50:22 put it on the other side as well um I
50:25 noticed the other day that
50:27 it's not producing light in the correct
50:30 direction so it's projecting light back
50:33 towards me as opposed to back into the
50:35 cabinet because when it's shifting it's
50:37 not you only have one face and it's that
50:40 face is doing that it's going to the
50:42 back you have to rotate it and so we
50:46 don't we'd have to you still have a hold
50:48 of that after copied it Renee after you
50:50 copy it while you still have a hold of
50:52 it can you just flip it you can revolve
50:55 it
50:57 okay so you could revolve it 360 and
51:01 then it should be you'd have to move it
51:05 Etc so um oh excuse me that's not
51:08 revolve is not the correct way of doing
51:09 it um I'm not sure be flipped the
51:12 surface you just didn't flip it yeah but
51:15 do we have a flip surface I don't can
51:18 flip it in 3D too can
51:20 you uh we have maybe not with you could
51:23 could if it was still a solid you could
51:24 have done it but yeah I why are you just
51:27 doing it off of one surface yeah why are
51:30 you doing one surface why don't you just
51:32 keep it as a solid and just make it you
51:34 know what 38 of an inch thick because
51:36 that's all you need to because you're
51:38 going to see it more in the scene like a
51:40 single face is easier to manage to me
51:42 and I'm limiting the faces you could do
51:44 that you're right no reason not to I
51:46 guess well that's a heavily lit shot so
51:50 yeah and this is back to Chief doing
51:52 automatic exposure trying to figure out
51:54 what the scene's doing you can overall
51:56 override this with manual explosure and
51:58 maybe I would get that lighting to
52:01 exactly what I wanted something like
52:03 this who
52:04 knows just a that is really cool that
52:08 right there that's yeah that that was
52:10 great thank you
52:12 reenee I think that was brilliant all
52:15 right sweet so
52:18 that's we need a Kevin
52:21 box we need what since Kev since Kevin's
52:25 not here today we need to put a Kevin
52:26 bot in there yes he did I have I have a
52:30 Kevin bot Kevin bot's
52:33 awesome I don't know if I call him Kevin
52:35 though that's what's crazy I have a lot
52:37 of Kevin items that I never put Kevin in
52:38 the
52:39 name oh there he is he's so funny and
52:42 you could turn him into a light source
52:44 and that'll be great um yeah exactly you
52:47 can make the cube that he's holding
52:49 light up so we are not done with all
52:53 that's new in X6 in x16 yet we're still
52:56 not done with it we're still not done
52:58 with it yeah oh my goodness yeah so it'd
53:00 be really interesting to see how many of
53:02 the people who are here are going to go
53:05 to Idaho um at the end of August is
53:09 anybody
53:11 going um there's a few people here yeah
53:14 show of hands just say yes there's a few
53:16 people that are here from Portland Nikki
53:18 is here and who else Nikki is here from
53:20 Portland and who else there's one other
53:22 person from Portland here I think just
53:24 Nikki you're not are Nikki are you going
53:27 to Idaho to Chief I'm driving if you are
53:30 I'd be happy to oh Ethan are you going
53:33 of course you're going yay going
53:39 absolutely I think I have time to
53:41 show like part one of translucent
53:45 materials oh so I don't know who Rock
53:48 pill is um are you you're going
53:53 to are yo you're just from Vancouver
53:56 hello
53:57 um you are you going to
54:00 Idaho from Vancouver he's just he's from
54:03 Vancouver no no no
54:05 he's well when I first saw Vancouver
54:07 there are two Vancouver right there's
54:09 the BC and then there's Washington we
54:12 don't want to put Washington down so
54:14 because you know they already feel like
54:16 they're the ugly steps sister and that
54:18 you're not ugly we love Vancouver it's a
54:20 beautiful place I'm just teasing you're
54:22 digging holes over there I am really
54:24 digging holes I'm sorry so
54:28 sorry we were just talking last night
54:31 about the beautiful Waterfront in
54:33 Vancouver Washington which is really
54:34 lovely and this great pizza place my
54:38 kids are loving this pizza place on the
54:40 waterfront in Vancouver so that's not a
54:43 thing nice Jeff Jeff Rexford is there
54:47 he's Bay Area he's in my neck of the
54:49 woods
54:52 fabulous um just real quick so this is
54:58 this would be an example of translucent
55:01 materials I'm going to rotate that
55:02 center around real quick oh the shades
55:05 you were able to translucent make oh
55:07 jeez that's fabulous right how did you
55:09 do that so show what did you do so this
55:13 is just turning that material into a
55:16 class of material that is um a
55:18 translucent material so that's in the
55:20 properties panel okay properties panel
55:23 material classes translucent and made it
55:25 translucent and then you're and so my
55:28 settings on this um and we'll just hit
55:31 this briefly because we only got a few
55:32 minutes but um 40% translucency in this
55:36 I still wanted to really show kind of
55:38 almost like a not a linen but like a
55:40 knit texture um and so that's what's
55:44 happening here and um the thing that I
55:46 didn't do which I could have done if I
55:48 really wanted a realistic knit T texture
55:51 is put in an opacity map which is a map
55:54 that is indicating that part part of the
55:56 material is see-through is just
55:58 non-existent to really get that woven
56:01 look because it's not always going to be
56:02 that way but just for easy way of doing
56:05 it just hit the translucency so this is
56:08 partially translucent and then
56:10 transmission roughness has to do with
56:13 translucency and and the roughness is um
56:16 think of it as a dispersing a light
56:19 source across the material um so like uh
56:23 a roughness of zero would be a pinpoint
56:26 where the light is just going to shine
56:27 right through the material right versus
56:30 roughness of 70 is that pinpoint is it's
56:33 almost like you're um you're throwing a
56:36 water balloon against the wall and it's
56:38 spreading right um so sweet it's kind of
56:42 dispersing that effect through through
56:46 um through the material so if I set this
56:48 to zero now you're going to see that
56:50 that um
56:52 sunlight really is um
56:56 targeted in a way it's just it's coming
56:59 through evenly so we're not seeing the
57:01 effect of that sun um hitting it and and
57:04 being absorbed by the
57:06 material so if I set this transmission
57:09 roughness to
57:11 100% now you're going to see that the
57:13 sunlight's really affecting the material
57:18 wow wow okay um I think another show
57:24 we're going to have to get into
57:26 mixed medium materials which get into
57:30 some really advanced stuff also um I'm
57:33 glad all you guys are live here because
57:35 I unfortunately sorry to everyone that's
57:37 here I am going to probably Lobby for
57:40 this to be taken down this is stuff I
57:42 train on and I usually have people pay
57:44 for this kind of thing so I think we
57:47 were we we are discussing potentially
57:49 taking off some of our Advanced courses
57:51 where this is this is really something
57:53 that you know is valuable information
57:55 that I'm sharing and I'm making all
57:56 competitors to me yes so well no and
58:00 it's actually fair to do that so what
58:02 Rene is really saying is that eventually
58:04 you won't be able to go back to you know
58:06 these these shows will be live for like
58:09 one or two weeks and then to get any
58:11 Back info you'll have to join like a
58:13 patreon group or join a group where you
58:16 pay um a regular amount it won't be a
58:19 huge amount but you make you have to pay
58:21 something to be able to watch the back
58:23 shows and I think that's totally fair
58:26 because we are considering it don't know
58:28 how it gives us it gives us an
58:31 opportunity to give more detailed stuff
58:34 go into it in more detail like we got up
58:36 we did one one and a half things today
58:39 yeah other shows we would have done 10
58:40 or 12 things in the in the time so um it
58:45 just makes it a way so that we can share
58:46 more material
58:48 too yeah we got more questions anything
58:51 else we got we're at 10:59 we're right
58:53 on time it's amazing we are ready to go
58:57 you guys this was great Renee Renee
59:00 thank you you are always I always
59:03 learned something from you and I really
59:05 appreciate your time and what you put
59:08 into this so fabulous thank you and I
59:11 always love seeing every I mean I always
59:12 love it I learned so much from you guys
59:15 it's here you know I always I feel like
59:18 this is such a huge value so um I really
59:21 appreciate getting the opportunity to be
59:23 part of this group so thank you very
59:25 much I hope you guys who are watching um
59:28 enjoy this as well and um have a lovely
59:31 I'm gonna show you one more thing before
59:32 you before have a Lov day okay I think I
59:36 repaired these let me see if they
59:38 actually are repaired or not are you
59:40 gonna ruin our day now Renee are you
59:41 gonna ruin day let's see oh I have a I
59:46 have what are those is that all um John
59:50 um py vanwinkle bottles that's my
59:53 nonfixed this is would be the X15
59:55 version of them uhhuh and let me see if
59:59 I have the newer versions of
1:00:02 them yeah these are the x16 versions of
1:00:06 them
1:00:08 wow so this is a mixed material class
1:00:12 where we
1:00:13 have um we have a metal map here we have
1:00:18 a glass map here we have a translucent
1:00:22 map and we have um a clear coat as well
1:00:28 and and this is all from one material
1:00:31 this whole thing is one material so wow
1:00:34 this is getting into mixed material
1:00:35 class which is very complicated um to
1:00:39 understand if you don't dive in like
1:00:42 this and be a big nerd like I am so you
1:00:43 can see here that the properties panel
1:00:46 looks pretty complex probably more
1:00:48 complex than you've seen before right so
1:00:51 we got a lot going on in here um anyways
1:00:54 maybe we'll get into this next time
1:00:57 there you go that's amazing anyway you
1:00:59 guys have a great weekend have a good
1:01:01 week we'll see you in a few weeks and um
1:01:03 take
1:01:05 care I like
1:01:08 this that one's
1:01:09 funny yeah that it's definitely funny
1:01:12 anyway thank you God that was great
