#####danta monitoring####
 nohup python3 -u /data2/web/jialj/WES_DB/GD/db_backup_monitor/DataMonitoring.py 2>&1 >> /data2/web/jialj/WES_DB/GD/db_backup_monitor/scan.log &
####data backup::crontab -e
0 2 * * * source ~/.bashrc && sh /data2/web/jialj/WES_DB/GD/db_backup_monitor/databackup_gd.sh  >> /data2/web/jialj/WES_DB/GD/db_backup_monitor/databackup.log 2>&1 
