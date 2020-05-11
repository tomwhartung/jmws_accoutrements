
# 1d-jane-upgrade_all_sites.md

Get all sites working on jane, now running 20.04, with the latest stable versions of underlying software:

- Python
- Flask
- Django

# Checklist

These are the sites I am supporting, and that need to be updated:

[ ] ArtsyVisions.com
[ ] Groja.com
[ ] JooMooWebSites.com
[ ] SeeOurMinds.com
[ ] TomHartung.com
[ ] TomWHartung.com

# Latest Stable Versions

Per the wikipedia.

- Python: 3.8.2
  - Stable release: 3.8.2
  - Already installed with 20.04
  - 3.8.x: Full support through 2021-04, with security fixes through 2024-10
- Flask: 1.1.2
  - Stable release: 1.1.2
- Django: 3.0.6
  - Stable release: 3.0.6
  - 3.2 LTS: due 2021-04, will be supported until at least 2024-04
  - 4.0: due 2021-12, will be supported until at least 2023-04


# Additional Goals

While updating these sites, also make the following changes:

[ ] ArtsyVisions.com
    - Content ok for now
[ ] Groja.com
    - Fix security alert: https://github.com/tomwhartung/groja.com/network/alert/Site/static/js/jquery-3.3.1.min.js/jquery/open
    - Reexamine conversions to prevent spam
[ ] JooMooWebSites.com
    - Update content on JooMooWebSites.com, replacing freelancer stuff with content aimed at selling my books
[ ] SeeOurMinds.com
    - Fix security alert: https://github.com/tomwhartung/seeourminds.com/network/alert/Site/content/static/content/js/jquery-3.3.1.min.js/jquery/open
[ ] TomHartung.com
    - Content ok for now
[ ] TomWHartung.com
    - Replace the WP version of TomWHartung.com with a new, minimal Flask version, also aimed at selling my books

Each site has its own file in this directory containing details about what I want to change.

# Plan for Upgrading

# Actual

