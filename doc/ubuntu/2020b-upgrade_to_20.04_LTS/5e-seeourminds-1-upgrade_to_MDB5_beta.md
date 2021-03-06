
# 5e-seeourminds-1-upgrade_to_MDB5_beta.md

Continuing to update SeeOurMinds.com .

# Upgrade to MDB5

For hints about how to do this, see `6-mdb5_tips_and_tricks.md`.

# Choose: Download or Use MDB CLI

The MDB CLI files have a more recent date:

- Mdb cli: 7/30
- Downloaded: 7/20

## Comparing File Listings

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

## `.mdb` Hidden File

Not shown above, the mdb-cli files include a hidden file:

```
$ cat mdb-cli/MDB5-Free/.mdb
{
  "packageName": "MDB5-Free"
}$
```

Presumably I can use the mdb cli to updates these at some future time.

## Using the Mdb Cli Files

It looks like it would be best to use the mdb cli files.

# Copy in Code

## Save Current Versions in `*-old` Directories

This makes it easy to grab the few custom files I have created as they are needed.

```
g mv  README.md  README-seeourminds.md
gc 'Renaming README.md to README-seeourminds.md .'
g mv README-MDB.txt README.txt
gc 'Renaming README-MDB.txt to README.txt , so it will be overwritten by the new version from MDB, if indeed there are changes.'
l
g mv css css-old , to save a copy of the old files.'
gc 'Renaming css to css-old , to save a copy of the old files, at least until I get the site working well with MDB5.'
g mv js js-old
gc 'Renaming js to js-old , to save a copy of the old files, at least until I get the site working well with MDB5.'
```

I shouldn't have to use these files, but it's nice to have them close by, in case I run into issues.

## Copy in the MDB CLI Files

Copy in the new files generated by running mdb cli.

```
l /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/
mv  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/.mdb .
ga .mdb
gc 'Adding hidden file static/content/.mdb , which was created by mdb cli.'
rm -fr img/
gc 'Deleted everything in the static/content/img directory because it is no longer needed by MDB5.'
ga  index-mdb5_template.html
gc 'Adding index-mdb5_template.html , which shows the tags I need to use in the django base.html template.'
l /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/
mv  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/License.pdf  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/README.txt  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/css  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/js  /var/www/seeourminds.com/htdocs/seeourminds.com/mdb-cli/MDB5-Free/src/ .
g rm static/content/License-MDB.pdf
gc 'Removing static/content/License-MDB.pdf because it is an obsolete MDB4 file.'
ga static/content/License.pdf
gc 'Adding the new MDB5 license file as static/content/License.pdf .'
ga static/content/README.txt
gc 'Adding the new MDB5 README.txt file as static/content/README.txt .'
ga static/content/css
gc 'Adding the new MDB5 css files in static/content/css .'
ga static/content/js
gc 'Adding the new MDB5 js files in static/content/js .'
ga static/content/src/
gc 'Adding the MDB5 src files in static/content/src/ .'
```

# Update the Django `base.html` Template

Using `static/content/index-mdb5_template.html` as a model, update the `templates/content/base.html` template.

- [x] Paste menu code from site into `base.html`
- [x] Update menu code to work with my items

## Fixing the Menu

Pasted in the code from the mdb site and it did not work at first.

Had some vexing issues but figured out the issue, which was quite stupid.
It turned out that I'd forgotten to add the django template code enabling it to find the `mdb.min.css` file.  D'oh!

Once I worked through my stupid issue, updating the menu code from the mdb template to contain my options is straightforward.

## Fontawesome Warning

Chrome dev tools gives this warning in the dev tools console when using my fontawesome link tag:

- "A cookie associated with a cross-site resource at http://fontawesome.com/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application>Storage>Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032."

It does not give a warning when using the fontawesome link tag that came with the MDB5 sample index.html file,
but the MDB5 sample file gives the same warning when using my fontawesome link tag.

### Maybe Try to Fix This Later

Tried a few things, but they didn't work.

- The stupid problems I was having with the menu were unrelated to this
- It's just a warning
- Maybe try to fix this later

Note that the warning also shows up on Groja.com , I just didn't notice it.
And from what I can tell, it is fontawesome's "fault."

### Tried a Few Things

Found a possible solution here:

- https://stackoverflow.com/questions/58270663/samesite-warning-chrome-77

I thought that adding this code inside my fontawesome tag fixed the issue,
but it seems like maybe the warning just goes away sometimes after reloads,
unless I change some of the markup.

```
response.setHeader("Set-Cookie", "HttpOnly;Secure;SameSite=Strict");
```

Also tried this fix, as suggested by the error message, **TO NO AVAIL:**

Added `SameSite=None` and `SameSite=Secure` to the link tag, and the warning message goes away,
**ONLY TO REAPPEAR WHEN I CHANGE CONTENT ON THE PAGE.**

Oh well.

# Update the Django `home.html` Template

## Masking Issue

It took some time to get the mask to work on the home page.

- 1. It would not work no matter what I would try
   - Even pasting code from the site into the mdb index.html template did not work
- 2. Copying the mdb css files from groja.com made it work ok, yay!
- 3. Was ready to ask about this in the mdb forum, but noticed that MDB5 beta is out
- 4. Tried to use mdb cli to update - see below - but that did not update the css files (*)
- 5. Downloaded the mdb5 beta package, copied the css files in, and it worked!!

(*) Tried using mdb cli to update css files:

```
$ mdb update
npm WARN deprecated core-js@2.6.11: core-js@<3 is no longer maintained and not recommended for usage due to the number of issues. Please, upgrade your dependencies to the actual version of core-js@3.
/usr/local/bin/mdb -> /usr/local/lib/node_modules/mdb-cli/index.js
+ mdb-cli@1.1.34
updated 2 packages in 25.281s
┌─────────┬────────┬───────────┐
│ (index) │ Status │  Message  │
├─────────┼────────┼───────────┤
│    0    │   0    │ 'Success' │
└─────────┴────────┴───────────┘
$
```

### Masking Issue Fix

This did not change the css files, however.
Maybe they got "updated" some place else and need to be installed somehow?

Downloading the beta version and copying in the files is what finally worked!

```
gosmss         # /var/www/seeourminds.com/htdocs/seeourminds.com/Site/content/static/content
l   /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/css/
l css
cp  /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/css/*
l   /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/js
l js
cp   /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/js/* js
cp  /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/index.html index-mdb5_template-current.html
gs .
ga .mdb
gc 'Running mdb cli updated the .mdb file but did not update my css files.'
ga css/mdb.min.css*
gc 'Updating css/mdb.min.css* to the beta versions downloaded from the site.'
ga js/mdb.min.js*
gc 'Updating the js/mdb.min.js* files to the beta versions downloaded from the site.'
ga index-mdb5_template-current.html
gc 'Adding the new version of the mdb5 index.html template file as index-mdb5_template-current.html .'
g mv index-mdb5_template.html index-mdb5_template-alpha_exp.html .'
gc 'Renaming the alpha version of the mdb5 index.html template file, which I have updated a time or two, from index-mdb5_template.html to index-mdb5_template-alpha_exp.html .'
```

## Rest of Home Page

- Fixed mdb5 classes in the form
- Had to add some hacky extra rows to the above-the-fold area
  - Thinking this might be due to using the beta release
- Adjusted margins in elements above-the-fold
- Fixed shadows in the cards in the below-the-fold area
  - The `hover-shadow` class does not seem to be working
  - Thinking this might be due to using the beta release

## Rest of Site

- [x] Quiz pages
- [x] Legal pages
- [x] Gallery pages
    - [x] Templates
    - [x] Check blockquote tags in these files, and update (*) as necessary:
        - [x] 0800-real-famous-world-famous.json
        - [x] 1410-fictional-tv-game_of_thrones-house_stark.json
        - [x] 1420-fictional-tv-game_of_thrones-house_baratheon.json
        - [x] 1430-fictional-tv-game_of_thrones-house_lannister.json
        - [x] 1440-fictional-tv-game_of_thrones-house_tyrell.json
        - [x] 1470-fictional-tv-game_of_thrones-no_house.json
        - [x] 1490-fictional-tv-game_of_thrones-other_houses.json
        - [x] 2400-fictional-tv-sopranos.json
        - [x] 2500-fictional-tv-twin_peaks-laura_and_friends.json
        - [x] 2800-fictional-tv-cheers-sam_and_diane.json
        - [x] 2810-fictional-tv-cheers-the_crew.json
        - [x] 2820-fictional-tv-cheers-customers.json
        - [x] 3310-fictional-tv-true_detective-1.json
        - [x] 3320-fictional-tv-true_detective-2.json
        - [x] 4900-politicians-founding_fathers.json
        - [x] 5000-politicians-us_presidents-1700s-1800s.json
        - [x] 5040-politicians-us_presidents-1900s.json

(*) Ensure all blockquote tags have `class='blockquote'` attribute set

