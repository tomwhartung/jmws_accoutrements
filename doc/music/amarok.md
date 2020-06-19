
# amarok.md

Moving my amarok config from barbara to bette.

I tested this once before, now I hope to do it for reals.

# Amarok Config

It's in `~/.kde/share`:

```
$ cd
$ cd .kde/share/
$ lsd */amar*
drwx------ 8 tomh tomh 4096 May  9 08:28 apps/amarok
drwx------ 7 tomh tomh 4096 May  8 13:29 apps/amarok-old
-rw------- 1 tomh tomh  220 May  9 08:28 config/amarok-appletsrc
-rw------- 1 tomh tomh  221 May  8 13:29 config/amarok-appletsrc-old
-rw------- 1 tomh tomh  120 May  9 08:28 config/amarok_homerc
-rw------- 1 tomh tomh   84 May  8 13:29 config/amarok_homerc-old
-rw------- 1 tomh tomh 3977 May  9 08:28 config/amarokrc
-rw------- 1 tomh tomh 2704 May  8 13:29 config/amarokrc-old
tomh@bette: ~/.kde/share
 $ ls -1d */amar*
apps/amarok
apps/amarok-old
config/amarok-appletsrc
config/amarok-appletsrc-old
config/amarok_homerc
config/amarok_homerc-old
config/amarokrc
config/amarokrc-old
$
```

We want to rename those directories, to make the names more self-explanatory and to make room for the files from barbara,
which we have in a tar file.

```
$ pwd
/home/tomh/.kde/share
$ ls -1d */amar*  > mv-1.sh
$ cp  mv-1.sh  mv-2.sh
$ vi mv-*
2 files to edit
$ paste mv-*
mv apps/amarok apps/amarok-test-delete_me
mv apps/amarok-old apps/amarok-installed
mv config/amarok-appletsrc config/amarok-appletsrc-test-delete_me
mv config/amarok-appletsrc-old config/amarok-appletsrc-installed
mv config/amarok_homerc config/amarok_homerc-test-delete_me
mv config/amarok_homerc-old config/amarok_homerc-installed
mv config/amarokrc config/amarokrc-test-delete_me
mv config/amarokrc-old config/amarokrc-installed
$ paste mv-* > mv.sh
$ chmod +x mv.sh
$ l
total 24
drwx------ 11 tomh tomh 4096 May  8 16:07 apps
drwxrwxr-x  2 tomh tomh 4096 Jun 18 13:41 config
drwx------  3 tomh tomh 4096 Dec 23  2016 kde4
-rw-r--r--  1 tomh tomh  186 Jun 18 19:44 mv-1.sh
-rw-r--r--  1 tomh tomh  246 Jun 18 19:45 mv-2.sh
-rwxr-xr-x  1 tomh tomh  432 Jun 18 19:45 mv.sh
$ ls -1d */amar*
apps/amarok
apps/amarok-old
config/amarok-appletsrc
config/amarok-appletsrc-old
config/amarok_homerc
config/amarok_homerc-old
config/amarokrc
config/amarokrc-old
$ ./mv.sh
$ ls -1d */amar*
apps/amarok-installed
apps/amarok-test-delete_me
config/amarok-appletsrc-installed
config/amarok-appletsrc-test-delete_me
config/amarok_homerc-installed
config/amarok_homerc-test-delete_me
config/amarokrc-installed
config/amarokrc-test-delete_me
$
```

Now unpack the tar file in subdirectory `unpack`, just to be "safe," and move the unpacked files to where they belong.

```
$ l
total 27868
-rw-r--r--  1 tomh tomh 28509126 Jun 18 19:42 amarok-2020_06_18-barbara.tgz
drwx------ 11 tomh tomh     4096 Jun 18 19:45 apps
drwxrwxr-x  2 tomh tomh     4096 Jun 18 19:45 config
drwx------  3 tomh tomh     4096 Dec 23  2016 kde4
-rw-r--r--  1 tomh tomh      186 Jun 18 19:44 mv-1.sh
-rw-r--r--  1 tomh tomh      246 Jun 18 19:45 mv-2.sh
-rwxr-xr-x  1 tomh tomh      432 Jun 18 19:45 mv.sh
$ mkdir unpack
$ mv amarok-2020_06_18-barbara.tgz  unpack
$ cd  unpack
$ tar -xvzf amarok-2020_06_18-barbara.tgz
. . .
. . .
. . .
$ cd ..
$ pwd
/home/tomh/.kde/share/unpack
$ pwd
/home/tomh/.kde/share
 $ l
total 28
drwx------ 11 tomh tomh 4096 Jun 18 19:45 apps
drwxrwxr-x  2 tomh tomh 4096 Jun 18 19:45 config
drwx------  3 tomh tomh 4096 Dec 23  2016 kde4
-rw-r--r--  1 tomh tomh  186 Jun 18 19:44 mv-1.sh
-rw-r--r--  1 tomh tomh  246 Jun 18 19:45 mv-2.sh
-rwxr-xr-x  1 tomh tomh  432 Jun 18 19:45 mv.sh
drwxr-xr-x  4 tomh tomh 4096 Jun 18 19:46 unpack
 $ l unpack/
total 27856
-rw-r--r-- 1 tomh tomh 28509126 Jun 18 19:42 amarok-2020_06_18-barbara.tgz
drwxr-xr-x 3 tomh tomh     4096 Jun 18 19:46 apps
drwxr-xr-x 2 tomh tomh     4096 Jun 18 19:46 config
 $ l apps/
total 11596
drwx------ 2 tomh tomh     4096 Jan 28  2017 RecentDocuments
drwx------ 7 tomh tomh     4096 May  8 13:29 amarok-installed
drwx------ 8 tomh tomh     4096 May  9 08:28 amarok-test-delete_me
drwxrwxr-x 2 tomh tomh     4096 Jun 18 13:41 color-schemes
drwx------ 4 tomh tomh     4096 May  8 13:22 desktoptheme
drwx------ 3 tomh tomh     4096 Dec 23  2016 kconf_update
drwx------ 2 tomh tomh     4096 May  9 08:18 kcookiejar
-rw-r--r-- 1 tomh tomh 11837160 May  8 13:41 kde_share_apps_amarok.tgz
drwx------ 3 tomh tomh     4096 Dec 23  2016 kssl
drwxr-xr-x 2 tomh tomh     4096 May 22 21:33 kwallet
 $ l unpack/apps/
total 4
drwx------ 7 tomh tomh 4096 Jun 18 16:41 amarok
 $ mv  unpack/apps/amarok apps/
 $ l apps/
total 11600
drwx------ 2 tomh tomh     4096 Jan 28  2017 RecentDocuments
drwx------ 7 tomh tomh     4096 Jun 18 16:41 amarok
drwx------ 7 tomh tomh     4096 May  8 13:29 amarok-installed
drwx------ 8 tomh tomh     4096 May  9 08:28 amarok-test-delete_me
drwxrwxr-x 2 tomh tomh     4096 Jun 18 13:41 color-schemes
drwx------ 4 tomh tomh     4096 May  8 13:22 desktoptheme
drwx------ 3 tomh tomh     4096 Dec 23  2016 kconf_update
drwx------ 2 tomh tomh     4096 May  9 08:18 kcookiejar
-rw-r--r-- 1 tomh tomh 11837160 May  8 13:41 kde_share_apps_amarok.tgz
drwx------ 3 tomh tomh     4096 Dec 23  2016 kssl
drwxr-xr-x 2 tomh tomh     4096 May 22 21:33 kwallet
 $ l unpack/
total 27856
-rw-r--r-- 1 tomh tomh 28509126 Jun 18 19:42 amarok-2020_06_18-barbara.tgz
drwxr-xr-x 2 tomh tomh     4096 Jun 18 19:47 apps
drwxr-xr-x 2 tomh tomh     4096 Jun 18 19:46 config
 $ l unpack/config/
total 16
-rw------- 1 tomh tomh  220 Jun 18 16:41 amarok-appletsrc
-rw------- 1 tomh tomh  120 Jun 18 16:41 amarok_homerc
-rw------- 1 tomh tomh 5301 Jun 18 16:41 amarokrc
 $ l config/
total 92
-rw------- 1 tomh tomh  221 May  8 13:29 amarok-appletsrc-installed
-rw------- 1 tomh tomh  220 May  9 08:28 amarok-appletsrc-test-delete_me
-rw------- 1 tomh tomh   84 May  8 13:29 amarok_homerc-installed
-rw------- 1 tomh tomh  120 May  9 08:28 amarok_homerc-test-delete_me
-rw------- 1 tomh tomh 2704 May  8 13:29 amarokrc-installed
-rw------- 1 tomh tomh 3977 May  9 08:28 amarokrc-test-delete_me
-rw------- 1 tomh tomh 2341 Feb  3  2019 audexrc
-rw------- 1 tomh tomh   66 Dec 23  2016 drkonqirc
-rw------- 1 tomh tomh   58 Nov 15  2016 emaildefaults
-rw------- 1 tomh tomh   44 Dec 23  2016 katerc
-rw------- 1 tomh tomh 1031 May  8 13:55 kconf_updaterc
-rw------- 1 tomh tomh  104 Dec 23  2016 kcookiejarrc
-rw------- 1 tomh tomh  434 May  8 16:08 kdebugrc
-rw------- 1 tomh tomh   39 Dec 23  2016 kdedrc
-rw------- 1 tomh tomh 3468 Jun 18 13:41 kdeglobals
-rw------- 1 tomh tomh  979 May  8 13:22 kglobalshortcutsrc
-rw------- 1 tomh tomh   69 Dec 23  2016 kio_httprc
-rw------- 1 tomh tomh   92 Dec 23  2016 kioslaverc
-rw------- 1 tomh tomh   74 May  8 13:55 kmixrc
-rw------- 1 tomh tomh  120 Dec 23  2016 ktimezonedrc
-rw------- 1 tomh tomh   88 Dec 23  2016 kuriikwsfilterrc
-rw------- 1 tomh tomh   74 May  8 16:08 kwalletrc
-rw------- 1 tomh tomh   22 Dec 23  2016 phonondevicesrc
 $ mv unpack/config/amarok*  config/
 $ l config/
total 108
-rw------- 1 tomh tomh  220 Jun 18 16:41 amarok-appletsrc
-rw------- 1 tomh tomh  221 May  8 13:29 amarok-appletsrc-installed
-rw------- 1 tomh tomh  220 May  9 08:28 amarok-appletsrc-test-delete_me
-rw------- 1 tomh tomh  120 Jun 18 16:41 amarok_homerc
-rw------- 1 tomh tomh   84 May  8 13:29 amarok_homerc-installed
-rw------- 1 tomh tomh  120 May  9 08:28 amarok_homerc-test-delete_me
-rw------- 1 tomh tomh 5301 Jun 18 16:41 amarokrc
-rw------- 1 tomh tomh 2704 May  8 13:29 amarokrc-installed
-rw------- 1 tomh tomh 3977 May  9 08:28 amarokrc-test-delete_me
-rw------- 1 tomh tomh 2341 Feb  3  2019 audexrc
-rw------- 1 tomh tomh   66 Dec 23  2016 drkonqirc
-rw------- 1 tomh tomh   58 Nov 15  2016 emaildefaults
-rw------- 1 tomh tomh   44 Dec 23  2016 katerc
-rw------- 1 tomh tomh 1031 May  8 13:55 kconf_updaterc
-rw------- 1 tomh tomh  104 Dec 23  2016 kcookiejarrc
-rw------- 1 tomh tomh  434 May  8 16:08 kdebugrc
-rw------- 1 tomh tomh   39 Dec 23  2016 kdedrc
-rw------- 1 tomh tomh 3468 Jun 18 13:41 kdeglobals
-rw------- 1 tomh tomh  979 May  8 13:22 kglobalshortcutsrc
-rw------- 1 tomh tomh   69 Dec 23  2016 kio_httprc
-rw------- 1 tomh tomh   92 Dec 23  2016 kioslaverc
-rw------- 1 tomh tomh   74 May  8 13:55 kmixrc
-rw------- 1 tomh tomh  120 Dec 23  2016 ktimezonedrc
-rw------- 1 tomh tomh   88 Dec 23  2016 kuriikwsfilterrc
-rw------- 1 tomh tomh   74 May  8 16:08 kwalletrc
-rw------- 1 tomh tomh   22 Dec 23  2016 phonondevicesrc
 $ l unpack/
total 27856
-rw-r--r-- 1 tomh tomh 28509126 Jun 18 19:42 amarok-2020_06_18-barbara.tgz
drwxr-xr-x 2 tomh tomh     4096 Jun 18 19:47 apps
drwxr-xr-x 2 tomh tomh     4096 Jun 18 19:48 config
tomh@bette: ~/.kde/share
 $ l unpack/apps/
total 0
 $ rmdir  unpack/apps/
 $ l unpack/config/
total 0
 $ rmdir  unpack/config/
 $ l
total 28
drwx------ 12 tomh tomh 4096 Jun 18 19:47 apps
drwxrwxr-x  2 tomh tomh 4096 Jun 18 19:48 config
drwx------  3 tomh tomh 4096 Dec 23  2016 kde4
-rw-r--r--  1 tomh tomh  186 Jun 18 19:44 mv-1.sh
-rw-r--r--  1 tomh tomh  246 Jun 18 19:45 mv-2.sh
-rwxr-xr-x  1 tomh tomh  432 Jun 18 19:45 mv.sh
drwxr-xr-x  2 tomh tomh 4096 Jun 18 19:48 unpack
 $ l unpack/
total 27848
-rw-r--r-- 1 tomh tomh 28509126 Jun 18 19:42 amarok-2020_06_18-barbara.tgz

$
```

The final result:

```
$ pwd
/home/tomh/.kde/share
$ lsd  */amarok*
drwx------ 7 tomh tomh     4096 Jun 18 16:41 apps/amarok
drwx------ 7 tomh tomh     4096 May  8 13:29 apps/amarok-installed
drwx------ 8 tomh tomh     4096 May  9 08:28 apps/amarok-test-delete_me
-rw------- 1 tomh tomh      220 Jun 18 16:41 config/amarok-appletsrc
-rw------- 1 tomh tomh      221 May  8 13:29 config/amarok-appletsrc-installed
-rw------- 1 tomh tomh      220 May  9 08:28 config/amarok-appletsrc-test-delete_me
-rw------- 1 tomh tomh      120 Jun 18 16:41 config/amarok_homerc
-rw------- 1 tomh tomh       84 May  8 13:29 config/amarok_homerc-installed
-rw------- 1 tomh tomh      120 May  9 08:28 config/amarok_homerc-test-delete_me
-rw------- 1 tomh tomh     5301 Jun 18 16:41 config/amarokrc
-rw------- 1 tomh tomh     2704 May  8 13:29 config/amarokrc-installed
-rw------- 1 tomh tomh     3977 May  9 08:28 config/amarokrc-test-delete_me
-rw-r--r-- 1 tomh tomh 28509126 Jun 18 19:42 unpack/amarok-2020_06_18-barbara.tgz
$
```

We will try it tomorrow, and hope it works!

# Getting It to Work

It did not work at first - I had the layout ok but no play counts.

Uninstalling and reinstalling amarok did the trick, however!  Yay!

