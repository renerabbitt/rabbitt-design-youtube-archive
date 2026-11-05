---
videoId: PTClBPpvfvM
title: Automatic Topography and Parcel Maps in Chief Architect Using AI and the Pro Plan
url: "https://www.youtube.com/watch?v=PTClBPpvfvM"
status: imported
---

# Transcript

0:00 What's going on people?
0:02 If you have my pro plan, there's going to be an update coming up here pretty shortly
0:06 where I give you an extra skill, but you can generate this skill yourself if you want
0:12 to.
0:13 I'm just going to show you how to use this skill.
0:15 Here's what the description of the skill is to be used with AI.
0:18 Some kind of a frontier model AI or some kind of AI running on your machine is this was
0:23 what my description was.
0:25 I want you to look up parcel information.
0:29 I want you to recreate a parcel using a polyline.
0:34 I want you to make it so that north bearing is Z positive.
0:41 That's the direction we're doing in terms of sheet space.
0:44 And then I want you to also overlay terrain data.
0:50 I want you to just create a DXF file for my parcel boundary should be a closed polyline.
0:58 And then add in all the major topography lines.
1:04 Those are 10 foot increments, meaning 10 foot in elevation increments.
1:10 And I want you to limit those to polylines where there's no more than 40 segments for
1:18 each polyline for each topography line.
1:21 That makes it so that we're not interpolating so much in the terrain data makes it a lot easier
1:25 in chief architect.
1:27 So then I want you to extend those terrain lines by 100 feet at least past the parcel boundary.
1:36 All right.
1:37 And that's basically the gist of that instruction.
1:41 And so I created a skill in AI.
1:43 So now all I have to do is pin that in my conversation and say, hey, go use this skill.
1:48 Go look up this project information and create a DXF file.
1:53 And I continue with my work.
1:55 And meanwhile, it's created a DXF file for me.
1:58 Now if you've got my pro plan, then you're going to want to switch to the working plot plan
2:03 view where we have a terrain already built here terrain printer.
2:08 And we have a lot size already built here that's reporting to an automatic area analysis.
2:13 So I'm going to show you how to utilize this feature set and this skill together.
2:19 So this is generated something new for me.
2:21 Here we go.
2:22 And I get to bring this in.
2:23 It's a DXF file mind you.
2:26 And I want to show the import assistant.
2:28 And I'm going to press OK.
2:30 And I'm going to go next.
2:31 Now another little detail that I said is I want to map these things by layer.
2:35 OK.
2:36 And I want to map them so that each next topography line is on its own layer.
2:40 All right.
2:41 And then I'll go through and clean it up from there.
2:44 And so you can see here it brought in contour elevation text.
2:47 I told it to give me text so that we know what the contour is.
2:51 All right.
2:52 But don't break the polyline.
2:54 And then we've got all of our majors here.
2:57 And then we've got a terrain perimeter and the parcel record.
3:01 So I told it to go ahead and map all these things separately.
3:04 Now in this case, I don't actually need to import the terrain perimeter.
3:07 I've already got it.
3:08 OK.
3:09 Here's I want to select these.
3:11 Shift select them.
3:12 OK.
3:13 And I want to convert the selected layers to elevation data.
3:16 All right.
3:17 Then we can say next.
3:19 Now we could do a single layer in chief architect called cat plot plan.
3:24 That would be a possibility for us.
3:26 But I'm going to go ahead and choose chief architect layers by name and then let those unique
3:31 layers come in.
3:32 And I can clean them up later if it bothers me.
3:34 OK.
3:35 And so or we could go to the advanced layer mapping panel and get even more specific with
3:40 this, which now I can come in here and say, hey, all these topos, I want actually this
3:46 to be terrain elevation data.
3:49 All right.
3:50 So that would just be right there.
3:52 So that's going to help.
3:53 OK.
3:54 And then in terms of the parcel record, we could say, hey, we want to map this cat plot plan.
4:01 And let's see.
4:02 Def points.
4:03 I don't even know that I needed to bring in that.
4:04 In contour elevation text, I could just say cat plot plan as well if I wanted to and get
4:11 rid of that when it comes in.
4:12 And so let me say next, I did specify that I wanted the unit of measurement to be feet.
4:18 So I can leave it as feet here.
4:20 And let me click finish and let's see what happens.
4:23 This is what it brought in.
4:25 Now I'm going to go ahead and kind of scoot this over for now because we're going to do
4:28 a little bit of work on this.
4:31 One is that the way this is drawn is Z is true north.
4:35 So we need to come into the cad menu into the north pointer and draw a little north
4:39 just straight up.
4:41 OK.
4:42 Next, I want to draw a cad line in here from this point.
4:46 All right.
4:47 I'm going to draw a cad line just like that.
4:49 I'm going to switch to, well, I can leave it on plot plan dimensions.
4:53 Let's use manual dimension, you know, drop down.
4:57 And then let's get to the angular dimension and draw an angle here.
5:03 And it's going to ask me do we want dimensions plot plan?
5:05 Turn on.
5:06 Yes, we do.
5:07 Now, I want to select this line and then zoom out and hold control.
5:12 And when I make a marquee, it will deselect what I have selected and it will select anything
5:18 that was not currently selected.
5:20 So we are inverting my selection if I hold control and draw a marquee over everything.
5:27 Let me try that again.
5:27 I didn't quite miss it.
5:28 I think my shift button is bound right now.
5:30 So let me try this one more time.
5:32 Select this cad line, hold control.
5:35 Oh, and for some reason, I'm not getting an inverted selection.
5:39 That's because I'm on a current tool.
5:41 Sorry about that.
5:42 So let me go back to select objects tool, select the cad line, hold control.
5:48 There we go.
5:48 I finally inverted the selection.
5:50 Now I can hover over this angular dimension, click it and press zero.
5:56 What's that going to do?
5:57 Not only is it going to rotate my parcel, right?
6:02 But it's also rotating that North pointer so that the bearings all stay correct.
6:07 And then I can start to get this in place to where it should be according to where my building is.
6:13 So let's say for argument sake, I know exactly where my building is and I know where it is
6:19 in terms of where it is on this parcel.
6:21 So I'm going to use point to point and pick where it is on that parcel and then
6:26 point to point to where actually my building is drawn.
6:28 I just didn't have a building drawn, you know, my mistake.
6:31 So there we go.
6:32 Now I've got this in the place that it needs to be oriented in the correct orientation.
6:39 And I've got just a little bit more to do here.
6:42 So here's that lot perimeter.
6:44 What I want you to do is we're going to union this and we want to union it from the
6:48 standpoint of having this selected.
6:51 So what I'm going to do is I'm going to get in real tight here.
6:53 I'm going to set the distance here to be one sixteenth of an inch.
6:56 This is not going to cause any discrepancies here when I go to use the union tool.
7:02 So I have the parcel perimeter that's already established that report store schedules
7:08 and generate some stuff for us automatically.
7:11 I've got that set so that it's only a sixteenth of an inch in height.
7:16 I'm going to use the union tool.
7:18 I'm going to hover over the parcel that was created for me by chat GBT.
7:23 And we don't want to retain the original objects.
7:26 And then once I've got that, I can click on this again and hover over and set that one
7:31 sixteenth to zero.
7:34 And then finally, this shows up in our editor bar, simplify polyline.
7:37 We're going to hit this twice.
7:39 First time is going to get rid of that spike line that was there.
7:43 The next one is going to get rid of this little diamond here.
7:47 Okay, there we go.
7:49 Now we have correct bearings and correct lot size.
7:53 Isn't that cool?
7:54 That just showed up.
7:56 So the last trick here is we're going to resize the terrain and we want to leave it
8:00 square.
8:01 That's important because you want the side of your elevations to just be looking into
8:05 a square terrain perimeter.
8:06 All right?
8:07 Because if you change the shape of this, your elevations are going to look incorrect technically.
8:12 So I want to make sure this is terrain perimeter square.
8:15 We've got that all locked in.
8:17 Here's the last bit is we can take that terrain perimeter and use the trim objects tool in
8:24 sticky mode and start to trim away data from away from our lot here.
8:30 Okay, I'm just trimming this away.
8:34 There we go.
8:35 Now I've got a nice clean topography right in the center of the lot.
8:39 The rest of this, we could just switch to an intersected mode and kind of come in here
8:43 and just wildly throw some more keys and delete because we don't need this stuff anymore.
8:49 You know, that was great info, but I didn't need that big of a census of the land there.
8:55 So we can just get rid of all this excess stuff like this.
8:59 There we go.
9:00 Now we've got this nice clean setup here.
9:03 I'm going to go ahead and open this up and specify that it should be layer again for
9:10 some reason that CAD plot plan is that color well, you know what I'll leave it.
9:15 So now when I go open my view, that's going to force the build of the terrain.
9:20 You could alternatively go into the terrain menu and click on build terrain.
9:24 Now I don't have a house here, so it's going to be hard to kind of locate this, but there
9:28 we go.
9:29 It just generated all the secondary contours.
9:32 Now if you're not working in my template, then you might not have the same setup for
9:36 terrain parameters, but this is how I've got the setup interval for frequencies.
9:40 You can see of contours is 12 inches and you want a primary contour every 10 lines.
9:45 Why?
9:46 Because this is what it looks like in a plot plan view now.
9:49 Nice and clean.
9:50 Look at this.
9:51 Now we can finally get rid of these text objects here.
9:54 We can just do that by just selecting all and select marquee similar and select all similar.
10:02 Get rid of those because our topo is actually showing the correct.
10:08 Yeah, showing is correct.
10:10 Look at that.
10:11 Isn't that nice and pretty?
10:13 Simple, easy.
10:14 We barely did any work.
10:16 This is how I'll built right.
10:18 Double check this.
10:19 Double check that the parcel is correct, but I could tell you that from the few times I've
10:23 done this, it's dead on the money.
10:26 Then finally, we're just going to clean up a couple things.
10:29 Maybe clean up this North pointer arrow.
10:32 Excuse me.
10:34 You can always, if you're worried about moving this, you can always just open it and just
10:38 change the length to something minuscule like 12.
10:41 If you don't even care about displaying that, that'd be another thing.
10:44 Also, you can open up our title block and spec plan.
10:48 Excuse me or layout and get to the plot plan view right here.
10:52 You might come in here and just match that North arrow by just dragging this like that.
10:56 Look at that.
10:57 Isn't that nice?
11:00 Quick, easy, easy way of doing this, easy way of getting that built.
11:05 It's mostly hands off, so hope that helps you out.
