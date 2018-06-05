#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
ORA='\033[0;33m'
NC='\033[0m'
echo "Testing HDFS configuration"
for i in `cat hdfs-site.xml |grep name|cut -d">" -f2|cut -d"<" -f1`
	do
		par_string="<name>$i</name>"
		a=`grep $par_string  default-hdfs.xml|wc -l`
		if [ $a -eq 1 ]
		then
			val_in_def_file=`grep -A1 $par_string default-hdfs.xml |grep value|cut -d'>' -f2|cut -d'<' -f1`
			val_in_clus_file=`grep -A1 $par_string hdfs-site.xml |grep value|cut -d'>' -f2|cut -d'<' -f1`
			if [ "$val_in_def_file" == "$val_in_clus_file" ]
				then 
					echo -e ${GREEN}"[OK]"${NC} $i"  "$val_in_def_file" | "$i"  "$val_in_clus_file
				else
					echo -e ${RED}"[DIFF]"${NC} $i"  "$val_in_def_file" | "$i"  "$val_in_clus_file
			fi
		else
			echo -e "${ORA}[WARN]${NC} Value $i is not present in default configuration"
		fi
done

