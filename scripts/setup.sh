#!/bin/bash

# ============================
# Config
# ============================

REPOSITORY_URL="git@github.com:HosokawaKenchi/ukb_rap_usage_notes.git"


# ============================
# Set up apt
# ============================

apt-get update > /dev/null 2>&1
apt-get install unzip

# ============================
# SSH Key generation & register
# ============================

echo "Generate new ssh keys..."
ssh-keygen -t rsa -b 4096 -f "/root/.ssh/id_rsa" -N "" <<< y > /dev/null 2>&1
echo "Generated new ssh keys!"
echo "Please open the following link to register your SSH key to Github"
echo ""
echo "https://github.com/settings/ssh/new"
echo ""
echo "The public key created is shown below. Please “COPY and PASTE” this key to register."
echo "########### PUBLIC KEY ############"
cat /root/.ssh/id_rsa.pub
echo "########### PUBLIC KEY ############"
read -p "Press ENTER to proceed to the next step..." -r

# ============================
# Set Email for Git
# ============================

read -p "Please enter the email address you would like to set up for Git: " EMAIL
if [ -z "$EMAIL" ]; then
  echo "No e-mail address has been entered. Processing will be aborted."
  exit 1
fi
git config --global user.email "$EMAIL"

# ============================
# Clone Repository
# ============================

# clone a repository
echo "Clone ${REPOSITORY_URL}"
git clone -q ${REPOSITORY_URL}