---
videoId: tcP1x_V_7nM
title: Creating A Leather Texture Using The Patch Tool And Maps In Photoshop
url: "https://www.youtube.com/watch?v=tcP1x_V_7nM"
status: imported
---

# Transcript

0:00 uh Hey Photoshop VIP users actually I
0:05 guess it's not called VIP what are we
0:07 calling this I didn't realize we had
0:09 some people in the Photoshop Club so
0:12 Photoshop Club people here you go first
0:14 video and sorry it took me so long um
0:17 I'm going to have to pump in a lot more
0:18 videos and I'll also give you some
0:19 actions and some brushes to use because
0:22 that's the whole point of being in this
0:23 club so really appreciate you being here
0:25 and um yeah sorry I didn't notice anyone
0:28 signed up for this so see a couple
0:30 people in here um someone just posted
0:34 this this image here which is a piece of
0:37 leather and I'm going to try to figure
0:39 out a way to make this tilable and I'm
0:42 just going to work through this now part
0:43 of the Photoshop Club is we have to kind
0:45 of work through this stuff just based um
0:47 on some knowledge that we already may
0:49 have and and so this particular video
0:51 might be a little bit Advanced for
0:53 someone that's not really all that
0:55 advanced in Photoshop so I'll just start
0:58 uh diving into this um first thing I
1:01 like to do is I'm going to just take
1:03 this again and copy it um to make
1:07 something tilable and easy thing to do
1:10 is double a canvas and flip this on top
1:13 of itself and stack it next to each
1:15 other the problem with this particular
1:17 texture is that we've got some light
1:19 spots and then we got some dark spots so
1:22 not the best setup um there are a few
1:26 things we can do in terms of like
1:27 adjustments possibly so we can hit hit
1:30 this with an equalize before I even do
1:31 that I want to duplicate this texture
1:33 and then in my layer stack over here I
1:35 might convert this to a Smart object
1:38 when I convert it to Smart object that
1:39 means we are no longer doing a
1:42 deconstructive work a destructive
1:45 workflow where we are damaging the
1:48 pixels of the original image instead
1:50 we're doing effects on top of the
1:52 original image and the original image is
1:54 preserved so the thing I'm thinking I'm
1:56 going to try here first is in
1:59 adjustments I want to see what happens
2:01 when um I come in here and do an
2:04 equalize now unfortunately you can't do
2:06 an equalize to a Smart object so I'm
2:08 going to bring up the raster object on
2:11 top of it in the layer stack and then
2:13 try and equalize and see what happens
2:15 now you'll notice here it tried to
2:18 equalize all the pixels across um the
2:22 the Spectrum okay and did that really
2:25 help well the next thing I would try to
2:27 do to just see what the effect of this
2:29 is when it's over laid on top of another
2:31 image is start changing the blend modes
2:33 and I can use my mouse wheel to change
2:35 these blend modes and you can see darken
2:38 is not really doing anything that we'd
2:39 want it to do darker color Etc lighten
2:41 is not going to really do anything that
2:43 we wanted to do so ultimately this isn't
2:46 really effective for this
2:48 particular um this particular image this
2:52 actually gets a little bit close we can
2:54 see here that it's doing some things but
2:56 you notice that we still have some
2:57 really dark pixels over here so maybe
2:59 maybe something next that I might try is
3:02 I might go back a step
3:05 and few steps in fact and go back to
3:09 before we're doing an
3:18 equalize actually it's not even going to
3:20 let me do that so let's just make
3:21 another duplicate contrl J make that
3:23 duplicate we can raster this image if we
3:25 want to the thing I'm thinking I might
3:28 want to try to do is replace color so we
3:32 need to right click on this layer
3:33 rasterize layer again image adjustments
3:37 replace color and maybe I can get into
3:39 the darkest channels and lighten them up
3:43 okay so same kind of thought here is I
3:46 want to really isolate the parts that
3:47 are super super dark now fuzziness is a
3:50 slider based on um almost like anti-as
3:54 pixels where um we're choosing you know
3:58 what our threshold is is for applying to
4:01 this particular pixel now you notice as
4:03 I drop this down we're getting really
4:05 specific about the pixels that we're
4:07 affecting with our adjustment here right
4:10 and as we keep dropping it down we can
4:13 really kind of isolate now there's some
4:15 big pixelation here which isn't all that
4:16 great right so this is a pretty tough
4:19 imaged process now I might get part of
4:21 the way there and just kind of feather
4:25 this just a little bit yeah something
4:28 like that and since we have this new
4:31 feature generative fill might come in
4:33 here with a lasso tool and actually use
4:35 my pen tablet to draw in a lasso in a
4:39 particular part and then just do some
4:41 generative fill so I'm holding the shift
4:43 key drawing in this other part and we
4:46 can hit generator fill and with the
4:48 subsequent menu which is offscreen I
4:51 don't know what's going on with this I
4:52 think it's a glitch with beta I can hit
4:54 generate and not actually type in a
4:56 prompt and what it's going to do is it's
4:58 going to fill based on it neighboring
5:00 pixels and the pixels that are within
5:02 the selection so we might get some to
5:04 something that's a little bit better but
5:07 you can see here we've still got an
5:08 issue with this and and what exactly was
5:10 happening well it was sampling all
5:13 layers in this case which means it was
5:15 also sampling the darker layer below it
5:17 that so that smart object below it
5:20 notice though that this now generative
5:22 fill is its own thing and we can um add
5:25 an adjustment layer on top of this
5:27 generative fill so if I create a new
5:29 fill or adjust adjustment layer um which
5:31 might be something like an exposure
5:33 layer we can have this adjustment layer
5:36 just apply to the layer below by holding
5:39 my ALT key getting in between the two
5:40 layers and clicking you'll see that icon
5:43 showed up and now this is applying just
5:45 to my generative fill layer so that I
5:48 can come in here and adjust my exposure
5:50 now my exposure block is blocked by my
5:53 face so you're not going to see this but
5:55 I just adjusted the exposure you can see
5:57 here what it's doing as I'm adjusting it
5:59 so I'm just just trying to get it close
6:00 to the rest of the pixels in this shot
6:02 right so we're getting to a point where
6:05 it's almost a normalized texture I'd say
6:07 this is good enough I'd say it's so good
6:09 in fact that I would just go h contr e
6:13 contr e contr e or just we could in fact
6:16 just select everything
6:17 here right so do just a shift select and
6:21 then contrl G is going to group
6:28 this and then from from here we can
6:31 convert it to an a smart object or just
6:33 merge the group so now that we have
6:35 merged the group let me control
6:39 all contrl C to copy get in the canvas
6:44 size and then I want to change this by
6:48 I'm going to click on the lower anchor
6:50 and then we're going to multiply this by
6:57 two and you can see what it did now I
6:59 still have that copy in my clipboard so
7:02 I get to paste this and then hit my V
7:05 key slide this over and here's where we
7:08 get to get into our properties and flip
7:11 this now my face is in the way again
7:13 let's just see if I can grab this panel
7:15 and bring it up here's that flip right
7:17 so got a flip there now you might just
7:20 take both of
7:22 these you can just shift and and click
7:26 now you can see I've got both of these
7:27 selected over here and I can alt drag
7:30 over and that makes a copy and then
7:32 while these are still selected flip
7:34 these right so now we've made a tilable
7:38 texture but you notice it's pretty
7:40 bad so we need to do a lot of fixing
7:43 here you can do this a number of
7:44 different ways um you might be able to
7:46 come in here with a patch tool you might
7:48 be able to come in here with a spot
7:50 healing brush spot healing brush might
7:51 be able to do a lot actually um let's go
7:53 ahead and group select this and we can
7:57 contr e to merge it all into one it's
7:59 kind of like a a clone tool if you will
8:02 and then we can kind of touch this all
8:05 up and hopefully kind of clean up some
8:07 of this stuff now no matter what this
8:10 texture in particular is going to be a
8:13 really difficult one to make anything
8:14 good out of it so you might actually use
8:17 the patch tool in
8:19 here and grab some of this good stuff
8:23 here and bring it over right actually
8:25 it's the opposite we want to grab some
8:28 of this over here here and bring it over
8:31 and that's going to get some
8:33 of that texture that we like that
8:36 leather texture that we like here and
8:39 you see it it does kind of a blend if
8:43 feel by the way if you're unaware and
8:45 you have a space Mouse you just got to
8:47 enable um a script to get it to work in
8:50 Photoshop and then you can use that
8:52 space Mouse to zoom in ETC which is a
8:55 really nice trick so grab in here bring
8:59 bring this
9:03 over and then you know we can always
9:06 kind of come in here and start using the
9:08 Clone stamp tool too
9:20 right so always a challenge to do some
9:23 of these textures some textures are way
9:26 easier than others
9:33 oops that
9:36 backwards keep doing it
9:44 backwards getting there
10:04 now the one thing to note here is I am
10:06 screwing up the tileable portion of this
10:08 so we're going to have to go back and
10:09 figure out how to tile this but I'll
10:11 show you some tricks on that
10:27 too I know this allows
10:30 Zone okay now we got to figure out how
10:32 to make this tilable again now you could
10:34 do what we did before which is just take
10:36 a sample of this duplicate it and flip
10:38 it about itself that's one way of doing
10:40 it another thing to keep in mind is you
10:41 can get to into filter other offset and
10:44 offset this by something you're going to
10:46 remember so600 and -600 that feels about
10:50 right and you notice we see you know
10:52 some areas here that need to be patched
10:54 so this is where you come in here get
10:56 real tight to the edge get real tight to
10:58 the edge you can use that patch tool
11:00 again kind of clean that
11:03 up right tight to the bounds of that
11:05 upper Edge is what I was looking for
11:07 there and then kind of this whole
11:13 section there we go so that if we do an
11:16 offset
11:17 again and go positive 600 this time so
11:21 positive 600 positive
11:23 600 we should see there's no tiling
11:26 issues so here we go we have a texture
11:28 it tiles appropriately there's one dark
11:31 patch in here that we don't love so we
11:33 might need to like kind of alleviate
11:35 just this dark area CU that's going to
11:37 show when this thing starts tiling over
11:39 and over again um so you got to notice
11:41 those things and you'll pick up on those
11:42 things as you go as you get better at at
11:45 creating textures so um there we go I
11:48 think we've got a pretty decent amount
11:50 of movement there so here's where I'm
11:52 going to export this and check some
11:53 things out now we know that this is
11:56 going to be our base color map or our
11:58 texture or diffuse map okay so I'm going
12:01 to hit my control shift alt W and that's
12:03 going to be an
12:09 export and takes a minute okay let's go
12:13 ahead and keep it as a PNG I'm going to
12:15 get into my materials section I've got a
12:18 section that's upholstery I should have
12:21 something that's called leather but I
12:22 don't so let's just go ahead and make
12:23 one so uh control shift new if you're on
12:26 control shift n if you're on a PC and
12:29 then we've got
12:32 leather and let's just call this
12:34 particular one
12:37 black uh leather one why not black
12:40 leather one I like to name that and and
12:43 not add the diffuse you know um suffix
12:47 and not add you know any other base
12:49 color map suffix Etc and then now we got
12:52 to look at this and kind of analyze it
12:54 and understand what would look correct
12:57 in terms of creating a map and a
13:00 roughness map and can we get a bump map
13:04 and a roughness map in one base map
13:07 right so I'm going to convert this to a
13:08 Smart object let's control J to
13:10 duplicate this and let's try a couple
13:12 things first I want to add on a curves
13:14 adjustment layer so um I'll just get
13:17 down to the bottom where I can add this
13:20 this is at the bottom of your screen and
13:21 you're not going to be able to see it
13:22 because my face is blocking it
13:25 but let's
13:27 go CES adjustment
13:30 layer and we'll make it apply to just
13:33 that piece below and then I want to
13:35 expand this window because this makes a
13:36 big difference um if I can kind of see
13:39 this and get in here tight but you can
13:42 draw in your curves adjustment or you
13:43 can kind of play around in here but as
13:46 I'm adjusting this I'm kind of seeing
13:48 the height right and we don't want this
13:51 too extreme so we really want to make
13:54 this kind of an um a tight band where
13:57 we're kind of decreasing this curve in
14:02 the whites and then bringing this in
14:04 this is going to be very very subtle and
14:07 kind of the same thing I'm I'm also
14:08 looking at this at the same time so uh a
14:11 bump map is going to be a a grayscale
14:13 map where you know our height is Black
14:16 or White right so we've got a depression
14:19 that might be black and then or an
14:21 indentation that might be black and then
14:22 we've got a raise section that might be
14:23 white now the roughness map is um the
14:27 darker it is the glossier it is so we
14:29 want this leather to be a cut in between
14:31 right and youd almost want that
14:34 leather's roughness to really kind of
14:36 pop so I'm kind of having both of those
14:38 in mind as I'm adjusting this and I
14:41 think a medium gray is appropriate for a
14:43 leather you can see here we've got a few
14:46 little dark areas and a few little light
14:48 areas this might be very close to what I
14:50 want to do so with that in mind that's
14:54 it now I added an adjustment layer
14:57 alternatively since this was a smart
14:59 object now let me just go ahead and
15:01 delete this since this is a smart object
15:04 we could have just come in here and
15:06 added an adjustment from the image
15:08 adjustments and this you can also adjust
15:12 after the after the fact because it was
15:14 a smart
15:15 object and I'll show you how to do
15:18 that okay so I'm going to adjust this
15:20 curve just a little
15:23 bit something right about there so
15:27 you'll notice over in my stack um if I
15:29 can get this up a little bit so you can
15:31 see it is that we've got this curves
15:34 section here if I double click on that
15:35 that brings up that adjustment right so
15:38 I can adjust it again so let me hit my
15:40 control shift alt W to export
15:43 this and we'll just click on this and
15:45 that starts the naming convention and
15:47 then
15:49 Dash roughness in this case why not so
15:53 the next thing is let's bring it back
15:55 into Chief and so I'm going to need to
15:59 bring my recording window down in here
16:01 which you're going to see for a second
16:02 and we'll switch to our main with cursor
16:05 there we go now we're back in Chief and
16:07 let's see what this looks like I'm going
16:09 to bring in a
16:12 sofa maybe something from my own
16:16 library and type in user you can't see
16:20 this but I just tabed down to user
16:22 catalog so filter to my own user catalog
16:24 with the term
16:27 sofa we'll find something I can use real
16:36 quick oh we got something with the
16:38 missing texture great
16:42 perfect yeah I was building a column
16:44 taper in another video and and that's
16:47 from the VIP section all right so from
16:50 here in this particular sofa this is a
16:52 good one because it was missing a
16:54 texture and I put this missing texture
16:56 file in there anytime something shows up
16:59 like that
17:01 so so here we go we get to locate our
17:04 brand new leather
17:08 texture in our
17:11 Upholstery and leather
17:15 section and our first map let's get our
17:18 bump map in there make that roughness
17:21 the bump map it's going to be pretty
17:24 subtle that's pretty good and then
17:33 thing that's not looking bad and then I
17:36 want to look at this one more time in
17:38 Photoshop I'm just going to stare at it
17:40 for a second and try to take a guess at
17:42 what the size of this sample might
17:44 actually be so um because we're going to
17:46 tile this leather over and over again I
17:48 kind of want to get an idea of what some
17:50 of these crackings might be so a little
17:53 length of crack might be I don't know a
17:55 couple inches 2 and 1/2 Ines and I'd say
17:58 from left left to right in this
17:59 particular texture I'm looking off
18:01 screen but 2 3 4 5 6 7 8 9 10 11 12 15
18:05 15 2 and a half something like 45 so
18:08 this scale is actually not that bad I
18:10 think we're pretty good right right
18:12 where we are and so let's just say black
18:14 Lea
18:21 one and let's throw in just a window
18:26 maybe we'll just the s
18:30 and let's see what this looks like now
18:32 immediately we see something going on
18:34 here where it's just too glossy
18:37 right way too glossy of a texture so
18:41 this is where we get back into Photoshop
18:46 okay we can do this on the fly back on
18:50 the Photoshop so here's where we get to
18:52 double click dot curves and we're going
18:54 to bring all this so that it's lighter
18:58 we want this a
19:03 lighter maybe something like
19:05 that and we just get to overwrite our
19:09 existing roughness
19:22 map this couch is terrible it's got no
19:25 um soft lines to it so would be nice to
19:27 be able to see that now usually you can
19:30 get in here and open the dialogue box
19:32 and it's going to automatically kind of
19:33 update that roughness
19:43 map so that took a little bit out but
19:46 not too much now um sometimes I want to
19:48 hit my F6 key a few times to kind of
19:51 refresh the
19:53 scene and it might be that I just don't
19:55 have enough windows in here or lights in
19:58 here to really um appropriately light
20:00 this cuz it might be that this leather
20:02 texture looks really good it's just that
20:03 we've got some kind of crazy hard
20:04 Lighting on
20:06 it you know maybe we'll throw in real
20:10 quick I'm going to throw a Scot on the
20:19 wall and then the other thing I noticed
20:21 with this texture is that that bump
20:23 map's just a little heavy
20:29 I actually think I'm okay with the
20:32 roughness now and I think it might just
20:34 be the bump that's a little heavy so
20:36 let's just take this way way down to a
20:38 0.002 or
20:42 0.001 and that might ease up a little
20:45 bit on the glossiness
20:47 too yeah that's actually looking pretty
20:50 good
21:03 the texture is a little stretched on
21:05 this couch but that might be the couch
21:06 itself that's causing that let's just go
21:08 ahead and throw in a different couch in
21:10 here
21:40 yeah I don't know it's not too bad it
21:42 could be a little less gloss totally
21:49 depends yeah this couch over here has UV
21:52 mapping that's a little bit stretched
21:54 this is less stretched so I think this
21:55 looks a little bit more appropriate just
21:58 get into this View
22:02 and rotate
22:04 this oh I got a place point in here
22:07 let's
22:26 see all right that's that's it I think
22:29 I'm done um might change the scale of
22:31 this just a little bit let's just see
22:33 what happens when we change the scale
22:34 this is all part of it no this is a
22:36 Photoshop Club but this is you know the
22:38 main reason you might even be in
22:40 Photoshop for messing around with this
22:41 kind of
22:43 stuff change the scale of this to
22:45 something like
22:53 42 yeah I don't know I like it so the
22:57 last bit is let's just just use the
22:58 adjust materials tool one more
23:04 time and add it to the
23:09 library there we go all right guys enjoy
23:13 um I'll have a lot more content coming
23:15 to you I'll have some brushes I'll have
23:17 some actions so stay tuned
23:23 [Music]
