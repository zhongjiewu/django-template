#!/bin/bash

FILE_DIR=$(dirname $0)

function install_pip_packages()
{
  pip install -r $FILE_DIR/requirements.txt
}

function install_npm_packages()
{
  npm install -g less
}

function install_by_apt_get()
{
  while read packages
  do
    apt-get install -y $packages
  done < $FILE_DIR/apt-get-packages.txt
  # link node
  which nodejs >& /dev/null
  if [[ $? -eq 0 ]]
  then
    ln -s `which nodejs` /usr/bin/node
  fi
}

function install_by_brew()
{
  uid=$(stat -f %u `which brew`)
  while read packages
  do
    sudo -u \#$uid brew install $packages
  done < $FILE_DIR/brew-packages.txt
}


if [ ! `whoami` == 'root' ]
then
  echo "Must run as root"
  exit
fi

if [[ $(which brew > /dev/null; echo $?) -eq 0 ]]
then
  echo "Found brew. Using brew to install"
  install_by_brew
elif [[ $(which apt-get > /dev/null; echo $?) -eq 0 ]]
then
  echo "Found apt-get. Using apt-get to install"
  install_by_apt_get
else
  echo "No supporting package management program found. Only support brew install apt-get Exiting"
  exit
fi
install_pip_packages
install_npm_packages
