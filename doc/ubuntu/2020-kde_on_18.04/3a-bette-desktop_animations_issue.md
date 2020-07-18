
# 3a-bette-desktop_animations_issue.md

Desktop effects do not work.

This is **not** a big issue.

# Troubleshooting

Found a couple of References, but they were unhelpful.
Saving them in this file for possible future reference.

## References

- (1) https://askubuntu.com/questions/1129364/desktop-effects-not-working-after-update-kubuntu-18-04
  - Found in original search
- (2) https://stackoverflow.com/questions/22318322/what-is-the-difference-between-opengl-and-xrender-in-kde-desktop-effects
  - Found in a comment to the solution in (1)

## Results

Running the command suggested in (1) gave some unexpected results.

```
# qdbus org.kde.KWin /KWin supportInformation | grep -i composit
Service 'org.kde.KWin' does not exist.
#
```

Rats.

Trying the suggestion in (2) -- note that the Rendering backend is **now set in Display and Monitor** -- was also unhelpful.

Ratsaroni.

