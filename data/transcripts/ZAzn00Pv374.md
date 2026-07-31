---
videoId: ZAzn00Pv374
title: Creating A Custom Multi Map Texture With Glass And Emitter
url: "https://www.youtube.com/watch?v=ZAzn00Pv374"
status: imported
---

# Transcript

0:01 What's going on VIP? I got a little
0:02 Photoshop action for you today. Um, I am
0:06 going to take this image and make it so
0:09 that it is a material that will be
0:11 applied to an appliance that came all
0:14 mapped out ready to apply materials to,
0:17 but it didn't come with materials. So, I
0:20 took a screenshot and this is a
0:22 combination. This is actually a really
0:23 cool technology. This is made by Smeg.
0:26 It's um the model number is uh SO4606
0:31 WNR
0:34 and it's called the Dolce Still Nova
0:37 Aesthetic line. And what it is is it's
0:39 combination steam oven and microwave.
0:42 And so it does traditional oven, steam
0:44 oven, convection oven, microwave cooking
0:46 allin-one. And it's relatively small.
0:49 So, it's great for um places like New
0:52 York where you got really small, you
0:55 know, footprints in kitchens and etc.
0:58 where you want some combination
0:59 appliances like this. And so, what I'm
1:01 going to do is I'm going to make this so
1:02 that this can be a material applied in
1:04 Chief Architect, but I'm also going to
1:06 make it improve to my standards for
1:09 materials and make this look a lot
1:12 better than you might otherwise see
1:14 from, you know, just downloading this on
1:16 the web or something like that. And I'm
1:18 going to show you how you can do the
1:19 same. So, first of all, I'm going to
1:20 crop these, you know, up to this white
1:23 pixel line here. And something that
1:26 might be a clever way of doing that is
1:29 we could crop based on transparent
1:31 pixels. And we could have made the white
1:33 background just be transparent
1:34 automatically with a couple tricks. Um,
1:37 so the way to do that, and it looks like
1:42 my
1:44 properties got screwed up here. Here.
1:46 There we go. Let me get this layers
1:47 panel. I like to have my layers panel
1:49 docked over here and that way I get on
1:52 the nice long stack because I do complex
1:55 things sometimes. So, I'm going to
1:56 unlock the background layer. I'm going
1:57 to double click it to get into layer
1:59 styles. And I'm going to use blend if to
2:03 knock this down so that white pixels
2:06 disappear and become transparent. And
2:09 then if I just hittrlgr
2:11 e that it just destructively applies
2:14 that effect where and now pixels are
2:16 transparent. And then I could get into
2:19 image and trim and transparent pixels is
2:25 checked on. Trim away. There we go. Let
2:28 me press okay. And look what happens
2:31 now. By default, my crop settings were
2:34 set to delete cropped pixels. that means
2:37 that there's no other pixels beyond
2:39 this. So, um, that's great. That did
2:41 exactly what I wanted it to do. So, that
2:43 was a really easy way of accomplishing
2:44 that task. Um, next thing that I'm going
2:47 to do is I'm going to use the marquee
2:49 selection and I'm going to just
2:52 highlight this. But before I highlight
2:54 this, I want to do a couple things. I
2:56 want to keep this little button feature
2:57 right here. So, I'm gonna just select
3:00 this guy. Okay. And we're gonna kind of
3:04 do the same trick we just did. I've got
3:07 that selection. I'm going to hitt
3:09 controll J, which copies that forward as
3:11 a little layer. And then if I were to
3:14 just um I'm going to add a solid color
3:19 background. This will just make it
3:21 really easy to kind of see what's
3:22 happening as I do it. So the solid color
3:25 that I'm going to pick is just a bright
3:26 color. Okay. And I'm going to bring that
3:28 down a layer. And why am I doing that?
3:31 because I want to get in close to this
3:32 so I can show you exactly how this is
3:35 going to work here. Okay. So, what I'm
3:38 going to do is I'm going to invert this
3:42 for now. Let me just control I. I just
3:46 inverted the colors. Okay. And then I
3:49 might do a levels change. CtrlM brings
3:52 me up the levels. I'm going to take the
3:55 medium gray pixels in this shot and I'm
3:57 going to make them darker. I'm going to
3:59 take the kind of white to not quite
4:01 white pixels and I'm going to make them
4:03 lighter. All right. And you can kind of
4:05 see what's happening here is I'm
4:08 somewhat isolating
4:10 that little set of pixels there. All
4:12 right. Now, with that in place, I can
4:15 double click the layer style and do the
4:17 same thing we just did, which is use
4:19 that blend if to get rid of everything
4:22 but just those black pixels, which is
4:24 all I was trying to keep anyways. All
4:26 right. and then Ctrl GRL E to stamp it.
4:30 Now that's we've destructively gotten
4:32 rid of everything else that was there. I
4:35 to invert it and I'm back to having that
4:37 I can get rid of this little color
4:39 layer. There we go. Now I have that as
4:42 just its own little icon that I'm
4:43 retaining. The reason I'm doing that is
4:47 I want to get back to the base layer and
4:49 make a selection here. And what I'm
4:50 going to do is I'm going to CtrlJ this
4:54 to copy that to a new layer. CtrlT for
4:58 transform. And then in this bottom I'm
5:01 going to reflect this. Flip it
5:03 horizontal. And I can drag it over to
5:06 this other side. And what did I
5:08 effectively do by doing that? I'm
5:10 getting rid of this reflection right
5:12 here that we don't actually want. All
5:15 right. So, we're getting rid of that
5:17 fake reflection and committing that
5:19 change. And then the last thing that I
5:21 can do is brush tool, sample this pixel
5:24 color, knock that out. And we still have
5:26 that icon in place. Awesome. This is
5:29 looking really good. Next thing was we
5:31 want to stamp this down. Why not? Let's
5:33 just get super destructive with this.
5:35 So, control E will stamp this down to
5:36 the layer below. And then M to get my
5:39 marquee selection. I can marquee this
5:42 handle. And we're actually going to need
5:45 this handle. So maybe I'll controll J it
5:47 forward. But then let's go back to that
5:50 original one. Let's toggle the display
5:52 of this layer so we're not seeing it
5:54 anymore. Let's hit control and that
5:57 layer to get that selection back. And
6:00 now we can just hit the remove button
6:02 here, which is going to do a generative
6:04 remove. For this, we probably could have
6:07 just filled this with a solid color.
6:08 That probably would have been okay as
6:10 well. Um, but I was just showing you for
6:12 more complex things where we want to
6:14 remove something, you could re use that
6:16 remove feature. Um, it does take longer.
6:19 We could have just filled it, right?
6:21 Would have been simple. So, this is
6:23 going to be my base diffuse map. The
6:25 last thing that I kind of want to note
6:27 is that this is transparent. I'm not
6:29 sure how that's going to work with the
6:31 model when we try to apply it. We'll
6:33 see, but we might have to make an edit
6:35 there. Now, this is just going to be my
6:38 base diffuse map. All right. What does
6:42 that mean? This just means this is the
6:44 color map. We are going to do some more
6:46 advanced things coming up, and I'm not
6:48 entirely sure how I'm going to do it,
6:50 but we'll get there. So, with this in
6:53 mind, let me export this. Ctrl Altshiftw
6:57 gets us an export dialogue box where we
7:00 can export this as a PNG. Let's uncheck
7:03 uh actually we're going to keep
7:04 transparency checked in this one. Export
7:07 this image. 1300's really high. Um maybe
7:11 we want to limit it to 1080. Just keep
7:13 in mind that we're going to have to do
7:14 that every time forward from here. And
7:17 maybe we just commit that change to the
7:19 image itself. Let's export this. I'm
7:22 going to export it into my downloads
7:24 folder where I rename this specifically.
7:27 Diffuse is a great way to rename this.
7:30 Um, but I'm also going to add a few
7:32 notes in here. So, this is going to be
7:34 uh dolce still
7:37 nova
7:39 um oven and then there we go. And then
7:43 we want to add diffuse. There's a very
7:47 big reason for doing that. Um it's for
7:51 we have a lack of tools in the asset
7:53 manager and chief architect. So if
7:55 you're trying to do a batch replacing of
7:59 images based on names, then you should
8:02 have a suffix for each name cuz
8:04 otherwise it might find something that
8:07 has a suffix such as your bump map or
8:10 roughness map where the first part of
8:12 the name is a match to your search term
8:15 and you're trying to do some kind of
8:16 automatic batch replacement. That sounds
8:19 complex. Ask me how I know. Just trust
8:22 me, bro. add the diffuse part at the end
8:25 of the name. I was not doing that for a
8:27 couple years and it's caused me
8:29 problems. All right, so there we go.
8:31 Now, I do have a script running on my
8:33 downloads folder. It's automatically
8:35 picking up any PGs and converting it to
8:37 a WEBP format. That is on purpose. And
8:41 so, um, what that means is that I'm
8:45 going to load up a WEBP, which is going
8:46 to be a much more compressed image file
8:49 type. And so here is the base image that
8:52 I created. But all I did was go, you
8:54 know, rightclick, new material. Okay, so
8:58 here's my new material that I started
8:59 on. Let me open this object and let's
9:02 import
9:04 our texture map, texture source map. And
9:07 so I'm going to get to my WEBP folder.
9:09 And dang it, it didn't seem to be
9:11 running, which is strange. And it should
9:14 be. Let me make sure that thing is
9:16 running so it does its job.
9:22 Run, baby, run.
9:30 And there we go.
9:36 Okay, the next thing about this is it's
9:38 going to just be set to stretch to fit
9:40 in both directions. And let's press okay
9:43 for now. and let's apply it front face
9:47 of this thing and see what it's looking
9:49 like now. Okay, so there's a couple
9:52 things
9:54 and going wrong here which I assumed
9:59 incorrectly. These are mapped the exact
10:01 same way. They're mapped
10:05 unfortunately.
10:09 Um, unfortunately they are mapped with
10:12 the little gold features top and bottom.
10:18 And what else is happening there? And it
10:22 must be just like a stretch to it's not
10:24 stretch to fit's not going to work. They
10:26 actually map this in a way that's like
10:28 tiled. So, in the Y scale,
10:32 boy, this is just going to be kind of
10:34 like a guess and check. No, it's not.
10:36 We're going to use the interactive
10:38 material editor tool,
10:42 which is telling me it can't be used on
10:46 this, which what does that mean when it
10:49 can't be used on something?
10:53 That's a good question. Why it can't be
10:55 used? because stretch to fit is enabled
10:57 in one axis, I guess.
11:00 So, let's try that again.
11:03 Yeah. See, now it works. Interesting.
11:07 So, we're going to slide this over. Look
11:09 at that. It's actually flipped,
11:12 which is which is very strange.
11:16 And if we stretch this, what do we get?
11:20 We stretch this.
11:23 Where is that based on? It's based on
11:24 where I clicked. Interesting. I actually
11:26 did not know that. So, that's a good
11:29 good thing to know.
11:32 Um, it's so strange that this is
11:34 flipped.
11:36 So, in the base object,
11:39 it might be that I need to get into the
11:41 3D panel and invert the surface
11:44 direction.
11:46 Does that change the fact that it's
11:48 flipped? No, it does not. So, I'm going
11:52 to click down here, and I'm going to try
11:54 to get this all freaking right. So, we
11:57 want to we want to slide this over.
12:03 And then we want to resize.
12:06 What's it resizing based on? Now,
12:09 I want to pin a spot that it resizes
12:12 based on. So, um,
12:20 boy, it's very hard to to use this tool
12:23 in a way that makes sense to me right
12:24 now. Let's see. There we go. Now, it's
12:27 resizing based on that point. So, should
12:29 be able to boy, how confusing.
12:34 We want this edge right at the right at
12:38 the bottom corner is what I'm looking at
12:41 there.
12:43 tool again right on that edge.
12:47 Now, there we go. So, if I scale this
12:52 up,
12:53 what am I getting
12:56 now? We're talking.
12:58 Doesn't that look just about right? Yes,
13:02 it does. Very cool. Let's paint this
13:05 little gold here.
13:09 Interesting. It's painting the handle
13:12 gold and it shouldn't be. So, this thing
13:14 is not mapped correctly. Dang it. And
13:16 I'm probably gonna have to put a face in
13:18 front of that to get that to work right.
13:21 And then it does seem as if somehow part
13:25 of this got flipped around the right
13:28 way,
13:30 which is strange, right?
13:35 But if we just switch to little Rage
13:37 Race view, what's this looking like?
13:39 Yeah, it's not looking too bad so far.
13:42 So, let's do some next steps. We're
13:44 going to battle through this. Um, I do
13:46 not feel like remapping this, so we're
13:48 just going to deal with what we've got
13:49 here, which is not not perfect, but
13:52 maybe not the worst thing either. Um,
13:56 we might
13:58 take a look at what happens when we use
13:59 the delete surface tool. Look at that.
14:00 Right behind is
14:03 some kind of a mapping that looks like
14:05 it's the correct mapping. And then,
14:08 what's this? Is this backwards as well?
14:09 This is backwards. And right behind it
14:11 is forwards.
14:14 So the normal direction of this object
14:16 is not great. Um,
14:21 if I
14:23 invert surface direction, I'm going to
14:25 try to replace this geometry again with
14:28 the original geometry
14:31 and then switch this to
14:34 millimeters as the unit of measurement,
14:36 which it was.
14:42 And did that invert geometry work? No,
14:45 it did not. So, that image is flipped.
14:48 Very strange. Yeah, not a whole lot I
14:51 can do about it. All right, so let's get
14:52 back to Photoshop. Let's start doing a
14:55 couple things now. I want a couple of
14:57 these items to be become transparent.
15:00 Uh, first of all, let's go ahead and
15:08 commit this change down. That blocked
15:11 out the handle. And then we're going to
15:14 um we're just going to copy this
15:16 forward. So full control J on the on the
15:18 layer so that we can start messing
15:20 around with this. And we know that the
15:22 metal pieces are actually mapped
15:24 correctly. So that's fine. We could
15:25 leave those alone. The things that we
15:28 want to light up are going to change.
15:30 And then I'm looking at the the source
15:33 image of this thing.
15:35 And if I were to take a guess,
15:37 it looks like there's a viewing window.
15:39 And I'll show you where that is. I think
15:41 the viewing window is
15:46 roughly in this area.
15:50 So there's glass
15:52 in kind of this area. And actually, I
15:55 think it's more like this. So we're
15:58 going to do that. We're going to set
15:59 this to be um glass in this case.
16:07 Yeah. And it'll just be a dark glass.
16:11 Okay. So, how do we do that? I'll show
16:14 you. Um, one, I'm going to draw out a
16:16 ruler just by um, in my view, I have
16:20 rulers turned on. I get to hover over
16:22 that ruler, bring this out, and it will,
16:24 if we have snaps turned on, it snaps to
16:26 that midpoint. So, there's my midpoint.
16:30 So if I wanted to, I could draw things
16:34 based on that midpoint.
16:36 And so I'm going to draw out another
16:38 ruler guideline for where I kind of want
16:41 my window. And then same thing, do one
16:45 more kind of where I want that window.
16:51 Something like that, I think.
16:58 And I'm just looking at the picture for
16:59 a source. There's no real great way to
17:02 do this otherwise. Um, so then I'll use
17:04 just the brush tool and we're going to
17:06 go I'm going to go brand new blank layer
17:09 and I'm going to stick a layer
17:10 underneath here that's another solid
17:12 color fill. And I'll make it white.
17:15 Okay. And so on that blank layer, I'm
17:19 going to turn on our
17:22 uh symmetry and I'm going to reflect
17:26 this horizontally, excuse me,
17:29 vertically, right down the center. Bam.
17:31 Hit done. And then with my brush tool,
17:36 well actually this tool first, we'll
17:39 just snap our selection right to there.
17:42 Then brush tool or even fill tool if you
17:45 want. brush tool works better for this.
17:47 Um, is that I'm just going to paint on
17:49 black right here. Bam. Just like that.
17:52 Now, what's the problem here? Well,
17:57 um, I went about this the wrong way. D
18:00 to deselect. We'll just get this sloppy.
18:02 We're just going to draw this out
18:04 sloppy. This will be a lot easier.
18:11 I just wanted to make sure that
18:15 I was able to
18:17 get this right on the line here. So, I'm
18:19 using the erase tool, holding shift, and
18:21 racing right on that line. This is This
18:24 is easy enough. We'll just do it this
18:26 way. My brain's not working that well.
18:30 So, what is this? This is my
18:32 transparency map. When I go export this,
18:39 make this 1080 as well,
18:45 right? Oh, and we got a problem. We have
18:47 a layer turned on up here. We want that
18:49 off. Let's export this again.
18:55 1080. It actually be 768. Let's make it
18:59 reduced.
19:02 We're going to pick this same name. And
19:04 we're going to change that end.
19:07 I call it before. I called that a
19:08 prefix. It's a suffix, you big dummy.
19:11 And then transparency.
19:14 Okay.
19:16 What does that do? What do we get out of
19:18 that? Let's go edit this material.
19:22 Get into the properties panel.
19:25 Um, in transparency,
19:29 we want transparency map right here. So,
19:31 we're going to hold shift, import. Let's
19:33 find that transparency maps right here.
19:36 Webpool.
19:39 Um, did I do that backwards? It looks
19:43 like I did it backwards.
19:45 That's okay. That's a quick fix. How do
19:48 we fix that? Let's
19:51 um group these two together.
19:54 And you guessed it, stamp. So, GRL E.
19:58 You stamped it. I invert it. Control
20:00 altshift W. Export it. transparency.
20:04 Set this back to 768 again. Um, will
20:09 this I think my
20:12 my current script will not overwrite
20:16 an existing. So, I'm going to go into my
20:19 WEBP folder and delete that just in
20:22 case. All right. So, export
20:27 and also going to delete this
20:33 Oops. What happened?
20:36 Oh, this is a new new glitch that I just
20:38 Okay, there we go. Um,
20:42 yeah, I want to replace it because it
20:43 didn't exist.
20:47 There we go. It just showed up in my
20:49 webp folder. So, we should be able to do
20:51 this. Should be able to do select,
20:58 replace with. And here we go.
21:02 So that just flipped that. Perfect.
21:05 Perfect. Perfect. And so what happened
21:07 there? There we go. We've got a
21:09 transparent surface there. Technically
21:12 that's actually seeth through back to
21:15 the layer behind it. Now if we're
21:17 getting clever, we could
21:20 come in here and use the delete surface
21:22 tool until the point where we can see
21:24 through this thing.
21:30 What did that get us? That got us to
21:32 there. What happens now? See, now you
21:35 can actually see through it. If you had
21:36 a light in here, you would see right
21:38 through. See? And so when we convert
21:42 this, it might be worth it to delete
21:44 those surfaces.
21:46 We'll see how how we feel like that
21:49 turns out. Okay. Uh what's up next?
21:52 Let's figure out how to light some of
21:54 the controls up. So, we can turn this
21:56 group off. Let's look at the controls.
22:00 Okay.
22:01 Simple enough. Um,
22:05 I already control Jade a copy forward
22:08 that we can mess around with. So, we
22:10 want to isolate some stuff. So, really,
22:12 um, this is going to be simple because
22:14 we just get to grab this color and start
22:16 painting some stuff over the top of this
22:17 real loosey goosey, right? We can just
22:20 paint right over the top of all this.
22:22 That's going to be just fine. We might
22:25 want to light up that
22:29 that power button. What look like what
22:31 looks like a power button. And
22:35 I think we could leave most of this
22:40 off. Maybe we'll just have the power
22:42 button turned on. And I'm not sure about
22:44 this top white section. Maybe we'll also
22:47 have just that top white section turned
22:49 on.
22:51 Um, let's make sure that we're using a
22:53 true black here.
22:57 There we go.
22:59 And before we do that, let's do a little
23:04 levels edit. So, we'll just take this
23:06 down to black and we'll take anything
23:07 that was kind of gray. We get in here
23:10 real tight.
23:12 Um, we might even be able to just
23:14 target. So, this is the targeting tool.
23:16 So, you take this
23:20 Drag that up. There we go. See how that
23:22 just lightened up like that.
23:30 There we go. Lightened up a bit. Some of
23:32 this stuff.
23:34 This color range is too close. Let's
23:37 just do a second round of this. Crl M
23:40 again.
23:54 Boy, it's just such a subtle
23:57 subtle little difference here.
24:00 Um, we could do image adjustment replace
24:03 color. It's another method for this. So,
24:05 we could just take the lightness down
24:07 there. Keep our sample clusters down.
24:09 There we go. So, now um how does this
24:12 work? what's lit up and what's not. I I
24:15 can never remember. So, I think that
24:18 uh before for our transparency, white
24:21 was the thing that's transparent. So, in
24:23 this case, white should be the thing
24:25 that's the active activator, right? So,
24:28 this should be correct. Let's throw this
24:31 down to
24:33 um because we're dealing with small
24:34 details, let's leave it at 1080.
24:36 Uncheck transparency in this case. Press
24:39 okay. Click on this guy and we're going
24:42 to change the name of this to
24:46 um opacity or emitter.
24:52 Get back into chief
24:54 use our adjust materials dio
24:58 in the property emissive map. Here we
25:01 go. So, shift, select, import,
25:04 and
25:09 and so if it's dark outside, like your
25:11 sun's turned off, is that thing lit up?
25:14 Well, not much. Um,
25:19 what did I do wrong? Should be an
25:21 emissive property to this now. Missive
25:24 map. Oh, there we go. This would be
25:28 helpful. Average light bulb. Look at
25:30 that. Bam. That thing's lit up now.
25:32 Isn't that cool?
25:35 There we go. Turn that off. It's lit up.
25:41 There's some pixelation here. So, got to
25:45 clean up. There's still some stuff
25:46 that's not quite 100% true black. That's
25:49 what's happening here.
25:52 So,
25:53 image adjustments, replace color. Let's
25:56 get this medium gray. Very, very light.
26:00 And there we go. Something like that.
26:03 Let's get that nice and bright. Let's
26:11 get this kind of black deal here. Get it
26:14 nice and black. Let's add to this
26:16 selection to get these medium gray spots
26:19 out of there again.
26:24 There we go. We forced them black. Let's
26:26 do that one more time.
26:30 Get this this back to lighting
26:37 this up.
26:42 I think it's okay.
26:44 Let's see if that helped our situation.
26:46 Let's go reexport this. I'm going to
26:49 leave it at 1300. Why not?
26:53 And I'm going to see if my tool will
26:57 replace this.
26:59 Does it? It does. It just puts a little
27:01 prefix here.
27:08 Remove
27:10 back to chief.
27:15 We have we have min. Select it. Replace
27:20 replace with. Yes, we're going to
27:22 replace it even though it's in some
27:24 something is what it's asking.
27:27 Okay. Have we updated it? And did that
27:29 clean it up a little bit? Let's see when
27:31 we turn the lights off. Yeah, that looks
27:33 a lot cleaner. Ain't that cool? So, this
27:37 is looking good. We just know that that
27:39 part, this one part's kind of inverted.
27:41 The texture is inverted, right?
27:44 Would have been nice if we fixed that in
27:46 the model itself.
27:49 Um,
27:51 could I do that? Yeah, we could do that.
27:55 Do I want to? No, I still don't want to.
27:58 Uh, all right. So, now the next part of
28:01 this is let's pull a little
28:05 elevation on this bad boy.
28:10 Let's stick a face in front of this
28:12 thing. Huh? Let's use the face tool. Why
28:15 not? It looks like we might have some
28:16 points we could snap to. There's a
28:18 point. There's a point. Here's a point.
28:22 Here's a point. Click it twice.
28:26 And you should have a face there. Um,
28:29 you might not see the face because it's
28:32 in plane with the other object. So,
28:34 contain selection mode. And I did select
28:37 the face and I'm going to drag it
28:39 forward. And while I'm dragging it
28:41 forward, I'm going to hit tab. And I'm
28:42 going to say 132th of an inch. And let's
28:45 see what happens. Did I get a face?
28:49 Doesn't look like it. Oh, it's down
28:51 here. This is an old old old chief
28:54 architect glitch.
28:57 Dang it. And let's see this
29:00 cross-section again.
29:02 So, um, how do we want this? We actually
29:05 want this to be ding to
29:10 Oh, we're just going to get real in
29:12 tight here because it's not going to
29:13 pick up my snap. So, light ping.
29:18 It looks like the model's a little out
29:20 of square. Poor modeling, my friends.
29:22 Poor modeling.
29:24 And what will we do? We're just going to
29:27 apply just a straight texture to this
29:29 thing. So, um, I've got a solid matte
29:33 here color. I'm just going to paint it
29:34 matte white and then adjust it.
29:38 So, instead, we're going to pick and say
29:45 this is
29:48 this color.
29:50 Something like that.
29:55 There we go.
30:00 And
30:02 it's
30:04 gray.
30:06 We'll put just a little bit of less
30:09 roughness on it.
30:14 Cool, cool, cool, cool. We are getting
30:17 there. That's getting really close.
30:19 What do we got to do next? Um, it would
30:22 be nice if we kind of set this up, you
30:25 know, for our reflection with this being
30:28 kind of a metal thing,
30:32 but it's not the worst thing in the
30:35 world if we just generically add some
30:37 more reflection.
30:43 Yeah, I'm not opposed to that. Um, we
30:46 could use a reflection map where we're
30:49 showing that our our glass is far more
30:53 reflective than something else.
30:58 Or I bet you if we just crank the
31:01 reflection up a little bit, that
31:02 probably looks pretty close. And because
31:04 we have this texture already 132nd in
31:07 front of that other piece, we probably
31:09 paint that.
31:11 Yeah, that is dang near there. How do we
31:13 deal with this thing UVM mapped in
31:18 reverse? Well, I'll show you how. I
31:22 didn't want to have to do this, but why
31:23 not? Let's get into Blender.
31:27 Fire this bad boy up.
31:33 And so,
31:36 what do we have? We have OBJ.
31:43 port right front OBJ. This is going to
31:45 mess up the scale of this thing a little
31:47 bit. Um, we're going to change our
31:49 shading up here in the top corner
31:52 so we can see the textures applied to
31:54 it, which the textures are missing. Um,
31:57 and we can see that the B, you know,
31:59 this thing is flipped. Z-axis, all that
32:02 stuff's all flipped. Um,
32:05 with this selected, I've got some tools
32:08 to be able to do a little bit of
32:10 rotation. So,
32:13 there we go.
32:18 And then let's kick into the m scenes
32:22 materials.
32:24 And what do we have here?
32:27 If we open up this object and we look at
32:30 materials, material one is just the
32:33 black texture. What's the texture that's
32:36 really cool? Is material 4. Okay. So,
32:40 for material 4,
32:43 here's where
32:45 um we're going to say that this is an
32:48 image, not
32:51 not what they've got here. Um, and I
32:54 can't remember how to make this an
32:55 image, but I believe that I click on
32:58 this little dot in the base color that's
33:00 right behind my head. Dang it. Let's
33:02 just do a no cam. So, um, this base
33:07 color, yeah, you click on this little
33:09 yellow dot and you're able to do a
33:13 texture, image based texture. And so
33:16 then you want to open that texture and
33:18 find
33:20 a little web peak guy here.
33:24 Use
33:26 what did that do? Nothing. Remember
33:28 because it's scaled wrong?
33:32 Dang. It doesn't really help us, does
33:35 it?
33:39 Doesn't really help us. But what I could
33:43 do to just help this whole situation
33:46 is
33:49 let's tab in
33:52 and
33:56 select some things
33:59 to figure out how this is mapped.
34:04 I just want these front faces, but it
34:06 looks like this thing's all
34:08 all beat up.
34:11 So I do have a utility in my tools
34:16 that can pick based on a color. And so
34:19 for this material for let me actually
34:21 remove this. Let me go back to a color.
34:26 Color color color
34:32 is How do we even do that? I'm not sure.
34:39 Yeah, there we go. I made it a pink
34:41 color. And so I have a tool that if I
34:45 switch to the number three key, which
34:47 gives me faces, right, there's a face.
34:49 There's a face. So these are the faces.
34:53 I can see where that material is
34:54 applied. And
34:57 I've got a
35:00 split by color picker is what we're
35:03 doing.
35:04 So sample selected color. Bam.
35:08 Select matching faces.
35:11 Oh, let me try again.
35:14 Sample selected face.
35:17 Sample selected face. No image texture
35:20 node found.
35:23 Image texture node. H.
35:27 Well, I don't know how I wrote this
35:29 thing.
35:31 Feel like it's not working for me.
35:39 Really, it looks like it's just this
35:43 this this
35:46 right
35:48 that all that's mapped. It also looks
35:50 like there is the control panel is
35:52 behind this
35:55 and they built that so that the control
35:56 panel could be mapped separately to a
35:59 separate image which would have been
36:00 really nice.
36:02 Yeah. So, if we get into
36:06 UV editing for that, for those
36:09 selections,
36:18 if we just did a
36:21 UV unwrap
36:23 and then project from view,
36:26 that that should be all that we're doing
36:28 here. Now, it's interesting that it
36:31 looks like it's selecting two triangles
36:32 here.
36:34 UV unwrap.
36:37 Oh, that was just my selection. There we
36:39 go. Yeah, that's it. So, if I were to
36:42 export this
36:46 as a new object in my downloads folder,
36:52 whatever the heck this is called
36:59 oven
37:01 and
37:04 the axis is going to be all screwed up.
37:06 That's okay. Scale is going to be messed
37:08 up, too. That's okay. We'll fix that and
37:12 chief. So if I open this, let's just
37:15 note
37:17 that the width is this 23 and a half.
37:20 We're going to replace this object now.
37:23 See what happens.
37:32 So far, all we needed to do is rotate
37:35 this this way and then retain aspect
37:38 ratio. paste that width
37:43 symbol
37:45 generate the block. Okay. All right.
37:49 Now, the mapping's wrong. We know that.
37:52 We knew that was going to happen.
37:55 So, we're going to
37:57 get this back in place. Rescale it.
38:03 Um,
38:04 we need
38:08 this tool again. Hit this little bottom
38:10 edge
38:14 so that it comes down like this.
38:25 Scale's a little off.
38:37 Okay.
38:40 Again,
38:49 it's finite scale detail. There we go.
38:55 Oops.
38:56 I don't know how this tool works.
39:01 Where does it pick its its point from?
39:05 I want to scale based on this corner
39:14 and it just jumps immediately. I wish it
39:17 it really did scale based on the point
39:18 that you're picking. It doesn't seem to
39:21 do that.
39:24 Isn't this frustrating? I'm learning
39:25 with you, by the way.
39:28 So
39:30 yeah, this is this is extremely
39:32 difficult to do because of this way it
39:36 scales. Let's see if we could go the
39:39 opposite way. Maybe we could get the top
39:41 corner
39:45 and scale it that way. That doesn't seem
39:48 to be very intuitive either
39:54 because I'm overcaling now.
39:58 Yeah. You know what would be helpful is
40:00 if we just knew the size of this thing
40:02 and we'd plug that in. Wouldn't that be
40:04 Wouldn't that make a lot more sense?
40:06 That make a lot more sense.
40:08 Height 17 and 1516. Let's go fix this
40:12 stupid texture.
40:16 So, what's this texture going to be?
40:17 It's going to be overall height. This
40:20 should be,
40:22 I would think,
40:26 That's the Y scale. Overall width should
40:30 be that 23 and a half.
40:33 And let's zero these out.
40:36 And see what happens. Yeah, that's way
40:39 out of scale. So,
40:44 how challenging way to ruin a video,
40:46 rabbit.
40:51 So if that's the scale, why is it like
40:54 five times the size?
40:57 Obviously that texture scale is not
41:00 directly coordinating
41:03 with this.
41:05 Clearly it's not.
41:09 Um which just means that the UV map is
41:11 not one one for the import scale. So
41:15 it's some kind of conversion issue.
41:24 So, is that the bottom corner? Yeah, it
41:26 is.
41:29 Wouldn't it be nice if this tool worked
41:31 so that I could rescale from this bottom
41:34 corner and lock in and keep it from
41:37 moving on the left side?
41:41 That'd be nice.
41:50 Yeah, I feel like this tool is upside
41:52 down.
42:09 Well, I'm going to be at chief
42:11 headquarters here pretty soon. So, I'm
42:12 going to ask him, what was the intended
42:16 way that this pins itself?
42:19 Like, how can we use it and make it so
42:21 that it pins?
42:23 That's what I want. Boy, this is getting
42:26 close just by guessing and checking. But
42:29 man, what a pain.
42:32 And why can't we just tap this up,
42:34 right?
42:38 You think those dimensions were exactly
42:40 half the size? It kind of seems like it.
42:48 Yeah, I can't tap the arrow key to go
42:50 up, which would have been really great.
42:53 You can use tab input, but
43:02 what a pain. And then when this gets
43:04 placed, I'm hoping that that locks
43:08 itself.
43:10 But oh, that's really close now.
43:14 Really, really close. I think I'm going
43:15 to leave that. Boy, what an exercise.
43:21 So challenging.
43:24 Okay, how are we looking now? This is
43:27 looking pretty good. I think I want to
43:29 darken this color a little bit.
43:39 But for the most part, yeah, that's
43:41 looking pretty good. Do we want to move
43:43 this face like 164th?
43:47 Maybe we could use transform, replicate,
43:49 move this in the Y leg 164th.
43:55 Yep, that still works out just fine.
44:00 Yeah.
44:03 So, let's grab this and
44:07 convert it to a symbol. What's it going
44:09 to be? It's going to be a fixture.
44:10 That's correct. Add library. Show
44:13 advanced options.
44:16 Um, let's kick this around. I'm not sure
44:18 why it was facing the wrong way.
44:19 Shouldn't have been. So, that's what
44:22 that looks like there. What else can we
44:25 do here?
44:27 We can
44:29 say that in the options
44:32 this does insert into a cabinet front
44:35 and we need to offset it based on
44:39 Oh, good question. Should have done some
44:41 dimensioning. So, the overall depth is
44:44 24 and 532.
44:47 So, we're going to say that
44:51 this is minus oh, let's see 2 and a half
44:55 inches or something, I'd say. We'll
44:58 double check that shortly. This is
45:01 appliance builtin
45:06 built-in base cab. Um, you might be able
45:08 to put this in a base cabinet. So, I'm
45:09 going to say go ahead, you know, and
45:12 then let's press okay.
45:15 Let's throw a base cabinet in here so we
45:17 can just test this out. Or excuse me, a
45:19 full height cabinet. That's what I want
45:21 really ultimately. And so, bam. Do I get
45:26 to place this? Oh, I got the wrong
45:29 direction, didn't I? Let's open this up
45:31 and get this right. So, this is going to
45:34 be negative front offset negative.
45:38 Hover over. Click and replace. Now,
45:40 here's the problem with this mapping.
45:42 Look how it moved. That's because
45:45 it's
45:47 based on a coordinate system is what
45:49 those offsets are.
45:52 So,
45:54 how do we fix this?
45:58 We set this to global symbol mapping.
46:01 Does that fix it? No, does not. In fact,
46:05 it makes it a lot worse. Um, global
46:08 symbol mapping is maybe where we would
46:10 have been able to plug in the correct
46:12 dimensions again. Let's try it.
46:18 I'm relearning some stuff here.
46:34 Yeah, this is uh that looks like it's
46:36 the correct dimensions now with global
46:39 symbol mapping. Basically, it's reuv
46:41 mapping. So, all we need to do is fix
46:45 this. And now we've got the correct
46:49 look. Isn't that great? Now, look what
46:52 happened. It inverted this thing again.
47:00 Oh, dang it. Dang it. Dang it. Dang it.
47:04 So, let's go back to our original
47:06 symbol, I guess.
47:10 Oh, that's funny. I should have thought
47:11 about that. I should have known that.
47:15 Oops.
47:18 This is millimeters. This is
47:23 Reset
47:28 object size.
47:31 Yeah,
47:33 that looks
47:35 correct. Did this invert? We don't know.
47:42 Surface direction. Let's press okay.
47:45 There we go. Now we're back to the
47:47 correct symbol.
47:51 Okay. So, let's take this and convert it
47:54 one more time. So, we're going to take
47:56 these two. Let's see. Make sure I'm
47:58 selected this. Control select the other.
48:00 Oops. Like this. Control select that. We
48:03 got both together. Convert it. This
48:06 appliance. Let's get the name right on
48:08 this, which is
48:11 smag multi. Oops. Smag multi.
48:18 Um
48:21 heck this is called multitech
48:24 oven
48:30 man what a what a what a lot of names
48:32 going on here. No.
48:39 Yeah. Microwave as well.
48:43 Uh uncheck the invert surface direction.
48:46 Let's get a preview of this. Make sure
48:47 it's still looking good. It is.
48:52 Yeah. 2D symbol should have been
48:55 automatically generated. Options panel
48:58 front offset negative. Uh what was it?
49:03 This minus what did I say? Minus three
49:06 or actually in this case + three.
49:10 Let's try that out. And then click hover
49:13 replace.
49:18 Look at that. And let's see if I got the
49:20 offset right. That looks like It looks
49:22 like I got that offset very close. Maybe
49:25 we'll just update it just a little bit.
49:28 Let's say that it's going to be I'm
49:30 going to say 20 and 78.
49:38 My choice place this thing. Um,
49:42 let's go a little bit for more more than
49:45 that even.
49:47 Goative 209.
49:51 All right. Um, what did I forget? What
49:53 was the step I forgot that could have
49:55 made this a little bit better?
49:58 Hopefully you guys know. Oh, I'm going
49:59 the opposite direction. There's my
50:01 problem.
50:03 Negative. What do
50:06 I said? I forgot to delete surface on
50:08 the back end so that it was actually
50:09 see-through. would have been nice. So,
50:12 let's do it. Why not? It's not going to
50:13 take us that long. So, here's what we're
50:15 doing. Delete surface tool. Delete this.
50:18 Delete that.
50:21 Delete that. That gets us to a
50:23 see-through thing. And you're really
50:25 never seeing the effects of that
50:28 anywhere else.
50:30 So, that does allow us to kind of see
50:32 through this in certain lighting. So,
50:35 now we should be able to select these
50:36 two. Let's do this again. Yeah. So, here
50:39 we go. Um, I'll rename it in a little
50:42 bit. This is going to be -21.5,
50:46 I think. And appliance built-in base
50:50 cab.
50:51 Yeah. And we'll rename this a little.
50:57 So, there that is.
51:00 Click in place.
51:03 That's looking sharp. That's looking
51:06 really sharp. And we can see inside the
51:08 box. Finally. Finally, we got it. I
51:13 think I think I think I think. Let me
51:18 copy this name.
51:20 Delete this thing. Let me grab the one
51:23 that I want.
51:28 That name. Let's do a little couple
51:31 search attributes that we want.
51:46 and let's tag this thing
51:51 in tags. Let's get this to a
51:55 uh this is a kitchen appliance that is
51:59 you know inserts into a cabinet
52:02 and this is short and narrow.
52:06 There we go.
52:10 That'll help people find it. That's it.
52:13 We did it.
52:15 That was a long video for that stupid
52:17 little thing. Uh but I think there's
52:19 some useful information in there.
52:21 Hopefully you got something out of that.
52:22 Um, obviously you're seeing me
52:23 troubleshoot some things. Um, obviously
52:26 I'm pretty rusty, so it's been a while
52:28 since I've done some of these advanced
52:30 symbol modifications. Uh, anyways, I got
52:33 more videos coming. Thanks.
