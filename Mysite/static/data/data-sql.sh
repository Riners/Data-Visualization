#!/bin/bash

for i in `ls ./age-income.csv`
do
	mysql -uroot -pAdmin@123 -e "use mysite;LOAD DATA LOCAL INFILE '$i' INTO TABLE AgeIncomeRelationship FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n';"
done
