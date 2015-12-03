USER=root
PASSWD=123
SQLPATH=/home/ubuntu/data_sync
OUTPUTPATH=/home/ubuntu/data_sync/stats

mysql -u$USER -p$PASSWD -e "source $SQLPATH/tem.sql" > /tmp/b01.csv
sed -i -e 's/\t/,/g' \/tmp\/b01.csv
iconv -c -f utf8 -t gbk /tmp/b01.csv > $OUTPUTPATH/zz.csv

