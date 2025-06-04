
# 3b-home_tomh-barbara-disk_usage.md

# What's What in My home Directory

Most of what I want to move over to the new install is in the tarHome tar file:

- Note: `tarHome` has been recently updated to get more relevant files
- So `home_tomh-tarHome_file/barbara-home_tomh-2025_06_03.tgz` should have everything I need

HOWEVER, since I'll be overwriting what's here, it would be nice to save the whole thing.

- Trying to tar up all of `/home/tomh` creates a file that is too large for this FAT drive!  RATS!!
- See details below

SO, copy all of /home/tomh to /media/tomh/2023-32A/for_barbara-24.04/home, like so:
- cd /media/tomh/2023-32A/for_barbara-24.04/home
- cp -r /home/tomh .
- This should have it all, just in case
- Turns out I need to delete the `~/tmp` and `~/.config` directories
  - For details, see the next section

## Where is all of this space being used?

This is how I figured out I needed to delete the `~/tmp` and `~/.config` directories.

- About half of the 7G is in .cache
  - 2.839G - .cache: not needed on new install
  - 0.605G - .config: best to start with new .config files
- Almost 1G is in .thunderbird, which we don't use anymore
- 0.153G - backup: don't really need to keep this, but OK
- 0.198G - Downloads: don't really need to keep this, but OK
- 0.693G - tmp: don't really need to keep this, and it contains a lot of junk
- 0.837G - snap: used by the OS
- 0.861G - personal: OK

## Gory Details From the Command Line:

```
tomh@barbara: ~
 $ du -sm .[a-zA-Z]* ; du -sm * | sort -n
1       .Xauthority
1       .bash_aliases
1       .bash_aliases-ava
1       .bash_aliases-barbara
1       .bash_aliases-bette
1       .bash_aliases-groja1
1       .bash_aliases-humphrey
1       .bash_aliases-jane
1       .bash_aliases-lauren
1       .bash_aliases-martha
1       .bash_aliases-mary
1       .bash_aliases-rita
1       .bash_aliases-veronica
1       .bash_history
1       .bash_profile
1       .bashrc
2839    .cache
605     .config
1       .gitconfig
1       .gnome
1       .gnupg
1       .gtkrc-2.0
163     .kde
1       .lesshst
47      .local
362     .mozilla
177     .npm
1       .pki
1       .ssh
1       .ssh-ava
0       .sudo_as_admin_successful
944     .thunderbird
2       .vim
1       .viminfo
1       .vimrc
1       .xscreensaver
1       .xscreensaver-10-15-20
1       .xscreensaver-15-25-30-35
1       .xscreensaver-30-45-55-60
1       .xscreensaver-300-450-550-600
1       .xscreensaver-45-60-65-70
1       .xscreensaver-5-10-15
1       .xscreensaver-60-75-80
1       .xscreensaver-day
1       .xscreensaver-night
1       .xsession-errors
6       .zoom
0       index.html
0       var_www
1       Desktop
1       Documents
1       Music
1       Public
1       RCS
1       Template
1       Videos
1       bin
1       d.e
1       jobsearch
1       r
1       r.140
1       r.160
1       r.200
1       r.80
1       r.vert
2       technical
7       work
13      Pictures
27      Calibre Library
153     backup
198     Downloads
693     tmp
837     snap
861     personal
tomh@barbara: ~
 $
```

