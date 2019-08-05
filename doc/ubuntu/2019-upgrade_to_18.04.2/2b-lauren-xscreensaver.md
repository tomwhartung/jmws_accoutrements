
# 2-lauren-xscreensaver.md

How to install xscreensaver after upgrading to 18.04 LTS.

## Reference

- https://www.debugpoint.com/2018/08/install-change-autostart-setup-screensaver-ubuntu-linux/

## Process

#### 1. Install

As root:
```
apt-get install xscreensaver xscreensaver-gl-extra xscreensaver-data-extra
apt-get remove gnome-screensaver   # "Package 'gnome-screensaver' is not installed, so not removed"
```

#### 2. Launch and Add to Launcher

Launch on command line:

As tomh:
```
xscreensaver -nosplash
```

#### 3. Ensure it Will run automatically

Find Startup Programs in dock search tool and ensure it will run when system boots.

#### 4. Add to Launcher

Find xscreensaver icon in dock search tool and add it to the Launcher.

#### 5. Adjust settings as necessary

Check times and other parameters in dialog.

