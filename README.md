# Ansible playbooks for configuring my raspberry pi

## Setup

#### Install ansible:
```bash 
 
cd /tmp
git clone https://github.com/ansible/ansible.git
cd ansible
make install
mkdir /etc/ansible
cp examples/hosts /etc/ansible/
 
```

#### Clone the raspberry git repository:
  
```
git clone git@github.com:fliphess/raspi-ansible-config.git
 
```

#### Edit ansible.cfg
```bash
vim ./ansible.cfg
```
 
#### Next: 
 
- Connect Display, Network and Keyboard to the Pi
- Boot the raspberry pi (Plug in power cable)
- run raspi-config: (This runs automatically at first boot)
	- expand (root) filesystem
	- change User Password to 'something'
        - enable boot to desktop -> Set to NO!
	(If "Run Memory Split is not in the menu click 'Advanced Options'):
	  - overscan -> enable  ( may be in : 'in advanced menu')
	  - run memory split -> GPU = 128 mb ( may be in : 'in advanced menu')
	  - turn on ssh server  ( may be in : 'in advanced menu')
	  - overclock -> modest 
	  - update raspi-config
	* Finish 
	* if asked to reboot, click "Yes"

- get ip -> ip a
- setup ssh: ssh-copy-id -i PUBKEY pi@<IP>

#### Run 
```bash 
./runme <host or ip> "recipes/<recipe file>"
```
- Get coffee and wait


## Modules: 

#### basic-config
Some basics to configure our raspberry pi into something wonderfull
Includes: 
  * Basic config for raspberry pi (to be listed)

#### remote-webserver
Configures a lighttpd webserver with php5 and cgi and setup a basic admin panel in python
Includes:
  * Lighttpd
  * php-fpm, fcgiwrap
  * python admin panel

#### fruitywifi 
Setup your raspberry pi to run fruitywifi pentesting tools 

#### metasploit 
Setup metasploit

#### security camera
Turn your raspberry pi + camera  into a remote wifi accessible security cam
  * spi, i2c
  * motion-mmal

#### NAS 
Setup your raspberry pi to be a homebrew network attached storage.
Includes: 
 * Samba - Windows Filesharing
 * SWAT - Samba Web Administration Tool
 * dnsmasq - DNS, DHCP, TFTP, PXEBoot 

#### Music Box
Setup your raspberry pi to serve your music 
<in progress>

*To setup a pxe boot, see https://github.com/fliphess/auto-netboot-builder*
