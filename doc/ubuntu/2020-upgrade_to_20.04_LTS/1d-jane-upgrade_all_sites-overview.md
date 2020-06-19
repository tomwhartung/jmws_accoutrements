
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

- [ ] ArtsyVisions.com
- [ ] Groja.com
- [ ] JooMooWebSites.com
- [ ] SeeOurMinds.com
- [x] TomHartung.com
- [ ] TomWHartung.com

For high-level details about each site, see the **"Additional Goals"** section.

# The Main Process of Processes

- [x] 1. Get all sites running locally on jane
- [x] 2. Make changes listed in the **"Essential Tasks"** section
- [x] 3. Get all sites running under apache -- but don't worry about SSL yet - **new backup**
- [ ] 4. Server shuffle:
  - [ ] 4.1 Start using bette for music
  - [ ] 4.2 Install Ubuntu server 20.04 Focal Fossa on barbara and make it the server
  - [ ] 4.3 Start using jane for tv surfing
- [ ] 5. Install Kubuntu Focal Fossa 20.04 on ava
  - [ ] 5.1 Get all sites running
  - [ ] 5.2 Get all sites running under apache -- but don't worry about SSL yet - **newer backup**
  - [ ] 5.3 Start using it for new development
- [ ] 6. Make changes listed in the **"Additional Goals"** section

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

Each site has its own file in this directory, e.g., `2a-artsyvisions.md`, containing details about what I want to change.

# Additional Goals - After Making Barbara the Server

Once barbara is the server and we have ava for development, also make the following changes:

- [ ] 1. ArtsyVisions.com - Django and Materialize
    - [ ] Review social networking icons
    - [ ] Remove free spiritual portrait offer
    - [ ] Review for anything glaring, but it should be ok already
- [ ] 2. TomHartung.com - Django and MUI-CSS
    - [ ] Should already be ok
- [ ] 3. SeeOurMinds.com - Django and Material Design Bootstrap [MDB]
    - [ ] Review social networking icons
    - [ ] Remove free spiritual portrait offer
    - [ ] Review for anything glaring, but it should be ok already
- [ ] 4. Groja.com - Flask and Material Design Bootstrap [MDB]
    - [ ] Review social networking icons
    - [ ] Remove free spiritual portrait offer
    - [ ] Set the price for portraits at $500 each
    - [ ] Reexamine conversions to ensure they work and to prevent spam
    - [ ] Should already be ok
- [ ] 5. JooMooWebSites.com - Flask and Material Design Lite [MDL]
    - [ ] Update content on JooMooWebSites.com, replacing freelancer stuff with content aimed at selling my books
    - [ ] Consider switching to Material Design Bootstrap [MDB]
    - [ ] Stick to content that says what I have for sale, and what's in progress and coming soon
    - [ ] **Do not duplicate what's on TomWHartung.com**
- [ ] 6. TomWHartung.com - ~~Wordpress~~ -> Django and Material Design Bootstrap [MDB]
    - [ ] Create new content on TomWHartung.com with a new menu and articles
    - [ ] Stick to content that says who I am and what I do, e.g., Download spreadsheets, article about my FFM results
    - [ ] **Do not duplicate what's on JooMooWebSites.com**

Each site has its own file in this directory, e.g., `2a-artsyvisions.md`, containing details about what I want to change.

# Plan for Upgrading

Current plans are very fuzzy.  Here are some ideas I am considering:

- Thinking I can install the stable versions I want to use globally and not worry about setenv and all
- If an off-brand Material Design CSS library is no longer supported, switch to MDB

Here is a list of sites and the sequence in which I am thinking I will upgrade them

- Upgrade the **no-brainer** ones first:
  - These require only making sure they work with the latest versions of the underlying software:
  - ArtsyVisions.com
    - Update to use the current versions of Django and Materialize
  - TomHartung.com
    - Update to use the current versions of Django and MUI-CSS
- Upgrade the **easier** ones next:
  - These require making only minor changes to existing issues and ensuring they work with the latest versions of the underlying software:
  - SeeOurMinds.com - do next to continue with Django work
    - Update to use the current versions Django and Material Design Bootstrap [MDB]
    - Fix security alert: https://github.com/tomwhartung/seeourminds.com/network/alert/Site/content/static/content/js/jquery-3.3.1.min.js/jquery/open
  - Groja.com - make the switch to working on the Flask sites
    - Update to use the current versions of Flask and Material Design Bootstrap [MDB]
    - Fix security alert: https://github.com/tomwhartung/groja.com/network/alert/Site/static/js/jquery-3.3.1.min.js/jquery/open
- Save the **hardest** ones for last:
  - JooMooWebSites.com - keep the Flask, and maybe some of the images, and dump everything else
    - Switch to using Material Design Bootstrap [MDB] instead of Material Design Lite [MDL]
    - Update all content on JooMooWebSites.com, replacing freelancer stuff with new content
    - New content should be aimed at selling my books and promoting my social networking sites
  - TomWHartung.com - Starting over from scratch!
    - Replace the WP version of TomWHartung.com with a new, minimal Flask version,
    - New content should be aimed at selling my books and promoting my social networking sites

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

