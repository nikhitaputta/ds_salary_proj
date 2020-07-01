#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:39:08 2020

@author: nikhitaputta
"""

import glassdoor_scraper as gs
import pandas as pd
path = "/usr/local/bin/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15 )  
df
