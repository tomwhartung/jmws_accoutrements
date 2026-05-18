
# 3-checklist-installation.md

This version of `3-checklist-installation.md` reflects the steps I am performing to install **Ubuntu 26.04** on `barbara` on **2026-05-17**.


# Installing Ubuntu 26.04

Much of this is quite straightforward, answering several easy no-brainer questions that do not require further comment.

## Running the Install

Following is a list of steps, for future reference, even when it's simple, but has been a while since the last time I did this:

- [X] Shutdown the PC
- [X] Disconnect all external USB storage drives
- [X] Use the USB drive to boot the PC
  - [X] **Did not need to go into the PC's BIOS to get it to boot from the USB drive!!**
    - Or not?  Unable to run installation routine.  Hmmm...
    - Able to use F10 to get into the BIOS and the boot order is ok but ...
    - When it's using the USB drive to boot up I see this error message:
      - "**[27.851426] hp_bioscfg: unable to set bios settings on hp systems**"
    - One possible idea is this is due to the BIOS being out of date, so maybe finding the latest version and installing that will help?

I won't be able to fix this tonight, so we will have to return to this later.  Rats!

- [ ] Running the install on **2026-05-??** at **??:?? PM**
  - [ ] Answer these easy no-brainer questions
    - *Choose your language* - English
    - *Accessibility in Ubuntu* - None
    - *Select your keyboard layout* - English (US)
    - *Connect to the internet* - Use wired connection
    - *What do you want to do with Ubuntu?* - Install Ubuntu
    - *How would you like to install Ubuntu?* - Ineractive Installation
    - *What apps would you like to install to start with?* - Extended selection
    - *Install recommended proprietary software?*
      - [X] Install third-party software for graphics and Wi-Fi hardware
      - [ ] Download and install support for additional media formats - *this option is unavailable and greyed-out*
    - *How do you want to install Ubuntu?* - Erase disk and install Ubuntu
    - *Encryption and file system* - No encryption
    - *Create your account*
      - Your name: Tom H
      - Your computer's name: barbara
      - Your username: tomh
      - Password: tomh
      - Confirm password: tomh
      - [ ] Require my passowrd to log in - **Uncheck**
      - [ ] Use Active Directory - Leave unchecked
    - *Select your timezone* - Denver
    - *Review your choices*
      - Erase disk and install Ubuntu, etc.
  - [ ] Clicking the **Install** button at **[note the time here]**
  - [ ] Install finished at **[note the time here]**
  - [ ] Clicking the **Restart now** button
  - [ ] Please remove the installation medium, then press ENTER:

