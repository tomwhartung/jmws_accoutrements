
# 3f-barbara-fix-tomwhartung.md

Figure out how to fix tomwhartung.com .

# SSL Issue?

Because the site works fine on jane, which does not use SSL,
but fails on barbara, which does use SSL, the issue is probably SSL.

## The Most Likely Reason SSL is Failing

The most likely reason the other sites work and tomwhartung.com does not is
because I switched tomwhartung.com from using WP to using django.

# Possible Fix: New Certificate

Assuming the issue is SSL, an obvious possible fix is to generate a new certificate.

