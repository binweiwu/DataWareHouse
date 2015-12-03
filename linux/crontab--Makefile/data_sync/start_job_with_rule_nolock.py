#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

stat_dir = '/home/ubuntu/data_sync/stats'
cur_dir = '/home/ubuntu/data_sync'


def get_valid_date(str):
    '''将输入字符串日期参数转换为datetime类型'''
    try:
        return datetime.datetime.strptime(str, '%Y%m%d')
    except:
        pass


def start_jobs(run_day):
    '''开始调用某一日的作业'''
    work_dir = stat_dir + '/' + run_day
    try:
        os.mkdir(work_dir)
    except:
        pass
    os.chdir(work_dir)
    make_str = 'make -k -r -j 3 -f ' + cur_dir + \
        '/Makefile day=' + run_day + ' ' + tag
    print "~" * 70
    print "Start job with rule on this day: " + run_day
    print "~" * 70
    os.system(make_str)

try:
    begin_date = get_valid_date(sys.argv[1])
    end_date = get_valid_date(sys.argv[2])
    if begin_date > end_date:
        (begin_date, end_date) = (end_date, begin_date)

    try:
        tag = ' '.join(sys.argv[3:])
    except:
        tag = ''
except:
    print "usage: python start_job_with_rule.py begin_date(like:YYYYMMDD) end_date(like:YYYYMMDD) [tag1 tag2 ...]"
    sys.exit(1)

for i in range((end_date - begin_date).days + 1):
    i_day = begin_date + datetime.timedelta(days=i)
    start_jobs(i_day.strftime('%Y%m%d'))
