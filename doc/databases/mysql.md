
# MySql

Notes on how to use the `bin/dbMySql*` scripts in this repository.

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

# Scripts Overview

