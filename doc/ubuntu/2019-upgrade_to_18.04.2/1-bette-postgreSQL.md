
# 1-bette-postgreSQL.md

New window opens entitled "Obsolete major version 9.5."

Notes:

The PostgreSQL version 9.5 is obsolete, but the server or client packages are still installed.
Please install the latest packages (postgresql-10 and postgresql-client-10) and upgrade the
existing  clusters with pg_upgradecluster (see manpage).

Please be aware that the installation of postgresql-10 will automatically create a default
cluster 10/main. If you want to upgrade the 9.5/main cluster, you need to remove the already
existing 10 cluster (pg_dropcluster --stop 10 main, see manpage for details).

The old server and client packages are no longer supported. After the existing clusters are
upgraded, the postgresql-9.5 and postgresql-client-9.5 packages should be removed.

Please see /usr/share/doc/postgresql-common/README.Debian.gz for details.


