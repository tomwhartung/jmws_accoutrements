
# 6b-analysis_of_requirements

Identify what the real goals are and the easiest way to acheive them.

# Self-Signed vs. Let's Encrypt

## Lessons Learned

I thought the Self-Signed certs would be good for use on the local host.

* This works, but we get an ugly red "Not secure" icon instead of the green lock that we want.
* There's really very little advantage to this, that I can see.

**I see nothing wrong with using http on jane, and https on barbara and ava.**

## Why Do This in the First Place?

Look at our reasons for doing this.

### PWAs

We first started this so we could play around with Progressive Web Apps (PWAs).

* For PWA development, we do not need https on the local host.
* If at some point it turns out that we do need https on the local host, we can
just learn to live with the ugly red "Not secure" message.

### Forms and Search

As time has progressed, this is inreasingly looking like a great idea:

* If we are going to host forms, we should be using https.
* If we want google search results to bring visitors to the site.
* If we want to sell **anything** online with total transparency, https is the way to go!

### Https Is a Must-Have!

Wordpress (and others?) are starting to display a notice when accessing the admin panel via http.

Once we get one site going, switching the others over should be a cinch.

# Re-considering the Goals

## Essential Goals

It's clear that we will need to use certificates from Let's Encrypt on the
production and backup hosts.

## Nice-to-Have Goals

It would be nice to have the development host match the production and backup
hosts, but in this case, that is really more of a nice-to-have goal than an
essential goal.

# Questions

## A Big Question

Is it possible to use the Let's Encrypt option on jane, even though it is not
accessible publicly?

**Try to figure out the answer to this question while setting up Let's Encrypt on ava and barbara.**

## A Smaller Question

Do we really need to use the Self-Signed option on jane?

It's looking like the answer is "No," and that we can revert back to http
on the development host.

We wasted a bit of time getting that all set up, but we can use what we've
learned to get the Let's Encrypt option going on ava and barbara.

