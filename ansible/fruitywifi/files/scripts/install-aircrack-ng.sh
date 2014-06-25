#!/bin/bash
# Install aircrack ng from source 

function die() { echo -e "Error in $0: $1\n"; exit 1;}

TMP="/tmp/aircrack-install" 

# Get url to latest version tgz
DOWNLOAD="$( curl -qqq  -- http://download.aircrack-ng.org/ 2</dev/null | grep Linux | sed -e 's/^.*="//' -e 's/">.*$//' )" || die "Failed to get download link"

# Get latest tgz
mkdir -p "$TMP" && cd "$TMP"          || die "Failed to create temp dir"
wget -O "$TMP/aircrack.tgz" $DOWNLOAD || die "Failed to download the latest version of AIRCRACK NG"

# unpack tgz
tar -xvzf "$TMP/aircrack.tgz"         || die "Failed to extract the download tgz file"

# get extracted dir
DIR="$( find . -maxdepth 1 -type d  | tail -1 )" || die "Failed to get extracted directory"
cd "$DIR" || die "Failed to cd to $DIR"

# Build 
echo "###################################################"
echo "# Running MAKE"
echo "###################################################"
make || die "Failed to make"

echo "###################################################"
echo "Running make install"
echo "###################################################"
make install || die "Failed to make install"

echo "###################################################"
echo "Updating aircrack-ng"
echo "###################################################"
airodump-ng-oui-update
