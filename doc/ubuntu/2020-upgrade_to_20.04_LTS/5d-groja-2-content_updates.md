
# 5d-groja-2-content_updates.md

Continuing to update Groja.com so it is just exactly perfect.

# Content Updates and Review

## Content Updates and Review - Checklist

- [ ] Upgrade MDB to latest version: MDB 5 alpha
- [ ] Check for and remove free spiritual portrait offer, if present
    - [ ] Check the "Making Money?!?" card on the About page
- [x] Ensure social media icons link to same accounts as artsyvisions
- [ ] Set list price for a spiritual portrait to $500
    - [ ] A price of $10 appears on the `get_your_portrait` conversion page
        - http://127.0.0.1:5000/conversion/get_your_portrait`
    - [ ] Check for other occurrences of the price

- [ ] Review About page and update as appropriate
- [ ] Review entire site for anything glaring

Processes and details appear below.

## Content Updates - Process and Details

Download, install, and test.

### Upgrade MDB to Latest Version: MDB 5 Alpha

References:

- From Email:
  - https://mdbootstrap.us16.list-manage.com/track/click?u=461480655ccce528d909d3f42&id=cb39f7716f&e=a65ba5c397
- Takes me to (redirects):
  - https://mdbootstrap.com/docs/standard/?utm_campaing=MDB5&utm_medium=news&mc_cid=b025dc7b85&mc_eid=a65ba5c397
- Get Started (button):
  - https://mdbootstrap.com/docs/standard/getting-started/installation/
- From README.txt file:
  - https://mdbootstrap.com/docs/standard/
- Installation Guide:
  - https://mdbootstrap.com/docs/standard/getting-started/installation/
- Relevant Wikipedia pages:
  - https://en.wikipedia.org/wiki/Node.js
  - https://en.wikipedia.org/wiki/Npm_(software)
- Covers three options for installing Node on Ubuntu 20.04:
  - https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04
  - Using apt is the first and easiest

#### Do I Want to Do This?

I love MDB but:

- They have dropped jQuery
- They want me to use MDB CLI, which requires NPM

Looking at the site using the default version (no MDB CLI, Node, or NPM) looks almost acceptable.
Some things are just missing, and could probably be easily "resurrected."

#### Do I Want to Install Node and NPM?

Installing the default versions of node and NPM is easily done using `apt`.

#### Checking Versions

Node:

- Version to be installed by apt: 10.19.0
  - 10.x: Maintenance LTS release from 2018-04-24, supported through 2021-04-01
- Latest stable version according to wikipedia: 14.6.0, released 3 days ago

The Installation Guide recommends installing "Node LTS (12.x.x recommended)."

- 12.x: Active LTS release from 2019-10-22, supported through 2022-04-01

NPM:

- Version to be installed by apt: 6.14.4
- Latest stable version according to wikipedia: 6.14.7, released 3 days ago

#### Quick Start Video Notes

Watched the Quick Start Video at:

- https://mdbootstrap.com/docs/standard/getting-started/quick-start/

In it, they show how to use MDB CLI to:

- Create a starting template
  - This template looks just like the sample index.html included in the download package
- Expand the template by copying and pasting code
  - I do not need to do this for groja.com
- Publish the resultant site to mdbootstrap.com
  - I see no reason to do this

There's nothing to lose by installing MDB CLI et. al., because it's a no-brainer now that I know how,
and I probably won't even use it anyway.

#### Decision

Use apt to install Node, NPM, and MDB CLI.

- I might not use them now, but they will be useful when I do other sites

**If I have issues using them for the other sites, remember to install a newer version of node.js .**

#### Installing Node, NPM, and MDB CLI

Use `apt` as follows:

```
```

#### Proposed Steps:

- 1. Download MDB-UI-KIT-Free-1.0.0-alpha4.zip and unpack
- 2. Copy files into `static` directory
   - 2.1. css/*
   - 2.2. js/*
- 3. Quickly test site
- 4. If everything looks ok, commit
- 5. If it looks messed up, revert


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

### Check for and Remove Free Spiritual Portrait Offer, If Present

### Check the "Making Money?!?" card on the About page

### Set list price for a spiritual portrait to $500

#### Fix the `get_your_portrait` conversion page

- http://127.0.0.1:5000/conversion/get_your_portrait`

Continued in next section!

## Review - Process and Details

### Check for Other Occurrences of the Price

### Review About Page and Update as Appropriate

### Review Entire Site for Anything Glaring

