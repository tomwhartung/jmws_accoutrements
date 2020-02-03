
# 3f-barbara-chrome.md

Installing chrome is easy, but I am thinking it would be good to note the commands I use, in case there are issues or whatever.

## Reference

With over 500 upvotes, this looks good:

- https://askubuntu.com/questions/510056/how-to-install-google-chrome

## Installation

Run these commands as tomh:

```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
# OK
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
# deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main
sudo apt-get update
sudo apt-get install google-chrome-stable
```

## Running Chrome the First Time

```
which google-chrome-stable
google-chrome-stable &
```

1. Log in to sync settings.
2. Find icon in taskbar, move it to a location next to Firefox, and lock it there.
3. Exit and use the taskbar icon to run it in the future.

