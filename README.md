HOWTO INSTALL THE RASPBERRY BYTE: 

# Install ansible: 
```bash 

cd /tmp
git clone https://github.com/ansible/ansible.git
cd ansible
make install
mkdir /etc/ansible
cp examples/hosts /etc/ansible/

```
# Clone the raspberry git repository:
  
```
git clone git@github.com:fliphess/raspi-ansible-config.git

```

# Edit ansible.cfg
vim ./ansible.cfg

# Next: 

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

  From the raspberry Git Repository:
  - Run the installer:
   ./runme <IP Address of the Raspberry Pi> <module to install>

- Get coffee and wait
