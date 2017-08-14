# tag_manager.md

Here is a guide to how I am setting up Google Tag Manager,
so I don't have to figure it all out all over again next time.

# Overview

## Google Analytics (GA)

### Purpose

- Gathers statistics
- Generates reports

### Compatible Tags

- Google Adwords Conversion Tag
- Google Adwords Remarketing Tag
- Facebook Pixel Code
- Others


## Google Tag Manager (GTM)

### Purpose

- Define rules for when tags should fire

### Tag Types

- GA Tracking Code
- GA Event Code
- AdWords Conversion Script
- Others


# References

## Information

- https://www.analyticsmania.com/post/google-tag-manager-vs-google-analytics/


## Login URLS

- https://analytics.google.com/
- https://tagmanager.google.com/


# Current Status

## SeeOurMinds.com

GA script near the end of base.html: UA-87860502-4

## Groja.com

GTM script near the beginning of base.html: GTM-5C9M49W

## JooMooWebSites.com

GA script in templates/jmws_beez3_idmygadget/google_analytics.php: UA-87860502-1
GA script in templates/jmws_protostar_idmygadget/google_analytics.php: UA-87860502-1
GA script in templates/jmws_protostar_tomh_idMyGadget/google_analytics.php: UA-87860502-1

## TomWHartung.com

GA script in wp-content/themes/idmygadget_twentyfifteen/google_analytics.php: UA-87860502-2

# Process

This is the process for adding new tags.




