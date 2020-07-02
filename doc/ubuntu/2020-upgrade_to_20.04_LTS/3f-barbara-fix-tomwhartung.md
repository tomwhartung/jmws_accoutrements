
# 3f-barbara-fix-tomwhartung.md

Figure out how to fix tomwhartung.com .

# Magically Fixed?

While setting up and testing using ava as a backup server, I made some changes to the `08*.conf` apache config,
specifically updating the `ServerName` and `ServerAlias` parameters to match the other config files.

This caused ava to work better than barbara was working - two out of four test production urls worked ok instead of none -
and then when I tried barbara again all four of the production urls worked ok.

Interesting!

So it turns out this fix is no longer needed.

