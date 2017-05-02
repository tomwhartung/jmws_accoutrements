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

Add the following code to the appropriate location in `galleries.html` :

```
{% block top_left_ad %}
  {{ block.super }}
{% endblock %}
```

## Step (3): Create ad and get code

### Process:

#### 3.1 Access the google adsense site in the browser:

* https://google.com/adsense

#### 3.2 Log in if necessary and access "My ads"

* "My ads" is an option in the hamburger menu up in the left-hand corner.

#### 3.3 Create a new Ad unit

* Click on (My Ads) -> Content -> Ad Units
* Click on "+ New ad unit"
* Fill in the form
** Google prefers the Responsive ads, so use that if possible.
** The standard for the name is: "[Block Name in Words] - [Ad size]"
** See the others ads and make sure it is consistent!
** Name: This time we are naming it: "Top Left Ad - Responsive"
** Ad size: Responsive (make sure it matches the name!)
** Ad type: Text & display (preferred - can change later)
** Text ad style: Default
** Custom channels: if this is new block, create one using the block name,
** I.e., Create custom channel -> Name: top_left_ad -> Save button
** Note that the new custom channel is selected, cool
** Backup ads -> Fill space with a solid color -> #CCCCCC
** Click on "Save"
* Select and copy all of the ad code into the mouse buffer.

## Step (4): Update `adsense.py`

#### 4.1 Paste code

Paste the code provided by google into `Site/content/adsense.py` ,
being sure to:

* Follow the naming conventions established previously
* Provide a definition for a corresponding "*_IFRAME" tag for display when RUNNING_LOCALLY
* Be mindful about formatting, being sure to leave spaces when necessary, etc.!

For this example, we create two new constants:

* `TOP_LEFT_RESPONSIVE_IFRAME` - for when we are RUNNING_LOCALLY
* `TOP_LEFT_RESPONSIVE_AD` - for use on the life site

These of course all look very similar except for minor differences in the
code supplied by google.

#### 4.2 Update `adsense_ads` dictionary

Update the `adsense_ads` dictionary that appears at the end of `adsense.py` with:

* key: `'top_left_ad'`
* value: `TOP_LEFT_RESPONSIVE_IFRAME` when RUNNING_LOCALLY
* value: `TOP_LEFT_RESPONSIVE_AD` when NOT RUNNING_LOCALLY



