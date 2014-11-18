# -*- coding: utf-8 -*-
import csv, sys
import _mysql, string
import MySQLdb
from collections import OrderedDict

db = MySQLdb.connect("192.168.1.1","root","root123","infor_production", init_command="set names utf8")
cursor = db.cursor()
rows = ()
rowsall = rows

f = open('read_file.csv', 'r')
for row in csv.reader(f):
#    print row[0]
    cursor.execute("""
    SELECT ip_maps.ip, campus_buildings_lists.campus_name, campus_buildings_lists.building_name, ip_maps.room, adm_users.name
    FROM (ip_maps LEFT JOIN adm_users ON ip_maps.adm_user_id = adm_users.id) LEFT JOIN campus_buildings_lists ON ip_maps.campus_buildings_list_id = campus_buildings_lists.id
    WHERE ip = %s 
    """, (row[0]))

    rows = cursor.fetchmany(1)
    if rows == ():
        rows = ((' '), )
    rowsall = rowsall + rows
    with open('write_file.csv', 'w') as csvfile:
        w = csv.writer(csvfile, lineterminator='\n')  
        w.writerows(rowsall)  

f.close()  
