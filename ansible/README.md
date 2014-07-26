# Ansible playbooks for configuring my raspberry pi

# Modules: 

## basic-config
Some basics to configure our raspberry pi into something wonderfull
Includes: 
  * Basic config for raspberry pi (to be listed)

## remote-webserver
Configures a lighttpd webserver with php5 and cgi and setup a basic admin panel in python
Includes:
  * Lighttpd
  * php-fpm, fcgiwrap
  * python admin panel

## fruitywifi 
Setup your raspberry pi to run fruitywifi pentesting tools 

## metasploit 
Setup metasploit

## security camera
Turn your raspberry pi + camera  into a remote wifi accessible security cam
  * spi, i2c
  * motion-mmal

## NAS 
Setup your raspberry pi to be a homebrew network attached storage.
Includes: 
 * Samba - Windows Filesharing
 * SWAT - Samba Web Administration Tool
 * dnsmasq - DNS, DHCP, TFTP, PXEBoot 

### To setup a pxe boot, see https://github.com/fliphess/debian-netboot-with-bnx2
