
# 1c-bette-apache_troubleshooting.md

Apache2 no longer runs on bette, and I wonder if switching to KDE is what broke it.

# Troubleshooting

## Troubleshooting Essentials

### Starting Apache2 and Finding the Error Messages

Trying to start apache2, and looking at the sources it gives for finding more information when there is an error:

```
# service apache2 start
Job for apache2.service failed because the control process exited with error code.
See "systemctl status apache2.service" and "journalctl -xe" for details.
# systemctl status apache2.service
blah blah blah "apache2.service: Control process exited, code=exited status=139"
# journalctl -xe
blah blah blah "apache2.service: Control process exited, code=exited status=139"
#
```

### Apache2 CommandHelp

More basics.

```
# apache2 -help
Usage: apache2 [-D name] [-d directory] [-f file]
               [-C "directive"] [-c "directive"]
               [-k start|restart|graceful|graceful-stop|stop]
               [-v] [-V] [-h] [-l] [-L] [-t] [-T] [-S] [-X]
Options:
  -D name            : define a name for use in <IfDefine name> directives
  -d directory       : specify an alternate initial ServerRoot
  -f file            : specify an alternate ServerConfigFile
  -C "directive"     : process directive before reading config files
  -c "directive"     : process directive after reading config files
  -e level           : show startup errors of level (see LogLevel)
  -E file            : log startup errors to file
  -v                 : show version number
  -V                 : show compile settings
  -h                 : list available command line options (this page)
  -l                 : list compiled in modules
  -L                 : list available configuration directives
  -t -D DUMP_VHOSTS  : show parsed vhost settings
  -t -D DUMP_RUN_CFG : show parsed run settings
  -S                 : a synonym for -t -D DUMP_VHOSTS -D DUMP_RUN_CFG
  -t -D DUMP_MODULES : show all loaded modules
  -M                 : a synonym for -t -D DUMP_MODULES
  -t -D DUMP_INCLUDES: show all included configuration files
  -t                 : run syntax check for config files
  -T                 : start without DocumentRoot(s) check
  -X                 : debug mode (only one worker, do not detach)
# apache2 -v
Server version: Apache/2.4.29 (Ubuntu)
Server built:   2020-03-13T12:26:16
#
```

More commands to know:

- https://linuxize.com/post/apache-commands-you-should-know/

## Set ServerName Globally

The first error message - and in truth it may be just a warning - said to set ServerName globally, so I did.

```
cd /etc/apache2
mkdir RCS
ci -l apache2.conf     # Installed version
vi apache2.conf
ci -l apache2.conf     # Added "ServerName bette" to stop the warning.
apachectl configtest   # Syntax OK
```

Also updated ServerName in `sites-enabled/020-groja.com.conf` .

**This fixed the error or warning message but it still will not start.**

## Searching for a Solution

This shows the same error.  Posted 2 months ago, no one has responded.

- https://stackoverflow.com/questions/60640440/apache2-service-control-process-exited-code-exited-status-139

I upvoted the question.  See **Possible PHP Problem** below.

These pages show similar issues, but I cannot see anything for `"...code=exited status=139"`

- https://askubuntu.com/questions/629995/apache-not-able-to-restart
- https://unix.stackexchange.com/questions/268613/apache2-service-failed-because-the-control-process-exited-with-error-code
- https://serverfault.com/questions/1016668/apache2-service-failed-with-result-exit-code

Presumably, the `status=139` is key.

### Canonical Livepatch

A command named `canonical-livepatch` allows updating the kernel while the machine is still running.

This was part of an earlier error message I was getting:

```
error in livepatch check state: check-failed
No payload available during refresh: cannot check: No machine-token.
Please run 'canonical-livepatch enable'!
```

Unfortunately, those commands are no longer in my history.

I got the key from this page:

- https://auth.livepatch.canonical.com/?user_type=ubuntu-user

Which shows how to install `canonical-livepatch`:

```
snap install canonical-livepatch
canonical-livepatch enable 92b377a4f46641609779b7f15f7b533d
```

I tried to enable it and it did not work until I got a key (i.e., `92b377a4f46641609779b7f15f7b533d`) from:

- https://ubuntu.com/livepatch

**They require a key and allow it to be used on only 3 hosts for the free user level.**

I am presumably using that key to allow me to keep the kernel up-to-date while the computer is running.

The version history on the ubuntu wikipedia page says this is a big thing in 20.04.


## The Problem Persists

Still getting the 139 error:

```
# service apache2 start
Job for apache2.service failed because the control process exited with error code.
See "systemctl status apache2.service" and "journalctl -xe" for details.
# systemctl status apache2.service
● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: failed (Result: exit-code) since Fri 2020-05-29 14:03:58 MDT; 40s ago
  Process: 9482 ExecStart=/usr/sbin/apachectl start (code=exited, status=139)

May 29 14:03:58 bette systemd[1]: Starting The Apache HTTP Server...
May 29 14:03:58 bette apachectl[9482]: Segmentation fault (core dumped)
May 29 14:03:58 bette apachectl[9482]: Action 'start' failed.
May 29 14:03:58 bette apachectl[9482]: The Apache error log may have more information.
May 29 14:03:58 bette systemd[1]: apache2.service: Control process exited, code=exited status=139
May 29 14:03:58 bette systemd[1]: apache2.service: Failed with result 'exit-code'.
May 29 14:03:58 bette systemd[1]: Failed to start The Apache HTTP Server.
# journalctl -xe
 . . .
 . . .
 . . .
May 29 15:27:05 bette systemd[1]: Starting The Apache HTTP Server...
-- Subject: Unit apache2.service has begun start-up
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
--
-- Unit apache2.service has begun starting up.
May 29 15:27:05 bette kernel: apache2[11744]: segfault at 7f90046b6940 ip 00007f900082c30b sp 00007ffc540ce9a0 error 6 in libphp7.2.so[7f9000598000+3fb000]
May 29 15:27:05 bette apachectl[11741]: Segmentation fault (core dumped)
May 29 15:27:05 bette apachectl[11741]: Action 'start' failed.
May 29 15:27:05 bette apachectl[11741]: The Apache error log may have more information.
May 29 15:27:06 bette systemd[1]: apache2.service: Control process exited, code=exited status=139
May 29 15:27:06 bette systemd[1]: apache2.service: Failed with result 'exit-code'.
May 29 15:27:06 bette systemd[1]: Failed to start The Apache HTTP Server.
-- Subject: Unit apache2.service has failed
-- Defined-By: systemd
-- Support: http://www.ubuntu.com/support
--
-- Unit apache2.service has failed.
--
-- The result is RESULT.
#
```

## Possible PHP Problem?

Looking at this page, which shows the same error, was posted 2 months ago, and so far no one has answered.

- https://stackoverflow.com/questions/60640440/apache2-service-control-process-exited-code-exited-status-139

But someone responded that it might be due to changing the version of PHP.

Maybe this could be it?

lauren:

```
tomh@lauren: ~
 $ php -v
PHP 5.6.40-1+ubuntu16.04.1+deb.sury.org+2+will+reach+end+of+life+in+april+2019 (cli)
Copyright (c) 1997-2016 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2016 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies
    with Xdebug v2.5.5, Copyright (c) 2002-2017, by Derick Rethans
tomh@lauren: ~
 $
```

bette:

```
tomh@bette: ~
 $ php -v
PHP 7.2.24-0ubuntu0.18.04.6 (cli) (built: May 26 2020 13:09:11) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
    with Zend OPcache v7.2.24-0ubuntu0.18.04.6, Copyright (c) 1999-2018, by Zend Technologies
    with Xdebug v2.6.1, Copyright (c) 2002-2018, by Derick Rethans
tomh@bette: ~
 $
```

Installing the KDE desktop may have caused this.

More evidence that PHP might be at fault.

lauren:

```
tomh@lauren: ~
 $ cd /etc/apache2/
tomh@lauren: /etc/apache2
 $ l mods-*/php*
-rw-r--r-- 1 root root 867 Jun  9  2017 mods-available/php5.6.conf
-rw-r--r-- 1 root root 102 Jun  9  2017 mods-available/php5.6.load
lrwxrwxrwx 1 root root  29 Jul  3  2017 mods-enabled/php5.6.conf -> ../mods-available/php5.6.conf
lrwxrwxrwx 1 root root  29 Jul  3  2017 mods-enabled/php5.6.load -> ../mods-available/php5.6.load
tomh@lauren: /etc/apache2
 $
```

bette:

```
tomh@bette: /var/www/html
 $ cd /etc/apache2/
tomh@bette: /etc/apache2
 $ l mods-*/php*
-rw-r--r-- 1 root root 867 Jun  9  2017 mods-available/php5.6.conf
-rw-r--r-- 1 root root 102 Jun  9  2017 mods-available/php5.6.load
-rw-r--r-- 1 root root 867 Mar  2  2017 mods-available/php7.0.conf
-rw-r--r-- 1 root root 102 Oct  1  2018 mods-available/php7.0.load
-rw-r--r-- 1 root root 855 Jul  7  2017 mods-available/php7.1.conf
-rw-r--r-- 1 root root 102 Jul  7  2017 mods-available/php7.1.load
-rw-r--r-- 1 root root 855 Feb  8  2019 mods-available/php7.2.conf
-rw-r--r-- 1 root root 102 Feb  8  2019 mods-available/php7.2.load
lrwxrwxrwx 1 root root  29 Jul  1  2017 mods-enabled/php5.6.conf -> ../mods-available/php5.6.conf
lrwxrwxrwx 1 root root  29 Jul  1  2017 mods-enabled/php5.6.load -> ../mods-available/php5.6.load
lrwxrwxrwx 1 root root  29 May 28 06:05 mods-enabled/php7.2.conf -> ../mods-available/php7.2.conf
lrwxrwxrwx 1 root root  29 May 28 06:05 mods-enabled/php7.2.load -> ../mods-available/php7.2.load
tomh@bette: /etc/apache2
 $
```

I can see how having both php5.6 and php7.2 enabled might be a problem.

Sure enough disabling php7.2 did the trick.  Check out my first answer ever posted on stackoverflow.com, woot!

- https://stackoverflow.com/questions/60640440/apache2-service-control-process-exited-code-exited-status-139

