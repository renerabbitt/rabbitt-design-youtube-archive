---
videoId: MS2Sj4YNfPM
title: Troubleshoot and Find High Polycount Items in Your Model in Chief Architect
url: "https://www.youtube.com/watch?v=MS2Sj4YNfPM"
status: imported
---

# Transcript

00:00 Oh, you interior designer, you.
00:06 You've been building bad habits.
00:08 You've been important stuff from stuff like 3D warehouse and you've forgotten to check
00:14 what the base count is of those items.
00:17 And next thing you know, you have a really simple model house like this and it's got 3 million
00:23 surfaces and there's barely anything in this house.
00:28 And 3 million surfaces is a lot.
00:30 So how do we troubleshoot this?
00:32 Because that's more than this model needs to have and if we keep on decorating this model,
00:37 it's quickly going to become 7 million surfaces on up to the point where last week I saw
00:42 one that was 30 million surfaces and I don't even know how they clicked anything.
00:46 The only way possible to deal with a 30 million surface count model is if you're running
00:51 a Mac, they just happen to run them better than PCs for that many surfaces.
00:55 But how do we troubleshoot this?
00:57 This is a really quick and easy little hacky kind of thing that works extremely well.
01:04 This is a two part video.
01:06 Video one, this is going to be in the free section.
01:08 Video two, I've got some utilities that will get you past this initial step and a further
01:15 delve into troubleshooting things that are a little bit more advanced.
01:18 So video one, this is super easy.
01:20 Check this out.
01:21 One, we're going to get into the 3D panel.
01:24 We're going to get into materials, plan materials.
01:27 This is just going to make this process go faster.
01:29 I'm going to control A to select all materials here and I'm going to merge all of them and
01:35 press OK.
01:36 This is a temporary thing.
01:39 The next thing that I'm going to do after that finishes up doing whatever it needs to
01:44 do here, I think quite fully merged.
01:46 That's fine.
01:47 I'm going to get into the file export menu.
01:50 So that's in file menu, export and very specifically I want to export as a 3DS model.
02:02 3DS, this one right here.
02:04 That's important.
02:06 3DS has a max vertices limit of 65,000.
02:10 OK.
02:12 So I'm going to throw this in my downloads folder.
02:15 Maybe I'll make a new folder just so we can see this example.
02:20 Project, OK.
02:23 And hit save.
02:26 This will start that export process.
02:28 The export process goes a little bit faster when you're not exporting all those materials.
02:32 That was the whole point of that.
02:34 First thing is it's going to kind of tabulate all the surface counts, put this together.
02:39 I'll pause for a second.
02:40 We don't need to see that part.
02:43 And so here we go.
02:44 That next part took about a minute and a half, two minutes.
02:47 Here's what we're looking at.
02:48 Maybe export error.
02:50 There's an error here.
02:51 I'm just going to press OK through all these error messages.
02:54 I'm not going to bother trying to write this down.
02:56 There's no point.
02:57 I'll tell you why.
02:58 First of all, this did just finish that export.
03:02 So this is on my machine somewhere.
03:04 So the next thing that I could do is just do a little undo.
03:07 If we want to look at undo history, we could even target this.
03:10 We got to open plan.
03:11 That's all I did, right?
03:12 And I pulled the camera.
03:14 OK.
03:15 So I'm going to undo.
03:16 While that's doing its thing, let me get back.
03:18 Over to actually, I don't even need to get to my downloads folder.
03:23 I'm going to end up deleting that export.
03:25 I don't need it at all.
03:26 Believe it or not.
03:27 The whole point of that export was so that I could get into the help menu and export
03:34 logs from the help menu.
03:36 I'm going to export the logs.
03:38 I'm going to put it in my downloads folder.
03:40 That's going to create a little zip archive.
03:43 It's going to tell me that that finished.
03:45 Let me pull open that log.
03:49 Let's go ahead and get to my downloads folder.
03:52 Here's this log right here.
03:55 And I'm specifically going to go to the message log text.
04:00 That's going to bring this up.
04:03 Look what's at the bottom of the log.
04:06 If we scroll all the way to the bottom, here we go.
04:09 Here's all those warnings.
04:11 What can I do with this?
04:13 I'm going to just select all these warnings, copy them.
04:16 I'm going to come back to Chief Architect.
04:18 We'll get into a little plan view here.
04:20 I'm going to paste them to so I have them as a reference.
04:25 Then I'm going to build a little custom schedule.
04:34 Let me open up this schedule.
04:37 Let's go ahead and pick for what our included categories are.
04:41 We want fixtures.
04:43 We want electrical.
04:45 We certainly want furniture and hardware.
04:52 Just in case, moldings, mill work.
04:56 And that's probably about it.
05:00 The next thing is columns to include.
05:02 We could get rid of everything except for.
05:06 We actually want label.
05:07 We just need label in there.
05:09 So let's add label back there.
05:11 We could leave group similar objects checked.
05:13 That's fine.
05:14 And let's press OK.
05:15 Now we've got this big, healthy list of things
05:18 that is inside of this plan.
05:20 What do I get to go do?
05:22 Look.
05:23 CHC5051 exceeds the vertex limit.
05:28 What do I go look at?
05:30 Where is this?
05:31 All right.
05:32 So it's not showing this, which means
05:34 that it must be a classification that's not quite here.
05:37 We want to make sure that this is including objects
05:40 from all floors it is.
05:42 And that it's including from all rooms it is.
05:46 And then maybe we need to choose some additional categories
05:50 or ensure other categories are checked just so that shows up.
05:54 The next thing is make sure that we are clicking
05:56 and sorting by name so that that's correct.
06:00 And there it is.
06:01 CHC5050.
06:04 If I go find object in plan, here's my edit menu, edit toolbar,
06:09 find object in plan.
06:11 And say it's on a layer that's not turned on right now.
06:14 Look at that.
06:15 There are those objects throughout the plan.
06:17 Let's go open them up.
06:18 And if we go look at the 3D panel,
06:21 we're going to see on this object,
06:23 this object is 475,000 faces.
06:29 We want this to be 10,000 faces.
06:31 Now, mind you, I have a bunch of videos about decimating.
06:34 If you didn't know this, if you never saw it,
06:36 and never saw the update, we did
06:38 build a new tool on my website, which
06:41 is for searching all of my videos, both on the membership side
06:46 and non-membership side.
06:48 So go ahead and go to that search tool and type in decimate.
06:52 And you're going to see a bunch of videos
06:53 about how we learn how to decimate things
06:57 and be able to break them down into much smaller objects
07:01 with fewer faces, basically.
07:03 So if I were to just take this, cancel this out,
07:06 delete those.
07:08 I'm just going to delete those pictures.
07:10 I don't care right now.
07:11 I'm just doing some troubleshooting.
07:12 We're kind of proving working concept.
07:15 So we know we got that 50.50.
07:17 That's there a couple times.
07:18 This K3, 2502.
07:20 Anything that starts with a K is typically color.
07:22 Color does not do a great job of limiting these.
07:26 So we could find these in plan.
07:28 Same thing and just delete them.
07:31 Let's go look one more time.
07:33 Let's our next thing, K27437.
07:37 There's this Elsonore.
07:38 Let's look up this Elsonore.
07:40 There's that.
07:41 Find this object in plan.
07:42 Let's go delete that.
07:44 And then heck, let's go check it out.
07:47 We went from, it was 370,
07:51 and it was 3,700 or something like that,
07:54 down to 1.4, just that quickly.
07:58 And so now this plan will just move a little bit faster.
08:01 Now let's go turn on a ray trace view
08:03 and do a little backdrop from lighting or something like that.
08:08 Throw a little backdrop in here.
08:12 And let's see if we can't improve this shot overall.
08:16 Isn't that cool?
08:17 And look how just smooth this thing.
08:19 Smooth is better now.
08:21 Very cool.
08:22 That's it.
08:23 Hopefully that helps you out.
08:24 That's a really, really quick way of diagnosing a plan
08:27 to see where all those really high poly count items are.
08:31 Go decimate those items, bring it back in the Chief,
08:33 optimize them.
08:35 Thanks.
