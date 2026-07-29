---
videoId: HzB6Y74St4I
title: Template Tuesdays - Managed Mode Tricks and Tips
url: "https://www.youtube.com/live/HzB6Y74St4I?si=QnGf7zQLCEJIu6Ro"
---

# Summary

This Template Tuesday session explains Chief Architect Managed Mode, why it is valuable for teams and cloud workflows, and how to use it safely and efficiently. The video argues that Managed Mode is the best way to work with a team because it bundles project files, layouts, linked files, materials, assets, and support documents into portable project files while reducing the old plan/layout/backup juggling workflow.

The first section explains how Managed Mode stores and migrates settings, toolbars, libraries, and project data into encrypted files under Windows program/app data locations. It warns that manually copying those encrypted files can duplicate a machine but may also cause cache or write issues, so the safer path is to use Chief's Managed Mode export/import tools.

The video then demonstrates exporting a `.caproj` file, choosing which linked resources to include, deleting and reimporting the project, opening `.caproj` contents with 7-Zip, and understanding why files can become large. The main file-size culprit is usually image assets and material texture maps, including large PNGs and HDRI backdrops. The video explains ways to reduce file size by lowering texture resolution or managing secondary maps, while preserving rendering quality where needed.

The middle section focuses on Pro Plan and project-template workflows. It explains copying layouts with linked plan files into new projects, using a separate logo/design criteria/spec plan to drive title block and layout content, replacing reference plan layouts for different builders or jurisdictions, merging unused plan materials to reduce file bloat, and avoiding broken references by using `Make a Copy With Links` instead of ordinary copy.

The session also covers design iteration management in Managed Mode. It shows using new folders, separate projects, project tags/filters, active/hold/inactive/archive categories, open-project filtering, and thumbnail images to help a team understand and share different versions or options. It also gives a detailed architectural file naming convention based on date, version, project name, and initials.

The later section explains archive recovery, backup management, asset management, project references, and cleanup. It shows how to rebuild a project from archived plan/layout files, why renaming layout files matters, how Managed Mode backups grow when projects and assets accumulate, where cached files live, why downloaded manufacturer catalogs and imported project assets slow backups, and why a periodic library/project export plus asset purge can be worth doing.

The session ends by showing plan references for as-built/proposed workflows, replacing linked reference plans, repairing broken project references, saving thumbnail images for design options, and reminding users that Managed Mode has a learning curve but gives a cleaner workflow once a system is established.

## Key Topics

- Chief Architect Managed Mode
- Team and cloud workflows
- Managed project export/import
- `.caproj` files
- Encrypted managed files
- Program data and app data storage
- Managed project assets
- 7-Zip project inspection
- File bloat from texture maps and HDRI files
- PNG versus JPEG texture tradeoffs
- Material resolution optimization
- Pro Plan template projects
- Make a Copy With Links
- Linked layouts and plan files
- Reference Plan Layout tool
- Design option folders
- Project tags and filters
- Project browser organization
- Naming conventions for project versions
- Online-only archive folders
- Rebuilding projects from archives
- Backup Managed Resources
- Asset Manager cleanup
- Purging unused assets
- Plan references
- As-built and proposed plan workflows
- Save thumbnail image

## Chapters

- `00:02` Opening and Managed Mode session topic
- `00:36` Why Managed Mode can take time due to read/write/cache performance
- `01:03` Managed Mode benefits for cloud and team workflows
- `01:43` Switching into Managed Mode and migrating existing settings
- `02:03` Managed files stored in ProgramData/AppData and encrypted
- `02:27` Warning about manually moving encrypted managed files
- `03:28` Template Tuesdays purpose and Pro Plan product context
- `04:08` Managed Mode project browser and adding extra files/URLs
- `05:24` Exporting a project and choosing which linked resources to include
- `06:12` Exporting bundles project resources outside Chief Architect
- `06:53` Managed Mode avoids missing material texture files
- `07:26` Deleting and reinstalling a `.caproj` file
- `08:33` File association issues with multiple Chief Architect versions
- `09:50` Inspecting `.caproj` file contents with 7-Zip
- `10:36` Large file size warning and project properties
- `11:20` Asset files and why project files become large
- `11:56` File bloat and when optimization is worth the time
- `12:15` JPEG versus PNG texture quality and file size
- `13:01` Reducing secondary texture map resolution
- `13:42` HDRI backdrop files and large radiance maps
- `14:25` Limiting file size in plan files used for templates/specs
- `15:09` Pro Plan layout copies with linked plans
- `15:21` Make a Copy With Links to Project
- `16:36` Copying only the needed layout and linked plans into a new project
- `16:49` Logo/design criteria/spec plan purpose
- `17:37` Replacing reference plan layouts for different design criteria
- `18:23` Merging plan materials to reduce exported project bloat
- `19:20` Broken linked reference example after deleting a linked plan
- `20:05` Replacing a missing plan reference and saving to clear warning icons
- `20:42` Creating design iterations in Managed Mode
- `21:09` Why ordinary copy is the old X16-style method
- `21:53` Managed Mode allows safe renaming without breaking links
- `22:05` Organizing design iterations into folders
- `22:25` Make a Copy With Links to New Folder
- `23:02` Creating separate projects for design iterations
- `24:16` Folders as tags/filters, not normal folders
- `24:49` Useful project tags: active, hold, inactive, archive, kitchen types
- `25:12` Dragging projects onto tags for filtering
- `26:07` Project browser buttons and showing open projects
- `26:52` Live comment about template projects with multiple layout sizes
- `27:12` Demonstration: drawing a small plan into pre-linked template layouts
- `28:01` Elevation update strategy and why auto-update can slow large projects
- `28:41` Managed Mode templates populate layouts and schedules as drawings develop
- `29:00` Sharing project files with a team
- `29:20` Unmanaged users can still open exported `.caproj` files
- `30:38` Export and Delete as the closest Managed Mode equivalent to Save As
- `31:55` Creating a blank project shell for recovery
- `32:54` Finding shipped Chief Architect templates in Program Files
- `33:33` Rebuilding a project from archived plan/layout files
- `35:47` Why renamed layouts are easier to recover from archives
- `36:35` Backup Managed Resources schedule and file size concerns
- `37:51` Offline project naming convention: date, version, project name, initials
- `39:15` Using printed version names to revert to an earlier project state
- `40:24` Archive folder and cloud online-only storage
- `41:13` Live question about layout sheet sizes
- `42:24` Multiple template pages for different graphic scales
- `44:21` Changing layout sheet setup and template page size issues
- `45:52` Using points, lines, and callouts to align title block elements across pages
- `48:09` Questions about project browser, tags, and pre-linked files
- `48:25` Creating template plan features without saving rooms into the template
- `49:41` Copying/importing cameras, elevations, and settings from a test copy
- `50:50` Dimension default considerations in template plans
- `51:38` Managed Mode temp/cache files and TreeSize inspection
- `52:42` User library cache and compressed library size
- `53:26` ProgramData and AppData managed file locations
- `55:13` Asset Manager and imported asset accumulation
- `56:00` Why bulk deleting referenced assets fails
- `57:15` Periodic purge workflow: export library/projects, delete, purge assets, reimport
- `58:28` Plan references overview
- `59:00` As-built/proposed plan reference workflow
- `59:39` Replacing as-built plan file while maintaining layout links
- `1:00:07` Turning on a reference display from the as-built plan
- `1:00:43` Plan References dialog and replacing references
- `1:01:31` Repairing broken project links and using correct copy tools
- `1:02:18` Save Thumbnail Image for design options
- `1:03:51` Closing advice: use Managed Mode and keep backups clean
- `1:04:24` Managed backup file contents and restore workflow
- `1:05:33` If backups take too long, reduce assets/projects and rewatch cleanup tips
- `1:05:43` Final close

## Search Keywords

- Chief Architect Managed Mode
- Chief Architect managed project
- Chief Architect caproj file
- Chief Architect project export
- Chief Architect export and delete
- Chief Architect make a copy with links
- Chief Architect managed mode team workflow
- Chief Architect cloud workflow
- Chief Architect project browser tags
- Chief Architect project folders filters
- Chief Architect managed mode backup
- Chief Architect Backup Managed Resources
- Chief Architect AppData ProgramData encrypted files
- Chief Architect asset manager purge
- Chief Architect material file bloat
- Chief Architect HDRI file size
- Chief Architect PNG JPEG textures
- Chief Architect 7-Zip caproj
- Chief Architect rebuild project from archives
- Chief Architect reference plan layout
- Chief Architect plan references
- Chief Architect as built proposed plan
- Chief Architect save thumbnail image
- Chief Architect template project
- Chief Architect layout links
- Chief Architect design options
- Chief Architect project naming convention
- Chief Architect online only archive
- Pro Plan managed mode
- Rabbitt Design managed mode tips
