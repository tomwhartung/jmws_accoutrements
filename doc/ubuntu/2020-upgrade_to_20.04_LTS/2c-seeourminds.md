
# 2d-seeourminds.md

Updating SeeOurMinds.com .

# Getting the Site to Run Locally

After installing django and providing a `gitignored/Site/Site/settings.py` file, the site still needed some help.

## Installing Additional Required Packages

### Fixing psycopg2 Error

This error occurs when I try to run `run.sh`:

- django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'

Process used to fix this error:

- 1. Checked for occurrences of 'psycopg2' in the code base - and did not find any!
- 2. Realized this is for postgres
- 3. Realized I am not using postgres on this site
- 4. Commented out the setting for DATABASES in `settings.py` - not sure why it was set in the first place

### Fixing Warning Messages

Several of these warning messages appear when I run `run.sh`:

- `models.py:649: SyntaxWarning: "is" with a literal. Did you mean "=="?`

Changing "is" to "==" in the lines mentioned in the messages seems to have fixed the problem.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Technical Updates Needed

## Security Issue

Examine security issue flagged by github:

- https://github.com/tomwhartung/seeourminds.com/network/alert/Site/content/static/content/js/jquery-3.3.1.min.js/jquery/open

## CSS Issue

The content of the `blockquote` tags look just like that of the `p` tags.
Something is not right here.

Example: Nixon's page:

- http://127.0.0.1:8001/image/5040-politicians-us_presidents-1900s/5062/

# Content Updates

Remove free spiritual portrait offer.

# Review

## Check the Icons

Ensure social media icons link to correct accounts.

## Test the Quiz

**I made several very minor updates to class Score in `models.py`, so we need to re-test the quiz to make sure it still works.**

