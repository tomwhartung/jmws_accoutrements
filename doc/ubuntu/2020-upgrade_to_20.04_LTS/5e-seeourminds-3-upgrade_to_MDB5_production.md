
# 5e-seeourminds-3-upgrade_to_MDB5_production.md

While continuing to update SeeOurMinds.com the MDB5 team released the production version.

# Upgrade to MDB5 Production

## Choose: Download or Use MDB CLI

### How to use Mdb Cli?

Apparently mdb cli has no option to update already-installed code:

```
 $ mdb help
┌─────────┬─────────────────────┬─────────────────────────────────────────────────────────────────┐
│ (index) │       Command       │                           Description                           │
├─────────┼─────────────────────┼─────────────────────────────────────────────────────────────────┤
│    0    │       'help'        │                        'show this info'                         │
│    1    │      'logout'       │                        'logout from cli'                        │
│    2    │       'list'        │                    'list available packages'                    │
│    3    │      'orders'       │                     'list all your orders'                      │
│    4    │       'init'        │                   'initialize chosen package'                   │
│    5    │      'publish'      │                     'publish your project'                      │
│    6    │     'unpublish'     │          'remove your project from the public server'           │
│    7    │     'set-name'      │                   'change your project name'                    │
│    8    │      'rename'       │ 'change your project name and update name on the public server' │
│    9    │     'projects'      │               'list all your published projects'                │
│   10    │  'set-domain-name'  │             'set the domain name for your project'              │
│   11    │ 'unset-domain-name' │           'remove the domain name from this project'            │
│   12    │      'update'       │             'update mdb-cli to the latest version'              │
│   13    │   'version (-v)'    │                     'print mdb-cli version'                     │
└─────────┴─────────────────────┴─────────────────────────────────────────────────────────────────┘
$
```

To use mdb cli to get new code, apparently I need to run `mdb init`

And before doing that, we might as well update mdb cli and npm:

**Note:** must be root to update mdb and npm.

```
$ mdb update
npm WARN deprecated core-js@2.6.11: core-js@<3 is no longer maintained and not recommended for usage due to the number of issues. Please, upgrade your dependencies to the actual version of core-js@3.
/usr/local/bin/mdb -> /usr/local/lib/node_modules/mdb-cli/index.js
+ mdb-cli@2.0.1
updated 3 packages in 20.008s


   ╭────────────────────────────────────────────────────────────────╮
   │                                                                │
   │      New patch version of npm available! 6.14.4 → 6.14.7       │
   │   Changelog: https://github.com/npm/cli/releases/tag/v6.14.7   │
   │               Run npm install -g npm to update!                │
   │                                                                │
   ╰────────────────────────────────────────────────────────────────╯

┌─────────┬────────┬───────────┐
│ (index) │ Status │  Message  │
├─────────┼────────┼───────────┤
│    0    │   0    │ 'Success' │
└─────────┴────────┴───────────┘
$ npm install -g npm
/usr/local/bin/npm -> /usr/local/lib/node_modules/npm/bin/npm-cli.js
/usr/local/bin/npx -> /usr/local/lib/node_modules/npm/bin/npx-cli.js
+ npm@6.14.8
added 434 packages from 885 contributors in 57.579s
$
```

### Using `mdb init`

Running `mdb init` in an empty directory:

```
gosm                  # /var/www/seeourminds.com/htdocs/seeourminds.com
mkdir mdb5-init
cd  mdb5-init
mdb help
mdb login
mdb init
l
l MDB5-Free/
cd  MDB5-Free/
```

**Note:** adding `mdb5-init` to `.gitignore`.

### Comparing the Files

The MDB CLI files have a more recent date:

- Mdb cli: 8/31
- Downloaded: 8/24

**HOWEVER,** I believe that is just because 8/31 is today's date.

I am not going to dive down into comparing these, but will only check the initial comments in `` and ``:

```
gosm                  # /var/www/seeourminds.com/htdocs/seeourminds.com
cd mdb5-init/MDB5-Free     # mdb cli version
more css/mdb.min.css
more js/mdb.min.js
```

Both versions show `Version: FREE 1.0.0` in both `css/mdb.min.css` and `js/mdb.min.js`.

## Deciding to Use Download Version

I am picking the download version, because I am more used to that sort of process.

**MOREOVER,** based on the options displayed by the `mdb help` command it appears to me that mdb cli is tailored towards publishing sites on their site.

# Using the Downloaded Version

Ran the following commands to perform the upgrade:

```
cd css
l
l /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/css/
cp  /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/css/* .
l
cd ../js
l /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/js
l
l /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/js
cp  /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/js/* .
cd ../src
l
cf
rm -fr js/ scss/
l /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/src/
cp -r /var/www/seeourminds.com/htdocs/seeourminds.com/unpack/mdb5/Free-1.0.0/src/* .
```

Ran a quick test of the site and decided to commit the files:

```
ga static/content/css static/content/js static/content/src/
gc 'Updated static css, js, and src files to MDB5 production version.'
```

