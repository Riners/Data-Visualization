# Web数据可视化设计服务运行教程 #
操作系统：Ubuntu Server 16.04
python版本：python3.5
Django版本：2.6
因为环境部署过程中，会涉及到更改软件更新源，修改数据库配置等操作，建议选择一台干净的机器进行，建议选择VMware创建虚拟机来进行部署。
一、安装需要的软件包
操作系统为Ubuntu Server 16.04
镜像下载地址：`https://mirrors.aliyun.com/ubuntu-releases/xenial/ubuntu-16.04.4-server-amd64.iso`
一键部署并运行项目
```
tar -xf project.tar
cd project
bash run.sh
```
脚本执行过程中，如有报错，按照提示排查问题，然后重新运行脚本即可。脚本运行结束之后，通过`http://ip:8080/air_quality`来访问web服务。
FAQ
run.sh脚本是用于一键部署该web服务的工具，如果遇到脚本运行报错，多半是依赖包安装问题，根据提示安装相关的依赖包即可,比如Django、pymysql、mariadb等。
