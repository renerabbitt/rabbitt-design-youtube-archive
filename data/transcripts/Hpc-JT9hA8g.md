---
videoId: Hpc-JT9hA8g
title: Pattern file from texture source-Chief Architect X-12
url: "https://www.youtube.com/watch?v=Hpc-JT9hA8g"
status: imported
---

# Transcript

0:09 [Music]
0:09 this is renee rabbit of rabbit design
0:11 and this is part of my tips tricks and
0:15 hacks for chief architect
0:15 playlist on my youtube channel please
0:19 take a look at that and
0:19 also subscribe this is going to be going
0:23 over
0:23 how to create a pattern file a pat file
0:27 if you will
0:27 from a texture source and chief
0:31 architects has
0:31 some stuff built into their software now
0:34 starting from i believe
0:34 x12 i could be wrong could have been x11
0:38 where they introduced that
0:38 and we're going to get into that in a
0:41 minute but in the description of this
0:41 video
0:41 i'm going to link you to this particular
0:45 thread which is on chief talk
0:45 chief architects forums and we're in the
0:50 section called symbols and content and
0:51 this particular thread is called
0:54 custom material generation with
0:55 substance player
0:55 now chief content uploaded this
0:57 themselves this is dustin cruz's work
1:03 fantastic irish at chief content and
1:03 he's created four different tools we can
1:07 use here using the substance player
1:08 and it describes how to get into these
1:09 tools so i won't go too far into it but
1:13 let's go ahead and jump into substance
1:14 player
1:14 and their tile building tool now here
1:18 i've got a quartz
1:18 hex tile that i've created using this
1:22 tool and i'm going to go ahead and
1:22 export this as a bump map to a folder
1:25 i've already
1:26 set up so base name i want to call this
1:30 we're just going to call this hex tile
1:32 to keep my naming conventions the way
1:33 i'd like them
1:33 and export all outputs and it's going to
1:37 be a very quick process there you go
1:39 that part's done
1:39 the next part is i want to go back and
1:41 switch my material to something that has
1:44 a very clean
1:44 image and we're going to explain why
1:47 that's so important here
1:47 in just a minute i'm going to export
1:51 this as well i'm going to change the
1:52 name of this
1:52 to textile underscore
1:56 bump and just export that
2:00 texture file or what should be called a
2:05 diffuse map
2:05 there we go and now we'll switch into
2:09 chief architect
2:09 and i'm going to get into my plan
2:13 materials
2:13 and we're going to create a new material
2:19 and we'll call it x tile in fact it'll
2:22 be hex tile number two
2:22 in my texture panel of my define
2:26 material data box
2:26 underneath texture source i'm going to
2:31 browse for that
2:31 well typically you would put in this
2:32 texture right here which is that marble
2:34 but
2:34 instead i'm going to put in the bump map
2:38 the purpose of this is
2:38 if i get back into my pattern panel
2:41 and get down into the pattern section i
2:45 can do a pattern from texture
2:45 and here we go this is how we can create
2:49 a texture
2:49 to match our diffuse map or that texture
2:54 source
2:54 now something to keep in mind here if we
2:57 were to
2:57 let's get back to that texture panel and
3:01 we're going to instead put in
3:01 this texture source when we get back to
3:04 our pattern
3:04 and create pattern from texture what's
3:07 going to happen is we're going to get
3:09 some of that marbling
3:09 effect or we possibly could so to avoid
3:12 that
3:12 this is why i export that second file
3:16 which was
3:16 a more clean image because once we've
3:26 back in our pattern panel pattern from
3:26 texture
3:26 here we go i can underneath
3:29 this section right here which is an
3:33 unnamed section
3:33 i can choose to keep pattern and texture
3:40 in sync so that back in my texture panel
3:42 if i change this to something like 60
3:43 inches
3:43 we're going to see that the pattern
3:46 itself has changed
3:46 with it so once that pattern
3:50 is in sync we can change this
3:57 back to our
3:57 marbled texture source and just to
4:01 finish this off
4:01 we can go ahead and add this normal map
4:05 and then in the properties panel
4:08 we can add a roughness map
4:08 and now we've got a full new
4:18 now that we've got that material we can
4:20 get into our 3d menu
4:20 get down into our material painter
4:23 and underneath our plan materials we can
4:26 find that
4:26 hex tile number two and let's take a
4:31 look at what he does there we go
4:31 now we've got that pattern file placed
4:34 on this wall
4:34 and that's it it's a pretty
4:36 straightforward process i know i've
4:38 kind of broken down the steps of this
4:42 but you can really get this done in a
4:42 really short amount of time being able
4:45 to
4:45 get these pattern files to look correct
4:48 in your vector views so you can pull
4:48 some
4:48 some pretty dynamic looking shots in
4:52 in chief architect so hope this helped
