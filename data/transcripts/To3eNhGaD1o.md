---
videoId: To3eNhGaD1o
title: Removing Objects or Parts From Sketchup 3d Warehouse Downloads For Use In Chief Architect
url: "https://www.youtube.com/watch?v=To3eNhGaD1o"
status: imported
---

# Transcript

0:03 This video is for those of you that like
0:05 to pick up some stuff from 3D warehouse
0:08 or outside sources and you are
0:08 downloading something that has multiple
0:11 objects that you don't need and it has
0:11 one object that you do need and how can
0:16 we isolate those. And I'm going to go
0:16 over a couple of misconceptions about,
0:20 you know, several approaches I've seen
0:22 people try to take and why they don't
0:25 work. So, here we go. I've got this
0:25 coffee table assembly here, right? And I
0:29 want just this coffee table in the
0:29 middle. I don't want this other part. In
0:33 fact, I don't even want any of the
0:33 decorations on top of this as well. I'm
0:37 going to download. There's a couple
0:37 different uh file types we could do.
0:39 SketchUp file and then oftent times you
0:43 might see a D AE file which is a colada
0:47 file. So I download that ends up in my
0:49 downloads folder. And then what I do,
0:49 and this is a common thing that people
0:53 do, is that they might go to their
0:53 downloads folder and then they might
0:56 find that file, which is a SketchUp
0:56 extension, and drag it straight into
0:59 Chief Architect. Now, this does work,
1:03 but I'd like to mention that this
1:03 automatically is going to import this as
1:10 a fixture symbol category. Okay,
1:10 fixture. So that's important to note
1:12 because in case you're actually trying
1:16 to import some kind of an electrical
1:16 symbol, you don't want to import that as
1:20 a fixture. You want it to import it as a
1:23 symbol category electrical. So another
1:23 way to do that is to go into file import
1:30 and then import 3D symbol and go find
1:30 your SketchUp or colada file. Do it that
1:35 way and then you get the prompt that
1:35 whether or not you want to change the
1:36 symbol category and you would change it
1:38 to electrical in that case. One more way
1:43 of doing that is we can always reconvert
1:45 a symbol. So we can go into our edit
1:45 toolbar, which this is usually docked at
1:49 the bottom of your screen, and we can
1:49 hover over this guy right here, convert
1:53 selected to symbol, and then that gives
1:55 us the option to pick that symbol
1:55 category where it might have been an
1:58 electrical
1:58 feature. Excuse me. Okay, so the next
2:02 part of this, and this is another one of
2:06 those common misconceptions that I've
2:06 seen, is that, hey, I want to get rid of
2:09 this other coffee table. Well, this
2:09 should be easy. I just get to hit this
2:11 explode block thing, right? So, edit CAD
2:17 block. Well, this is not some kind of
2:19 explode architectural block tool that
2:20 you might have seen where we make an
2:22 architectural block out of multiple
2:26 objects. This is we're changing the
2:26 representative 2D CAD for this symbol.
2:30 So, if you go into the symbol, when the
2:34 symbol is created, a number of things
2:37 happen. One is that it converts any
2:37 polygons that create this mesh that make
2:42 up this symbol. It converts those into
2:42 triangles and then it autogenerates some
2:47 kind of two-dimensional CAD
2:47 representation of this. So we can
2:49 generate this CAD block. Okay. Now I
2:53 don't want to get too off path, but we
2:54 are going to talk about triangle counts,
2:57 polygon counts, cuz that's going to
2:57 matter in Chief Architect. You can't
3:01 just go downloading any 3D warehouse
3:01 item without considering how many poly
3:06 count there is in that item. Okay, but
3:06 before we get to that, let's just go and
3:10 see. This is kind of the misconception
3:13 is, hey, if I just get rid of all this
3:13 this stuff in the middle here, if I just
3:17 delete this and then save this,
3:17 shouldn't that just get rid of it in 3D?
3:22 Right. And in fact, no, it doesn't. when
3:24 we pull a little camera view. Yeah, even
3:25 though it looks like it's just two
3:26 little coffee tables next to each other,
3:31 it still has all that 3D geometry. So,
3:31 that is not a way that we get to get rid
3:35 of the geometry coming from the symbol
3:37 that we downloaded. So, how do we get
3:39 rid of that geometry? Well, we have a
3:42 tool called the delete surface tool.
3:46 Okay, delete surface tool. And as I
3:46 hover over surfaces, these are faces
3:49 essentially. Okay. And actually, it's a
3:53 collection of faces. We'll get into the
3:55 details on that in just a little bit. I
3:57 get to just click and it will delete
3:57 part of that geometry. Cool. That's all
4:01 we needed, right? So, I just get to
4:01 carefully go delete all that geometry
4:07 and I'll be done. Unfortunately, not.
4:07 Once we rebuild the 3D, and we rebuild
4:09 the 3D by any number of different ways.
4:13 I could place a cabinet in here or I
4:13 could place some kind of architectural
4:17 feature or I can just modify something
4:19 that's already in here like my terrain
4:19 in this case. And look what happens. It
4:24 rebuilt the 3D and all of a sudden this
4:24 little dome is back in place. So, how do
4:29 we make our changes be permanent? Well,
4:31 we're going to use that delete surface
4:33 tool. Delete. Delete. Delete some
4:33 surfaces. And now I get to select this
4:36 object which still shows a bounding box.
4:40 This is our bounding box. That's how
4:42 Chief resizes something based on a
4:42 bounding box. I get to choose that and
4:44 then I get to hit that convert selected
4:49 to symbol. Now, I'm not ready to change
4:51 this to the symbol category I want,
4:51 which is furniture. So, I can just leave
4:56 this as fixture and I can leave add to
4:57 library and show advanced options
4:57 unchecked and press okay. And what this
5:02 is going to do is it's going to load it
5:02 as an object that's being placed into my
5:06 mouse. Right. So, now we're in a place
5:09 object mode. And then in my edit
5:11 toolbar, I could in fact toggle
5:11 replacement mode and just replace the
5:13 symbol that's here. And when we go open
5:19 it, guess what? We have now gotten rid
5:19 of that second little coffee table. Now
5:24 I have a lot more things to get rid of.
5:26 And you can see here the delete surface
5:28 tool is going to take in account all
5:28 these little tiny leaves, right? And so
5:33 how do we get rid of all these in an
5:33 efficient way? And this is where I want
5:37 to come back and kind of show you what
5:37 the difference is between a symbol that
5:41 has smoothing turned on and a symbol
5:42 that does not. And let me go back to our
5:47 SketchUp 3D warehouse where we get to
5:47 see a polygon count. I want to be really
5:52 clear about what this is. This is a
5:52 polygon count. Now, what is a polygon?
5:55 Well, it's not a triangle. It really is
6:01 pretty much anything that has closed
6:03 edges, right? makes a shape, makes a
6:06 closed polyline if you will. And you
6:06 want to kind of um uh understand that in
6:12 terms of what chica chief architect
6:12 calls a polygon, which would be a closed
6:15 polyline. That means it could be
6:15 five-sided, six-sided, who knows, right?
6:20 So, however many sides that is, what
6:27 in, if you have a five-sided polygon,
6:27 all of a sudden that's going to be, you
6:30 know, a bunch of little triangles
6:30 instead. So this number is just the base
6:34 number. Once it actually gets converted
6:36 to triangles, it can be considerably
6:36 more than this. So even though this says
6:41 71,000 in the case that we brought this
6:44 into Chief Architect and maybe I could
6:46 go back a few steps before we replace
6:47 this
6:47 object. Right now if we go and look at
6:53 this, even though it said 71,000 in
6:55 SketchUp, when we go look at the 3D
6:56 panel down at the bottom, number of
6:56 faces, it's in fact 82,000 faces. So,
7:00 there were some faces that weren't just
7:06 triangles. Now, 82,000 faces is a lot.
7:07 You get enough of these, it's going to
7:09 really slow a scene down. Just to give
7:12 you an example of what a heavy scene
7:12 might be is if you're on an M1 chip or
7:19 you're in a 2000 series RTX graphics
7:19 card, a scene of about 2 million polies
7:24 is really going to start challenging
7:24 your system. If you're on, you know, an
7:30 M2 chip, lower 3000 series, you know,
7:30 seen of 2.5 million. If you're on um one
7:36 of your higher RTX cards, you know,
7:36 consumer grade RTX cards, you're going
7:38 to be in the 3 million range. How do we
7:42 know how many uh how much surface count
7:44 is? Well, when I just refresh a scene
7:44 down at the bottom here, it's telling me
7:48 how many surface there are. So, I'm at
7:50 106,000 surfaces. And a large part of
7:50 that is just how heavy this particular
7:52 symbol is. Chief Architect makes symbols
7:59 in less than 10,000 polyc count, which
7:59 is really, really low, which should give
8:03 you some appreciation about what their
8:04 engineers do in terms of creating
8:04 symbols that are really low weight and
8:10 make your scene nice and move fast and
8:10 rebuild fast. So, how do we get this to
8:14 a lower poly count? Well, you're going
8:14 to need a third party software for that,
8:17 or you're going to have to be really
8:19 careful about the objects you choose
8:19 from 3D Warehouse. Now, the next part
8:23 about this is let's just open this
8:26 object up. I want to change symbol
8:26 surface smoothing. Okay. And I'm going
8:31 to change this to zero just so you can
8:34 see how many triangles are in this
8:34 symbol. You're going to see that it's
8:36 rebuilding right now. And it's going to
8:37 create a bunch of vector lines in just a
8:43 second. Now, what this is doing is it's
8:45 saying that any faceted edge or angle,
8:45 and I've gone over this in several other
8:48 videos. You might see me say this over
8:51 and over again, but any faceted angle,
8:53 whatever this angle is, if it's less
8:55 than our set smoothing angle, Chief
8:56 Architect is going to smooth it. It's
8:57 going to round those edges. So, you can
9:02 see here, we've got edges that are in
9:03 plane with each other. So, if a
9:03 smoothing angle of one is going to get
9:08 rid of those edges that are in plane
9:08 with each other, right? Right. So, if I
9:12 set that to one, it would rebuild this.
9:12 And you're going to see this surface top
9:16 at the very top. It's suddenly going to
9:19 look like it's one single face. And in
9:21 fact, it's multiple faces, but Chief
9:24 Architect is just not drawing vector
9:24 lines on top of your symbol anymore. So,
9:29 you can kind of see how this is working.
9:31 Now, what happens when you leave this
9:31 symbol smoothing down really low is that
9:36 when we use the delete surface tool, the
9:39 delete surface tool takes any kind of
9:42 smooth surface as one single face to
9:44 delete. So, when we have this really
9:44 low, it means we're going to all of a
9:47 sudden do a lot more work with the
9:47 delete surface tool if we wanted to
9:49 remove this geometry cuz it's going to
9:51 make us pick these individual triangles
9:55 to delete. So, now the inverse is true
9:58 as well. If I set the symbol smoothing
10:00 almost to 180 degrees, which would be
10:03 flat right now, every surface is as
10:03 smooth as it could be so long as it has
10:08 some kind of a joined edge, which means
10:12 that um the model itself has no gaps in
10:15 it. It's modeled correctly. Now, with a
10:17 smoothing angle that high, the delete
10:20 surface tool is going to delete a lot
10:22 more in one click, right? So, we're
10:22 going to get a lot more use out of this
10:27 tool. we might be able to get rid of
10:27 more of this geometry a lot faster. Now,
10:32 a trick that I like to use is I like to
10:35 actually turn on a line
10:35 over as a method, and that just helps us
10:39 see things that we might have missed
10:41 when we're using this tool to delete
10:44 things. Now, ultimately, I picked a
10:44 symbol that was going to be challenging
10:47 because I wanted to show you that yes,
10:50 you could go through and delete all
10:50 these little leaves, and it's going to
10:51 take you a while. But the thing I'd like
10:57 to point people to in in uh in case they
10:59 need it is that Blender is a free
10:59 software. Yes, if you had SketchUp, you
11:03 could modify that geometry in SketchUp.
11:05 And of course, that would be a really
11:05 easy way to do it because those objects
11:09 are built in SketchUp anyways. But if
11:09 you don't have SketchUp and you'd like
11:14 to try really powerful open-source
11:14 communitydriven setup software, it would
11:19 be Blender. And so Blender can do a few
11:21 things that might make this a lot
11:21 easier. And at the same time, we might
11:24 be able to optimize this symbol a little
11:28 bit, making it a better symbol to import
11:31 into Chief Architect. So, I'm going to
11:31 bring Blender into my main window here.
11:35 And I do have an add-on. And my add-on
11:37 is that I went and looked up how can I
11:40 import SketchUp files natively because
11:42 out of the box, Blender does not do
11:42 that. Okay. So, I did go look that up.
11:44 That's in a YouTube video somewhere. You
11:49 can add on the ability to import
11:49 SketchUp files. And so I just get to go
11:54 locate my SketchUp file. And let's see,
11:56 what was it called? That was a funny
11:57 one. This case, it's component 37. So
12:02 we're going to open up component
12:02 37. And there we go. Here's our symbol.
12:07 Now, because this is a SketchUp file,
12:09 these objects are separate when they
12:09 come into Blender as opposed to bringing
12:13 them in Chief Architect where they are
12:16 converted and turned to one static
12:18 symbol. I still have the hierarchy
12:20 coming from SketchUp. So these are
12:20 individual objects. So if I wanted to
12:22 get rid of this stuff, that'd be really
12:25 easy. I just get to select this and
12:25 delete. Bam. Done. Very simple. So this
12:28 is why this is a powerful tool for those
12:32 of us that might be bringing in things
12:34 from 3D warehouse and we don't want to
12:34 pay for SketchUp is we can come in here
12:36 and delete the things that we don't want
12:41 very very easily. Another thing about
12:41 this is let's just take this for example
12:45 is I'm going to select all these and
12:47 let's just say I do want this as one
12:47 symbol all together. So I get to select
12:52 all these as an object and as an object
12:52 I can join these together. And so when I
12:58 join these together I can do a couple of
13:01 modifications to them all as one object.
13:03 All right. So that's one thing to
13:03 consider. The next thing to consider and
13:08 let me just show you. I've joined these.
13:10 Now, these are just one object. Keep in
13:13 mind, I'm no expert in Blender. I know
13:15 just enough. There's just a few things
13:15 that are easy enough for me to pick up.
13:19 We're in some mode where I get to just
13:19 highlight and select. And that's what I
13:23 did. And then I rightclicked to join
13:25 once it's joined. And again, you can
13:25 look all of this up. It's easy to find
13:27 this on the internet because Blender is
13:33 a huge program and it's got a lot more
13:37 um um there's a much larger user base.
13:38 And so there's going to be a lot more
13:40 YouTube videos out there. So I get to
13:40 put on a scene modifier. And that scene
13:44 modifier I'm going to do is decimate.
13:44 And this is an industry standard where
13:46 we're taking some kind of poly count and
13:52 we're trying to redu reduce it through
13:52 some kind of algorithm that's built into
13:56 the software. And so you can see here
13:58 this is showing face count at 74,000.
13:58 I'm going to triangulate this because I
14:01 know Chief Architect's going to do that
14:03 anyways. And then I just get to click a
14:06 ratio and drag it down. And you can see
14:09 this face count number is dragging down
14:12 with it. Okay. And my target is I want
14:12 this in less than 10k poly. But what I'm
14:18 doing now is I'm looking at the symbol
14:21 itself and in real time it is getting
14:23 edited. And look at that. We finally
14:26 went so low that it's no longer even
14:26 recognizable. So I can drag that back up
14:31 a little bit. And I kind of want that to
14:33 make sure those, you know, those leaves
14:35 are still showing up and that this is
14:35 still looking like a symbol that I might
14:39 use. And so I'm just under 10k poly now.
14:42 And this still looks pretty good. Now,
14:43 keep in mind, we can see that there's
14:46 some kind of faceted edges here. And
14:46 maybe that's not good. And maybe that
14:47 won't look good in Chief Architect, but
14:50 you also have to remember that Chief
14:50 Architect will smooth this in a way in a
14:56 better way than Blender does. So it can
14:58 retain the shape and might look just
14:58 perfect. And it's takes a trained eye to
15:03 kind of see where this is going to get
15:04 smoothed and how it's going to end up
15:06 looking like because right now this
15:06 doesn't look that great. But when we
15:10 apply some smoothing to it, it might
15:12 actually turn out just right. So I'm
15:12 going to go ahead and export this file
15:17 now. And I'll export it as a wavefront
15:17 OBJ because that's one of the file types
15:21 that Chief Architect can take. So
15:23 Wavefront
15:23 OBJ. Blender takes an industry standard
15:29 which is the upaxis is Y. In our case,
15:29 we want the up axis to be Z. And then it
15:34 is going to be some scale that makes no
15:35 sense to Chief Architect, but that's
15:36 okay. It's actually going to be the unit
15:40 of measurement is meters. We can always
15:43 convert that when we import. So, export
15:51 OBJ. And I forgot to even name it. Let's
15:53 see what I even did. See, I'm going to
15:54 put it in the downloads folder. and
16:03 SketchUp. Now, back in Chief Architect,
16:05 I get to just bring this in. But not
16:05 only do I get to bring it in, I could
16:07 just replace the geometry of the object
16:12 that's here by opening the symbol up,
16:14 getting to the 3D
16:14 panel, and then replace geometry is
16:19 right here. Now, you could choose
16:19 anything that you want at this point.
16:21 Um, and the reason I say that is because
16:25 the unit of measurement is incorrect.
16:25 This is kind of a backwards thing that's
16:29 in Chief Arctic that I hope that they
16:31 fix someday. I'm going to choose that
16:33 same exact one that I had before. And
16:35 the only reason I'm choosing the same
16:35 exact one as I had before is because now
16:39 I'm going to change the unit of
16:41 measurement. And this is
16:41 when it's going to have us reimpport
16:44 something. So, in fact, I should have
16:48 used I'm sorry, I made a mistake. I
16:48 should have used that replace geometry
16:52 and find the geometry that I need. But
16:52 now that I have that unit of measurement
16:55 set to meters, this should be easy
16:57 enough. So, converted SketchUp
16:57 OBJ place that it's in meters. There we
17:03 go. It's brought in. Now, I want you to
17:03 note that the number of faces stayed the
17:07 same. It's 82,000. Okay. But in
17:07 actuality, when we go check this out, is
17:12 that when I open this up, we're going to
17:15 see that there we go. It has been
17:15 updated to 9,000 faces. Now, when we
17:18 decimated this, some of the materials
17:21 got changed, and that's up to you. This
17:27 also should help you kind of understand
17:27 that if you needed a symbol to split its
17:32 materials up, you could set that up in
17:33 Blender ahead of time before you
17:34 imported it. But now, we have this
17:37 object. It's got that side table
17:38 removed. It's been decimated down to
17:40 just 94 or 9,000 polyc count. So, it's a
17:47 nice lightweight symbol. And there we
17:48 go. And it's just going to paint a
17:48 couple new textures on there and I'm all
17:54 done. So, that's the easier way to split
17:55 geometry up. So, you can use either of
17:55 these methods is use that delete surface
18:00 tool, reconvert something to a symbol,
18:03 etc. Now, I get into a lot more symbol
18:05 advanced symbol modification into my
18:06 paywalled section of YouTube. If you're
18:09 interested in that kind of stuff, go
18:09 check that out. Um, and then on top of
18:15 that, you can always come up and open
18:17 this up, get into the advanced sizing
18:17 panel and set this up for stretch planes
18:21 and bounding boxes so that this
18:21 stretches parametrically the way that
18:23 you need it to. Say you want to stretch
18:25 this and maybe change the width of this,
18:29 but you don't want to touch the plant is
18:30 you're going to have to rotate this and
18:31 get to a point where you're cutting
18:31 through geometry in the middle without
18:34 touching that plant. In which case, you
18:37 probably would have just removed the
18:37 plant. So, I hope this video was helpful
18:43 to you. I know this gets a little bit
18:44 into the advanced size, but this is
18:44 stuff we need to learn when we're trying
18:50 to source uh objects from thirdparty
18:51 places where we're not just hiring
18:51 someone to make the object for us, where
18:55 it's optimized for chief architect,
18:55 we're just trying to find it online free
18:58 somewhere. This would be some stuff that
