
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

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Installing Additional Required Packages

Postgres is needed I am sure, but will do this later.

# Technical Updates

## Security Issue

Examine security issue flagged by github:

- https://github.com/tomwhartung/groja.com/network/alert/Site/static/js/jquery-3.3.1.min.js/jquery/open

## Broken Icons

Icons are broken.

1. Figure out why
2. Figure out why they work ok on the other sites
3. Fix to work like the other sites, as appropriate

# Content Updates

The content on this site is OK as-is.

# Review

Review conversions with an eye to prevent spam.

Ensure social media icons link to correct accounts.

