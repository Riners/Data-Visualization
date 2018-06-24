#!/bin/bash
#Author: Riners Ma
#created: 2018-06-14

#脚本需要运行在root用户下，判断当前用户是否为root
if [ `id -u` != 0 ];then
	echo 'Please run it in root user!'
	exit 1
else
	echo "You are root user!Let's begin!"
	sleep 2
fi


BASEDIR=`pwd`
#更改软件更新源为阿里云源，然后安装相关软件包
mv /etc/apt/sources.list /etc/apt/sources.list.bak
cp conf/sources.list /etc/apt/
apt-get clean
apt-get update && apt-get -y upgrade
apt-get -y install python3-pip
mkdir ~/.pip
cp $BASEDIR/pip.conf ~/.pip/
pip3 install Django==2.0.6
pip3 install pymysql
apt-get -y install mariadb-server
#配置数据库信息
sed -i "s/127.0.0.1/0.0.0.0/g" /etc/mysql/mariadb.conf.d/50-server.cnf
service mysql  restart
#创建数据库并导入数据
mysql -e "drop database if exists mysite;"
mysql -e "create database mysite;"
mysql mysite < $BASEDIR/conf/mysite.sql
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'Admin@123' WITH GRANT OPTION;"
#运行Django的web服务，端口可修改
python3 $BASEDIR/Mysite/manage.py runserver 0.0.0.0:8080
