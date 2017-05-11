
# MySql

Notes on how to use the `bin/dbMySql*` scripts in this repository.

# Security Warning

These scripts allow easy access to mySql databases without a password.

## Whom Do You Trust?

If people whom you do not trust have access to your machine, either:

1. ensure you have to enter a password to access the database, or
2. do not use these scripts.

With some configurations, you should also be concerned about people
looking over your shoulder!

## MySql Warning

Everytime you run one of these commands, MySql will display the following warning:

```
mysql: [Warning] Using a password on the command line interface can be insecure.
```

So be careful when running these commands, and
if you have any doubt about the trustworthiness of the people nearby
when you run them, simply do not use them.

# Background and Aliases

## Background

This documentation is going to be brief because I have been
developing these scripts over the past several years and am
well-acquainted with how they work.

Just want to make some formal notes because we are starting to
use PostGres now, so the ability to remember how to use these old
ones may become a bit fuzzy over time.

## Aliases

I am used to using the following aliases to run these commands:

```
export DB_BACKUP_DIRECTORY='...'
export DB_CREDENTIALS_FILE='/...'
alias 'bu'='dbMySqlBackup'
alias 'ms'='dbMySqlCommand'
alias 'rs'='dbMySqlRestore'
alias 'gobu'="cd $DB_BACKUP_DIRECTORY"
```

# MySql Scripts

All `dbMySql*` scripts are written in python3.
Scripts that have the python `.py` extension are support scripts.
You should have no reason to run these from the command line.

## dbMySqlCredentialsEg.py

Contains database names and passwords, allowing easy access to your
database on the command line.

### Security Warning

You should keep this file hidden and set its permissions to 700:

```
cd ~/secret/directory
chmod 700 $DB_CREDENTIALS_FILE
```

### Backup and Restore

These scripts allow running abbreviated commands to backup and restore
a mysql database.

#### Backup File Name Format

The backup files have names formatted as follows:

* `[siteName]-[YYYY_MM_DD]-[hostName]-[optionalSuffix].sql.gz`

#### Advantages

The backup command allows you to specify an `optionalSuffix` when
backing up the database.

The restore command allows you to override any combination of the
date, `hostName`, or `optionalSuffix` when restoring the database.

This allows you to easily:

* copy the database from one host to another
* revert to a version backed up on a previous date
* restore an earlier version after getting hacked
* revert to an earlier version created before messing something up while experimenting

### How to Use

If you decide to use these scripts, examine this file carefully for full
documentation as to how to set up this key component for your environment.

## dbMySqlFunctions.py

Contains python functions used to implement two or more commands.

## dbMySqlCommand

Runs the `mysql` command, allowing you to use a short string to specify the
database name.  Gets the password for the database from the
`$DB_CREDENTIALS_FILE` .

### Example Using Alias

```
ms xx    # see Note below
```

Note: `xx` is a one-or-two letter abbreviation for the database that you
set up in your personal version of `dbMySqlCredentialsEg.py` .

## dbMySqlBackup

Backs up the db into a file in `$DB_BACKUP_DIRECTORY` .

The file

### Example Using Alias

```
gobu
ls -altr
bu xx    # see Note below
ls -altr # notice new filename
```

Note: `xx` is a one-or-two letter abbreviation for the database that you
set up in your personal version of `dbMySqlCredentialsEg.py` .

### Example Using Arguments

```
gobu
ls -altr
bu xx 01-before_experimenting    # (*) see how to restore this below
ls -altr # notice new filename
```

## dbMySqlRestore

Restores the db from a backup file in `$DB_BACKUP_DIRECTORY` .

### Example Using Aliases

```
gobu
ls -altr
rs xx    # see Note below
```

Note: `xx` is a one-or-two letter abbreviation for the database that you
set up in your personal version of `dbMySqlCredentialsEg.py` .

### Examples Using Arguments

Restore to version created before experimenting messed something up:

```
gobu
ls -altr
rs xx 01-before_experimenting   # (*) see bu command used above
```

Restore production backup taken on New Year's Day 2017:

```
gobu
ls -altr
rs -h prod_host -d 2017_01_01 xx
```

