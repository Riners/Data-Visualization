#!/bin/bash
for i in "$1"
do
a=`echo $i|awk -F '.' '{print $1}'`;
mysql -uroot -pAdmin@123 -e "use mysite;LOAD DATA LOCAL INFILE '$i' INTO TABLE $a FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n';"
done
