---
videoId: uwN0QHEy8yY
title: Template Tuesdays - Toolbar Tricks You Didnt Know In Chief Architect X18
url: "https://youtube.com/live/uwN0QHEy8yY?feature=share"
---

# Summary

This Template Tuesday session demonstrates advanced Chief Architect X18 toolbar customization workflows, including how to create hidden/toggleable toolbars, add built-in tools and custom library-object tools, create custom toolbar icons, and transfer toolbar definitions between configurations by editing exported `.toolbar` configuration files.

The session begins with a strong warning that the workflow involves touching Chief Architect configuration files outside the application. The recommended safety practice is to make backups, avoid asking Chief Architect support to troubleshoot self-modified configuration files, and only edit the narrow toolbar code sections that are understood.

The main workflow uses two helper programs: Notepad++ for inspecting and editing toolbar configuration text files, and TreeSize Free for finding the temporary Chief Architect backup directory while managed resources are being backed up. The key trick is that managed Chief Architect resources are temporarily decrypted into a temp directory during backup creation, and toolbar files can be copied from that temp directory before the backup completes and the temp files are deleted.

Inside Chief Architect, the video shows how to create a new toolbar by dragging tools into an empty toolbar area, rename the toolbar, control which view types it appears in, turn it off by default, and make it available as a right-click toolbar toggle. It also shows why floating toolbars should be docked before sharing configurations with other users to avoid toolbars opening off-screen on different monitor setups.

The video then demonstrates adding a custom Place Library Object button, linking it to an extended style painter library object, and assigning it a custom PNG icon. The icon workflow uses existing Chief Architect button resources as visual references, Photoshop or Photopea for editing, 128 x 128 transparent PNG output, and Chief Architect's browse button to attach the custom icon to the toolbar button.

The most advanced section shows copying toolbar definitions from one configuration file to another. The safe edit is to copy the line containing the toolbar's tool codes from a source `.toolbar` file and paste it over the corresponding line in the destination `.toolbar` file. The video warns not to rename the toolbar or edit the view-state code while doing this, because invalid codes can break the toolbar configuration and require a reset.

The ending covers related tips: adding toolbar-configuration-switch buttons to an existing toolbar, choosing icons for those configuration buttons, adjusting Chief Architect color preferences for dark mode visibility issues, understanding the basic structure of toolbar config files, resetting toolbars if they break, using Stream Deck or 3D mouse radial menus for hotkey workflows, and current Pro Plan X18 beta/template updates.

## Key Topics

- Chief Architect X18 toolbar customization
- Hidden and toggleable toolbars
- Time logging toolbar setup
- Custom Place Library Object buttons
- Linking toolbar buttons to library objects
- Creating Chief-style custom toolbar icons
- Photoshop and Photopea icon editing
- Chief Architect dark and light icon folders
- Backing up before modifying configuration files
- Managed resource backup temp directories
- Using TreeSize to locate temporary backup files
- Copying `.toolbar` files during backup generation
- Editing toolbar configuration files in Notepad++
- Transferring toolbars between configurations
- View-type visibility codes in toolbar files
- Built-in tool codes vs custom tool codes
- Resetting Chief Architect toolbars
- Docking shared toolbars to avoid off-screen placement
- Stream Deck and 3D mouse radial menu alternatives
- Pro Plan X18 beta updates and area analysis troubleshooting

## Chapters

- `00:01` Opening, live-show intro, broken toe story, and warning about risky toolbar hacking
- `01:58` Safety disclaimer: make backups and do not ask Chief Architect support to fix self-modified config files
- `02:56` Why toolbar transfer is needed, especially with project management mode
- `03:28` Recommended utility: Notepad++ for color-coded config editing
- `04:42` Recommended utility: TreeSize Free for scanning directories and locating temp files
- `05:32` Using TreeSize to inspect disk usage and Chief Architect-related storage
- `06:08` Discussion of RAID 0 drives, backup speed, and Chief Architect file-write performance
- `07:27` Live chat greetings and custom-library-button limit discussion
- `09:29` Goal for the session: create a custom tool and move it to other toolbar configurations
- `10:07` Tip: pin other toolbar configurations as buttons inside the current configuration
- `11:05` Pro Plan template help/manual and Discord suggestion workflow
- `12:17` Why Rabbitt Design toolbars contain many custom tools
- `13:37` Creating a hidden Time Tracker toolbar
- `13:49` Opening Customize Toolbars from right-click or Tools menu
- `14:21` Dragging tools to blank toolbar space vs adding to an existing toolbar
- `15:25` Renaming a new toolbar and choosing view-type availability
- `16:43` Turning the toolbar off by default and exposing it as a right-click toggle
- `17:30` Example of terrain toolbars as temporary floating toolbars
- `17:51` Why shared toolbars should be docked before distribution
- `18:42` Chat discussion about custom Place Library Object icons changing unexpectedly
- `20:36` Adding a Place Library Object tool to a toolbar
- `21:47` Linking the custom toolbar button to an Extended Style Painter object
- `22:22` Chief Architect generates a default icon for the linked object
- `23:07` Locating Chief Architect button resources in Program Files
- `23:43` X18 dark and light icon folders
- `24:20` Swapping dark and light icon folders and the need for backups
- `24:53` Choosing an existing cabinet icon as a starting point
- `25:19` Editing an icon in Photoshop with Chief Architect-style colors
- `26:51` Exporting the new icon as a transparent PNG
- `27:42` Assigning the custom PNG icon to the toolbar button
- `28:57` Main trick: transferring toolbars between configurations outside Chief Architect
- `29:25` Creating a placeholder toolbar in the target configuration
- `30:41` Lack of direct toolbar export in managed mode
- `31:00` How managed backup decrypts resources into a temporary directory
- `32:01` Capturing toolbar files before backup completion
- `33:48` Finding `%AppData%`, local app data, and temp folders on Windows
- `35:40` Looking for the active Chief Architect temp directory
- `36:12` Starting Backup Managed Resources
- `36:52` Refreshing TreeSize and watching temp folders grow
- `37:15` Opening the temporary settings folder containing toolbar configs
- `38:48` Waiting for the desired `.toolbar` files to appear
- `39:48` Copying source and target `.toolbar` files to Downloads
- `40:39` Opening both toolbar files in Notepad++ side by side
- `41:29` Finding the source Time Logging toolbar definition
- `42:14` Understanding blank view-state lines and why not to edit them
- `43:50` Copying the toolbar tool-code line from source to target
- `44:59` Copying the modified Kitchen Base Cabinets toolbar line
- `45:34` Importing the edited toolbar configuration back into Chief Architect
- `46:25` Handling import conflicts and replace/duplicate choices
- `47:49` Confirming the transferred Time Tracker toolbar and custom tool work
- `48:19` Cleanup: rename and hide the transferred toolbar
- `48:43` Adding buttons that switch to other toolbar configurations
- `49:52` Choosing custom icons for toolbar-configuration buttons
- `50:27` Icon sizing guidance: keep icons 128 x 128
- `51:13` Dark mode icon and interface color preference discussion
- `53:34` Explaining toolbar config file structure
- `55:02` Custom button data folders, custom icon numbers, and tool code prefixes
- `57:31` Resetting toolbars from preferences if a configuration breaks
- `58:37` Stream Deck and 3D mouse radial menu hotkey workflows
- `59:57` Initial wrap-up and Chief Architect event discussion
- `1:00:53` Pro Plan stability and current beta/version notes
- `1:02:54` Correction: current version vs development version in Discord
- `1:04:04` New working-light view, project information fields, and title block data
- `1:07:15` Area analysis troubleshooting schedule bonus tip
- `1:08:18` Final close

## Search Keywords

- Chief Architect toolbar tricks
- Chief Architect X18 toolbar configuration
- Chief Architect custom toolbar
- Chief Architect hidden toolbar
- Chief Architect toggle toolbar
- Chief Architect time tracker toolbar
- Chief Architect custom place library object
- Chief Architect custom library button
- Chief Architect toolbar icon
- Chief Architect icon PNG
- Chief Architect dark icons
- Chief Architect light icons
- Chief Architect resources buttons dark
- Chief Architect resources buttons light
- Chief Architect .toolbar file
- Chief Architect toolbar config file
- Chief Architect managed resources backup
- Chief Architect temp directory
- TreeSize Chief Architect backup
- Notepad++ toolbar config
- transfer toolbar between configurations
- copy toolbar from one configuration to another
- toolbar view type codes
- toolbar tool codes
- custom 137 toolbar icon
- reset Chief Architect toolbars
- Chief Architect toolbar off screen
- dock toolbar before sharing
- Chief Architect Stream Deck
- Chief Architect 3D mouse radial menu
- Pro Plan Chief Architect X18
- Rabbitt Design Pro Plan
- area analysis troubleshooting Chief Architect
- Chief Architect dark mode preferences
- Chief Architect table input background
