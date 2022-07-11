# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:46:37 2022

@author: 916620
"""

import datetime
import os 

current_Datetime = datetime.datetime.now()

start_time_cls_1_string = '09:00'
start_time_cls_1_date = datetime.datetime.strptime(current_Datetime.strftime('%Y:%m:%d')+":"+start_time_cls_1_string,'%Y:%m:%d:%H:%M')

stop_time_cls_1_string = '05:00'
stop_time_cls_1_date = datetime.datetime.strptime(current_Datetime.strftime('%Y:%m:%d')+":"+stop_time_cls_1_string,'%Y:%m:%d:%H:%M')

start_time_cls_2_string = '18:00'
start_time_cls_2_date = datetime.datetime.strptime(current_Datetime.strftime('%Y:%m:%d')+":"+start_time_cls_2_string,'%Y:%m:%d:%H:%M')

stop_time_cls_2_string = '21:00'
stop_time_cls_2_date = datetime.datetime.strptime(current_Datetime.strftime('%Y:%m:%d')+":"+stop_time_cls_2_string,'%Y:%m:%d:%H:%M')

if current_Datetime >= start_time_cls_1_date and current_Datetime < stop_time_cls_1_date:
    print("Starting cls 1")
    os.popen('')
else:
    print("Stopping cls 1")
    os.popen('')

if current_Datetime >= start_time_cls_2_date and current_Datetime < stop_time_cls_2_date :
    print("Starting cls 2")
    os.popen('')
else:
    print("Stopping cls 2")
    os.popen('')