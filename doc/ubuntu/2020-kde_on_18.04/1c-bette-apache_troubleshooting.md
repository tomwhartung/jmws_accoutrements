
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

## Set ServerName Globally

The first error message - and in truth it may be just a warning - said to set ServerName globally, so I did.

```
cd /etc/apache2
mkdir RCS
ci -l apache2.conf   # Installed version
vi apache2.conf
```

Also updated ServerName in `sites-enabled/020-groja.com.conf` .

**This fixed the error or warning message but it still will not start.**

## Searching for a Solution

This shows the same error.  Posted 2 months ago, no one has responded.

- https://stackoverflow.com/questions/60640440/apache2-service-control-process-exited-code-exited-status-139

I upvoted the question.

These pages show similar issues, but I cannot see anything for `"...code=exited status=139"`

- https://askubuntu.com/questions/629995/apache-not-able-to-restart
- https://unix.stackexchange.com/questions/268613/apache2-service-failed-because-the-control-process-exited-with-error-code
- https://serverfault.com/questions/1016668/apache2-service-failed-with-result-exit-code

### Canonical Liveupdate??  Or Livepatch??

A command named `canonical-livepatch` allows updating the kernel while the machine is still running.

This was part of an earlier error message I was getting:

```
error in livepatch check state: check-failed
No payload available during refresh: cannot check: No machine-token.
Please run 'canonical-livepatch enable'!
```

I tried to enable it and it did not work.
Unfortunately, those commands are no longer in my history.

**They require a key and allow only 3 hosts for the free user level.**

