#定义shell变量
WORK_DIR := /home/ubuntu/data_sync

#定义脚本依赖,作业不要放在这个上面!!!
send_mail : rpt_order_principal_day hh temp_email
	python $(WORK_DIR)/send_mail.py
	@touch send_mail
hh: create_table uc_apply uc_area_group temp 

rpt_order_principal_day :     
	@touch rpt_order_principal_day_start
	python $(WORK_DIR)/rpt_order_principal_day.py
	@touch rpt_order_principal_day

create_table :     
	@touch create_table_start
	mysql -uroot -p test < /home/ubuntu/data_sync/create.sql
	@touch create_table

uc_apply : create_table
	@touch uc_apply_start
	mysql -uroot -p test </home/ubuntu/data_sync/uc_apply.sql
	@touch uc_apply

uc_area_group : create_table    
	@touch uc_area_group_start
	mysql -uroot -p test </home/ubuntu/data_sync/uc_area_group.sql
	@touch uc_area_group

temp : uc_area_group    
	@touch temp_start
	sh /home/ubuntu/data_sync/temp.sh
	@touch temp

temp_email : temp    
	@touch temp_email_start
	python /root/ufenqi/test/rpt_email.py
	@touch temp_email

