---
videoId: 9OAv42V2B-w
title: Cloud Sync Multiple User Libraries for multiple devices/end users in Chief Architect
url: "https://www.youtube.com/watch?v=9OAv42V2B-w"
status: imported
---

# Transcript

0:04 Okay, Chief Architect, Chief Talk users.
0:06 I got a really cool video to share today
0:08 and that is
0:08 how to sync multiple user libraries
0:11 without overriding one or the other over
0:17 the cloud. I don't know if they even
0:17 describe that quite right. The goal here
0:22 is we've got multiple users or multiple
0:24 devices that are using
0:24 Chief Architect and we want to be able
0:27 to sync all user libraries into one user
0:33 catalog seamlessly without having any
0:33 overriding issues and we want to be able
0:38 to do it over the cloud. And this has
0:41 been an issue of mine for years and I
0:43 finally figured out a workaround and
0:43 it's awesome and it works perfectly for
0:46 me so far.
0:47 So,
0:49 um
0:49 a little bit of disclaimer, we're going
0:53 to be utilizing a couple different
0:56 catalog locations within Chief
0:56 Architect, which is the Chief Architect
0:59 bonus catalogs and the Chief Architect
1:01 manufacturer catalogs.
1:01 And so, um the case in point is that
1:05 I've got one user and they have their
1:08 user library located let's just open up
1:12 File Explorer and we'll give you the
1:14 example.
1:14 So, in my Z drive
1:17 I have this is my user library. I've got
1:23 another user that's got this user
1:23 library, another user that's got this
1:25 user library. So, we've got three users
1:29 in this case, right? We've each got our
1:32 own user libraries. It's each they're
1:32 each in one single cloud service, right?
1:38 This is in one drive, this particular
1:38 one's in Dropbox. They're being synced
1:42 to Dropbox.
1:42 All three users can see these three user
1:48 libraries. Inside of this user library,
1:49 it's named
1:49 user library. Even though it's user
1:51 library two folder, it's still named
1:53 user library and that's important. It
1:58 needs to stay that way.
1:58 But these are three separate users user
2:02 libraries. So, this could be called
2:03 Frank's user library, this could be
2:05 called John's user library.
2:06 Anyways, let's get past that.
2:08 Back in the Chief, I'm just going to do
2:11 a couple things. I want to copy paste
2:13 some information and that just makes
2:13 this job easier. I'm going to go under
2:19 my preferences, general tab, folders
2:19 and I'm going to note the location of my
2:23 user library
2:23 and let's just open I'm going to get the
2:27 sticky notes and just paste it there.
2:29 This is quick and easy.
2:29 And then get back and I'm going to show
2:31 my pathing for the manufacturer library.
2:38 Which let's just click show in Explorer.
2:41 I'm in Windows 10 Chief Architect X11. I
2:43 get to click in this window and copy.
2:43 Alternatively, you could right click on
2:47 the folder properties
2:47 and get to the location and copy as well
2:54 of that.
2:54 You actually need to right click on the
2:58 manufacturer library's properties. Get
3:00 the location here as well.
3:01 Um
3:01 but I'm just going to copy right here,
3:06 go over to sticky notes
3:08 do another line
3:08 and then back to Chief and let's just go
3:12 to the bonus library, show that in
3:15 Explorer.
3:15 And same thing.
3:19 I want to
3:19 copy this location.
3:22 Sure, it's actually the same location
3:25 cuz
3:25 we just got to the root, right?
3:27 Okay. So, I have those locations. I'm
3:33 going to note that look in my user
3:33 catalog under user libraries for user
3:40 one, there's one item called test.
3:40 In user library, that was my cat that
3:45 you might have just heard meow.
3:47 In user library,
3:48 um
3:48 two, there's a material called test two.
3:53 In user library three, there's a
3:53 material called test three. I'm only
3:55 telling you that because we are somehow
4:00 going to get those material items into
4:02 this user catalog.
4:02 Although they are in completely
4:06 different user libraries.
4:07 So, let's shut down Chief and I'm going
4:11 to go to a website that's going to make
4:11 this job a lot easier and I will include
4:15 this in the link.
4:15 It's a freeware shell extension. I
4:17 encourage you to donate to whoever wrote
4:23 this because it's a fantastic little bit
4:25 that saves a lot of headache.
4:25 And at the very top of this page
4:29 see if I can even get my page up to
4:33 work. It's not.
4:34 Is
4:34 you know, quick start, you just click on
4:37 download, it takes you back down to
4:39 this. I'm going to going to get the
4:39 64-bit version, download it, install it.
4:43 And the first thing it's going to want
4:45 to do is shut down
4:45 um File Explorer and you just let it.
4:50 It'll shut down these. That's why we
4:51 saved
4:51 this pathing is because now I'm going to
4:57 open up two windows. Open one, I'm going
4:59 to hit control new. I'm going to hit the
5:02 Windows key right and tile these side by
5:04 side.
5:04 And so,
5:06 in the one view
5:11 I'm going to grab this so I get this
5:14 location.
5:14 Paste it. There we go. There's my user
5:18 library.
5:18 Actually, I want to get to user library
5:22 two. Okay.
5:22 In the left window
5:35 Okay, and I'm going to go to
5:35 manufacturer libraries. So, note that I
5:41 am in user library two, which has an
5:44 item in it called test two.
5:45 And
5:45 I'm going to right click on this and
5:49 something that's new here is you're
5:49 going to get a new line item after you
5:52 install that shell extension, which is
5:55 pick link source.
5:55 And this uses a script built into
5:58 Windows called symbolic link. And that
6:04 makes a hard link to a file. I kind of
6:06 explained that a little bit. But I'm
6:08 going to go ahead and click on this,
6:08 left click on it. I've now selected this
6:12 as a symbolic link. I'm going to bring
6:14 it over to the manufacturer libraries,
6:14 I'm going to right click in this window
6:19 and there's two more new line items.
6:22 Cancel that link creation or drop
6:24 symbolic link.
6:25 It's going to bring up the
6:28 administrative control
6:29 um
6:29 and then what you're going to see here
6:31 is
6:31 look at this. Let's see if we can
6:36 increase the size of my
6:36 It looks like a shortcut, but if you
6:38 hover hover over it, it's called symlink
6:43 cuz it's a symbolic link. The size of it
6:45 is zero bytes.
6:45 But the difference between this and a
6:49 shortcut is when Chief goes into its
6:51 manufacturer libraries and sees this
6:51 file, it doesn't see it as a shortcut,
6:56 it sees it as this user library.
6:56 And when you place this user library
7:02 inside of the manufacturer libraries
7:05 it will show up alongside your other
7:08 user library in the user catalog.
7:09 So,
7:09 to explain this further, the reason
7:14 we're doing this is because
7:14 if we synced manufacturer libraries
7:18 across all three items
7:18 that could possibly work. There's just a
7:22 little bit more power in this because
7:25 maybe the pathing of user A's
7:25 manufacturer libraries is different from
7:29 the pathing of user B's manufacturer
7:31 libraries.
7:31 So, this works in that we can keep it at
7:35 all in one cloud sync, all in one
7:37 location and
7:37 and forward this this user library link
7:42 to to
7:42 um wherever it's located in your cloud
7:44 service. So, the next thing is we'll go
7:48 over to
7:48 let's just go to the bonus libraries.
7:51 I've never tried this part before. I've
7:55 only done one, so let me let me see if
7:58 this works.
7:58 Same thing. We're going to right click
7:59 on this guy, pick link source, get over
8:03 to the bonus libraries
8:03 and drop symbolic link.
8:08 Same deal.
8:08 And so, user library under user library
8:13 three folder has a material item called
8:15 test three.
8:15 So, now we've dropped those two links in
8:25 And just going to open up a file to have
8:37 And fingers crossed, look at that.
8:42 How cool is this? This is so cool.
8:42 So, now I've got a desktop and a laptop
8:50 and another user working remotely from
8:50 some other office and we all three have
8:56 our own user libraries and they have
8:59 their own items in them.
8:59 And they're syncing together seamlessly
9:05 in one catalog. If these were within
9:07 folders, they'll show up as separate
9:09 folders as well.
9:09 But they won't show up as separate
9:10 folders as in you won't see a folder
9:14 that says
9:14 uh well, let's give an example. Let's do
9:17 this.
9:17 We might be able to get this out of the
9:20 core library, too.
9:21 So, I have my original There we go. My
9:27 original user library.
9:27 Let's pick link source. There it is.
9:32 Shut this down.
9:33 And let's see if we can get four in
9:39 What do you think?
9:39 I guess only option left is core
9:41 library. So, let's see if this will
9:44 work.
9:44 Be really interested if you could get
9:52 So, in this user library, I've got a
9:52 bunch of folders, subfolders, etc. Let's
10:03 So if this works, it should show
10:03 um not only that test 1 2 3, but also
10:09 all of my folders intact and in the
10:09 correct named folders as I had them.
10:16 Oh my goodness.
10:19 Amazing.
10:19 This is my originally user library.
10:22 That's from user library one. This is
10:26 from user library two.
10:26 They open up just as they should.
10:32 So I guess the thought here is
10:32 if you've already got a library and
10:33 you're already syncing that library,
10:36 make sure that everybody starts with
10:36 that library. But then every subsequent
10:41 item that anyone
10:41 user adds to that library is going to
10:45 show up in
10:45 you know, their own pathing.
10:51 I guess the trick you're going to have
10:53 to figure out is the folders
10:57 may duplicate themselves.
10:57 If you don't create new folders for
11:01 every item. But
11:01 this is syncing across four devices now.
11:07 Pretty clever. I love it.
11:08 Anyways,
11:08 I hope someone figures out an awesome
11:10 way to do this. I know I'm going to be
11:11 messing around with it because I've got
11:15 another user that I share with
11:17 and
11:17 and this is just I don't know, this is
11:20 such a time saver. Maybe you name your
11:22 folders, you know, user one's drafting
11:24 tools, user two's drafting tools, that
11:25 kind of thing.
11:26 But uh
11:26 So I hope this helped someone. I'm so
