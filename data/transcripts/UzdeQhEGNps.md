---
videoId: UzdeQhEGNps
title: Troubleshoot High Polycount Part 2 in Chief Architect
url: "https://www.youtube.com/watch?v=UzdeQhEGNps"
status: imported
---

# Transcript

00:00 VIP, you remember that other video? That one like should be at the top of the screen right now?
00:05 That one where I was part one. This is part two. This is part two right here.
00:10 How do we find and troubleshoot some really slow plans? This is gonna be part two. There is gonna be actually a part three
00:16 believe it or not, but
00:18 part two is just another step in finding things that add up to really high poly count in your plan.
00:25 And so I made this little utility that does require blender, but blender's free.
00:30 Guess what? This utility is also free to you as well as any other utilities you find in the folder linked in the description of this video.
00:40 Oh, I just bought diet right there.
00:44 We Sunday.
00:46 Anyways, in part one, we showed hey, if we just export with the 3DS file type,
00:53 that's got a cap limit on number of vertices per item, right?
00:57 And so it just won't export those really high poly count items and it also warns you about it.
01:02 And then we grabbed and intercepted the log to give us all those warnings,
01:06 built the schedule so we could find those objects, get rid of them. And there we go. We reduced the poly count.
01:11 Here's the next part about that is you might have an item that is
01:15 is instant across your plan many, many times.
01:19 Maybe it's like a door handset or who knows?
01:25 Maybe it's an LED light. Actually, there's a bonus catalog,
01:29 which you've architect that's a bonus LED light catalog and they are high poly count.
01:34 And they're like one of them's 14,000 poly count.
01:37 You put in a hundred lights. You got a really slow plan all of a sudden.
01:41 So this utility I made is to find those instance things that might be higher poly count than they need to be.
01:50 And so we already exported that 3DS file. So I get to just drag and drop this.
01:55 Now I do believe you might need a plugin that you have to install for 3DS,
02:00 which I think it's included in Blender. I tell you to go YouTube that Google that you're going to find it.
02:05 But I'm just going to drag and drop this 3DS in here and say import.
02:10 I'm going to take a second to get it inside of this plan and keep in mind that are zero coordinate in chief architect corresponds with zero center of the screen and blender.
02:23 So if you're not someone that's drawing at zero, you might run into this problem where yeah, looks like buildings way out here.
02:33 Now I'm going to hit my G key. That's the move key and then I'm going to hit X to move this on the X axis to just get this closer to the center.
02:41 That's all I wanted to do. Next thing is up here up at the very top here.
02:48 And I can't zoom in because it's stealing my hot key there. But there's this viewport shading where it's wire frame.
02:53 And so I'm going to do wire frame and I'm going to click off the model.
02:56 Now this is just that house model being brought in. I don't really need to know how to use Blender to use this utility because all we're going to do is get into edit references.
03:10 And we'll get into the add-ons panel here and you can go click this drop down and install from disk.
03:18 And what you're going to do is you're going to download my utilities and go install them from disk and this one in particular that we're talking about is going to be the poly count finder utility.
03:28 Okay. These other ones are may have created a video on a couple of these that are just part of a video.
03:36 And we can go over those again in detail. If you leave something in the comments, you want to know about some of the other utilities in there. Let me know.
03:43 But this should install a little pull around tab here that if you actually if you hit the N key and is in Nancy, NATO, what have you.
03:55 There it brings it up and you'll see at the bottom of my tabs anyways because I've got some other stuff installed is rabbit tools in rabbit tools.
04:03 There's a number of different things in here. You might need to minimize these might feel a little bit overwhelming, but just look for the all caps.
04:11 And that's a way you can minimize each of these. These are the different programs that I installed. So if you only installed the poly count utility, then you're only going to see one item here.
04:22 And so I'm going to get to that grouped poly count finder and I'm just going to hit scan scene.
04:27 And it's that fast. It's quick and easy. And here you go. It's telling us we have a hundred and thirty seven thousand poly count based on 27 items at 5,000 items a piece.
04:40 The way this utility works is just looking for items, you know, because in the item tree, these are not named in a way that make all that much sense to us.
04:49 So we don't know that their duplicates are not we can't just go by name what it's doing is it's finding items with the exact same face count and then figuring out that these are, you know, one item.
05:02 Done over and over and over again. So here we go. We've got 27 items at five. So if I click on this, we're going to find this and I kind of zoom in to try to understand what this is and sure enough, it's all of the cabinet hardware in this plan.
05:17 And maybe we could make this particular cabinet hardware be less poly count. That would actually be pretty easy to do. So that's all that this utility does is it just points out what you might have missed in terms of maybe you have a high volume of something.
05:32 This all came to be because I mentioned in the previous video that there was a 30 million poly count plan. I had to diagnose and it turns out that the handset on the door was some ridiculously high poly count thing and they had a billion doors and, you know,
05:50 doop two handsets per door. So it just ended up being something like 5 million poly count just on the door handsets. So this is just a really easy fast way to find something that might be able to get optimized in chief architect.
06:05 Anyways, let me know if you have any problems installing getting this to work. If you've got a plan to test it on and love to hear about it, drop something in the comments. Thank you.
