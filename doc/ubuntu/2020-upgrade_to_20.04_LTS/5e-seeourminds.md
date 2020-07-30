
# 5b-seeourminds.md

Continuing to update SeeOurMinds.com .

# Upgrade to MDB5

For hints about how to do this, see `6-mdb5_tips_and_tricks.md`.

## Choose: Download or Use MDB CLI

The MDB CLI files have a more recent date:

- Mdb cli: 7/30
- Downloaded: 7/20

### Comparing File Listings

Comparing lists of downloaded files to those from MDB CLI:

```
$ l unpack/License.pdf mdb-cli/MDB5-Free/License.pdf
-rw-r--r-- 1 tomh tomh 147944 Jul 30  2020 mdb-cli/MDB5-Free/License.pdf
-rw-r--r-- 1 tomh tomh 147944 Jul 20 09:58 unpack/License.pdf
$ diff unpack/MDB-UI-KIT-Free-1.0.0-alpha4-files.txt mdb-cli/MDB5-Free/MDB5-Free-files.txt
2c2
< MDB-UI-KIT-Free-1.0.0-alpha4-files.txt
---
> MDB5-Free-files.txt
59c59
< src/js/free/dropdown.js
---
> src/js/free/animate.js
71d70
< src/js/mdb/util/keycodes.js
156a156,157
> src/scss/free/_animate-extended.scss
> src/scss/free/_animate.scss
158d158
< src/scss/free/_breadcrumb.scss
165d164
< src/scss/free/_footer.scss
167d165
< src/scss/free/_images.scss
186a185
> src/scss/free/forms/_form-outline.scss
tomh@ava: /var/www/seeourminds.com/htdocs/seeourminds.com
$
```

The mdb-cli files could indeed be a bit more up-to-date, and it makes sense that the download file could lag behind it.

### `.mdb` Hidden File

Not shown above, the mdb-cli files include a hidden file:

```
$ cat mdb-cli/MDB5-Free/.mdb
{
  "packageName": "MDB5-Free"
}$
```

Presumably I can use the mdb cli to updates these at some future time.

### Using the Mdb Cli Files

It looks like it would be best to use the mdb cli files.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Copy in Code


# CSS Issue

Hopefully upgrading to MDB5 will resolve this issue.

The content of the `blockquote` tags look just like that of the `p` tags.
Something is not right here.

Example: Nixon's page:

- http://127.0.0.1:8001/image/5040-politicians-us_presidents-1900s/5062/

# Content Updates

- [ ] Remove free spiritual portrait offer
- [ ] Consider adding a search box

# Review

## Check the Icons

Ensure social media icons link to correct accounts.

## Test the Quiz

**I made several very minor updates to class Score in `models.py`, so we need to re-test the quiz to make sure it still works.**

