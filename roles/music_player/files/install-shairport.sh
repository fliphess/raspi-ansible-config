#!/bin/bash
cd /tmp
git clone https://github.com/hendrikw82/shairport.git
cd shairport
make
mv shairport /opt
