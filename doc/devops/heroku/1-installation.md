
# Heroku Installation

Installed heroku on bette during the fourth Real Python class.

## References

Heroku installation (see the Debian/Ubuntu section):

- https://devcenter.heroku.com/articles/heroku-cli

Details from class can be found in:

- in 08-real_python_class/2017_03_07-Lesson_4/class_notes.txt in the always_learning_python repo

## Steps

Ran these commands to install heroku on bette on 2017-03-07:

```
sudo apt-get install software-properties-common
```

Oops, looking at this later, apparently this was supposed to be run on "Debian only." (Hmm, Ubuntu is debian, right...?)

After looking it up, I see it installs the add-apt-repository command, so we should be ok.

```
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
heroku --version          ## heroku-cli/5.6.29-ac5c0de (linux-amd64) go1.7.5
```

