---
videoId: KdTW-VHQorY
title: Split A UV Map   One Object With Multiple Textures Using Blender
url: "https://www.youtube.com/watch?v=KdTW-VHQorY"
status: imported
---

# Transcript

0:00 In our previous video, we created this
0:03 chair using Turbo 3D and
0:06 from there, I'm going to show you how to
0:08 split this mesh up into multiple
0:12 different UVs so that we can paint the
0:14 base separately from the main lounge
0:18 part of the chair, the cushions, the
0:20 fabric, etc. So, how do we do this?
0:23 I've got a particular workflow that
0:24 works really well for this and it's
0:26 going to utilize Blender. Blender is
0:28 free and you're going to utilize some
0:30 tools that are edited for Blender and
0:32 this is the first version of those
0:34 tools. It's a beta, if you will, okay?
0:37 And so, the first thing that I'm going
0:40 to do is I'm going to regenerate this
0:41 particular model and I'm going to
0:43 regenerate it with one thought in mind.
0:46 I'm going to bring up um
0:48 my ChatGPT in this case. You can use any
0:51 AI that you might be subscribed to.
0:53 There's so many of them out there. They
0:55 all work quite well. And so, what I'm
0:57 going to do is I'm going to add a photo
1:01 image of that chair and I'm going to
1:03 say, "Hey,
1:06 please make the base of this
1:11 lounge chair into a bright pink that is
1:14 matte and does not reflect much."
1:20 And the reason that I'm doing this is
1:23 because I've generated a tool in Blender
1:26 that can take a predominant color and
1:29 make a selection of all of the
1:33 um polygons in that mesh that might have
1:38 that color applied to it from the UV
1:41 map. Now, that sounds complex and
1:44 actually that's about as
1:46 simplified as I could make that
1:47 statement. Just know that what we're
1:49 doing is we're trying to target
1:52 faces of this object that have that
1:55 brown base color. And we're doing it by
1:59 forcing Tripo to generate a new mesh and
2:03 a texture where the base is pink, and
2:05 that's in heavy contrast to that green
2:09 fabric. And so that will make it easier
2:11 for us to isolate, okay? So I'm going to
2:13 go ahead and download this image.
2:19 Here we go.
2:22 We'll get back into Tripo 3D.
2:32 And let's see, I'm already in
2:35 I guess I need to log in somehow here.
2:37 Let's just get into my links.
2:39 And if you saw it in the previous video,
2:41 the first video in this playlist, this
2:42 is a continuation of that. So if you're
2:44 just watching this as an independent
2:46 video, I would encourage you to go look
2:47 at the playlist that this video is a
2:49 part of. And that's for this model
2:52 generation workflow. And so I'm going to
2:54 get into Tripo Studio. I do have an
2:56 affiliate link in that first video, so
2:58 if you want to help me out and you do
3:00 feel like purchasing Tripo, click on
3:02 that link and you'll get to this and
3:04 then all we all win.
3:05 Um so here's our smart topology mesh is
3:07 what we're going to be utilizing. We can
3:09 see here that I had previously done this
3:11 chair from the previous video. There we
3:13 go. And so we're just going to do a
3:15 brand new one.
3:16 And so let me go back to this smart
3:19 topology mesh, upload, and I'm going to
3:21 find my pink chair this time around. And
3:24 the topology is set to be 5,000. We We
3:27 knew that we could get this at around
3:29 the 2,500 range and have it be pretty
3:31 good, set to triangles, and we'll
3:34 generate that model.
3:38 And so now that the model is generated,
3:40 I am going to generate the texture for
3:42 this model as well. So we're hitting
3:44 about 55 points for this. Again, for you
3:47 know, the amount of times that I need
3:49 assets like this, I'm never going to hit
3:51 my cap on this. I'm not too worried
3:53 about that. So, I just do this kind of
3:55 freely without worrying about it. Um so,
3:57 I would say if somehow you're producing
3:59 more models than me, maybe you might
4:00 consider that. But, if you're not
4:02 producing more models than me, which
4:04 that's the guess is that you're not, uh
4:06 then I would say don't stress about
4:08 hitting these things that they take up
4:09 tokens and and points etc. You're
4:12 probably never going to hit that cap.
4:15 And so, this is generating that texture.
4:17 We'll be right back to it.
4:19 So, there we go.
4:21 Simple enough. So, we already know we
4:23 can do a little export here. We want to
4:25 make sure that, you know, you could do
4:27 um FBX as a file type. That's fine. It's
4:30 eventually going to get re-converted
4:31 anyways. You could do OBJ. That's fine
4:34 as well. I'm just going to do OBJ.
4:35 That'll make it simple. Texture
4:37 resolution set to 1K.
4:40 Go ahead and hit export and target where
4:42 you want to export to.
4:45 So, I'm just going to export to my
4:47 downloads and we're going to fire up
4:50 Blender. And so, I've got a new file
4:52 here. I will say that I have a few
4:54 things set up in Blender that are for my
4:57 preferences. And uh the way that we do
5:00 this is that uh when you first install
5:03 Blender and you first open up a new
5:05 file, you do have the ability to make
5:07 some changes that you can commit back to
5:10 that being your default file. So, one of
5:13 the things that I like is I don't like
5:15 working in metric even though a lot of
5:17 these third-party services are generally
5:20 speaking working in metric. I'm going to
5:22 work in Imperial. That's just my own
5:24 preference. So, that's up to you if you
5:26 want to set up your Blender this way.
5:28 But, how you do that is there's a little
5:30 sidebar menu over here.
5:33 And
5:34 let me preface before I even get into
5:36 that sidebar menu by saying that hey,
5:40 you may feel overwhelmed over the fact
5:42 that this is a new software and you may
5:43 have never used it before. And all I'm
5:46 going to tell you is I'm just going to
5:47 give you exactly what you need to work
5:49 through this. It's up to you if you want
5:51 to continue to learn how to use Blender.
5:53 I've been using it for a couple of years
5:55 now. I've been learning it on the go.
5:57 And I find it to be um a pretty good
5:59 software in terms of my ability to learn
6:03 um it as I go. Uh the resources
6:06 available online. It's all It's all
6:08 there. So, you can learn a lot from
6:11 utilizing Blender for just some really
6:13 basic things. And so, what I have in my
6:16 scene setup and maybe I can just split
6:18 my cam over to the left-hand side so we
6:20 can see this
6:21 is that
6:23 there is a tab here called scene and I
6:25 have changed my unit system to Imperial
6:28 and I've changed my unit scale to this
6:30 scale 0.025400.
6:35 Okay?
6:36 And then once that's done, you can get
6:39 in Let me s- just flip my main camera
6:41 back over here again.
6:43 Um we can get into the file menu.
6:47 And what did we do here?
6:49 Um
6:50 Point now I'm not remembering how
6:51 exactly we do this.
6:54 There is a way to save this
6:56 as your default and I feel like I'd have
6:58 to go look it up again.
7:00 But it was a quick look up was that I
7:02 committed the change that I made back to
7:05 my default file. So, when it opens up,
7:08 it always has this setting set up.
7:11 Um and yeah, and I'm thinking of exactly
7:13 how to do that. So,
7:15 save startup file. There we go.
7:16 Defaults, save startup file.
7:19 And that commits that change.
7:21 So, now that I have that set up, I'm
7:23 going to go ahead and bring this in.
7:26 And I'm going to find my download of
7:29 this. Here it is. There's my round
7:31 armchair. I'm just going to bring this
7:32 OBJ file into here. Drag it right into
7:35 the window and it's going to prompt me
7:36 that I'm going to import wavefront
7:39 object ID. Now, the forward axis and the
7:42 Y axis are actually technically
7:44 incorrect for how we're going to do this
7:46 if we're utilizing Chief Architect. But,
7:48 what I will say about this is part of
7:50 this series is that we're going to get
7:52 into some other softwares such as
7:55 Substance Painter if you really want to
7:57 take these assets to another level. And
8:00 so, I would just say leave these axis
8:02 the way they are and I'm going to import
8:05 wavefront object. Um for me, typically,
8:08 the scale modifier, if I take this up to
8:10 30, it's going to be closer to the
8:12 actual true Imperial dimensions. So, I'm
8:14 going to do that ahead of time.
8:16 And let me press import. So, there we
8:18 go. Now, I have a couple of add-ons
8:22 turned on here. One is in the edit menu
8:26 under our preferences,
8:29 there is a whole section here for
8:30 add-ons.
8:31 And so, something that I searched and is
8:34 kind of part of the Blender package is
8:36 the Bull Tool.
8:38 It's what this is called, Bull Tool. All
8:40 right, so that's one thing. The next
8:42 thing is if you look in the description
8:44 of this video, I will have included a
8:46 link to my Blender add-ons. And I will
8:50 tell you those Blender add-ons are in
8:53 beta. The way they look now, they might
8:55 change. But, their function's going to
8:58 largely remain the same.
9:00 At their base level, I think they're
9:02 pretty good tools. I do see room for
9:05 improvement. So, I imagine
9:07 I'm just going to improve them over
9:09 time. So, you can come back to this
9:10 video, re-download those tools, and
9:13 reinstall them into Blender, and they
9:15 might have improved versioning or
9:17 something like that. So, I will try to
9:19 leave versioning in the name of the
9:22 add-on itself so that we could see what
9:24 version we're on versus what version you
9:26 have installed. That would be pretty
9:27 helpful.
9:28 So, that's something I plan on doing by
9:30 the time that this video gets published.
9:32 Currently, it's not that way. So, what
9:34 you can see here is this comes in as a
9:36 group of a bunch of individual tools and
9:39 then on top of that I said I had the
9:40 bull tool installed. And so in this
9:44 window when we've dragged our object in
9:46 here and it's still selected, that's
9:48 what that orange highlight is about. I'm
9:50 going to hit the N key, okay? As in
9:55 Nancy.
9:56 And this will bring up and tell me what
9:58 the dimensional scale is for this. So
10:00 that if I wanted to get closer to the
10:02 true scale, I could actually come in
10:04 here and punch in those numbers. But
10:07 keep in mind we can kind of do that in
10:09 Chief Architect as well. So it's
10:12 there's a give and take there,
10:14 you know, when we want to get this scale
10:16 perfectly in Blender versus just dealing
10:18 with it outside of Blender.
10:20 And so then the next thing and part of
10:22 just this interface and I would
10:24 encourage you to go look up some just
10:25 basic tutorials on Blender in case I'm
10:28 missing some details here is that at the
10:30 at the top of this interface are
10:32 different ways of shading this mesh.
10:35 And so you can see here there is a way
10:38 to shade this mesh with a material
10:40 preview. And so when we click that on we
10:43 can see our material applied to our
10:45 lounge chair here. So there's that.
10:48 Really bright pink. The rest of this
10:50 actually looks pretty good. And so what
10:52 I get to do from here is when I had that
10:55 N key pressed we can see that we've got
10:57 a bunch of side items here. Some of
10:59 these are some other add-ons that I've
11:01 installed but what you should see if
11:03 you've installed my stuff correctly is
11:05 Rabbit Tools.
11:07 And so in Rabbit Tools if you've
11:08 installed all of the add-ons that are
11:11 included in the folder that I'm linking
11:13 you to then you'll see a bunch of
11:15 different things that you can minimize.
11:16 And the things that you can minimize are
11:18 in all caps, okay?
11:21 Currently anyways at the time of this
11:22 video.
11:24 And so what I have here a couple of
11:27 different tools, one of which is
11:28 material UV paint and then split by
11:32 color picker. And this is going to be
11:34 the main one we're using. And so, I'm
11:37 going to expand this. I'm going to make
11:39 the selection of the object, and I'm
11:41 going to hit a key that's going to be a
11:43 really common workflow thing that you
11:45 do.
11:46 I'm going to hit tab.
11:48 Right now, this object we have selected
11:51 is in object mode. If we have multiple
11:54 objects in a scene, that means we're
11:56 selecting on an object-by-object basis.
12:00 When we hit tab, this takes it into edit
12:03 mode. Default edit mode is going to show
12:07 us vertices.
12:09 If we hit a number two key, that's going
12:12 to make us select edges.
12:14 Okay?
12:15 What's a vertice? What's an edge?
12:17 Vertice is going to be the
12:18 individual points that make up these
12:20 little polygons, all right?
12:23 An edge is going to be an individual
12:24 edge that make up these individual
12:26 polygons. If we hit the three key, which
12:28 is what we're going to hit, that makes
12:30 it so that we can select individual
12:33 faces, just like this, all right? And
12:36 so, with this tool enabled, which is
12:39 split by color picker, we want to pick a
12:43 face that has the color that we want to
12:46 split, all right? Right now, if we were
12:49 to go take a look at this in what would
12:51 be called UV editing, so there's a tab
12:54 for this at the very top, it will split
12:56 your window. It will show the source
12:59 image that's being applied to this
13:02 object, all right? That's the source
13:05 image. If we select a little triangle
13:07 here, we could see where that triangle
13:09 is.
13:10 If we make a big marquee selection of a
13:12 bunch of triangles, you can see exactly
13:15 how this relates to the map that it's
13:18 generating from.
13:20 So, you can see if I select kind of the
13:22 base over here, it's going to pick out
13:24 that Yeah, that's pink. That's there,
13:26 all right? So, that's how this mesh
13:29 relates to that 2D image. So, now let me
13:32 get back to just a modeling workflow and
13:34 I'm going to choose this color here and
13:37 I'm going to select that pink face down
13:39 there.
13:40 And let me hit that N key for Nancy
13:42 again to bring up my side tools, get the
13:45 rabbit tools.
13:46 And so, in this um
13:49 drop down for split by color picker,
13:51 we have the ability to sample
13:55 and my face is covering it, sample the
13:57 selected face. So, I have a face
14:00 selected. I'm going to choose that.
14:02 That's going to load that color match up
14:05 here. And then, I want to select
14:09 matching faces.
14:11 And
14:12 you know, if this is set up well enough,
14:14 it should do a pretty darn good job of
14:17 selecting all the faces we need.
14:20 Now, we're still in that edit mode. We
14:22 can see this in the top of the screen.
14:24 That's why we're seeing individual faces
14:26 here. While all these things are
14:28 selected, we can just right click and do
14:32 something called separate. And so, we're
14:34 going to separate by selection.
14:38 What did that do? That just created a
14:40 new object over here from that
14:42 selection. All right?
14:45 So,
14:46 that part's done.
14:48 The one extra thing that I'm going to do
14:50 about this and this gets into a little
14:52 bit more um of a complex idea of how UV
14:56 mapping and UV textures relating to
14:59 meshes even works is that currently, if
15:03 we were to go hit tab, we're going to
15:06 get back into object mode when we hit
15:08 tab. Hit tab, gets back in object mode.
15:11 We can now see that we have one object,
15:13 two objects. Look at that. All right?
15:16 When I select this second object, if I
15:19 were to hit tab again, now we're just
15:22 that base.
15:24 I can hit A to select all of the faces
15:28 of this base, and I can get into the UV
15:32 editing tab, and we can see where it's
15:34 mapping to this texture.
15:37 Now, we no longer care about this
15:39 mapping to that original texture.
15:41 Really, all we want is in Chief
15:42 Architect, we want to be able to apply a
15:44 wood material to this and have it look
15:47 perfect. And so, what we want to do is
15:50 we want to recalculate
15:53 the way that that UV texture relates
15:57 to those faces. So, what I'm going to do
16:00 here is there's there's several main
16:02 ways that we calculate how automatically
16:06 how we can calculate a texture being
16:08 applied to a mesh. One of which is, I've
16:12 mentioned in some other, you know,
16:14 videos that might be hard to find, is
16:16 that we do what's called a bicubic cubic
16:19 mapping or
16:21 um
16:22 essentially a tricubic mapping as well.
16:25 Where think of it like this, we have
16:27 this mesh
16:29 and let's just say we have a box, and on
16:31 that box is all of our is our texture
16:35 repeated on each side.
16:37 And we're going to shrink that box until
16:40 it hits that mesh, and think of it like
16:42 a shrink wrap. As it hits the mesh, it
16:45 starts to wrap around it.
16:47 That's kind of like a bicubic mesh,
16:50 because when let's just say the top face
16:53 and the and the side face kind of meet
16:55 and hit that mesh and start wrapping,
16:57 then it determines that there's a seam
16:59 somewhere there, and that's where it's
17:01 going to generate a stitch between that
17:04 texture on how it's applied to that
17:06 mesh. So, that would be a really common
17:09 way of getting some automatic UV texture
17:14 map to apply to something and get pretty
17:16 good results. All right, and it's hard
17:18 to explain that without showing it, but
17:20 you can certainly look up some videos
17:21 about by cubic tri cubic mapping.
17:24 Another thing that people do is that
17:28 or we do in the industry is that
17:31 every one of these faces has a surface
17:34 normal. It's the direction that we
17:36 consider it the front face and the
17:38 direction that it's facing out. So that
17:41 if I'm looking at this right along the
17:43 x-axis
17:45 this face right this little triangle
17:46 right here in the front where my cursor
17:48 is, that's going to be you know
17:50 directionally just right on that x-axis.
17:53 That's the degree it's hitting. It's
17:55 basically hitting a um in this case what
17:58 would that be a negative 90 degree. All
18:01 right, that's the direction of the
18:02 normal surface normal. That's the
18:04 direction of the front face where it's
18:06 projecting if we're looking at it from
18:08 the top down. Now if we were to rotate
18:10 around the side, you know, one of these
18:12 is going to be at like a negative 45
18:14 degrees something like that.
18:16 So there is some mapping where we're
18:17 taking an average direction
18:20 and applying a map based on some
18:23 algorithm that's utilizing that. And so
18:26 um what I'm going to do is while I have
18:29 these faces selected, I'm going to right
18:33 click on it
18:34 and I'm going to go UV unwrap faces and
18:38 in this case I'm going to use something
18:40 called smart UV project and it is taking
18:43 that average surface normal direction
18:45 and an angle limit before it considers a
18:49 new face. Meaning that, you know, two
18:51 faces next to each other and they're
18:53 within 66 degrees we're going to
18:55 consider them as part of one face.
18:57 Right, so
18:59 I'm just going to hit unwrap. That's it.
19:01 That's as simple as that. It's a simple
19:03 process. Right clicked and then I got to
19:05 that UV
19:07 and submenu smart UV project and I'm
19:09 going to hit unwrap and see what it does
19:12 on the left-hand side. Has it figured
19:14 out that all those faces on the bottom
19:16 pretty much
19:17 same surface direction, we're going to
19:19 just apply this uniformly, meaning we
19:22 took a wood texture, placed it right on
19:24 top of that, it would apply at that
19:26 scaling, okay? And then the same thing,
19:29 all those individual faces, it's kind of
19:31 figuring out, look, these individual
19:33 faces are almost roughly the same height
19:36 as these triangles are, which means that
19:39 wood texture is going to apply in a
19:41 similar way across everything. This is
19:44 going to look really sharp. How can we
19:46 prove this? How can we make sure that
19:48 this is exactly the way we want it?
19:50 Well, that's now been UV mapped, we
19:53 could switch back to our modeling here.
19:56 You're going to see that, you know,
19:57 obviously that texture doesn't look
19:58 correct now. Let's go ahead and hit A,
20:02 that's going to select all those faces.
20:04 If that didn't work for you, by the way,
20:05 it might just be that you're in
20:07 uh object mode, just remember you make
20:09 your selection, hit tab, that'll get you
20:12 into this edit mode, hit the three key
20:15 to select faces, and you can hit A to
20:18 select all faces.
20:20 Now, with that all done, and we've got a
20:22 selection now, and this has the original
20:26 material applied to it.
20:28 Here's the big thing we need to focus on
20:30 now
20:31 is that because these are
20:34 even though we re-UV mapped the base, it
20:37 still has the original texture applied
20:40 to it. And so, as an object parameter,
20:43 if we were to export this as an OBJ file
20:46 and import it into Chief Architect, it
20:48 would still just be one texture, and we
20:51 couldn't apply a separate texture to the
20:53 base, even though we seem to have
20:55 isolated it. So, what do we need to do?
20:57 We need to assign some new material to
21:00 it, almost like a place marker in this
21:01 case. This is probably the easiest way
21:04 we can do this utilizing Chief Architect
21:06 as our end goal.
21:08 So, in that right sidebar, again, we're
21:10 going to get over to this right sidebar,
21:13 the bottom entry here is material
21:16 properties. I'm going to click on that.
21:19 And we're going to see that there This
21:21 is kind of a confusing menu, in my
21:23 opinion. We're going to see that this is
21:25 that original texture that it's
21:26 utilizing. I'm going to add a slot here.
21:30 And
21:31 I want you to keep something in mind.
21:34 I think that I have an extra step in
21:36 here that I don't need. And it's just
21:38 that I don't know how to reduce that
21:40 step yet. So, for now, this is what I
21:43 know is we're going to add a material
21:46 slide, and we're going to assign a new
21:48 material or, you know, hit the new right
21:51 here. And so, this becomes material. By
21:54 the way, when we export this object and
21:56 import it into Chief Architect, these
21:59 names are what show up in Chief
22:01 Architect. So, it might be nice to come
22:03 in here and say this is
22:06 we want to name it according to what the
22:07 sofa is, which I've long forgotten what
22:10 the name of this sofa is. Let me go see
22:12 if we can figure that out, cuz it would
22:13 be worth our time.
22:15 Laszlo, l a s z l o, okay.
22:20 So, I'm going to name this Lasz
22:24 lo base.
22:26 And the reason I put the name of that in
22:29 there is because down the line, it helps
22:32 you just keep away from potentially
22:35 naming something the same exact name,
22:37 which over time
22:40 some texture might get overwritten with
22:42 another texture if it were the same
22:44 name. It can create a problem at times.
22:47 So, it's a good idea to just put the
22:49 name of the object that you're trying to
22:51 create inside of that material property.
22:54 So, Laszlo base, I'm actually going to
22:56 rename the other one
22:58 Laszlo
23:00 fabric.
23:02 Okay?
23:03 And I have a new material here, but I
23:06 haven't assigned it yet, or maybe I did.
23:08 It looks like I may have done it
23:09 already, but I just want to make sure
23:11 that I'm clicking that assign button.
23:13 It's assigning it to all these. If
23:15 instead I chose the Laszlo fabric and
23:17 clicked assign, you see what happened
23:18 there in our viewport. So, Laszlo base,
23:21 I'm assigning it. There we go. It
23:23 already has a UV map. We got back into
23:25 UV editing, we're going to see there we
23:27 go. That's what's going on. Now, right
23:29 now there's no texture loaded up with
23:31 this, so that if we exported this into
23:33 Chief Architect, it might have a warning
23:35 that says there's no texture. But
23:37 actually, that's okay, and we'll show
23:38 you that in just a second here.
23:40 So, now that I have this assigned to
23:42 some new material, and I like what's
23:44 happening with the material up above,
23:46 this is still fine.
23:48 I'm going to go ahead and export this.
23:51 I set up my hot keys so that I'm hitting
23:54 a similar hot key to what I do in my
23:56 other program, so I'm going to just use
23:57 an a hot key to export. But otherwise,
24:00 for you, you're going to go to a file
24:01 menu, export, and we're going to choose,
24:04 in this case, Wavefront object, okay?
24:08 And so, here's where um this
24:12 dialogue box might be a place where you
24:14 want to add additional places where you
24:16 save things. And because I, by default,
24:19 do not want to save in the documents
24:21 folder, I want to save in downloads.
24:23 I've never been able to figure out how
24:24 to make downloads my default folder. Um
24:27 so, that's something maybe we I learn in
24:29 the future and we discuss, but here we
24:31 go. I'm going to click on downloads.
24:32 This is where I'm going to export this,
24:34 and I'm going to name this that Laszlo.
24:38 And I'm sure.
24:41 Now, I will note that it is nice if you
24:43 keep Blender open because over time,
24:46 when you're doing this, you might find
24:48 out that you may need to make some
24:50 edits. And then one nice convenient
24:52 thing about keeping Blender open means
24:54 that when we go to export, it's going to
24:56 go ahead and retain the settings that
24:58 you did at the last export. And so that
25:00 you just get to overwrite your file over
25:02 and over again, which makes some
25:04 workflow in other software really,
25:06 really easy as we get into
25:08 um some higher-tiered things.
25:12 I know this video might seem like a
25:13 cumbersome process. As you become
25:16 proficient in this, you get to a point
25:19 of getting a very high-level asset at a
25:22 very
25:23 low poly count, low texture resolution
25:26 that looks realistic in 3D in about 15
25:30 to 25 minutes, which that at the time of
25:33 this video is about as fast as I can do
25:35 one of these at the level that I like to
25:37 take them, okay? So, it's not a ton of
25:39 time if you're commissioned and you've
25:41 built in some um
25:44 some good, you know,
25:46 um buffering for creating spec furniture
25:49 versus some furniture that you just have
25:50 in your catalogs.
25:52 And so here we go. I'm going to say
25:54 export this way front object, simple as
25:56 that, and that part's done.
25:58 Now, when I come into Chief Architect,
26:00 and we can see that this was the
26:01 previous version of this that we
26:02 couldn't, you know, apply some new
26:04 textures to, I'm just going to come into
26:06 my downloads folder in this case.
26:09 There's my chair. I like to just drag
26:11 and drop because I know that I will
26:14 re-convert this. And the reason I'll
26:16 re-convert it is because I'm going to be
26:19 um I'm going to end up
26:22 changing the scale of that object. Okay?
26:26 And when you try to change the scale of
26:29 an object as you bring it in,
26:31 um
26:33 it retains its original aspect ratio. So
26:36 that when we do things like add stretch
26:38 planes, if we want to stretch something
26:39 in a particular way, what happens is it
26:42 messes with things because it's
26:44 remembering its original size. That's
26:47 why I always want to re-convert my
26:49 object and add it to my library. So it's
26:52 easy to just drag this in. That makes
26:54 life a lot easier, especially if you're
26:56 in a 3D view, super easy to just rotate
26:58 this 3D, and then also just click on it
27:01 one more time, and you can drop it to
27:02 the ground by using your
27:04 your temporary dimensions in this view,
27:07 and then we can even rotate this.
27:09 We are going to want to rotate this in
27:10 the object itself. So, get to this 3D
27:13 panel, rotate it once,
27:16 so that the front face there we go.
27:18 That's what we're looking for, and then
27:20 of course resize this. Now, what's cool
27:22 about this?
27:24 We know that we have a separate base,
27:26 and it's UV mapped correctly. If we were
27:28 to click on our original and apply a
27:30 wood texture, look what happens.
27:31 Everything's wood.
27:33 If we click on this base and try to
27:35 apply it, there we go. We have a unique
27:37 texture on the base separate from the
27:40 top of this model. That's perfect. And
27:43 what we can do with this model in its
27:45 current configuration, it's not going to
27:47 be easy to apply a new fabric to this
27:50 and have it look really nice. Like, we
27:51 could give that a shot just to show you
27:52 what this looks like. So, I'll try
27:56 just some fabric that I might have in my
27:57 library.
28:02 And
28:03 let me just use my tag system to get to
28:05 that. We're going to just find some
28:07 textiles.
28:10 And try to find some texture here, and
28:13 I'll apply it.
28:14 And so, it will look okay. It will look
28:17 okay, but it won't quite have
28:19 all of the fidelity of the original map.
28:23 And so,
28:25 if we continue in this video series, I'm
28:26 going to show you how to get a texture
28:29 that we can tint in a way that's always
28:32 going to look really, really nice. And
28:34 so, speaking of which, let's go ahead
28:36 and try to tint this. And so, we're
28:38 going to get into the adjust material
28:40 tool. I'll come in here. I'll say, "Hey,
28:43 let's blend this with some texture."
28:45 We're going to change this to maybe like
28:46 an orangish looking couch. We'll see
28:49 what this looks like with the blend with
28:51 texture tool. And you know, it looks
28:53 okay. Doesn't look terrible. Um I
28:55 certainly wouldn't want a monochrome
28:57 looking sofa like this. Maybe we'll
28:59 choose a different color like blue.
29:02 And let's get to the
29:03 Yeah, let's get the light kind of a navy
29:05 blue.
29:08 Yeah, looks okay. It's not bad.
29:11 We're going to continue with this
29:12 particular lounge chair and I'm going to
29:14 show you how to start making this look
29:16 really really impressive. And that's
29:19 when we're going to jump into some other
29:21 software that isn't free, unfortunately,
29:23 Substance
29:24 Painter. And uh
29:26 And
29:27 I find that software so enjoyable that
29:30 it's worth the cost for me even though I
29:31 don't necessarily warrant the cost in
29:33 terms of pure production coming out of
29:35 that software. It's one of my favorite
29:37 softwares to use. So, I chalk that up as
29:41 just a hobby software for me that
29:43 happens to make assets look really
29:45 really impressive like this asset over
29:47 here. Or, you know, if we take a look at
29:49 some of my brand new sofas, I just keep
29:52 getting better over time with my output.
29:54 I'm really proud of the things that I've
29:56 been producing and it's largely coming
29:58 from that software. Let's see if I can
30:00 find a brand new one.
30:03 We'll see if we can pick up.
30:07 Got some that I just man, am I proud of
30:09 them.
30:14 Bear with me. I'll get there. I'll get
30:16 there. I'll get the one I want.
30:21 Of course I can't find them.
30:23 Must have the wrong top tags for them.
30:25 Try this. Show in folder.
30:35 Yeah, looks like I got to update my
30:36 tags.
30:38 You big dummy.
30:45 >> I'm pumping these out like crazy.
30:49 Because I find this process to be really
30:51 enjoyable. Here's maybe one that might
30:52 be a good texture setup.
30:56 Yeah, that's pretty good. Um, you know,
30:59 a lot of what we're seeing here is DLSS
31:01 trying to figure out
31:03 what those textures look like. If I were
31:05 to come in here and up a sample rate and
31:06 turn off DLSS, then maybe we'll get a
31:09 lot more detail coming out of that
31:11 sofa.
31:13 Yeah, some cool little
31:14 things happening. And again, all these
31:17 assets I'm making end up being really
31:19 low poly count. 4,300 for a sofa, that's
31:23 dang low. It really is. I recently redid
31:27 an old one that I built a long time ago.
31:32 Again, really low poly count, and when
31:34 we let this kind of iron out with its
31:38 everything, look at that. You just get a
31:40 lot of detail in the fabric and
31:41 everything.
31:43 Pretty cool. I'm going to show you how
31:45 we can utilize some of the tools I've
31:47 built so that we can do some special
31:49 mapping on pillows and stuff like this
31:51 so that the patterns being applied to it
31:53 always apply correctly. So, stay tuned
31:56 with this series, and let me know if
31:57 you're interested in this. I'm going to
31:58 keep expanding on this. I know that for
32:01 the most part my architectural design
32:03 people
32:04 um don't really care about this all that
32:07 much. This series should still get you
32:09 to building some architectural details
32:11 very easily if you follow along. I know
32:14 that my interior design people, you're
32:16 going to love these videos, so stick
32:18 with me.
32:19 Thank you.
32:42 >> Mhm.
