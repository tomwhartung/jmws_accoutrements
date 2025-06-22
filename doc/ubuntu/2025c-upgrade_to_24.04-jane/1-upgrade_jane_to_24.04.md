
# 1-upgrade_jane_to_24.04.md

The upgrade to 22.04 two weeks ago went ok, except now the screen sometimes flicers.

- For details see `../2025b-upgrade_to_22.04-jane/1-upgrade_jane_to_22.04.md`


# Upgrade Jane - Again

Upgrading to 24.04 should be straightforward and safe

- If it goes horribly wrong somehow, implement *Plan B* in `../2025b-upgrade_to_22.04-jane/1-upgrade_jane_to_22.04.md`:
  - 1. See `../2026a-fresh_install_of_26.04-jane/1-install_26.04-jane.md`
  - 1. Review the analysis of jane's disk partitions
  - 1. Adapt the *Suggested Process* to work for 24.04 instead


# Preparations

- [ ] Update `tarHome` to backup most relevant files for adding to new install
- [ ] Run `tarHome` on jane to be sure we have the latest
- [ ] Review the procedure here:
  - https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/index.html

Extra steps taken, because they seem to make sense to me:

- [ ] Closed chrome windows and tabs that I no longer "need"
- [ ] Rebooted and exited Chrome, leaving only a couple of Konsole windows open

Doing the upgrade:

- [ ] Run the command:
  - `do-release-upgrade`
  - Started at around 
  - Finished about 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Messages

**While running the process, it stopped and displayed some messages.**

Following are some details about these messages:

## Message about 


### Action taken:


## Message about 


### Action taken:


## Message about 


### Action taken:


## Message about 


### Action taken:


## Message about obsolete packages

```
Remove obsolete packages?


XXX packages are going to be removed.

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

