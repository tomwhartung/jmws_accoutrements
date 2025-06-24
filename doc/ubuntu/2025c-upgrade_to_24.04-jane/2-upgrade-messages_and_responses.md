
# 2-upgrade-messages_and_responses.md

During the upgrade, the following messages appeared.
Along with each message, I list how I responded.


## Message: "Third party sources disabled"

```
Updating repository information

Third party sources disabled

Some third party entries in your sources.list were disabled. You can
re-enable them after the upgrade with the 'software-properties' tool
or your package manager.

To continue please press [ENTER]
```

### Action Taken:

-> Pressed [ENTER]


## Message: "Do you want to start the upgrade?"

```
Calculating the changes

Do you want to start the upgrade?


165 packages are going to be removed. 612 new packages are going to
be installed."1905 packages are going to be upgraded.

You have to download a total of 2,817 M. This download will take
about 5 minutes with your connection.

Installing the upgrade can take several hours. Once the download has
finished, the process cannot be canceled.

 Continue [yN]  Details [d]

```

### Action Taken:

-> Entered 'y'


## Message: "xscreensaver and xlockmore must be restarted before upgrading"

```
xscreensaver and xlockmore must be restarted before upgrading

One or more running instances of xscreensaver or xlockmore have been detected on this system. Because of incompatible library changes,
the upgrade of the GNU libc library will leave you unable to authenticate to these programs. You should arrange for these programs to
be restarted or stopped before continuing this upgrade, to avoid locking your users out of their current sessions.

   <Ok>
```

### Action Taken:

- 1. Found an `xscreensaver` and killed it
- 1. Unable to find an `` process so not worrying about it
- 1. Pressed [ENTER] to proceed


## Message:

```
```

### Action Taken:

-> 


## Message:

```
```

### Action Taken:

-> 



## Message:

```
```

### Action Taken:

-> 


## Message:

```
```

### Action Taken:

-> 

