
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
  - Update gateway to 192.168.0.1
2. .ssh changes - guessing here
  2.1. Rename `~/.ssh/known_hosts` on `barbara` to `~/.ssh/known_hosts-2020_11_14`
  2.2. Rename `~/.ssh/known_hosts` on `ava` to `~/.ssh/known_hosts-2020_11_14`
3. Switch cable
4. Switch to new "Wired - forethought - tp-link" connection
5. Test access to `barbara`

# New LAN - Xfinity.com

Notes pertaining to how my lan is set up for using xfinity's connection.

I want this to be as similar as possible to what I am using now.

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

