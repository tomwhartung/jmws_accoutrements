
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

The MDB4 `hoverable` and `z-depth-*` classes are gone.

Now use the `hover-shadow` and `shadow-*` classes.

- **Note:** the `hover-shadow` and `shadow-*` classes must be in different, i.e., nested, `div` elements
- I like to use `hover-shadow` on the outer `div` and `shadow-*` on the inner `div`

For example:

```
<div class="card hover-shadow m-2">
 <div class="shadow-5">
  <div class="card-body">
   . . .
   . . .
   . . .
  </div><!-- .card-body -->
 </div><!-- .shadow-* -->
</div><!-- .card -->
```

For more hover effects see:

- https://mdbootstrap.com/docs/standard/content-styles/hover-effects/

## Forms

Css classes for forms have changed someone.

- Each input tag should be in a div with `class="form-outline"` instead of `"md-form"`
- `label` tags should now have `class="form-label"` set

