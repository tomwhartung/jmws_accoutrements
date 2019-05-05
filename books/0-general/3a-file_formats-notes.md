
# 3a-file_formats-notes.md

Notes and concerns about the various file formats available for publishing ebooks.

## The Main Concern: Images

### Initial Impressions

Putting "thumbnail" images in tables works fine in odt, docx, and pdf files.

Following are some disappointments found when converting odt to epub, mobi, and azw3 formats.

- Tables of images look like crap
- Centered images are no longer centered
- Captions can be misplaced from the image at some screen sizes

### Brute Force Fix

Next time consider:

- Combining images with their captions into a single jpg
- Combining multiple images into one, each including its caption, into a single jpg

This will be foolproof but will also require a bit of work.

## Exporting and Converting

### Exporting

- Exporting a pdf from Libre Office works ok
- Exporting an epub from libre office does not work at this time
  - Tried all options

### Converting

- Use calibre to convert
  - Add odt or docx file
  - Convert option opens a dialog box
  - Have NOT tried all options - not by a long shot

The conversion dialog box contains a lot of options and one group of them is dependent on the output file type.

- Converting with calibre works much better than exporting from libre office
- There are still issues with the images, though
  - Tables of images do not look right
  - The images are not centered on pages with just one image

### Calibre Conversion Options

Have been trying these, and it seems that at least they do not make it any worse:

#### Fresh tries, 2019-05-05:

##### ODT -> MOBI

- Look & Feel
  - [x] Disable font size rescaling
- Heuristic Processing
  - [ ] Maybe try this at some point
- Page Setup
  - Output profile
    - Have tried Kindle and Tablet, but images get messed up
    - [x] Default Output Profile - try this time
  - Input profile
    - Default Input Profile
- Structure detection
- Table of contents
  - [x] Force use of auto-generated ToC
- Search and Replace
- MOBI output
  - [x] Do not add ToC to book
- Debug

Results:

- OK except the tables containing images are messed up
  - Should be able to fix this by using the individual images to create a new combo image

