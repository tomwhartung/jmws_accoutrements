
# 6-b-flexibility_plan.md

We need the ability to easily find and change the links we have in our content.

# Using Python Dictionaries

Idea: Use python dictionaries to store the links:

- Source links: specific to an affiliate site and possibly a specific advertiser
- Active links: source links actively used on the site
- AffiliateLinks model class: assigns source links to active links

## Process Overview

1. Source link storage:
   - Store affiliate source links in vendor-specific python dictionaries
   - E.g., afl_cj_bn, afl_cj_???, afl_???_???

2. In class AffiliateLinks, assign these to the python dictionaries used in the content
   - E.g., afl_content, afl_button

3. Active link usage:
   1. View gets active links from the AffiliateLinks model
   2. View passes active links to the view template
   3. Templates reference the active links, e.g., `{{ afl_button['wild_at_heart'] }}`

