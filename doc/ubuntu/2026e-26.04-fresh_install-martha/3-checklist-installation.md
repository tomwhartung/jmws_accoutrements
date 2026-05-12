
# 3-checklist-installation.md

This version of `3-checklist-installation.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-11**.


# Installing Ubuntu 26.04

Much of this is quite straightforward, answering several easy no-brainer questions that do not require further comment.

## Running the Install

Following is a list of steps, for future reference, even when it's simple, but has been a while since the last time I did this:

- [X] Shutdown the PC
- [X] Disconnect all external USB storage drives
- [X] Use the USB drive to boot the PC
  - [X] May need to mess with the BIOS to get it to boot from the USB drive
  - [X] To enter the BIOS, power on the PC then immediately press the **Delete** key
  - [X] To change the Boot Sequence:
    - Find the *Boot Priority* box in the middle and near the top of the main page
    - Click on the USB-A image "*UEIF USB Key*", and drag it to the left of the internal disk image "*UEFI Hard Disk: ubuntu (WD Blue SN570)*"
    - Click on the *SETTINGS* box on the left side of the page
    - Click on the *Save & Exit* option in the menu that appears in the main area of the screen
  - [X] For more information about the BIOS, see the manual in this directory: `PROCOMP_b686-manual.pdf`
- [X] When the GNU GRUB menu appears:
  - Use the arrow keys (if necessary) to select the *Try or Install Ubuntu* option
  - Press the Enter key
- [X] Starting the install on **2026-05-11** at **9:42 PM**
  - [X] Answer easy no-brainer questions
    - *Choose your language* - English
    - *Accessibility in Ubuntu* - None
    - *Select your keyboard layout* - English (US)
    - *Connect to the internet* - tomsasus
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
      - Your computer's name: martha
      - Your username: tomh
      - Password: tomh
      - Confirm password: tomh
      - [ ] Require my passowrd to log in - **Uncheck**
      - [ ] Use Active Directory - Leave unchecked
    - *Select your timezone* - Denver
    - *Review your choices*
      - Erase disk and install Ubuntu, etc.
  - [X] Clicking the **Install** button at **10:04 PM**
  - [X] Install finished at **10:09**
  - [X] Clicking the **Restart now** button
  - [X] Please remove the installation medium, then press ENTER:


