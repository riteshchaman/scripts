db_type=`grep -w server.jdbc.database /etc/ambari-server/conf/ambari.properties|cut -d= -f2`
db_name=`grep -w server.jdbc.database_name /etc/ambari-server/conf/ambari.properties|cut -d= -f2`
db_host=`grep -w server.jdbc.hostname /etc/ambari-server/conf/ambari.properties|cut -d= -f2`
db_user=`grep -w server.jdbc.rca.user.name /etc/ambari-server/conf/ambari.properties|cut -d= -f2`
backupdir_name=/var/log/backups
date=`date +"%Y%m%d-%H%M%S"`
if [ ! -d $backupdir_name ]
then
    mkdir -p $backupdir_name
fi
if [ $db_type == postgres ]
then
        echo "The Ambari database is postgres. Running backup command"
        pg_dump -h $db_host -U $db_user $db_name > /var/log/backups/ambaridb_bakup-$date 2> $backupdir_name/script-err_$date
        if [ $? == 0 ]
        then
                echo "Backup successfully taken"
        else
        	 echo "back up has error. Please check $backupdir_name for log file"
        fi
else
        echo "No database found. Please run the command manually"
fi

echo "Backing up Jaas file"
cp  /etc/ambari-server/conf/krb5JAASLogin.conf /etc/ambari-server/conf/krb5JAASLogin.conf_$date
