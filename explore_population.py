#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:36:00 2021

@author: aarongorman
"""

cv.data.show_locations()
#'United Kingdom'

# Note data format and key names!
# can design bespoke demographic make - up

joburg_pop = {
   '0-9':  286620,
  '10-19': 277020,
  '20-29': 212889,
  '30-39': 161329,
  '40-49': 104399,
  '50-59': 51716,
  '60-69': 36524,
  '70-79': 22581,
  '80+':   7086}

cv.data.country_age_data.data['Johannesburg'] = joburg_pop
#You can then use these data via 
sim = cv.Sim(location='Johannesburg')