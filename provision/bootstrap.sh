#!/usr/bin/env bash

##
# Bash script to provision VM, used to set up test environment.
# The is the correct home for one time builds/installations 
# required to set up the demonstrators.
#
# Be aware this script is only the first time you issue the
#    vagrant up
# command, or following a
#    vagrant destroy
#    vagrant up
# combination.  See the README for further detais.
##

# apt update
apt-get update

# Install tools for downloading and building matchbox and dependencies
apt-get install -y git build-essential make cmake

# We will install these headers as we need boost.  The opencv packages aren't currently used but kept here for future use
# opencv ubuntu packages: libopencv-dev libcv-dev libopencv-features2d-dev libhighgui-dev 
# remove the above packages so FindOpenCV.cmake doesn't get confuseds
apt-get remove -y libopencv-dev libcv-dev libopencv-features2d-dev libhighgui-dev 
apt-get install -y libboost-all-dev zlib1g-dev libjpeg8-dev libpng12-dev libtiff4-dev libjasper-dev libgtk2.0-dev python-numpy libopenexr-dev

# Set up OpenCV build directory
rm -rf /vagrant/build
mkdir -p /vagrant/build/opencv-bin
cd /vagrant/build

# Set OpenCV version number
OPENCVVER=2.4.6.1

# Download and extract the OpenCV source, create and move to a build directory
wget -O opencv-${OPENCVVER}.tar.gz http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/${OPENCVVER}/opencv-${OPENCVVER}.tar.gz && tar zxf opencv-${OPENCVVER}.tar.gz
mkdir opencv-$OPENCVVER/build
cd opencv-$OPENCVVER/build

# Build and install OpenCV
cmake .. -DCMAKE_INSTALL_PREFIX=../../opencv-bin
make -j6
make install

# Move to matchbox build dir (/vagrant/build on this VM)
cd /vagrant/build

# This is the path to the installed OpenCVConfig.cmake
# NOTE: a *full* path to the file should be passed to cmake, hence the addition of `pwd`
pwd
cmake .. -DOpenCV_DIR=`pwd`/opencv-bin/share/OpenCV/
make -j6
cpack

ls -al *.deb
dpkg --info *.deb

sudo dpkg -i scape-matchbox*deb
ldd /usr/bin/mb_extractfeatures
/usr/bin/mb_extractfeatures --help
ldd /usr/bin/mb_compare
/usr/bin/mb_compare --help
ldd /usr/bin/mb_train
/usr/bin/mb_train --help
