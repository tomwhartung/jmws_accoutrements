# AdSense.md

Here is a guide to how I am setting up AdSense ads,
so I don't have to figure it all out all over again next time,
and they can be consistent, even if "next time" is a week or
five years or whatever from now.

# Rules

Please follow these rules, so that code is consistent and easy to maintain!

### Rule (1): All ad source code is in `Site/content/adsense.py` .

### Rule (1): All ads are served in `Site/content/templates/content/base.html` .

### Rule (1): Each ad has its own block in `base.html` .

### Rule (1): Each ad's block contains only the source code markup for that ad, and nothing else.

### Rule (1): If a page wants to include the ad in a `*_ad` block...

If a page wants to include the ad in a `*_ad` block, it needs to:
(1) include that block in its template and
(2) call block.super().

# Process

This is the process for adding a new ad block:

* `top_left_ad`

to the Galleries page, i.e., the `Site/content/templates/content/galleries.html` template.

## Step (1): Update `base.html`

#### Rule: All ads are served in `base.html` .

Add the following code to the appropriate location in `base.html` :

```
{% block top_left_ad %}
  {{ adsense_ads.top_left_ad | safe }}
{% endblock %}
```

## Step (2): Update `galleries.html`

#### Rule: If a page wants ads in a *_ad block, it needs to include that block and call block.super().

