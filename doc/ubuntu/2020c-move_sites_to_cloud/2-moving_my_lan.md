
# 2-moving+my_lan.md

Notes to help move my lan from forethought.net to xfinity.

# Existing LAN - Forethought.net

Notes pertaining to how my lan is set up for using forethought.net's connection.

## Shared Values

These values are shared by **all existing connections**.

- DNS Servers: 192.168.30.2, 192.168.31.2
- Netmask: 255.0.0.0
- Gateway: 10.0.0.1
- broadcast: 10.255.255.255

Sources:

- (0) - Linux host -> `/etc/hosts` `ifconfig` and Settings -> Connections

## Hosts and Their Static IP Addresses

- ava's IP Address: 10.0.0.117
- barbara's IP Address: 192.168.1.116
- bette's IP Address: 10.0.0.112
- jane's IP Address: 10.0.0.113
- lauren's IP Address: 10.0.0.110

Sources:

- (0) - Linux host -> `/etc/hosts` `ifconfig` and Settings -> Connections

# Update Existing LAN - Move `ava` to TP-Link

Moving host `ava` from the asus wireless router to the TP-Link router, **so we can use it to access `barbara`**.

1. Create new connection in Settings -> Connections
- Wired - forethought - tp-link
  - Update IP address to 192.168.1.117
  - Update gateway to 192.168.1.1
2. .ssh changes - guessing here
  2.1. Rename `~/.ssh/known_hosts` on `barbara` to `~/.ssh/known_hosts-2020_11_14`
  2.2. Rename `~/.ssh/known_hosts` on `ava` to `~/.ssh/known_hosts-2020_11_14`
3. Switch cable
4. Switch to new "Wired - forethought - tp-link" connection
5. Test access to `barbara`

# New LAN - Xfinity.com

Notes pertaining to how my lan is set up for using xfinity's connection.

I want this to be as similar as possible to what I am using now.

## Updating Asus Router

Need to change the configuration on the Asus Router to work with the Xfinity modem/router.

### 1. Update LAN IP Addresses

- Current IP of Asus router is 10.0.0.1
- Current IP of Xfinity modem/router is 10.0.0.1

**Need to change IP of Asus router to 10.0.0.2 .**

[x] 1. Change IP of Asus router to 10.0.0.2
    [x] 1.1. Asus Config -> Advanced Settings -> LAN
    [x] 1.2. LAN IP tab -> IP Address field -> 10.0.0.2
    [x] 1.3. Click on Apply

**Now access Asus router at 10.0.0.2 .**

### 2. Update WAN IP Addresses

- Current WAN IP Settings:
  - IP Address: 192.168.1.2
  - Subnet Mask: 255.255.255.0
  - Default Gateway: 192.168.1.1

**Need to change these to use Xfinity router at 10.0.0.1 .**

- New WAN IP Settings:
  - IP Address: 10.0.0.2
  - Subnet Mask: 255.255.255.0
  - Default Gateway: 10.0.0.1

[x] 2. Update WAN IP of Asus router to 10.0.0.2
    [x] 2.1. Asus Config -> Advanced Settings -> WAN
    [x] 2.2. Internet connection tab -> IP Address field -> 10.0.0.2
    [x] 2.3. Internet connection tab -> Default Gateway field -> 10.0.0.1

**DO NOT CLICK ON APPLY QUITE YET!!**

### 3. Update WAN DNS Addresses

- Current WAN DNS Settings:
  - DNS Server1: 192.168.30.2
  - DNS Server2: 192.168.31.2

**Need to change these to use Xfinity name servers at 75.75.75.75 .**

- New WAN DNS Settings:
  - DNS Server1: 75.75.75.75
    - Should be ok
  - DNS Server2: 2001:558:feed::1
    - Will this work?

[x] 3. Change DNS Servers on Asus router to 75.75.75.75
    [x] 3.1. Asus Config -> Advanced Settings -> WAN
    [x] 3.2. Internet connection tab -> DNS Server1 field -> 75.75.75.75
    [x] 3.3. Internet connection tab -> DNS Server2 field -> 2001:558:feed::1
    [x] 3.4. Click on Apply

Check:

[x] On command line:
  [x] `ping 10.0.0.2`
  [ ] `ping 10.0.0.1`
  [x] `ping google.com`
[x] In xfinty phone app

### 4. Trying DHCP

Try setting up the Asus to use DHCP to get its IP address.

- Asus router -> General -> Network Map -> Internet status: Disconnected
  - Click on Disconnected
  - Spins then skips Step 1 and advances to ...
  - Step 2 Internet Setup
    - Static IP is selected
    - Change to Automatic IP (DHCP)
    - Click on Next
    - Host Name(optional) field:
      - Fill in Asus
    - DNS Server1 field:
      - Already set to 75.75.75.75
    - Click on Next
    - Spins then **backs up** to ...
  - Step 1 Check Connection
    - Says step 1 of 2 is to Turn off the Cable/DSL modem
    - Now says to click next to use new router IP address: 10.0.1.2
    - Reboots and redirects to 10.0.1.2
  - Step 3 Router Setup
    - Keep previous wireless settings tomsasus/pwd
    - Click on Apply
  - Completed Network Configuration Summary
    - Wireless - unchanged
    - WAN
      - WAN Connection Type - Automatic IP
      - WAN IP - 10.0.9.188
    - LAN
      - LAN IP - 10.0.1.2
      - MAC C8:60:00:AB:B6:D4
    - Click on Next

Asus -> General -> Network Map -> **Internet status: Connected!**

Xfinity phone app shows new device named **Asus-13**

**I think it will be ok to allow the Xfinity modem to set the IP of the Asus dynamically.**

We really just need static IP on the hosts.  **I think.**

## Static IP on `bette`

Give `bette` a static wired IP address on the new network.

### Create new Connection on `bette`

- Settings -> Network -> Connections -> + (new)
- Select Wired Ethernet and Click on Create
  - Connection Name: Wired-xfinity-asus-static
  - IPv4 Tab:
    - Method: Manual
    - DNS Servers: 75.75.75.75
    - Click on "+ Add"
      - Address: 10.0.1.112
      - Netmask: 255.0.0.0 -- filled in automatically
      - Gateway: 10.0.**1**.2 -- Use the new Asus IP!

Seems to work OK!

## Static IP on `jane`

Give `jane` a static wired IP address on the new network.

### Create new Connection on `jane`

- Settings -> Network -> Connections -> + (new)
- Select Wired Ethernet and Click on Create
  - Connection Name: Wired-xfinity-asus-static
  - IPv4 Tab:
    - Method: Manual
    - DNS Servers: 75.75.75.75
    - Click on "+ Add"
      - Address: 10.0.1.113
      - Netmask: 255.0.0.0 -- filled in automatically
      - Gateway: 10.0.**1**.2 -- Use the new Asus IP!

Seems to work OK!

## Update System Files

Update `/etc/hosts` and `.ssh/*` files on `bette` and `jane`.

### Fix `/etc/hosts` Files

[x] 1. Fix entries for `bette` in `/etc/hosts` on `jane`
    -  Change `10.0.0.112` to `10.0.1.112`
    -  Also fix `lauren`: change `10.0.0.110` to `10.0.1.110`
[x] 2. Fix entries for `jane` in `/etc/hosts` on `bette`
    -  Change `10.0.0.113` to `10.0.1.113`
    -  Also fix `lauren`: change `10.0.0.110` to `10.0.1.110`
[x] 3. Fix entries for `jane` in `/etc/hosts` on `bette`

### Fix `.ssh/*` Files

Remove `~/.ssh/known_hosts` files on `bette` and `jane`.

## Static IP on `lauren`

Give `lauren` a static wireless IP address on the new network.

### Change the Connection on `lauren`

- Settings -> Network -> Wireless -> tomsasus -> '>' icon
  - Click on Settings Button
  - IPv4 Settings Tab:
    - Method: Manual
    - DNS Servers: 75.75.75.75
    - Edit values under Addresses
      - Address: 10.0.**1**.110
      - Netmask: 255.0.0.0 -- filled in automatically
      - Gateway: 10.0.**1**.2 -- Use the new Asus IP!

Update `/etc/hosts` and remove the `~/.ssh/known_hosts` file.

Seems to work OK!

## Static IP on `ava`

Give `ava` a static wireless IP address on the new network.

### Create new Connection on `ava`

- Settings -> Network -> Connections -> + (new)
- Select Wired Ethernet and Click on Create
  - Connection Name: Wired-xfinity-asus-static
  - IPv4 Tab:
    - Method: Manual
    - DNS Servers: 75.75.75.75
    - Click on "+ Add"
      - Address: 10.0.1.117
      - Netmask: 255.0.0.0 -- filled in automatically
      - Gateway: 10.0.**1**.2 -- Use the new Asus IP!

Update `/etc/hosts` and remove the `~/.ssh/known_hosts` file.

Also update `/etc/hosts` on `bette`, `jane`, and `lauren`.

Seems to work OK!


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Notes From Yesterday

## Shared Values -- Wireless, DHCP

These values are shared by **new connections**.

- WAN IP Address (1): 107.2.247.79
- DNS Mode (2): DHCPv4
- Primary DNS (2): 75.75.75.75
- Secondary DNS (2): 2001:558:feed::1
- Netmask (1): 255.255.255.0
- Gateway (1)(3): 10.0.0.1 ??
- broadcast (3): 10.0.0.255

Sources:

- (1) - Xfinty app -> My Network -> Advanced Settings -> LAN & WAN
- (2) - Xfinty app -> My Network -> Advanced Settings -> DNS Server
- (3) - Linux host -> `ifconfig`

## Hosts and Their Automatic IP Addresses

- ava's IP Address: N/A
- barbara's IP Address: N/A
- bette's IP Address (3)(4): 10.0.0.40
- jane's IP Address (3)(4): 10.0.0.180
- lauren's IP Address (3)(4): 10.0.0.123

Sources:

- (3) Linux host -> `ifconfig`
- (4) Xfinty app -> Connect (Devices or X Devices Not Connected->Device) -> Device Details -> IP Address (way at the bottom)


?????????????????????????????????????????????

I do not recall trying static IP on wireless.

## Shared Values -- Wireless, Static IP

These values are shared by **new connections**.

- WAN IP Address (1): 107.2.247.79
- DNS Mode (2): DHCPv4
- Primary DNS (2): 75.75.75.75
- Secondary DNS (2): 2001:558:feed::1
- Netmask (1): 255.255.255.0
- Gateway (1), (3): 10.0.0.1
- broadcast (3): 10.0.0.255

Sources:

- (1) Xfinty app -> My Network -> Advanced Settings -> LAN & WAN
- (2) Xfinty app -> My Network -> Advanced Settings -> DNS Server
- (3) Linux host -> `ifconfig`

## Hosts and Their Static IP Addresses

- ava's IP Address: 10.0.0.117 ??
- barbara's IP Address: 192.168.1.116 ??
- bette's IP Address: 10.0.0.112 ??
- jane's IP Address: 10.0.0.113 ??
- lauren's IP Address: 10.0.0.110 ??

