#!/bin/sh
cur_date=`date '+%Y-%m-%d %H:%M:%S'`
echo 'NOW TIME:'.$cur_date
pwd_dir=`pwd`
echo $pwd_dir
pid=`ps -ef | grep jialj| grep GD_WES_CLINIC | grep -v grep|awk -F' ' '{print $2}'`
echo $pid

if [  -n "$pid" ]; then 
echo "There are processes running,Start the next process 1 day later !" 
exit 0
else
cur_date=`date '+%Y-%m-%d %H:%M:%S'`
echo 'Start At:'.$cur_date
cur_day=`date '+%Y-%m-%d'`
suffix=cur_day
clinic='clinic.'$cur_day'.json'
echo $clinic
coresnv='coresnv.'$cur_day'.json'
echo $coresnv
note='note'.$cur_day.json
echo $note
corecnv='corecnv'.$cur_day'.json'
echo $corecnv
supplement_report='supplement_report'.$cur_day'.json'
echo $supplement_report
negative_appendix='negative_appendix'.$cur_day'.json'
echo $negative_appendix
extend_data='extend_data'.$cur_day'.json'
echo $extend_data
cd /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/
mkdir $cur_day
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_CLINIC --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$clinic
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_RESULT --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$coresnv
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NOTE --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$note
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_VUS --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$corecnv
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_SUPPLEMENT_REPORT --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$supplement_report
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NE_APPENDIX --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$negative_appendix
/usr/local/bin/mongoexport --host 10.100.15.30 --db gd --collection GD_WES_EXTEND --out /data2/web/jialj/WES_DB/GD/db_backup_monitor/json/$cur_day/$extend_data
zip -r $cur_day.zip $cur_day
rm -rf $cur_day
touch md5.txt
/usr/bin/md5sum *.zip >> md5.txt
cd /data2/web/jialj/WES_DB/GD/db_backup_monitor/
echo 'Sucesss'
cur_date=`date '+%Y-%m-%d %H:%M:%S'`
echo 'End At:'.$cur_date
fi 
