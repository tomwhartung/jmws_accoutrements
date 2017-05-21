# switching_servers

Following are the steps we need to run to switch the host serving the websites.

# Current Config

At this time we are using:

* ava as the production host
* barbara as the backup host

# Goal

Define the processes for switching between these two, so we can easily do this in
"the heat of the moment" (e.g., when ava goes down unexpectedly in the middle of the night).

# Processes

## Process (1) Switch from ava -> barbara

This process covers how to switch the current server from ava to barbara.

- [ ] Access the router
- [ ] Access the router's _________ option page
- [ ] Change the _____ from _____ to ____
- [ ] Test and confirm the switch

Maybe keep an eye on the log files for a bit to ensure every thing is working ok.

## Process (2) Switch from barbara -> ava

This process covers how to switch the current server from barbara back to ava.

# Why?

The process is simple and intuitive enough, but
we are adding https to one (and eventually most) of
our sites, and this may complicate things.

That is, I am concerned specifically about:

* The impact using https may have on this process
* The fact that we don't do this very often means it's easy to forget the simple steps


