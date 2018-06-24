#!/bin/bash

for i in `ls ./ip_info.csv`
do
	mysql -uroot -pAdmin@123 -e "use mysite;LOAD DATA LOCAL INFILE '$i' INTO TABLE ipv4_addr_info_1 FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n';"
done
