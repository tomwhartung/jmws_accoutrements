
# 6-mdb5_tips_and_tricks.md

Tips learned about MDB5 while updating the sites to use it.

## Masks

The MDB4 `mask rgba-black-strong` classes used on the home page of groja.com no longer work the same.

Now use code such as `class="mask" style="background-color: rgba(0, 0, 0, 0.6);"`.

For more masking effects see:

- https://mdbootstrap.com/docs/standard/content-styles/masks/

## Shadows

The MDB4 `z-depth-1-half`, etc. classes are gone.

Now use the `shadow-1`, `shadow-1-strong`, ... `shadow-5`, `shadow-5-strong` classes.

For more hover effects see:

- https://mdbootstrap.com/docs/standard/content-styles/hover-effects/

## Hoverability

The MDB4 `hoverable` class is gone.

Now use the `hover-shadow` class.

For more hover effects see:

- https://mdbootstrap.com/docs/standard/content-styles/hover-effects/
