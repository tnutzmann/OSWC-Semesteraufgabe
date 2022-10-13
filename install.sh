#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
apt -yq update && apt -yq upgrade
apt -yq install apache2 apache2-utils python3 && apt-get clean -yq

a2enmod cgi

wget https://raw.githubusercontent.com/tnutzmann/OSWC-Semesteraufgabe/main/conf/cgi-apache.conf -O /etc/apache2/conf-available/cgi-enabled.conf

a2enconf cgi-enabled

mkdir -p /var/www/html/cgi && cd /var/www/html/cgi

git clone https://github.com/tnutzmann/OSWC-Semesteraufgabe.git
mv OSWC-Semesteraufgabe/src/* .
rm -rf OSWC-Semesteraufgabe/

chmod 707 /var/www/html/cgi
chmod 705 /var/www/html/cgi/index.cgi
chmod 666 /var/www/html/cgi/todo_cgi.log
chmod 666 /var/www/html/cgi/todo.db

systemctl restart apache2
