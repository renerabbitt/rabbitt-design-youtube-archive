---
videoId: 8RmWC8IGl9U
title: Advanced Symbol Editing Session in Chief Architect X16
url: "https://www.youtube.com/watch?v=8RmWC8IGl9U"
status: imported
---

# Transcript

0:01 uh well I think it was bound to happen
0:03 that VIP you got something a little bit
0:05 Advanced that's what this is going to be
0:08 um I'm trying to render something um to
0:11 just have in my portfolio that I know
0:13 will look amazing and and uh and I
0:17 thought it was going to take very little
0:19 effort to render and then I realized
0:21 Chief Architect has some glitches that
0:23 are happening an x16 well basically it's
0:26 not a glitch it's that theyve changed
0:27 the rendering engine so it doesn't work
0:29 the same way and so my shelf tools are
0:33 not working correctly and some of the
0:36 are not rendering out correctly either
0:38 all right so I'm going to show you how
0:40 I'm fixing these I'm also going to show
0:41 you how these even work um which is
0:44 pretty Advanced this is a very Advanced
0:46 system now I've done something to repair
0:49 this system recently or maybe not
0:53 necessarily repair but um accommodate a
0:57 change that came in x16 x16 allowed us
1:00 to change the thickness of a cabinet
1:03 door from its fixed 3/4 of an inch up to
1:08 4 in actually in
1:12 actuality um it can even be larger than
1:14 that but you can't set it larger than
1:17 that you can make a cabinet door larger
1:19 than that by creating a geometry that's
1:22 greater than 4
1:24 in and then converting it to a cabinet
1:27 door and applying it and Chief will
1:30 accept a larger cabinet door which opens
1:33 up some
1:34 possibilities but what that did to my
1:38 shelf tools was that I had not set those
1:41 tools to be a specific depth which is
1:43 3/4 of an inch I set them to be whatever
1:46 the geometry was so what happened in x16
1:49 is suddenly those tools were no longer
1:52 dynamic they would not resize with the
1:55 cabinet itself so if you resize the
1:57 cabinet in previous versions it would
2:00 actually resize the geometry of the
2:02 Shelf no longer so what I had to do was
2:05 I had to go back in and in the advanced
2:08 sizing panel I had to uncheck update
2:11 when object Dimensions change okay and I
2:15 had to and what that does is
2:17 automatically check update when object
2:19 dimensions changeed for bounding box
2:22 spacing and then set my depth to 3/4 of
2:25 an inch and we see on the right hand
2:26 side there we go right so and just to
2:30 show you this full process let's just um
2:34 I'm going to set this front spacing back
2:37 to 0 in and show you what it was before
2:40 this is what it was before so Chief was
2:42 seeing this as its full depth so that
2:45 when you tried to modify it the the
2:47 Shelf itself it wasn't really doing
2:49 anything so I needed to uncheck update
2:52 when object Dimensions changed set this
2:54 to 3/4 of an inch and what you'll see
2:57 when I hit tab or enter is this front
3:00 will automatically put that set back
3:04 right and we can see the bounding box
3:06 has changed what this makes the software
3:09 capable of doing now makes it a little
3:12 bit more dynamic in a way is that when I
3:14 then apply this to say this shelf if I
3:18 come in here and
3:20 edit what I have to do and this is
3:22 different than what we previously did I
3:24 will click on this Thor left and I need
3:27 to get into Appliance Thor drawer
3:30 specify which brings up this dialogue
3:32 where we see the thickness is 3/4 of an
3:35 inch well if I set this to something
3:37 like 2 in watch what happens to the
3:40 geometry we actually get some resizing
3:43 capabilities that we wouldn't have
3:44 otherwise had right which is makes them
3:48 a little bit more dynamic in a way so
3:50 set this back down to that 3/4 of an
3:52 inch or whatever it was set to and the
3:56 next part of this is I want to fix the
3:57 rendering issue and the rendering issue
3:59 we talking about here is is this little
4:01 bit right here so what's happening is
4:04 Chief also changed the way that they
4:06 smooth symbols and so we're seeing some
4:09 Vector smoothing we're seeing some cold
4:12 surfaces we're seeing some flipped
4:14 normals you don't know what any of that
4:17 is not necessarily information you need
4:19 to know it's just that it's causing an
4:21 issue with my rendering right so here we
4:24 go I've got this symbol and so what I'm
4:26 going to do is I'm going to use the
4:27 delete surface tool to kind of clean
4:29 this up a bit and get this back to
4:31 something that looks better what I think
4:34 is happening is I'm getting some Z
4:36 fighting between the Surface here that's
4:39 on the inside of this right where it's
4:43 fighting let's just call this salt it's
4:46 fighting that salt and the glass it's
4:48 holding the same Z coordinate so it's
4:51 doing some Z fighting and I'll show you
4:54 if I change this glass material I'm
4:56 going to switch to component base so I'm
4:58 not changing all the glass in the entire
5:00 scene and that's going to make it make a
5:02 duplication of this glass oh actually
5:03 it's not so the glass here in this
5:06 case is actually not glass we want to
5:10 Define this as glass that's very
5:12 interesting actually just showing as
5:15 just basically a blank PNG texture if
5:18 you will or I'm not really sure how it's
5:20 coming up with this at all it's just a
5:23 transparent texture interesting so I'm
5:26 going to
5:27 instead designate this as a trans
5:29 transparent texture and we'll see crown
5:32 glass at 1.52 that's the standard crown
5:35 glass let's see what happens does this
5:37 change anything well not really but we
5:40 can see that we've got a lot of surfaces
5:42 going on in this particular mesh right
5:45 so next thing is I want to open this up
5:47 and in the 3D panel I want to see if if
5:51 I invert the surface direction does that
5:54 affect
5:55 anything
5:57 and it's not really doing anything in
6:00 terms of affecting that geometry and
6:01 then the other thing that you can always
6:04 um give a shot at and let's just see
6:06 what this means cold layered transparent
6:09 surfaces I'm going to bring up that help
6:11 menu I'm going to launch help I'll put
6:13 this on my side window and I'll show you
6:16 Chief's um explanation of cold layered
6:19 transparent surfaces so this is in the
6:22 section five when we look at the help
6:25 menu and this is um indicating faces the
6:29 faces section right so cold layered
6:32 transparent surfaces if you need to
6:35 troubleshoot the appearance of a
6:36 transparent symbol generally this box
6:39 should be left unchecked so it doesn't
6:42 actually tell you really what's
6:44 happening here but I will tell you that
6:46 this does have some positive effects
6:48 when you're dealing with a transparent
6:49 surface at times so I'm going to leave
6:52 that unchecked press okay and here's the
6:54 next part I'm going to get into the
6:55 delete surface tool but before I even do
6:58 that I'll show you one more trick we've
7:00 got some new classification in materials
7:03 for transparency and that is thin if we
7:06 choose thin what happens is uh Chief by
7:10 default will apply a material to both um
7:14 our positive UV Direction and our
7:17 normals Direction the back side of a
7:21 face okay so Chief by default applies
7:24 material to a back
7:26 face which is different from say like a
7:28 SketchUp okay if we click thin it will
7:32 no longer apply to a back face now it's
7:35 only applying to one side face okay
7:38 something else we're going to notice is
7:40 the reason that this is so dark right
7:41 now is it's taking on the material color
7:45 so I'm going to set this back to a true
7:48 white so I've set this to a true
7:53 white material class
7:57 transparent and we can see
8:00 well this does look like glass but we
8:03 still have that Z fighting issue so now
8:05 we're on to the next part and keep in
8:09 mind when I turned off or rather when I
8:12 checked thin and no longer really have a
8:15 glass look at the base of this symbol
8:18 and so I do want to retain that so
8:20 that's something I'm probably going to
8:22 revert back okay so here's the next part
8:25 I'm gonna kind of slip in here all right
8:28 I'm G to slip in and I'm going to use
8:30 the delete surface tool and I'm going to
8:32 delete the inner wall here and I think
8:35 that's what's going to help me stop that
8:38 Z fighting so when I delete the inner
8:40 wall and it should update look at that
8:43 bam this looks a lot better already
8:45 right so let me just get inside delete
8:48 that in wall kind of the same thing
8:50 coming in here now if you're having
8:52 problem deleting the entire wall as a
8:54 whole what you would need to do is
8:56 change the symbol smoothing and you
8:58 would increase increase the symbol
9:00 smoothing or decrease the symbol
9:02 smoothing so that we would be joining
9:04 faces
9:05 or in a way detaching faces from from
9:09 being joined so that we can get an
9:11 accurate delete surface from the delete
9:13 surface tool now look at this this looks
9:16 fantastic so what's my next step I need
9:19 to make sure I'm not doing anything to
9:22 this scene to rebuild the 3D and so that
9:26 before the 3D rebuilds which would then
9:29 return those surfaces I just
9:31 deleted we can reconvert this to a new
9:34 symbol so here we go I'm going to
9:36 reconvert this to a new symbol convert
9:38 selected to symbol and we can retain
9:41 that it's a cabinet door or not totally
9:44 up to you I'm just going to say I'm not
9:47 even going to add it to well I will add
9:49 it to the library and I'm just going to
9:51 leave this as the name fixture doesn't
9:53 matter because I'm going to show you
9:54 what I'm going to do next so let me just
9:57 press okay actually yeah I'll press
10:02 okay and we can just drop this in here
10:05 to take a look see what this is looking
10:07 like there we go right so that's the
10:10 fixed geometry now here's the next part
10:12 it would be simple to just add this to
10:14 the library rename it you know add some
10:16 search attributes add some tags Etc and
10:19 then you're just done right but here's
10:22 my problem with that I already have so
10:25 many settings done to this particular
10:28 symbol in my library that it would be
10:30 really really cumbersome for me to go
10:33 through all that work so here's the
10:35 solve for that I've got this in my
10:38 library now I'm going to move over to a
10:40 different plan and in this different
10:43 plan I've placed a point and we can do
10:46 that by getting into our CAD menu um
10:49 here's our CAD menu see for points bam
10:53 input point so I input a point at 0
10:56 location okay absolute location 0 0
11:00 press okay then I placed my geometry so
11:03 here's my new geometry right that's my
11:06 new symbol I'm going to do a point too
11:08 on the center of this to the center of
11:10 the scene and then I'm going to look in
11:13 my camera here and so what I'm doing
11:16 here is I'm exporting the mesh here okay
11:20 I'm exporting the geometry so I'm going
11:22 to get into the file menu export and
11:26 then 3D model 3DS
11:30 and we can truncate that doesn't matter
11:32 and I'm going to just save this as
11:33 replacement in a place that I know all
11:36 right now here's the next step I need to
11:40 find this in my catalog which is in this
11:43 section here let me just find that
11:45 project
11:47 item I can let's see it's not in
11:52 that which one was this this
12:01 a tricky one to find it might
12:06 be that's it right there all right
12:09 cooking jars so I get to open this
12:12 object up all right that's going to
12:14 bring up this menu now here's what I
12:16 need to note when we replace geometry
12:20 that's my next step I'm going to take
12:22 the geometry I just exported and replace
12:25 this embedded geometry with that
12:27 exported geometry when I do that it will
12:31 reset one thing the origin offset it
12:34 will also reset Advanced sizing and
12:36 stretch planes but it should retain
12:38 everything else here so I need to make
12:42 sure that I've got a screen clipping of
12:44 this or I'm remembering this so in this
12:46 case I've got 6 in and8 in now let me
12:50 replace geometry I find that 3DS right
12:56 it's going to ask me if we want to
12:57 rename the Importer texture or in this
13:00 case I just want to use the existing
13:02 texture instead of the imported texture
13:04 and do this for all remaining conflicts
13:06 let me press okay there we go so that's
13:09 where I need to make sure that I've got
13:11 that same dimension in here which was
13:13 six
13:15 and 1 18 I believe there we go if we
13:18 look at Advanced sizing and we can see
13:20 it the bounding box retained its size we
13:23 can see in advanced sizing everything is
13:26 still the same the other thing That
13:28 Remains the Same is any tags any search
13:30 attributes I had Etc now I know you
13:34 might not ever need to watch this video
13:36 but it's useful information maybe you do
13:39 who knows there's a number of different
13:41 use cases for this I can think of one
13:43 right off the bat matterport scan maybe
13:46 for some reason you need to replace the
13:47 geometry because you need to change the
13:49 scaling that it imported has because I
13:51 do have the opportunity now since I
13:53 replaced the geometry to change the
13:56 scale that it imported as in this case I
13:59 don't want to touch that I'm going to
14:00 leave the smoothing angle alone and
14:03 let's just press okay now this is in the
14:06 software it's in the library exactly
14:08 where it was before it retained its
14:10 search attributes it retained its tags
14:13 let me go back to my main scene and see
14:15 what I can do so I'm going to take that
14:17 same item find it in my library actually
14:21 it's in right now and you can see it's
14:23 still the same classification so when I
14:25 hover over and
14:27 replace there we go it should just
14:29 replace in like kind so now I want to
14:32 just examine this and see if I want to
14:34 make any changes to the materials now we
14:36 can see here it didn't retain any kind
14:39 of edits that we did in the scene in
14:41 terms of its materials right so it's
14:43 bringing in that just clear material
14:45 that doesn't make any sense but the
14:47 other thing that I think it did that's
14:49 kind of beneficial and this is a quirky
14:51 little thing happening within Chief
14:53 Architect is that this particular model
14:56 came from a SketchUp model when you UV
14:59 map something in SketchUp by default and
15:03 then import from SketchUp it sets all
15:07 textures to 1 in by 1 inch okay and
15:12 that's a really funny scale it doesn't
15:15 leave you with a lot of Dynamics in
15:18 terms of re uh scaling that texture it
15:21 limits you in a way when you replace the
15:24 geometry it re UV maps and so you can
15:28 see here that the scale of the UV
15:31 mapping has shrunk considerably so this
15:34 is a little bit of extra work now for me
15:36 to go through and fix it but it's work
15:38 that I don't necessarily mind doing
15:40 because I think it's an improvement so
15:43 let me go find this back in my library
15:45 again we're going to open this up and we
15:46 have to go through this and kind of
15:47 painstakingly do something with this
15:50 so let's just see if I
15:53 can it would be helpful if I just knew
15:55 the name of it cooking jars there we
15:57 goes open this object I'm off on the
16:01 sidebar you can't see that in the
16:02 recording window but now you should be
16:04 able to see this and so here's where I
16:06 get into the materials panel here's
16:09 another kind of nice thing about this I
16:12 get to clue um choose these and you see
16:15 these naming conventions being used here
16:17 they're not really all that helpful tell
16:19 you the truth right they're not really
16:21 indicating what these things are so in
16:23 this case I get to kind of come in here
16:25 and fix some things so I'm going to
16:27 single click on this and we're going to
16:29 say that this is wood texture that makes
16:32 a lot more sense right and now I can
16:35 doubleclick this edit the source
16:38 material I get to rename this maybe it's
16:41 just Wood Oak something like that and
16:46 the texture size is probably more
16:48 appropriately going to be 20 by 20 which
16:50 is what Chief um standard texture is
16:53 when you create a new texture in your
16:55 library as 20 X20 I also have the
16:58 opportunity to maybe improve some of
16:59 these things so this one in particular
17:01 maybe we could put something in the
17:02 roughness map maybe put something in the
17:04 bump map ambient occlusion map um this
17:07 one I'm going to skip that for but I'll
17:08 show you where this is really beneficial
17:10 and we're going to make a better texture
17:12 out of this all right so there we go
17:14 Wood Oak I press okay look at that nice
17:18 organized we're making some improvements
17:20 I'm okay with that this takes time yes
17:22 but I'm okay with it if you're ever
17:25 curious about my systems and what it
17:27 takes to build my system
17:29 and why I openly and freely share
17:32 information on how to build these
17:34 systems is you can see right here they
17:36 take so much time to rebuild and because
17:40 I sell them at volumes you get the
17:42 benefit of getting something that you
17:45 couldn't rebuild yourself for the amount
17:47 of money it takes to just purchase the
17:50 item but this is all great info you
17:52 could build your own systems if you
17:54 wanted to all right so here's the next
17:56 one looks like it might be salt so I'm
17:58 just going to call
17:59 salt granular whatever we call it and
18:02 let's open this guy
18:10 up and so this one would be really
18:13 simple to just copy this texture paste
18:16 it into ambient occlusion it's going to
18:18 make some fake Shadows if you will let
18:21 me set that scale up to 20 in and you
18:25 see here if I close out this ambient
18:27 occlusion what it does it kind of it
18:29 takes away some of that detail you can
18:31 see um when the ambient light is uded if
18:35 we paste this in it's going to create a
18:37 little bit more you know fake shadowing
18:39 it adds a little bit of texture we could
18:41 also jump this into the bump map and and
18:44 have a little bit of texture there as
18:46 well now if I wanted to I could put a
18:50 texture in the bump map that had a lot
18:53 of detail and I'll show you what I mean
18:55 um and I just have some generic textures
18:57 for this kind of thing especially in my
18:59 like my brushed section of my Metals so
19:02 or not brush excuse me metal flake
19:04 section we'll show you just how crazy
19:06 this can look if you put some you know
19:08 high volume texture in
19:10 here now we're getting because the scale
19:14 of this is very different in terms of
19:17 pixel to pixel and its detail to the
19:20 scale of that bump map we're getting a
19:22 bunch of small little bumps right and
19:25 maybe that's beneficial I will say that
19:28 makes makes this texture a little more
19:30 heavy and you might not ever notice this
19:34 detail so I'm not sure that I would do
19:36 that maybe a solve or maybe you know
19:39 work around for this is just choose a
19:41 texture that's super low resolution in
19:44 fact maybe we will just make a texture
19:46 for that purpose so let me go in and I'm
19:49 going to fire up Photoshop that's going
19:51 to be on a second screen maybe we can
19:52 switch to that in a second um in the
19:54 meantime I'm just going to close this
19:56 out and press okay
20:01 there's our salt texture cool and
20:04 something that's helpful when we're
20:05 seeing this preview on the rightand side
20:07 is just change this drop down menu to
20:09 standard rendering menu and we're going
20:10 to start seeing there we go that's sized
20:12 up to that 20 we can see that that top
20:15 Oak cap is that Oak um that cap you know
20:18 is sized appropriately now uh the salt
20:21 is not funny that they even have salt in
20:24 the uh in the texture itself but let's
20:26 click on this next one it looks like it
20:27 might be grain so we'll just call it
20:36 that there go grain I do want to just
20:40 take this texture drop it into the bump
20:42 map but before we do I want to I like
20:44 showing you what this looks like when we
20:46 drop it into the bump map
20:49 so we go we're going to take this
20:51 texture drop it into
20:53 the
20:55 [Music]
20:56 and and it should be a very subtle
20:59 effect in this case um if we kick this
21:01 up to something like two it's going to
21:03 be a little heavy I
21:10 think very hard to see with that preview
21:13 I need to switch and get my rabbit logo
21:15 back in here because that's one of the
21:17 better ones for really examining texture
21:20 it's not only a good plug but it really
21:23 helps me see when they bump Maps being
21:25 effective or not and it's probably
21:27 because this grain is um so similar in
21:30 in um in its color value um that we're
21:34 not seeing a huge effect from that bump
21:36 map we invert it eh not a huge effect
21:39 let's go ahead and paste this in the
21:40 ambient inclusion map and look at what
21:42 that does that really brings out like an
21:44 shadowing effect if you will so it
21:46 almost take away that bump map that's
21:48 going to make this more lightweight and
21:50 we set it to 20 by 20 there we go press
21:53 okay see in the
21:55 preview yeah that's sized appropriately
21:58 very
22:02 cool so we just have a few more textures
22:05 we've got the salt one sugar oh look at
22:07 that salt and sugar how funny I think
22:09 these just should be white textures but
22:11 let's go ahead and see if we size this
22:13 up what
22:21 happens the
22:26 N all salt label I know
22:29 not look at that isn't that funny
22:31 because it re UV mapped it didn't
22:33 necessarily map in a way that is
22:36 helpful so I might have to bump that up
22:39 or top or bottom or whatever or maybe we
22:41 will just replace it so that could be
22:43 something that we do as well so let's
22:45 see salt
22:48 body we're going to call that salt body
22:50 we're going to select the material and
22:51 we'll just pick it from our plan
22:53 materials um or you can even do it from
22:55 Material defaults so it might be
22:58 something like
22:59 like
23:02 um wall stre let's
23:05 go the cabinet material no I don't think
23:09 so this will def default to something
23:13 that potentially gets changed by
23:15 accident so maybe not see if we've got
23:18 just white in
23:19 here white cabinets white let's go
23:24 white and we'll make a
23:27 cup let's go gloss
23:31 white loss white roughness is 0% great
23:39 perfect um don't know what this is but
23:42 let's go black
23:48 trim I'm going to go ahead and pause and
23:50 work through this we'll get back in just
23:52 a
23:54 second okay here's the big reveal
23:59 see what this looks like look at that so
24:01 we've got standard glasses back on this
24:04 so we get that thickness in the base
24:06 here what you're seeing by the way in
24:08 that base is actually um the individual
24:11 faces right so um even though Chief has
24:15 an excellent excellent smoothing
24:18 algorithm um that doesn't mean that it
24:20 can just fake um smooth surface with
24:25 transparency right so you're going to
24:28 have some issues like this where it's
24:29 just kind of doing some funny little
24:30 wonky things now you could do a couple
24:32 things to try to like mitigate these
24:34 issues which is maybe we open this up
24:37 and change some of the smoothing angle
24:39 sometimes that can have an effect so if
24:41 we set this back down to like zero you
24:43 see what happens over here right this is
24:46 showing us our true vectors we did that
24:49 you're really going to see um an
24:52 improvement in the glass but it's going
24:55 to be faceted in a way right
24:58 see that it's faceted so but from this
25:02 distance that's a great Improvement okay
25:05 let's see if we can kind of pump that up
25:06 and catch a middle ground let's just set
25:08 this to really
25:11 3° or we want to just get past just a
25:15 little bit of that vectoring there so
25:16 maybe go up to
25:18 12° and then drop down from there
25:22 8° I think 8 degrees looks about right
25:29 see what that looks like yeah that's
25:30 looking really sharp really good looking
25:34 I like it I think that's it I think
25:36 that's done I just need to make sure
25:38 that I'm conforming that in my actual
25:39 Library item so and to open that object
25:42 up from the library there we go we know
25:44 the magic number is eight
25:49 bam and now that I've done all that work
25:52 here comes the big payoff I'm going to
25:53 replace just this section right here guy
25:57 and I'm going to have to do a little bit
25:59 of work to get it to fit on the shelves
26:01 because this is a super narrow shelf but
26:04 we know that I can edit that
26:08 now so here's just to show this one more
26:11 time here's the edit of that I'm going
26:12 to pick this guy right there I'm going
26:14 to come in specify Appliance door drawer
26:17 I'm going to shave an eighth of an inch
26:20 off of this and that should have it fit
26:23 perfectly on the
26:26 shelf and it's looking really really
26:29 really good really good
26:33 cool now we wanted to go full circle on
26:38 this forgot one thing here we're going
26:41 to come into Photoshop open up that
26:44 [Music]
26:47 file get into my materials get into my
26:52 metals and I actually I'm going to end
26:55 up sorting this in a different way so
26:57 here's that metal flake and we're going
26:59 to take a couple of
27:01 these maybe we'll just take
27:08 right and automatically this brings up
27:11 um camera Raw on upon input but we're
27:15 just going to say open and then we're
27:17 just going to export this again and this
27:19 time we will reduce it
27:22 considerably so um if you're new to
27:24 photoshop Control Alt shift w
27:29 gets us our export as menu and this is
27:32 where we have the opportunity to shrink
27:34 this way way down and in fact I mean it
27:37 needs to be such low resolution I would
27:39 even say something
27:41 like
27:43 um see how close this let's go
27:48 10% yeah something like that perfect
27:51 this is a real low resolution image now
27:54 and so and I do not want to have
27:55 transparency check this causes some
27:57 problems in Chief Architect and we will
28:00 leave it as PNG because that's a
28:02 lossless format you're going to get a
28:04 lot more crisp details because Chief
28:06 Architect really really really
28:09 compresses and puts in artifacts when
28:12 you dump a jpeg into the bump map it's
28:16 something you should know um okay so I
28:19 want to get into my materials and I have
28:21 a section here that's Global bump normal
28:23 procedurals okay and I'm going to make a
28:25 new folder if you're on PC control shift
28:28 n is make a new folder and I'm just
28:30 going to call this low res pein
28:35 Noise Okay that's an industry term pein
28:38 noise so it's just a pearlin noise map
28:40 and we're just going to call this pein
28:42 one why not and that's just a very good
28:46 generic bump map for making a bunch of
28:49 little you know height right so let me
28:52 open up my library object one more time
28:54 we're going to make the source edit here
28:56 get into materials get into that salt
28:59 how easy this is to find now it's all
29:01 nice and organized come into the edit
29:04 menu texture panel get into that bump
29:07 map we're going to go find that pearing
29:09 noise
29:14 right as bam and look at that that looks
29:19 great
29:22 perfect boom boom
29:25 boom okay
29:29 replace in kind going to have to edit
29:32 the depth again see if we even notice
29:34 that
29:35 bumpiness you know a little bit you can
29:38 see it it's
29:41 there once this Den noises and just a
29:44 second bam yeah there's a little texture
29:47 there these look
29:50 great if you watch this far I'm really
29:52 glad you stuck with me this is cool
29:54 information not necessarily something
29:56 you need to know for your every every
29:58 day drafting sessions but it is you know
30:01 it can be very useful information you
30:03 can see here I put an eighth of an inch
30:06 on the Z Delta for this item and it
30:10 should have been a negative e of an inch
30:13 notice they are floating so case you
30:15 didn't know that you can always edit the
30:18 geometry according to the bounding box
30:21 so I'm going to actually say this is
30:24 yeah8 of an inch which is going to move
30:27 that quarter inch
30:30 overall cool people that have bought the
30:33 Shelf tools or the full Library keep a
30:36 lookout you're going to get an update
30:37 one of these days soon if I ever get
30:40 through all of this work
30:47 [Music]
