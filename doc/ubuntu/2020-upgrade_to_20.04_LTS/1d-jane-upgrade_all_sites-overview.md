
# 1d-jane-upgrade_all_sites-overview.md

Get all sites working on jane, now running 20.04, with the latest stable versions of underlying software:

- Python
- Flask
- Django

Find detailed descriptions of steps taken in `1e-jane-needed_for_all_sites.md`.

# Checklists

These checklists contain the sites I am supporting, and that need to be updated.

## Checklist: Basic Functionality

Tracking the progress in getting the home pages of these sites to render without errors or warnings.

- [x] ArtsyVisions.com
- [x] Groja.com
- [x] JooMooWebSites.com
- [x] SeeOurMinds.com
- [x] TomHartung.com
- [x] TomWHartung.com

## Checklist: Essential Tasks

Tracking the progress in making essential updates to the content on these sites.
These changes include security updates and essential review items.

- [x] ArtsyVisions.com
- [x] Groja.com
- [x] JooMooWebSites.com
- [x] SeeOurMinds.com
- [x] TomHartung.com
- [x] TomWHartung.com

For high-level details about each site, see the **"Essential Tasks"** section.

## Checklist: Additional Updates to Content

Checklist to track the progress in getting the content reviewed and updated on these sites.

- [x] ArtsyVisions.com
- [x] Groja.com
- [ ] JooMooWebSites.com
- [ ] SeeOurMinds.com
- [x] TomHartung.com
- [ ] TomWHartung.com

For high-level details about each site, see the **"Additional Goals"** section.

# The Main Process of Processes

- [x] 1. Get all sites running locally on jane
- [x] 2. Make changes listed in the **"Essential Tasks"** section
- [x] 3. Get all sites running under apache -- but don't worry about SSL yet - **new backup**
- [x] 4. Server shuffle:
  - [x] 4.1 Start using bette for music
  - [x] 4.2 Install Ubuntu server 20.04 Focal Fossa on barbara and make it the server
  - [x] 4.3 Start using jane for tv surfing
- [x] 5. Install Kubuntu Focal Fossa 20.04 on ava
  - [x] 5.1 Get all sites running
  - [x] 5.2 Get all sites running under apache -- but don't worry about SSL yet - **newer backup**
  - [x] 5.3 Start using it for new development

# Essential Tasks - Before Making Barbara the Server

Make these essential changes before updating barbara to be the server:

- [x] 1. ArtsyVisions.com - Django and Materialize
    - [x] Content ok for now
- [x] 2. TomHartung.com - Django and MUI-CSS
    - [x] Content ok for now
- [x] 3. SeeOurMinds.com - Django and Material Design Bootstrap [MDB]
    - [x] Fix security alert: https://github.com/tomwhartung/seeourminds.com/network/alert/Site/content/static/content/js/jquery-3.3.1.min.js/jquery/open
- [x] 4. Groja.com - Flask and Material Design Bootstrap [MDB]
    - [x] Fix security alert: https://github.com/tomwhartung/groja.com/network/alert/Site/static/js/jquery-3.3.1.min.js/jquery/open
    - [x] Content ok for now
- [x] 5. JooMooWebSites.com - Flask and Material Design Lite [MDL]
    - [x] Will update content later
- [x] 6. TomWHartung.com - ~~Wordpress~~ -> Django and Material Design Bootstrap [MDB]
    - [x] Replace the WP version of TomWHartung.com with a new, single-page Django site
    - [x] Will update content later

# Actual Steps Taken

Find details for installing underlying software used by more than one site, e.g., installing django and flask, in:

- `1e-jane-needed_for_all_sites.md`

Find details for each site in the `2*.md` files in this directory:

- `2a-artsyvisions.md`
- `2b-tomhartung.md`
- `2c-seeourminds.md`
- `2d-groja.md`
- `2e-joomoowebsites.md`
- `2f-tomwhartung.md`

