---
videoId: QLzRgG26iVk
title: CAD Block Fill Style Tips For Chief Architect X16 Premiere
url: "https://www.youtube.com/watch?v=QLzRgG26iVk"
status: imported
---

# Transcript

0:02 what's going on Chief Architect users
0:05 I've got a situation here where we're
0:07 importing something from 3D
0:07 warehouse and that item from 3D
0:10 Warehouse is coming in a little a skew
0:16 and it's coming in with a funny little
0:17 fill style which I'll show you in a
0:17 second I'm just going to throw in one of
0:23 my own rugs for my catalog and we're
0:23 going to show that when we place this
0:25 over the top that line from that rug is
0:29 coming right through and we don't want
0:29 that we don't want that as an effect and
0:32 if we go and try to change the draw
0:34 order and push this up to something
0:37 above the furniture layer that line
0:37 still in fact is coming through this
0:39 piece of furniture so first thing let's
0:43 go ahead and rotate this thing so that
0:45 it's straight up and down so I'm just
0:45 going to get a top down view make this a
0:49 little bit easy I could of course do
0:52 something like draw some kind of an
0:52 inference line here if you wanted to get
0:57 the absolute accuracy you would get into
1:01 the cad menu do a cad detail from view
1:01 so that you could actually snap straight
1:07 to this particular CAD block so we'd
1:09 explode this CAD block now these are
1:09 just lines that we can snap to giving us
1:13 a bunch of different snap points so that
1:15 I can grab a line like the one I just
1:15 drew and then grab another line and use
1:22 our angle tools to pick up this angular
1:24 Dimension and of course you got to
1:24 switch to something like um I have a cad
1:28 Dimension default that will Dimension to
1:31 CAD so there there we go
1:31 27.3 de is how much I want to rotate
1:33 this symbol so I can come back in here
1:39 open this up
1:39 27. 38 let's see if I actually guessed
1:44 the right direction we want to rotate
1:47 this uh let's see I believe in the
1:48 negative Direction in Z nope I got it
1:53 wrong here we go positive direction
1:55 there we go so now that's perfectly
1:55 aligned and then let's get into that 2D
2:00 symbol let's go ahead and choose to
2:02 generate the block that's going to
2:02 generate this new block and once I've
2:04 got that I want to open this up so from
2:09 the edit menu get into edit CAD
2:09 block let's see why this isn't producing
2:14 any kind of fill style that's because
2:14 none of these lines they're all broken
2:16 lines because this particular symbol has
2:21 a lot going on with it it's got a lot of
2:24 vertices to it so it's not completing
2:24 the segments so what I want to do is I
2:28 want to highlight all of this and use
2:31 our extend object objects tool in our
2:31 edit toolbar and draw some lines through
2:36 here a few times using that tool over
2:38 and over
2:38 again just to extend these lines as much
2:43 as possible so I can get a large segment
2:46 like this okay from there I want to pick
2:48 kind of where my Center Point's at and
2:49 just draw in a line to just cut through
2:54 here and we can use the trim tool to
2:57 trim the object past that line right
2:57 that's just leaving us with this line on
3:02 the one side the next thing I kind of
3:02 want to do is I'm going to draw in kind
3:06 of an inference line here for the back
3:06 of the sofa cushion and the front of the
3:11 sofa cushion and then I'll pick up that
3:13 one line again and I'm going to hold
3:13 control and draw Marque key over the top
3:19 of this what that did is invert the SE
3:22 selection within the Marquee so I can
3:22 just hit delete and it's just leaving me
3:27 that one large segment that I could copy
3:30 paste and reflect about this Center Line
3:32 and then use the extend tool to extend
3:35 it to the left hand side so and extend
3:38 to this left hand side if I can seems
3:38 like we've got something here that's not
3:44 quite matching up there we go I just
3:44 needed to unsnap and snap it back in and
3:49 the last thing I want to do here is just
3:53 hit close polyline all right the next
3:53 piece of this is I'm just going to make
3:56 a shape out of our polyline tool I'll
3:56 just do half of this sofa and then that
4:01 way I can hold hold the fky to kind of
4:01 fill it this corner fill it this corner
4:05 and so I'm just making that cushion
4:05 extending this forward and then copy
4:08 paste reflect about and Union the two
4:12 and I don't want to retain the original
4:14 objects all right the last piece of this
4:20 puzzle is I'm going to subtract that
4:20 inner cushion from the outer segment and
4:24 I do want to retain the original objects
4:26 but then I need to find the piece that
4:26 has the line cutting across here and go
4:30 ahead and delete it it what does this
4:32 leave us with well once we get rid of
4:35 our little inference lines that's a
4:36 perfect looking
4:36 sofa the last bit is that we've got a
4:42 closed piece here so we can designate
4:42 different fills here so I'm going to go
4:46 a solid fill and maybe I'll just go a
4:46 light gray color and then I'll go solid
4:52 fill and maybe I'll do all white color
4:53 for the
4:53 cushion right now I can close this
4:56 window make sure to save the cad block
4:59 and all instances of that CAD block and
5:03 when we get back into this we can say we
5:08 can use the cad block fill style which
5:11 is straight from the cad block or
5:11 overwrite that get into the fill style
5:14 panel set to solid and this will give us
5:20 a solid fill of whatever color we like
5:22 so this is now finally finished we've
5:22 got a solid fill color on this now kind
5:29 of a bonus to this video of course that
5:31 got you through through that portion of
5:33 it but I would say on the whole when I
5:36 want to um import something from 3D
5:36 Warehouse like this often times those 3D
5:41 Warehouse symbols are going to come in
5:41 with a really large surface count in the
5:46 3D menu we can always check this out
5:46 26,000 that's not super large we could
5:52 of course deal with that but something
5:52 that um you might try out is blender is
5:59 a free software here and so I imported
6:01 this symbol into blender first with a
6:01 SketchUp add-on making it so that it can
6:07 open SketchUp files and I just added a
6:09 modifier and that modifier was the
6:09 decimate modifier I'll go back a few
6:11 steps just to show you this so here is
6:18 our 26,000 polyc count sofa with that
6:21 decimate modifier I just get to kick
6:21 this ratio down and you can start to see
6:27 that this sofa starts to get a little
6:27 more simplified if we really want to see
6:31 what it's doing let me show you what it
6:33 looks like in terms of a wire frame and
6:36 once we decimate watch what it's doing
6:38 it's just getting rid of that surface
6:41 count right and so something to
6:41 understand and it takes a little bit of
6:43 practice is that we can get this to look
6:49 very realistic still within Chief using
6:52 Chief's built-in smoothing algorithms
6:53 now you're going to lose some things
6:53 like the piping but maybe that doesn't
6:57 matter to you maybe you would like a
6:59 nice light scene so you can see here
6:59 I've decimated this down to 10,000 poly
7:05 and it still looks pretty good so
7:05 there's a little food for thought we
7:06 would just export this as an obj file so
7:12 file export and then let me just go
7:13 wavefront
7:13 obj I'll pick this up want to make sure
7:20 that the up Axis is z the scale um
7:20 blender automatically goes in meters so
7:24 it's going to be a different scale than
7:25 you want um so you can just leave that
7:25 scale one to one export this wave front
7:30 object let me get back to Chief
7:30 Architect and right in the 3D panel menu
7:35 over here in the replace geometry
7:35 section we can just click on that find
7:41 our symbol there's that West Elm sofa
7:45 chair obj notice that it's shrunken
7:47 quite a bit we need to change our
7:47 drawing unit to meters that'll resize it
7:52 back up we can of course put that
7:52 27. 38 degrees so we're going to have to
7:57 do this little piece
7:57 again and actually now straightened up
8:02 we can do 90 there we go we want the
8:02 front of this oriented so that it's in
8:08 the negative y direction and we should
8:08 have retained our 2D symbol during this
8:10 because we only do this ask as needed or
8:15 maybe I should have done never
8:15 beforehand let's just see if it retains
8:17 it does in fact retain let's take a look
8:22 at what this looks like in 3D with a
8:24 maybe we'll put a light
8:24 overhead and get that camera rendering
8:33 and there we go kind of the last thing I
8:35 like to do is I like to have a nice
8:35 upholstery kind of texture to work with
8:40 as a base starter so I've made a couple
8:41 of these and then just paint this out
8:42 and we're starting to look pretty good
8:46 right and then rendering mode I'm just
8:47 going to kick this back up to Quality
8:47 and sharpening up a little bit so we can
8:51 really see this thing shine and then the
8:54 last thing is maybe I'm changing the UV
8:56 scale of this Tex texture down to
8:56 something like 15 we're cutting that in
9:01 half and yeah that doesn't look too bad
9:04 that's a night nice lightweight sofa
9:13 cool Le a leave a like this is kind of
9:15 uh the stuff that I put into my VIP
9:15 membership area of YouTube so um you
9:18 know at times I'll drop in these little
9:22 free tidbits and then I might move this
9:24 to the membership area so leave a like
