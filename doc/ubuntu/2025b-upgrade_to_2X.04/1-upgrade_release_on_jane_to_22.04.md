
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

While running the process, it stopped and displayed some messages.

- For details, see the next section


# Messages

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

> According to a security audit by Taylor Hornby (Defuse Security), the current implementation of Encfs is vulnerable or potentially vulnerable to multiple types of  attacks. For example, an attacker with read/write access to encrypted data might lower the decryption complexity for subsequently encrypted data without this being  noticed by a legitimate user, or might use timing analysis to deduce information.  Until these issues are resolved, encfs should not be considered a safe home for sensitive data in scenarios where such attacks are possible. 13 169

### Action taken:

- Killed xscreensaver, but did not see an instance of xlockmore running
- Pressed <Enter> to continue

## Message about 

> Upgrade to the firefox snap  Starting in Ubuntu 22.04, all new releases of firefox are only available to Ubuntu users through the snap package.  This package update will transition your system over to the snap by installing it.  It is recommended to close all open firefox windows before proceeding to the upgrade. 13

### Action taken:

- Killed xscreensaver
- Pressed <Enter> to continue


