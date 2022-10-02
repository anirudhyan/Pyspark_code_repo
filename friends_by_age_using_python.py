# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:34:01 2022

@author: anirudhya n
"""

with  open("fakefriends.csv",'r') as f1:
    global no_of_frnds_dict 
    no_of_frnds_dict = {}
    global no_of_people_dict 
    no_of_people_dict = {}
    for line in f1:
        records_trimmed = line.strip()
        records = records_trimmed.split(',')
        age = int(records[2])
        no_of_frnds = int(records[3])
        
        if age in no_of_frnds_dict.keys():
            no_of_frnds_dict[age] = no_of_frnds_dict[age] + no_of_frnds
            no_of_people_dict[age] = no_of_people_dict[age] + 1
        else:
            no_of_frnds_dict[age] = no_of_frnds
            no_of_people_dict[age] = 1
    avg_no_of_frnds_by_age ={}
    for k1,k2 in no_of_frnds_dict.items():
        avg_no_of_frnds_by_age[k1] = no_of_frnds_dict[k1]/no_of_people_dict[k1]
    print(avg_no_of_frnds_by_age)
                