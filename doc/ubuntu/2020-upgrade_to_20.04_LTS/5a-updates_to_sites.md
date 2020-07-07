
# 5a-updates_to_sites.md

Continuation of process originally defined in `1d-jane-upgrade_all_sites-overview.md`.

# Checklist

Checklist of the sites I am running, to make it easy to track my progress.

## Checklist: Additional Updates to Content

Checklist to track the progress in getting the content reviewed and updated on these sites.

- [ ] ArtsyVisions.com
- [ ] Groja.com
- [ ] JooMooWebSites.com
- [ ] SeeOurMinds.com
- [x] TomHartung.com
- [ ] TomWHartung.com

# Updates to Make to Sites

Once barbara is the server and we have ava for development, make the following changes:

- [ ] 1. TomHartung.com - Django and MUI-CSS
    - [ ] Should already be ok
- [ ] 2. SeeOurMinds.com - Django and Material Design Bootstrap [MDB]
    - [ ] Upgrade MDB to latest version
    - [ ] Review social networking icons
    - [ ] Disable saving results on the server
        - [ ] Test the 4-question version of the quiz to ensure saving results is properly disabled
        - [ ] Ensure site no longer mentions saving results is an option
        - [ ] Test the **88-question version** of the quiz
    - [ ] Remove free spiritual portrait offer
    - [ ] Copy portraits that need to be added from bette to ava
    - [ ] Review for anything glaring, but it should be ok already
- [ ] 3. Groja.com - Flask and Material Design Bootstrap [MDB]
    - [ ] Upgrade MDB to latest version
    - [ ] Review social networking icons
    - [ ] Remove free spiritual portrait offer
    - [ ] Set the price for portraits at $500 each
    - [ ] Reexamine conversions
        - [ ] disable any that are unused
        - [ ] ensure the remaining conversions work ok
        - [ ] ensure spam is prevented
- [ ] 4. ArtsyVisions.com - Django and Materialize
    - [ ] Review social networking icons
    - [ ] Remove free spiritual portrait offer
    - [ ] Review for anything glaring
    - [ ] Should already be ok
- [ ] 5. JooMooWebSites.com - Flask and Material Design Lite [MDL]
    - [ ] Update content on JooMooWebSites.com, replacing freelancer stuff with content aimed at selling my books
    - [ ] Consider switching to Material Design Bootstrap [MDB]
    - [ ] Stick to content that says what I have for sale, and what's in progress and coming soon
    - [ ] **Do not duplicate what's on TomWHartung.com**
- [ ] 6. TomWHartung.com - ~~Wordpress~~ -> Django and Material Design Bootstrap [MDB]
    - [ ] Upgrade MDB to latest version
    - [ ] Create new content on TomWHartung.com with a new menu and articles
    - [ ] Stick to content that says who I am and what I do, e.g., Download spreadsheets, article about my FFM results
    - [ ] **Do not duplicate what's on JooMooWebSites.com**

# Actual Steps Taken

Sites have their own site-specific file in this directory, e.g., `5b-groja.md`, containing details about what is changing.

# Plans for Updating

If an off-brand Material Design CSS library is no longer supported, switch to MDB.

Here is a list of sites and the sequence in which I am thinking I will upgrade them.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

This list needs review.

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

