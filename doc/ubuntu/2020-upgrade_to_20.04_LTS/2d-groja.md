
# 2b-groja.md

Updating Groja.com .

# Getting the Site to Run Locally

After installing flask and providing a `gitignored/Site/groja_config.py` file, the site still needed some help.

## Grabbing a Copy of the Database

Copy the required db files from the production host, `ava`.

```
$ gog                          # /var/www/groja.com/htdocs/groja.com
$ cd gitignored/db/
$ l
total 0
-rw-r--r-- 1 tomh tomh 0 May  9 16:08 .this_dir_intentionally_left_empty
$ fromAva NameEmail.db
. . .
. . .
. . .
$ fromAva NameEmailSchema.sql
. . .
. . .
. . .
$
```

# Technical Updates

## Security Issue

Examine security issue flagged by github:

- https://github.com/tomwhartung/groja.com/network/alert/Site/static/js/jquery-3.3.1.min.js/jquery/open

### The Fix

Github says the fix is to upgrade jquery to 3.5+.

Note: **MDB 4 uses jQuery 3.5.1,** and we are using MDB 4 on the new tomwhartung.com.

- 1. Update jQuery to see if warning goes away
- 2. If it does, update the remaining MDB files

This fix works ok!
However, now we really **need to run a regression test on the entire site** to make sure everything still looks ok.

## Broken Icons

Icons are broken.

Fixed by copying link tag used for font Awesome from seeourminds.com .

**Note: tried using the link tag content used on the new tomwhartung.com - which is what the MDB site
recommends for using with MDB 4 - and it did not work.**
That is just an FYI, something to think about when we get to working on that site.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Installing Additional Required Packages

Postgres may be needed I am not totally sure, but will look into this later.

Or the site might use sqlite?  Need to make sure, but I am anxious to do my server shuffle.

# Content Updates

The content on this site is OK as-is.

# Review

Review conversions with an eye to prevent spam.

Ensure social media icons link to correct accounts.

