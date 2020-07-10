#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:43:00 2020

@author: nikhitaputta
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split(' (')[0])
minus_KCAd = salary.apply(lambda x: x.replace('K','').replace('CA$',''))

#Delete these rows as they were duplicate
#df.drop([721,722,723,724], axis=0, inplace=True)

#Delete any duplicate rows
#df.drop_duplicates(subset=None,keep='first',inplace=True)

df['min_salary'] = minus_KCAd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_KCAd.apply(lambda x: int(x.split('-')[-1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#Company name text only

df['company'] = df.apply(lambda x:x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)
df['headquarters_location'] = df['Headquarters'].apply(lambda x: x.split(',')[0])
#df.drop('same_location',axis=1, inplace=True)
df['same_location'] = df.apply(lambda x: 1 if x.Location == x.headquarters_location else 0, axis = 1)

#df.columns

df.same_location.value_counts()

#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#parsing of job description (python, etc.)
df['Job Description'][2]

#pyhton
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#tableau
df['tableau_yn'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#Computer Science
df['computer_science_yn'] = df['Job Description'].apply(lambda x: 1 if 'computer science' in x.lower() else 0)
#machine learning
df['ml_yn'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)
#SQL
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index=False)
