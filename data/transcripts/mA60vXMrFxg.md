---
videoId: mA60vXMrFxg
title: CA SHORTS-CAD Tricks For Creating Patterns in Chief Architect
url: "https://www.youtube.com/watch?v=mA60vXMrFxg"
status: imported
---

# Transcript

0:02 so my professional colleague Kelly
0:02 fredline who has the Facebook group
0:05 called presentation by Design it's a
0:06 great group I was just working with the
0:11 create pattern tool in X15 and it's a
0:11 great tool and you can really struggle
0:16 with that tool though if you're trying
0:16 to match up patterns it takes there's a
0:20 pretty large learning curve when we're
0:24 trying to match texture patterns to
0:24 Vector lines right and I think she did a
0:29 great job I'm going to show some tricks
0:30 in the case that you don't necessarily
0:32 want to match up the texture perfectly
0:35 but you do want something that is
0:35 tileable and limits the number of vector
0:40 lines it's creating because the more
0:40 Vector lines you get in a pattern the
0:46 more complex that makes the scene and
0:47 you can see some serious system
0:47 slowdowns and even some corrupted files
0:51 if you have enough Vector lines being
0:53 produced from a number of different
0:53 patterns so let's go ahead and create a
0:57 pattern and I'm going to create kind of
0:59 a simple OG pattern and I'm not even
1:01 going to name it at this point so
1:01 here we go I'm not too worried about the
1:05 bounding box here because we're going to
1:07 resize it something to keep in mind
1:07 though is we can only resize by dragging
1:11 the edit handle on the right side of the
1:13 screen or the top side of the screen
1:13 right so that's the only way that we can
1:19 um resize our our pattern box so keep
1:19 that in mind I'm going to create an OG
1:24 that kind of looks like a diamond so
1:26 we'll start with the regular polygon
1:26 tool and I'll set it number of sides six
1:30 and then inch and a half is pretty good
1:31 because that means that we're going to
1:31 end up making a three inch wide Diamond
1:34 which I think is an appropriate size for
1:39 that so there we go I'm going to go
1:39 ahead and place this I'm going to rotate
1:42 it so that we're going to start creating
1:44 our diamond shape and then I want to
1:44 stretch this out first so I'm going to
1:50 use the edit tool stretch Cad and I'm
1:50 going to kind of grab an inference snap
1:55 draw this through the center line of my
1:58 shape and then drag this down and let's
2:00 see we said inch and a half side so I'm
2:02 going to drag this down 3 4 quarters of
2:04 an inch
2:04 all right and then from here let me go
2:08 ahead and delete this but I'm still
2:08 probably using yeah that stretch CAD
2:10 tool so now I'm going to draw and kind
2:13 of grab the pointed edge of this diamond
2:17 and kind of stretch well I'm going to
2:19 actually draw this through
2:21 the center here
2:21 and stretch this way and we're going to
2:26 go another 3 8.
2:26 and then kind of the same thing on the
2:31 other side so I'll drag this let's see
2:31 I'll shape this bring this up here again
2:36 kind of snap this to that Center Line
2:40 and then drag this another 3 8.
2:40 okay and that getting close to the shape
2:45 that I want so let me go ahead and do a
2:46 point to point and this will just help
2:46 me kind of line things up and then let's
2:51 draw some additional inference stuff
2:51 we're just going to use the line tool
2:55 and we're going to pick up inference
2:55 snap here so that we get a right angle
2:57 and then snap here and then we can pick
3:03 up Center Line here and kind of Center
3:05 Line here and this is kind of getting
3:05 the shape that I want to generate my OG
3:12 shape from so now I'm going to use
3:12 alternate draw mode with the line tool
3:17 draw it to here draw it through that
3:17 midpoint to here and then finally to the
3:22 point and so now oops
3:22 and I grabbed one extra additional
3:25 little piece there
3:25 is the piece that I want so now I can
3:27 use that fillet tool and just hold your
3:32 F key
3:32 which I can't seem to be getting oh you
3:36 know what this didn't quite complete
3:36 let's and this is picking up what looked
3:40 like a funny snap all right
3:40 F key and go ahead and fill up this as
3:46 much as we can there we go and this is
3:49 looking pretty good so I'm using um
3:49 contained mode for my selection so I
3:52 might be able to just grab some of these
4:01 right and so there's my curve and that's
4:04 a pretty curve next thing I want to do
4:05 one more inference snap pick up this
4:05 corner bring it down and then use that
4:10 closed polyline tool then copy reflect
4:10 about Center and now we've got two sides
4:16 of shape let's Union this and then copy
4:18 reflect about Center again and let's
4:18 start seeing what this looks like now
4:21 one problem with Chief is I notice
4:21 especially in the pattern tool that
4:23 things are off just a little bit they're
4:27 picking up the snap Grid or they're not
4:30 quite you know to decimal accuracy so
4:30 we're gonna need to Union on the top end
4:35 of this diamond but we're also going to
4:37 have to subtract on the bottom end and
4:37 then Union the two together in order to
4:42 get this shape to truly meet up
4:42 perfectly okay so that's kind of the
4:45 problem with this pattern tool that you
4:49 might run into so what's the approach
4:49 going to be well I already have it set
4:51 so my dialog box when I Union something
4:55 discards the remnants so I know that I
4:55 need to copy this and then paste hold so
5:01 that I have an additional copy the next
5:03 piece is I can drag this down kind of
5:03 snap it to that top of that OG and now I
5:08 can Union to this right there there we
5:08 go so now I have one shaped object here
5:13 at this point I can actually probably
5:13 just take this point to point and take
5:17 this to this point and then reduce this
5:21 point because we're going to end up
5:23 unioning it to this piece and also
5:23 reduce this point because we're going to
5:27 end up unioning it to this piece so we
5:27 could actually go ahead and do that now
5:30 let's go ahead and Union the two there
5:32 we go now we've got one shape to
5:32 subtract this item from so I'm going to
5:36 just extend this through because it
5:36 doesn't really matter I'll extend this
5:40 through and then I can go ahead and
5:40 subtract this one side and that's going
5:44 to leave me one Remnant here kind of
5:47 same thing extend this through and
5:47 that's going to leave me oh well that
5:49 actually did something kind of funny now
5:51 didn't it we're going to actually pull
5:54 this down instead all right and now we
5:56 can go ahead and make that subtraction
5:57 again
5:57 so if I did this correctly these should
6:02 match up perfectly when we go ahead and
6:05 copy this and then do a point to point
6:06 and we should pick up this snap right
6:06 here look at that now the last piece of
6:11 this puzzle is kind of taking these two
6:14 pieces let's grab this point right here
6:16 let's drop it down to the bottom point
6:16 right here and then we're going to edit
6:19 this box we're going to edit this box so
6:24 that it kind of let's see how's this
6:26 going to go not there we're going to
6:26 actually snap it to the side of this guy
6:30 right here right and then we're going to
6:33 snap this down to the point and there we
6:37 go an infinitely repeating OG pattern
6:41 looks pretty good so just some couple
6:41 tips and tricks we went over the stretch
6:47 CAD tool we went over unioning we went
6:49 over just the closed polyline we went
6:49 over a bunch of you know inference snaps
6:54 and how that creates
6:54 some symmetry if you will and and some
6:58 tips and tricks about subtracting versus
7:03 just rotating flipping and unioning so
