#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import click

stat_dir = '/home/ubuntu/data_sync/stats'
cur_dir = '/home/ubuntu/data_sync'


def get_valid_date(str):
    '''将输入字符串日期参数转换为datetime类型'''
    try:
        return datetime.datetime.strptime(str, '%Y%m%d')
    except:
        pass

def start_jobs(run_day, tag):
    '''开始调用某一日的作业'''
    work_dir = stat_dir + '/' + run_day
    try:
        os.mkdir(work_dir)
    except:
        pass
    os.chdir(work_dir)
    make_str = 'flock -xn /tmp/start_job_with_rule.' + run_day + \
        '.lock make -k -r -j 3 -f ' + cur_dir + \
        '/Makefile day=' + run_day + ' ' + tag
    click.secho("~" * 70, fg='green')
    click.secho("Start job with rule on this day: " + run_day, fg='blue')
    click.secho("~" * 70, fg='green')
    os.system(make_str)

@click.command()
@click.argument('begin_date')
@click.argument('end_date')
@click.argument('tag', nargs=-1)
def main(begin_date, end_date, tag):
    begin_date = get_valid_date(begin_date)
    end_date = get_valid_date(end_date)
    try:
        if begin_date > end_date:
            (begin_date, end_date) = (end_date, begin_date)

        try:
            tag = ' '.join(tag)
        except:
            tag = ''
    except:
        click.secho("oops!", fg='red')

    for i in range((end_date - begin_date).days + 1):
        i_day = begin_date + datetime.timedelta(days=i)
        start_jobs(i_day.strftime('%Y%m%d'), tag)

main()