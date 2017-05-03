# AdSense.md

Here is a guide to how I am setting up AdSense ads,
so I don't have to figure it all out all over again next time,
and they can be consistent, even if "next time" is a week or
five years or whatever from now.

# Rules

We *must* follow these rules, so that code is consistent and easy to maintain!

#### Rule (1): `base.html` defines all ad blocks

* 1.1: Each ad has its own block in `base.html` .
* 1.2: Each ad's block contains only the source code markup for that ad, and nothing else.

#### Rule (2): If a page wants an ad ...

To include the ad in a *_ad block, a page needs to:

* include that block in its source and
* call block.super() inside the block, to get the ad code

#### Rule (3): All ad source code is in `Site/content/adsense.py` .

* 3.1: Define a `*_IFRAME` variable for when we are `RUNNING_LOCALLY`
* 3.2: Define a `*_AD` variable for use on the life site

#### Rule (4): Each **location** maps to a single block and one channel

#### Rule (5): Each **ad unit** maps to a single block and one channel

* 5.1 Most locations display only one size ad (Example A)
* 5.2 Some locations display more than one size of ad (Example B)

# Process

This is the process for adding new ad blocks.
We cover two examples:

* Example A: add `top_left_ad` to the Galleries page
* Example B: add two differently sized `top_row_ad` blocks to the Galleries and Quiz pages

## Step (1): Update `base.html`

All ads are served from `Site/content/templates/content/base.html` .

#### Rule (1): `base.html` defines all ad blocks
#### Rule (4): Each **location** maps to a single block and one channel
#### Rule (5): Each **ad unit** maps to a single block and one channel

#### Example A:

Add the following code to the appropriate location (near the top) in
`Site/content/templates/content/base.html` :

```
{% block top_left_ad %}
  {{ adsense_ads.top_left_ad | safe }}
{% endblock %}
```

#### Example B:

Add the following code to the appropriate location (near the top) in
`Site/content/templates/content/base.html` :

```
{% block top_row_ad %}
  <div class="row">
    <div class="col-md-12">
      <div class="text-center">
        {% block top_row_large_billboard_ad %}
          {{ adsense_ads.top_row_large_billboard_ad | safe }}
        {% endblock %}
        {% block top_row_large_leaderboard_ad %}
          {{ adsense_ads.top_row_large_leaderboard_ad | safe }}
        {% endblock %}
      </div><!-- .text-center -->
    </div><!-- col-md-12 -->
  </div><!-- .row -->
{% endblock %}
```

Note that there are three new blocks:

* `top_row_ad` - corresponds to the channel
* `top_row_large_billboard_ad` - serves larger (billboard) ads in this block
* `top_row_large_leaderboard_ad` - serves smaller (leaderboard) ads in this block

## Step (2): Update page templates

#### Rule (2): If a page wants an ad ...

If a page wants to include the ad in a `*_ad` block, it needs to:

1. include that block in its template and
2. call `block.super()` .

#### Example A: Update `galleries.html`

##### 2.A.1 Updating `galleries.html`

Add the following code to the appropriate location (near the top) in
`Site/content/templates/content/galleries.html` :

```
{% block top_left_ad %}
  <div class="col-md-4">
    {{ block.super }}
  </div><!-- col-md-4 -->
{% endblock %}
```

#### Example B: Update the templates

We now add these blocks to `galleries.html`, `gallery.html`, and `quiz_base.html`

##### 2.B.1 Updating `galleries.html` and `gallery.html`

Add the following code to the appropriate location (near the top) in
`Site/content/templates/content/galleries.html` and
`Site/content/templates/content/gallery.html` :

```
{% block top_row_ad %}
  {% block top_row_large_billboard_ad %}{{ block.super }}{% endblock %}
  {% block top_row_large_leaderboard_ad %}{% endblock %}
{% endblock %}
```

We are showing the *content* of the `top_row_large_billboard_ad` block in the
`top_row_ad` *channel* block.

##### 2.B.2 Updating `quiz_base.html`

Add the following code to the appropriate location (near the top) in
`Site/content/templates/content/quiz_base.html` :

```
{% block top_row_ad %}
  {% block top_row_large_billboard_ad %}{% endblock %}
  {% block top_row_large_leaderboard_ad %}{{ block.super }}{% endblock %}
{% endblock %}
```

We are showing the *content* of the `top_row_large_leaderboard_ad` block in the
`top_row_ad` *channel* block.

## Step (3): Create ad and get code

Following is the process for creating and obtaining the ad code from google:

#### Rule (4): Each **location** maps to a single block and one channel
#### Rule (5): Each **ad unit** maps to a single block and one channel

### 3.1 Access the google adsense site in the browser:

* https://google.com/adsense

### 3.2 Log in if necessary and access "My ads"

"My ads" is an option in the hamburger menu up in the left-hand corner.

### 3.3 Create a new Ad unit

* Click on (My Ads) -> Content -> Ad Units
* Click on "+ New ad unit"

### 3.4 Ad names, sizes, and channels

Google prefers the Responsive ads, so use that size if possible.

- The standard for the name is: "[Block Name in Words] - [Ad size]"

We are also using Horizontal ads, Large Leaderboard and Billboard.

#### 3.4.1 Name, size, and channel used by Example A:

* Name: Top Left Ad - Responsive
* Size: Responsive
* Channel: top_left_ad

#### 3.4.2 Names, sizes, and channel used by Example B:

For the gallery pages:

* Name: Top Row Ad - Large Billboard
* Size: Large Billboard (click on "Recommended" and pick "Horizontal banner")
* Channel: top_row_ad - same as for the quiz pages

For the quiz pages:

* Name: Top Row Ad - Large Leaderboard
* Size: Large Leaderboard (click on "Recommended" and pick "Horizontal banner")
* Channel: top_row_ad - same as for the gallery pages

### 3.5 Fill in the form

This process is the same for all ads, except for the:

* names
* ad sizes
* custom channel

For details, see the previous section.

#### 3.5.1 Filling in the form:

- The standard for the name is: "[Block Name in Words] - [Ad size]"
- See the others ads and make sure it is consistent!
- Name: This time we are naming it: "Top Left Ad - Responsive"
- Ad size: Responsive (make sure it matches the name!)
- Ad type: Text & display (preferred - can change later)
- Text ad style: Default
- Custom channels: if this is new block, create one using the block name,
- I.e., Create custom channel -> Name: top_left_ad -> Save button
- Note that the new custom channel is selected, cool
- Backup ads -> Fill space with a solid color -> #CCCCCC
- Click on "Save"

Select and copy all of the ad code into the mouse buffer.

## Step (4): Update `adsense.py`

#### Rule (3): All ad source code is in `Site/content/adsense.py` .

Prerequisite: all of the code for the ads created in Step (3) is available

#### 4.1 Copy and paste ad code

Paste the code provided by google into `Site/content/adsense.py` ,
being sure to:

* Follow the naming conventions established previously
* Provide a definition for a corresponding `*_IFRAME` tag for display when `RUNNING_LOCALLY`
* Be mindful about formatting, being sure to leave spaces between double and single quotes, etc.!
* Be mindful about formatting - PEP-8!!

#### Example A:

For this example, we create two new constants:

* `TOP_LEFT_RESPONSIVE_IFRAME` - for when we are `RUNNING_LOCALLY`
* `TOP_LEFT_RESPONSIVE_AD` - for use on the life site

These of course are all going to look very similar except for:

* the width, height, and id attributes in the `*_IFRAME` code
* minor differences in the `*_AD` code supplied by google

Still it must be **absolutely perfect,** so be careful and double- and triple-check for typoes!

#### Example B:

For this example, we create four new constants:

* `TOP_ROW_LARGE_BILLBOARD_IFRAME` - for when we are `RUNNING_LOCALLY`
* `TOP_ROW_LARGE_LEADERBOARD_IFRAME` - for when we are `RUNNING_LOCALLY`
* `TOP_ROW_LARGE_BILLBOARD_AD` - for use on the life site
* `TOP_ROW_LARGE_LEADERBOARD_AD` - for use on the life site

These of course are all going to look very similar except for:

* the width, height, and id attributes in the `*_IFRAME` code
* minor differences in the `*_AD` code supplied by google

Still it must be **absolutely perfect,** so be careful and double- and triple-check for typoes!

#### 4.2 Update `adsense_ads` dictionary

Update the `adsense_ads` dictionary that appears at the very end of `Site/content/adsense.py` as follows.

##### 4.2.A Example A:

For example A, add the following entries to the dictionary:

* key: `'top_left_ad'`
* value: `TOP_LEFT_RESPONSIVE_IFRAME` when `RUNNING_LOCALLY`
* value: `TOP_LEFT_RESPONSIVE_AD` when **NOT** `RUNNING_LOCALLY`

##### 4.2.B Example B:

For example B, add the following entries to the dictionary:

* key: `"top_row_large_billboard_ad"`:
* value: `TOP_ROW_LARGE_BILLBOARD_IFRAME` when `RUNNING_LOCALLY`
* value: `TOP_ROW_LARGE_BILLBOARD_AD` when **NOT** `RUNNING_LOCALLY`

and

* key: `"top_row_large_leaderboard_ad"'`
* value: `TOP_ROW_LARGE_LEADERBOARD_IFRAME` when `RUNNING_LOCALLY`
* value: `TOP_ROW_LARGE_LEADERBOARD_AD` when **NOT** `RUNNING_LOCALLY`

## Step (5) Test

#### 5.1 Test `RUNNING_LOCALLY`

Start the development server and access this URL:

* http://127.0.0.1:8000/galleries

If that looks ok, i.e., there is a grey box where we want the ad to be ....

#### 5.2 Test **NOT** `RUNNING_LOCALLY`

Restart apache:

```
sudo service apache2 restart
```

And access this URL:

* http://jane.seeourminds.com/

Note that it may take awhile to see an actual ad in this location.

And if that looks ok, i.e., there is an open area where we want the ad to be ....

## Step (6) Commit, push, and deploy

Commit and push the changes to github.

Log on the backup and production hosts, and pull the new code.

