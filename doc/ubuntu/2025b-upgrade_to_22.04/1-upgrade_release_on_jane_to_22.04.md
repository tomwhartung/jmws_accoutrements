
# 1-upgrade_jane.md

Jane has a lot of stuff on there (e.g., my sites and React, etc.), so we don't want to do a fresh install


# Upgrade Jane

- Upgrading to 22.04 should be straightforward and safe
- Consider upgrading to 24.04
  - Note that we can hold off on doing this for a year or two


# Preparations

- [X] Update `tarHome` to backup most relevant files for adding to new install
- [X] Run `tarHome` on jane to be sure we have the latest
- [X] Review the procedure here:
  - https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/index.html

Extra steps taken, because they seem to make sense to me:

- [X] Closed chrome windows and tabs that I no longer "need"
- [X] Rebooted and exited Chrome, leaving only a couple of Konsole windows open

Doing the upgrade:

- [X] Run the command:
  - `do-release-upgrade`
  - Started at around 6:45 PM
  - Finished about an hour later


# Messages

**While running the process, it stopped and displayed some messages.**

Following are some details about these messages:

## Message about xscreensaver and xlockmore

- There are incompatible changes have been made to a library that these packages use

> xscreensaver and xlockmore must be restarted before upgrading

> One or more running instances of xscreensaver or xlockmore have been detected on this system. Because of incompatible library changes, the upgrade of the GNU libc  library will leave you unable to authenticate to these programs. You should arrange for these programs to be restarted or stopped before continuing this upgrade, to avoid locking your users out of their current sessions.

### Action taken:

- Killed xscreensaver, but did not see an instance of xlockmore running
- Pressed <Enter> to continue

## Message about Encfs

- Encfs is vulnerable to attack
- Encfs is a file encryption system, which to my knowledge, I am not using at this time.

> Encfs security information

> According to a security audit by Taylor Hornby (Defuse Security), the current implementation of Encfs is vulnerable or potentially vulnerable to multiple types of  attacks. For example, an attacker with read/write access to encrypted data might lower the decryption complexity for subsequently encrypted data without this being  noticed by a legitimate user, or might use timing analysis to deduce information.  Until these issues are resolved, encfs should not be considered a safe home for sensitive data in scenarios where such attacks are possible.

### Action taken:

- Pressed <Enter> to continue

## Message about Firefox snap

> Upgrade to the firefox snap

> Starting in Ubuntu 22.04, all new releases of firefox are only available to Ubuntu users through the snap package.  This package update will transition your system over to the snap by installing it.  It is recommended to close all open firefox windows before proceeding to the upgrade. 13

### Action taken:

- Pressed <Enter> to continue

## Message about `/etc/sysctl.conf`

Got this message about a change I had made to `/etc/sysctl.conf`:

```
Configuration file '/etc/sysctl.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** sysctl.conf (Y/I/N/O/D/Z) [default=N] ? Y
```

- I did indeed change this file, and both the before and after versions are checked into RCS
- If I want or need to make the change again, see `2-sysctl.conf-rcsdiff_output.md` in this directory

### Action taken:

- Chose "Y", to "install the package maintainer's version"
- Pressed <Enter> to continue

- Pressed <Enter> to continue

## Message about the window switcher

Saw a pop up message from the system (NOT from the upgrade process) about the window switcher being broken.
It said I should contact my distribution manager (or something) about this.

### Action taken:

The message disappeared before I could copy or otherwise respond to it.

- No action taken

## Message about obsolete packages

```
Remove obsolete packages?


158 packages are going to be removed.

Removing the packages can take several hours.

 Continue [yN]  Details [d]y
```

### Action taken:

- Typed "Y" and pressed <Enter> to continue

## Message about the process being complete

Including this for the sake of completeness:

```
System upgrade is complete.

Restart required

To finish the upgrade, a restart is required.
If you select 'y' the system will be restarted.

Continue [yN] Y
```

### Action taken:

- Typed "Y" and pressed <Enter> to continue

