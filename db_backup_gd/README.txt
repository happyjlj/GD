【说明--数据备份和监控】
1.数据备份
	每天早上2点，备份一次，7个表格
	0 2 * * * source ~/.bashrc && sh /data2/web/jialj/WES_DB/GD/db_backup_monitor/databackup_gd.sh  >> /data2/web/jialj/WES_DB/GD/db_backup_monitor/databackup.log 2>&1
2.数据监控
	监控每天存入CLINIC的数据
	nohup python3 -u /data2/web/jialj/WES_DB/GD/db_backup_monitor/DataMonitoring.py 2>&1 >> /data2/web/jialj/WES_DB/GD/db_backup_monitor/scan.log &
