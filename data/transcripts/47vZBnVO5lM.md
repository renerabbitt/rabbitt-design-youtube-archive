---
videoId: 47vZBnVO5lM
title: Optimizing 3rd Party Furniture From CGTrader and 3d Warehouse For Chief Architect X16
url: "https://www.youtube.com/watch?v=47vZBnVO5lM"
status: imported
---

# Transcript

0:01 if you are a designer interior or
0:05 interior architectural design designer
0:07 doing spec design spec finishes in Chief
0:10 Architect this is the video you've
0:13 really really been dying for me to make
0:16 I've put this off for a while because um
0:19 why did I put this off well because I'm
0:20 utilizing tools that I am not a
0:22 professional in um I know how to use
0:25 them just enough to do what I want to do
0:27 but I don't feel so proficient in them
0:30 that I feel like I should be advising
0:31 but then I come to realize you know what
0:33 it's a stepping stone I maybe have more
0:36 information than you do and maybe this
0:38 information can help you out and in
0:41 doing so maybe I will be educating
0:43 myself as well so uh I'm going to point
0:45 you to a couple of things a couple of
0:48 websites right off the bat um I want you
0:50 to please download blender because
0:52 that's what we're going to be using it's
0:53 a free software um it's an industry
0:56 standard for many different video game
0:58 developers and it's a really awesome
1:01 tool and it's uh and it's open source so
1:03 people build stuff for it all the time
1:07 and so what we're going to be doing is
1:08 we're going to be getting some kind of
1:11 model off of the net that isn't
1:13 optimized for Chief Architect and then
1:16 we need to optimize it and this could be
1:18 a couple things that you've run into
1:19 before one maybe the poly count of the
1:22 object you're getting or purchasing is
1:24 just through the roof and chief just
1:26 doesn't handle that well or two maybe
1:29 it's that it's bringing in other uh
1:31 meshes that you don't want to bring in
1:33 it came together with a group of other
1:36 things maybe other Furniture within the
1:38 series or maybe it's that it's all one
1:43 color and you know it's this is actually
1:46 something that has like three or four
1:47 different colors three or four different
1:49 materials in Chief Architect so here we
1:52 go let's get into this and I'm going to
1:54 start off by just going to my own
1:57 website rabbit design.net and in the
2:00 hamburger menu here if we click on that
2:02 we've got resources down at the bottom
2:05 and then there is a model search now I'm
2:07 not going to search a model in this case
2:09 I'm actually going to go to one of the
2:10 known FFN affiliate trade download links
2:13 here and so I'm going to go to Herman
2:15 Miller because I know exactly what I'm
2:16 looking for I want the can chair all
2:20 right so I'm just going to search the
2:21 can chair here it is can lounge chair
2:24 now Herman Miller is a little bit better
2:26 than most in terms of its modeling they
2:29 do a pretty good job of low poly count
2:32 modeling which is great for Chief
2:33 Architect they might not be the most
2:36 realistic models but they certainly are
2:38 good enough so you click on this little
2:40 download button it's going to give you
2:42 different file types I'm going to go
2:43 ahead and use SketchUp and that's going
2:45 to Bam download to a known folder then
2:49 let me get into blender this is how
2:52 blender opens up I have a box here
2:54 selected I'm going to delete that I
2:57 won't go too far into
3:00 um how to use blender there's a ton of
3:03 great tutorials out there on the web but
3:05 I will just show you what I'm doing to
3:08 to make this particular object
3:10 compatible with Chief Architect so I'm
3:12 going to get into the file menu now
3:14 there's some um there's some edits that
3:17 you can do and I'd have you look this up
3:19 but um I added something that enables
3:23 SketchUp importing so that's an add-on
3:26 within a blender so you can add on
3:29 things like this and uh boy I couldn't
3:31 even tell you off the top of my head
3:33 where that is I've always had to look up
3:35 tutorials on this but um there is always
3:37 a way to add on additional features so
3:39 go check that out and then so now when I
3:42 get into import I'm going to see a
3:45 SketchUp import I also made it so that I
3:47 could import 3DS these aren't native to
3:49 blender when you first open it up so
3:52 here we go I've got a SketchUp model I
3:53 get to go find that model I just
3:55 downloaded here's that hey can lounge
3:58 chair we're going to import it and then
4:01 I can just navigate now I'm using a 3D
4:03 mouse to navigate um you'd have to look
4:05 up some things on how to navigate
4:07 otherwise this is mouse wheel in and out
4:09 um right click brings up a menu so left
4:12 click is um brings up some kind of a
4:15 selection so middle Mouse makes it so
4:17 that we can pan around way too fast mind
4:20 you and that's about as far as I'll go
4:23 I've got some settings set up so that my
4:25 3D mouse does um something similar to
4:27 how I have it in Chief Architect so the
4:30 main thing that we're looking to do is
4:32 well actually let's just come in Chief
4:35 Architect where I have this imported
4:37 already and let's take a look at this
4:39 for one it's all one color so that's not
4:42 very helpful and two is that well
4:45 although this isn't terrible it's not
4:47 great either it's 59,000 faces okay and
4:51 so that's pretty high you get enough of
4:54 these objects in a plan and it's going
4:56 to get extremely high so a lot of times
4:59 we'll be finding some Source model say
5:00 it's from um CG Trader or something like
5:04 that where the poly count is in the
5:06 hundreds of thousands and so this
5:08 workflow is going to be really important
5:10 to you so what I want to do here is I
5:13 want to do what's called a decimation so
5:16 I'm going to take particular objects
5:19 here that are in the scene and I'm going
5:20 to decimate them now I could try to join
5:25 these objects that are going to end up
5:27 being the same material by just shift
5:30 selecting
5:31 them and then right clicking and click
5:34 on join and that might make this a
5:37 little bit faster but it's not
5:39 necessarily the best method because when
5:42 we use the decimate modifier it might
5:44 decimate things that are already a low
5:48 poly count like the seat
5:50 cushion um at a different rate than what
5:53 it would decimate some of the uh things
5:55 that have a much higher poly count but
5:58 we've got a little sidebar here and in
6:00 that sidebar is
6:01 modifiers and so I just get to click on
6:04 that and just start typing you don't
6:05 even need to click in a window to start
6:07 typing and that brings up decimate and
6:10 then we see here we've got some kind of
6:12 ratio so if I click and drag and then
6:16 look at the chair in the scene as I keep
6:19 dragging this down look at that it's
6:21 starting to change the
6:24 geometry now it might be really nice if
6:27 I went through and kind of did did some
6:30 one by one decimation and that would get
6:33 me some real finite control I want you
6:36 to also notice at zero decimation we're
6:39 at a face count of
6:41 38,000 so once I
6:44 start bringing this down we see that
6:47 face count number actually dropping down
6:49 at the bottom of the screen here oops
6:52 that's funny my zoom function doesn't
6:54 quite work there so I can just click and
6:57 drag and that face Count's getting to 14
6:59 ,000 10,000 that's getting to kind of
7:02 the level that we want here so that's
7:04 much better right so as I decimate this
7:07 down and we just want to make sure that
7:09 you know maybe that piping is staying
7:11 intact that might be important Etc the
7:14 other thing to keep in mind is that
7:16 we're seeing this tessellation right and
7:20 the thing you should know is that Chief
7:22 Architect has a really great smoothing
7:24 algorithm where we can easily smooth
7:27 faceted angles that are around 30° 40°
7:31 Etc without affecting other things so I
7:34 get to decimate this down to the point
7:36 where that piping starts to disappear
7:39 and then back it out a little bit I'm
7:41 getting to about 6,000 faces that's not
7:44 bad it's actually pretty good so and it
7:47 still looks like the original chair let
7:50 me go ahead and try this again so I'm
7:52 going to click on a couple other items
7:53 here I'm going to shift click and I'm
7:55 going to make the last shift click the
7:57 thing that I just decimated and then if
8:00 I were to hit contrl plus L as in Lima I
8:04 think I get to
8:05 just copy
8:07 modifiers and so that should have copied
8:10 that decimation modifier to these other
8:12 objects making it really easy to Just
8:15 Adjust from there so this one I might up
8:18 that ratio just a little bit to get that
8:20 to look a little bit more smooth sure I
8:23 think that's fine the other one that was
8:25 did a pretty good
8:27 job very cool
8:30 so I'm down to about 9,000 face count
8:34 that's not bad the next part is that we
8:36 clearly need to remap the texture here
8:40 and it might be that I even want to do
8:42 something where we're doing a cubic
8:45 remapping and a cubic
8:47 remapping when we talk about a UV map
8:50 we're talking about the correlation
8:52 between a two-dimensional image as it
8:54 applies to a 3D mesh okay and so the 3D
8:59 mesh is represented by a bunch of
9:00 triangles if you will and so as we've
9:03 got that triangulation we need to
9:06 understand where do those triangles
9:07 exist when they are applied to a
9:10 two-dimensional image and that's going
9:12 to determine how our two-dimensional
9:14 image is applied back to that mesh
9:17 essentially okay so if we were to just
9:19 go take a look at this as an object and
9:22 I'm going to get into the top little
9:24 menu items here and I'm going to go
9:26 ahead and click on UV editing at the top
9:29 here
9:30 just an easy way to get to it and then
9:32 we've got this split screen the left
9:35 side of the screen represents where our
9:37 image would be is just this Square okay
9:41 the right side is still showing us our
9:43 scene now I want to make sure that I'm
9:45 selecting this automatically puts us
9:47 into what's called edit mode and blender
9:49 this is where we can edit vectors
9:52 vertices bases and edges the verticy
9:56 would be an individual point so if we've
9:58 got three points then the face would be
10:01 the triangulation testation of those
10:04 three points that would be our face then
10:06 in between so our face is connected to
10:08 those three vertices and those three
10:10 vertices and that face end up making
10:13 three edges so we could switch to a
10:16 selection where we're either selecting
10:18 vertices those individual points where
10:21 we might want to move them XYZ we're
10:23 selecting an edge where we might want to
10:25 move that XYZ or we're selecting a face
10:28 where we might want to move that and
10:30 XYZ so I want to make sure that I'm
10:32 selecting all okay and then there is a
10:37 UV tab up here and so if I um were to do
10:42 a cube projection with the cube
10:44 projection would be is that think of it
10:47 as we're placing a cube around this
10:51 entire chair and that Cube this how I
10:55 like to visualize it that Cube has our
10:57 image whatever our texture is going to
10:59 be in Chief Architect in Twin motion
11:01 whatever our texture is going to be that
11:04 image is applied to all sides of the
11:06 cube and as that Cube shrinks it hits
11:10 mesh and it starts wrapping itself
11:12 around until it hits another side so if
11:14 we have a cushion and it's at a little
11:16 bit of an angle that cube is just going
11:17 to hit that cushion and then just start
11:19 to wrap until it creates seams and so
11:22 that's a cube projection so if I hit
11:25 Cube projection we're going to see here
11:28 it automatically show shows us all those
11:30 vertices all that triangulation as it
11:33 sits on a two-dimensional map so if we
11:35 were to place a map on top of this we're
11:38 seeing these individual curved sections
11:41 Etc now blender has something that they
11:44 call Smart UV project and what's nice
11:47 about it is yeah we could put a map on
11:50 top of this and it would work quite well
11:52 but it not might not wrap at the seams
11:55 the way we want it to and so blender
11:58 actually has something called smart UV
12:00 project let's try this and see what
12:03 happens here it tells me an angle limit
12:06 this is an angle limit basically before
12:08 we're generating some kind of a seam so
12:10 I think 66° is plenty and then let's
12:14 just go ahead and press okay the island
12:16 margin is basically do we have a gap um
12:20 are we going to push the vertices to the
12:22 bounds of our 2D mesh or we're going to
12:24 leave a little bit of a border there
12:27 okay and so that would be the island
12:29 margin and I'm not going to go over
12:30 anything else here so let me go ahead
12:32 and press okay and you can see it's
12:35 splitting that piping out it's splitting
12:37 these individual faces it splits it up
12:39 until it sees some kind of 66 degree
12:42 overlap and so this is that smart UV
12:46 projection now it might have been that
12:48 would would have been beneficial to for
12:50 us to pull that piping out of here
12:52 because the piping ends up taking a lot
12:54 of this map which means that um our map
12:57 itself we're going to have to shrink the
12:59 scale of it if we wanted it to be
13:01 applied in a way that makes a lot of
13:03 sense or we're going to have to take
13:05 this full selection and in the rightand
13:07 side scale this up and so the scale of
13:10 this going up would be we're essentially
13:12 changing the scale of how um our
13:16 two-dimensional image would be applied
13:18 to these vertices so that if I wanted to
13:20 scale this so that my two-dimensional
13:23 image would be a one toone scale to the
13:25 to the face of the cushion right here
13:27 I'm basically ballparking it right now
13:29 now all right we'll see what this looks
13:31 like in just a second the next thing I
13:33 need to make sure I I'm doing here is
13:36 I'm going to get back into just an
13:37 object mode with this selected I want to
13:40 make sure that I've got a different
13:42 material applied now I'm not great at
13:44 this software but I think I get to go to
13:46 this little material Tab and I think I
13:49 can add with a plus icon a new material
13:54 slot or it might be actually I think I
13:57 did that wrong I think we just just got
13:59 to add a material here okay and then
14:02 this is the base color of that material
14:04 let's just make it PL pink to really see
14:06 it and then there is a way to apply this
14:10 material to our selection I might have
14:12 to be in edit mode so that we have faces
14:16 selected so let's just select all and
14:19 then if I assign that new material here
14:22 there we go you see in the preview that
14:24 it changed that material I'm going to
14:26 have to do that again now I know there's
14:28 a better way to do this I just know it I
14:31 just feel it anytime something feels
14:33 like it's not that efficient I just know
14:34 there's a better way but this is what I
14:36 know of this software I'm selecting
14:38 another object and we're going to have
14:41 to make another material here um there's
14:43 a few materials in this material class
14:45 here but I think I'm just going to do
14:46 that same thing I'm going to hit the
14:47 plus icon going to say new material
14:51 we're just going to call this doesn't
14:52 matter we get to rename this anyways
14:55 rename okay and we'll get back to that
14:58 edit mode
15:00 where I'm selecting
15:03 all and then I'm going to assign that
15:06 new material
15:08 rename and I think that's about it I
15:11 think this is properly mapped the way I
15:13 need it to be mapped now something to
15:15 keep in mind blender scale units I
15:18 believe is in meters unless you've
15:21 changed it so I might need to get into
15:24 What's called the scene options and get
15:26 into the units panel here and there we
15:29 go change it from metric to Imperial and
15:32 change it into maybe inches instead of
15:35 feet okay and so now I get to export
15:39 this whole scene and take a look at how
15:41 we did so I'm going to export and I'm
15:44 going to use wavefront an obj file
15:46 because we know that that Imports easily
15:49 into Chief
15:50 Architect and then let's just call this
15:55 Herman Miller in lounge chair and a few
16:01 things we need to make sure that we're
16:03 doing here and one is that we want the
16:05 up AIS to be uh Z in this case okay so
16:09 we want to make sure that that's
16:10 happening do not check limited to
16:12 selected only unless you truly are only
16:14 trying to export something that you have
16:16 selected in the scene um I'm going to
16:19 export UV coordinates normal Maps yep
16:22 Etc and then let me
16:24 export now back in Chief I just get to
16:27 come in here and I'm just going to make
16:28 make a
16:30 copy drag this out and I'm going to open
16:33 this
16:34 up and I mean and I imported this just
16:38 like you typically would except for that
16:39 I did not add it to library I like to
16:41 make my edits before I add something to
16:44 the library so now I just get to be in
16:46 the 3D panel and then replace geometry
16:50 and I get to go
16:51 find that obj file I just
16:55 created um which I don't know where I
16:58 saved it been inocent by accident there
17:01 it
17:03 is so there it goes it replaces that
17:06 geometry the scale units still seems to
17:09 be off I didn't quite get that set up
17:11 right so we're going to have to change
17:13 this drawing unit to meters and watch it
17:16 scale up saw that get to General we see
17:19 the scale looks correct now now
17:21 something about x16 the tessellation is
17:24 showing up even with a pretty heavy
17:26 smoothing angle so something's going on
17:28 here the other thing is when you replace
17:30 the geometry it will not update the
17:32 number of faces until you close this
17:34 down and open it back up again okay we
17:38 do see that this is UV mapped to three
17:40 different colors so that part's really
17:42 good great and let's just press okay and
17:45 see if we can't apply those colors now
17:48 before I get too far into this I'm going
17:50 to open this back up and just see what
17:52 the face count of this this was to see
17:55 how I did you know I cut it down
17:57 significantly 19 18,000 not great but
18:01 it's certainly good enough the main
18:02 issue there was that piping um as it
18:05 lines the cushion was going to be really
18:07 difficult to decimate without just
18:09 losing it entirely so you might have
18:11 wanted to do that if you really need to
18:13 make a super low poly count version of
18:15 this I just say get rid of the piping
18:17 altogether and we could do some cool
18:19 things maybe we'll still touch on that
18:21 so there we go there's our 45° you can
18:24 see here tessellation showing up we're
18:26 not getting some Vector smoothing that's
18:28 too bad you might be able to do
18:29 something about that in blender I'm not
18:31 sure it might just be that we need to um
18:35 make sure that we're welding vertices
18:36 what's called welding vertices so that
18:39 could have been a problem um and that's
18:41 you know again coming back to my lack of
18:43 knowledge but for the purpose of what I
18:45 needed to do here I could have gotten to
18:47 this point very very quickly without
18:50 worrying about this at all so let me get
18:53 into General panel check out a few
18:55 things you know I might want to redo the
18:58 cad block let me press okay and let's
19:00 apply a couple things here so I'm just
19:02 going to apply a leather texture to what
19:04 I know is
19:07 leather I've got some stuff in my
19:10 library so I know that these cushions
19:12 are leather bam and so this is you kind
19:15 of going to start looking like something
19:17 here pretty quick got a gold leather
19:19 texture let me check out a couple of
19:21 these there we go that's looking pretty
19:23 good and then um I think just a black
19:28 black stainless material on the frame
19:32 and then the last part is this is a
19:34 black piece too right we could see that
19:37 frame and the way that's acting look at
19:40 that doesn't that look nice and now this
19:43 is a usable piece of furniture bam we've
19:46 got our spec Furniture it's um it's got
19:49 a significantly lower poly count and
19:52 it's looking pretty good now I'm really
19:54 curious to see what happens if we could
19:56 take the smoothing from a previous
19:58 version and improve on this by importing
20:02 it from a previous version let's try
20:04 that out real quick before we get back
20:06 into blender so I'm going to open up X15
20:09 that utilizes a completely different
20:11 algorithm for its
20:15 smoothing let's just do a little import
20:18 3D symbol I'm going to find that same
20:25 symbol I am not going to add it to the
20:28 library we're going to put it as a
20:29 Furnishings interior
20:32 class here we go you get to change the
20:35 geometry of this now unfortunately you
20:37 have to repport it to change the
20:38 geometry of it so we're going to have to
20:40 get in 3D replace geometry because
20:43 otherwise it does not enable the tool to
20:45 change the um sizing of it so you could
20:49 just do some multiplication um in um by
20:53 keeping the restraints locked if you
20:55 resized it manually but I like to do it
20:57 this way it's changing the source object
21:00 so uh there we go we'll change it to
21:03 meters that'll size it way up bam like
21:05 this and notice here Look chief X15 is
21:09 doing a great job of smoothing this out
21:12 right so that's a big part of this and
21:16 so let me just press okay bam and now
21:19 let me add it to the library actually
21:21 let's go ahead and uh do a little CAD
21:22 block because the cad block was bad as
21:24 well right so there's our new CAD block
21:27 cool let's add it to the
21:35 library I clear anything oops where is
21:38 my library on this guy 1x16 where is X
21:42 Library there we go now let's export
21:46 this export
21:49 Library bring this downloads
21:59 now I should be able to get into that
22:04 folder
22:07 downloads and we're going to find that
22:09 calib file by file type in this
22:13 case there it is I get the drag bring it
22:17 into
22:18 x16 bam it Imports that symbol it's
22:22 place that symbol let's take a look at
22:24 what this looks like when we open it up
22:26 in 3D look at that so so it doesn't have
22:29 all that Vector issue isn't that
22:32 crazy right so that's an improved symbol
22:35 coming in and the smoothing seems to be
22:37 working correctly as well so now let's
22:39 just paint our materials the way we want
22:42 it there's a reason to keep X15 you know
22:46 I have reported this and I didn't get
22:48 any much feedback on this um I was asked
22:51 to give more examples and you know at at
22:54 that point I was just thinking you know
22:56 what I don't want to have to give more
22:57 examples I just take my word for it I'm
23:00 a top technician it doesn't work please
23:04 go check it out so there we go and let's
23:07 see if we increase the smoothing does it
23:09 actually improve the quality of this I
23:10 want to get this uh 79 degre smoothing
23:14 and yeah I think on the whole we don't
23:16 see all this little micro tessellation
23:19 that's happening in
23:21 this we don't see it in this symbol
23:23 right over here this looks pretty good
23:25 right pretty sharp so very nice now
23:29 let's go back into blender what was the
23:31 thought that we were thinking about
23:32 doing something in blender
23:35 here oh let's
23:39 see now I kind of forget oh what would
23:41 happen all right so what would happen if
23:43 we got rid of the piping here let's just
23:45 go back a bunch of steps or we can just
23:48 repport this whole thing so way before
23:51 we did our UV mapping Etc and I might
23:54 even just re UV map this just to show
23:56 you um what can happen with it but let
23:58 me just do a brand new
24:02 file don't save get rid of this let's
24:06 import that again it's not a 3DS file
24:10 it's a SketchUp
24:19 file and so let's get rid of the piping
24:23 and here's what I think is interesting
24:25 about getting rid of the piping is that
24:27 we can actually SCT these little side
24:29 pillows here and before we even start to
24:32 decimate let's get into sculpting so
24:35 we're going to have to sculpting tab
24:37 here and we're in sculpt mode now and if
24:40 you roll down a little ways you'll get
24:43 to the cloth filter what's really cool
24:45 about the cloth filter is up here at the
24:48 top we can set this to inflate or expand
24:53 in this case and click and drag left or
24:56 right and we can add some kind of little
24:59 bit of features here right something
25:02 that looks a little bit more relaxed or
25:04 realistic even the other thing that we
25:07 could do is we could set this um we
25:10 could set this bottom piece here this
25:13 cushion to be some kind of a collider
25:15 now I'm not sure how to do that um I
25:18 haven't gotten into this enough to know
25:22 what I'm doing here um I'm thinking that
25:25 I probably could
25:26 search in yeah I searched collisions and
25:30 there we go physics Collision so maybe
25:33 this makes this a collider same kind of
25:35 thing here so remember if we shift click
25:37 and then shift click the next object
25:40 that has a modifier on it then hit
25:42 contrl L we get to copy that modifier
25:45 over so now this should also have a
25:47 modifier
25:49 collision and it doesn't settings are
25:52 inside the physics Tab and let's just
25:55 add Collision again so I think now if I
25:58 go to sculpting maybe maybe my you know
26:03 idea is correct here and that I get to
26:05 do a little bit of gravity and click and
26:09 play and I click the wrong way I want to
26:12 go down so that it knocks into something
26:15 below all right so I have something
26:16 wrong here one second I'm going to
26:18 figure this
26:20 out okay I had to pause but I got it so
26:24 here's what's going on is I'm going to
26:26 switch to that object mode again I'm
26:28 select this guy and actually this panel
26:31 right here is where we get to the
26:32 physics panel right here is where we get
26:34 to say that this is a collider okay so
26:37 very easy to get to that we don't need
26:38 to add a modifier in that case so we're
26:40 just going to select this guy right here
26:42 and we can see that that's a collider
26:44 now all right so the next part is that
26:46 we want to sculpt and so when we get
26:48 back into sculpt mode and our active
26:50 tool is that cloth simulator then we
26:53 need to hit the N key which brings up
26:56 our active tool and check use collisions
27:00 and so this is going to take up a lot of
27:02 resources when you're using this but I'm
27:04 just going to kind of click and drag and
27:06 show that the collisions are actually
27:08 working now before I even set this up I
27:11 want to make sure that I've got a few
27:12 things here I think the cloth mass in
27:15 this case is I'm going to decrease this
27:17 substantially and cloth dampening I
27:19 might increase this okay so I'm going to
27:22 click and move to the right should drop
27:24 this down and we should start to see
27:27 this in
27:29 interacting piece
27:32 below there we go you can see it it's
27:34 hitting it now isn't that kind of
27:38 crazy now another thing you can do with
27:41 this as I go a little overboard here is
27:44 we can switch from Gravity to inflate or
27:47 expand and let me click and I think drag
27:50 left and it can kind of get this to
27:53 inflate or
27:56 deflate right
27:59 click and drag
28:03 right isn't that crazy all right so I'm
28:07 going to go back up a little little
28:09 level there here we go something like
28:11 this but yeah you can do some pretty
28:13 wild stuff with this you can also just
28:16 use this the sculpting tool so I might
28:19 just come in here and we've got a draw
28:21 mode here I believe if I hold shift it
28:24 will actually smooth a lot of these
28:25 vertices that just were kind of of
28:28 goofed up when we use that collider
28:30 modifier okay so look at that I can just
28:33 kind of clean this up and so then after
28:35 I get this looking the way I want it to
28:37 and maybe a little bit more realistic we
28:39 can still then go apply that decimation
28:42 as a modifier to these cushions and get
28:45 something that looks maybe even a little
28:47 bit more realistic at the sacrifice of
28:50 maybe some additional um vectors right
28:53 so let's just switch
28:56 to an object mode
28:59 I've got these two selected we can click
29:01 on that modifier we can come in here and
29:05 decimate and then drop this down from
29:08 18,000 verticy just keep kicking this
29:12 down and yeah even at 3,000 faces not
29:17 vertices even at a 3,000 face count
29:19 we've got a lot of those cool little
29:21 features we did in there and then we can
29:23 repport it in Chief Architect again and
29:25 check it out and on top of that after
29:28 the decimation modifier I believe we
29:30 could still come in here with the
29:32 sculpting tool and kind of shift click
29:35 and do a little bit of clean up so some
29:38 really cool stuff you can do in blender
29:40 to make some um very goodlooking
29:43 permanent Furnishings inside of the
29:47 software let me know if you have any
29:49 questions about this I'm actually pretty
29:51 happy with my n result I'd be you know
29:53 just fine with this maybe I'll go back
29:55 in and do a little bit more decimation
29:57 maybe I will miss around with how this
29:59 cushion looks as it's sitting on here
30:01 and then of course you can modify
30:03 individual things drop this down expand
30:06 it stretch it do whatever you need to do
30:08 and then the last thing that might make
30:10 this symbol even more Dynamic is getting
30:12 into the advanced sizing and then put a
30:14 stretch plane in the width zero in
30:16 stretch plane in the width so you could
30:18 use this to make their lounge chair as
30:21 well look at that Isn't that
30:25 cool very cool Dynamic modeling
30:29 neat let me know if you have any
30:31 questions
30:40 [Music]
