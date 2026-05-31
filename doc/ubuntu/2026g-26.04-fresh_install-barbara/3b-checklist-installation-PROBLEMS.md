
# 3b-checklist-installation-PROBLEMS.md

This file details the PROBLEMS I had running the steps to install **Ubuntu 26.04** on `barbara` on **2026-05-17**.


## Running the Install - What Went OK

Following is a list of steps, for future reference, even when it's simple, but has been a while since the last time I did this:

- [X] Shutdown the PC
- [X] Disconnect all external USB storage drives

## **Problems** Running the Install

The short version is: HP has retired this PC!!

- I was unable to install 26.04 on **2026-05-17**
- I tried again on 2026-05-26, and that's when I figured out these efforts were futile

### Details Part 1

Following are the details of efforts made on **2026-05-17**:

- [X] Use the USB drive to boot the PC
  - [X] **Did not need to go into the PC's BIOS to get it to boot from the USB drive!!**
    - Or not?  Unable to run installation routine.  Hmmm...
    - Able to use F10 to get into the BIOS and the boot order is ok but ...
    - When it's using the USB drive to boot up I see this error message:
      - "**[27.851426] hp_bioscfg: unable to set bios settings on hp systems**"
    - One possible idea is this is due to the BIOS being out of date, so maybe finding the latest version and installing that will help?
    - Getting an updated copy of the BIOS requires the PC's "serial number, product number or product name":
      - Here is the number on a sticker on the back: MXL1220HN4
        - This is also on a sticker on the side, and is probably what we want!
        - Bzzt the web page says it's invalid.  Bastards!
      - Here is what looks like the product name on a sticker on the side: SYS/HP:6000/SFF/CD2:775:3.0/4
        - That is helping, giving a list of product names that match somewhat, but they are micro-towers and not what I have!
      - Here is the product key on a sticker on the side: 326XF-BQPVG-CFYB3-3FFV2-H9HDW
        - This is probably the Windows 7 [!!!] Product Key, pfft...
      - Maybe this will help find the BIOS we (presumably) might need:
        - BIOS -> File -> System Information:
          - Product Name: DC6000
          - SKU Number: BZ270US#ABA
          - Processor Type: Intel(R) Core(TM)2 Duo CPU E8400 @ 3.00GHz
          - System BIOS 786G2 v01.14
          - Chassis Serial Number: MXL1220HN4
          - Asset Tracking Number: MXL1220HN4
          - ME Firmware Virsion 5.2.10.1023
          - Management Mode: AMT
        - BIOS -> File -> About: System BIOS and Setup Utility (C) 1982-2010
      - Try this for grins:
        - BIOS -> Advanced -> Power-On Options:
          - POST Mode: Change from QuickBoot to FullBoot
            - I think this just made it do a memory test
          - POST Messages: Change from Disable to Enable
            - I think this just made it so I see more errors ...
            - Turned this back off

- This page, that I found when I first started trouble-shooting all this, explains how to update the BOIS on an HP **laptop**:
  - https://gist.github.com/eNV25/c8001491dc0440656ff7b0ae18993ba1?permalink_comment_id=4821494
- Note that this page is about HP **laptops**

### Details Part 2

This section contains details of efforts made 2026-05-26, when I finally had some more time to delve into all this.

The bottom line is here:

- **This URL: https://support.hp.com/us-en/retired-products says the HP Compaq 6000 Pro Small Form Factor PC is retired**
  - This could explain why I am having difficulty, ya think?!?!

The details follow:

- Tried running `fwupd`, `fwupdmgr` and `fwupdtool esp-list --verbose`, and got this warning
  - `UEFI ESP partition not detected or configured`
  - `See https://github.com/fwupd/fwupd/wiki/PluginFlag:esp-not-found for more information.`
- Tried searching for this error message, and google's AI thingie says it means:
  - "your system's EFI System Partition (ESP) is either missing, unmounted, or lacks the correct partition type."
- Delving into that, the ESP is supposed to be in `/boot/esp`, but that is missing from `barbara`
  - Running `df` shows that `/boot` is in the `/dev/sda2` partition
- **However:**
  - I ran the *disks* utility and saw there is a 1M `/dev/sda1` partition on the disk
  - I swear at one point I saw a page where I could download a new version of the BIOS? (*)
- But **now** the hp site is telling me this computer is *retired:* https://support.hp.com/us-en/retired-products
  - That might explain why this URL shows only All-in-One PCs and Towers: https://support.hp.com/us-en/deviceSearch?q=HP%206000%20SFF&origin=swd
    - (*) Maybe that page where I could download a new version of the BIOS I saw was really for one of those models?

**MOREOVER,** I can just use the Ubuntu that I already have installed (25.10) to upgrade to 26.04.

- So I am thinking about doing that, and probably will do so, soon...

