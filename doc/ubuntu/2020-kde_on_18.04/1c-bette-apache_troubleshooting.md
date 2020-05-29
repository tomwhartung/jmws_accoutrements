
# 1c-bette-apache_troubleshooting.md

Apache2 no longer runs on bette, and I wonder if switching to KDE is what broke it.

# Troubleshooting

## Troubleshooting Essentials

Trying to start apache2, and looking at the sources it gives for finding more information when there is an error:

```
$ service apache2 start
Job for apache2.service failed because the control process exited with error code.
See "systemctl status apache2.service" and "journalctl -xe" for details.
$ systemctl status apache2.service
...
$ journalctl -xe
...
$
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

## Canonical Liveupdate

This allows updating the kernel while the machine is still running.

**They require a key and allow only 3 hosts per personal user.**

