
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

- Found an `xscreensaver` and killed it
- Unable to find an `` process so not worrying about it
- Pressed [ENTER] to proceed


## Message: "Upgrade to the Thunderbird Snap"

```
-- Configuring thunderbird --

Upgrade to the thunderbird snap

Starting in Ubuntu 24.04, all new releases of thunderbird are only available to Ubuntu users through the snap package.

This package update will transition your system over to the snap by installing it.

It is recommended to close all open thunderbird windows before proceeding to the upgrade.

    <Ok>
```

### Action Taken:

-> I am not using Thunderbird so I just pressed [ENTER] to proceed


## Message: "Configuration file '/etc/apache2/apache2.conf' "

```
Configuration file '/etc/apache2/apache2.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** apache2.conf (Y/I/N/O/D/Z) [default=N] ? Y
```

### Action Taken:

-> Noticed a few cusTOMizations near the end of the file
-> Saved just the cusTOMizations in a separate file named `apache2.conf-cusTOMizations`
-> Ensured the most recent version is checked in
-> Entered "D" to see the differences, it looks like they just deleted the `# vim:` line at the end of the file
-> Entered "Y" to **install the package maintainer's version**


## Message: "Configuration file '/etc/apache2/sites-available/000-default.conf' "

```
Configuration file '/etc/apache2/sites-available/000-default.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** 000-default.conf (Y/I/N/O/D/Z) [default=N] ? Y
```

### Action Taken:

-> Used `rcsdiff  -r1.1  000-default.conf` to see a few changes I made long ago
-> Saved just these differences in a file named `000-default.conf-changes_made`
-> Ensured the most recent version is checked in
-> Entered "D" to see the differences, **see these differences below**, they're mostly what I changed
-> Not really sure whether I will use apache again, so ...
-> Entered "Y" to **install the package maintainer's version**
-> **If we decide to run apache again, we can come back to all this**

### Differences:

Other than the changes I made, it looks like they just deleted the `# vim:` line at the end of the file.

```
*** 000-default.conf (Y/I/N/O/D/Z) [default=N] ? D
--- /etc/apache2/sites-available/000-default.conf       2020-06-18 17:22:52.777213594 -0600
+++ /etc/apache2/sites-available/000-default.conf.dpkg-new      2024-03-18 06:35:36.000000000 -0600
@@ -8,10 +8,8 @@
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

-       ### ServerAdmin webmaster@localhost
-       ### DocumentRoot /var/www/html
-       ServerAdmin junk@tomhartung.com
-       DocumentRoot /var/www
+       ServerAdmin webmaster@localhost
+       DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
@@ -19,9 +17,8 @@
        # modules, e.g.
        #LogLevel info ssl:warn

-       LogLevel info
        ErrorLog ${APACHE_LOG_DIR}/error.log
-       CustomLog ${APACHE_LOG_DIR}/access.log vhost_combined
+       CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
@@ -30,5 +27,3 @@
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
 </VirtualHost>
-
-# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

Configuration file '/etc/apache2/sites-available/000-default.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** 000-default.conf (Y/I/N/O/D/Z) [default=N] ? Y
```


## Message: "Configuration file '/etc/apache2/sites-available/default-ssl.conf' "

```
Configuration file '/etc/apache2/sites-available/default-ssl.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** default-ssl.conf (Y/I/N/O/D/Z) [default=N] ? Y
```

### Action Taken:

-> Used `rcsdiff  -r1.1  default-ssl.conf` to see the changes I made long ago
-> Saved just these differences in a file named `default-ssl.conf-changes_made`
-> Ensured the most recent version is checked in
-> Entered "D" to see the differences, it looks like a lot of them but it could be a lot of changes to whitespace
-> Not really sure whether I will use apache again, so ...
-> Entered "Y" to **install the package maintainer's version**
-> **If we decide to run apache again, we can come back to all this**


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

