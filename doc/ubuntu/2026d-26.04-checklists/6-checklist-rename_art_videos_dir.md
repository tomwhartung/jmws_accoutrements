
# 6-checklist-rename_art_videos_dir.md

This version of `6-checklist-rename_art_videos_dir.md` reflects the steps I am performing to install **Ubuntu 26.04** on `[hostname]` on **2026-05-20**.


# Goal - Big Picture

We want to start recording audio for use in videos, and so is not necessarily `music`, but
we do *not* want to create a new subdirectory in `/art`.

This is something that's done **only once**, so it makes sense we do it as we upgrade **multiple** Linux hosts to **Ubuntu 26.04**.

**Because it would be best to keep *all* Linux hosts in sync, once we do this for one host we should do it on the others ASAP.**

- [X] Directory renamed for *all* Linux hosts
  - [X] Process completed for *`martha`*
  - [X] Process completed for *`barbara`*
  - [X] Process completed for *`ava`*
  - [X] Process completed for *`jane`*
  - [X] Process completed for *`bette`*
    - [X] **Note: there is no `/art/` directory on `bette`**

# Goal - This Host

Rename `/art/videos/` to `/art/av/` on all disks, fix broken links, and update aliases.

# Process

- [X] Rename `/art/videos/` to `/art/av/` on all disks
- [X] Fix all links that point to `/art/videos/` to point to `/art/av/`
- [X] Change all `go*` aliases in `.bash_aliases` that reference `/art/videos/` to now reference `/art/av/` instead
  - [X] Note: fixing these in the file on one host enables fixing it on subsequent hosts by just scp-ing the new file on over

