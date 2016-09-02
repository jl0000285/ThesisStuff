# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:01:49 2016

@author: o-4

Simple file parser program written to make data sets with catagorical data in them readible for shogun 
machine learning algorithms 
"""

import subprocess
import csv
import numpy as np


#lc = last column, variable that tells the parser whether or not the last column needs to be saved in a seperate file
#t_file = namae of the target file 



def parse_file(lc, t_file):
    "target file"
    t_file = "../data/uci/adult/adult.data" 
    t_in = []
    "Conversion boolean-boolean to see if a data set requires set conversion"
    c_b = False; 
    
    with open (t_file, 'rb') as csvfile:
        rdr = csv.reader(csvfile, delimiter=',')
        for row in rdr:
            t_in.append(row)
            for i in row:
                try:
                    float(i)
                except ValueError:
                    c_b = True;
    num = 0    
    cols = []   
    
    """
    If conversion is neccessary, iterate thru values of the first line, then 
    add unique values in columns were conversion fails into a list.
    """
    
    if(c_b == True):
        for i in t_in[0]:
            try: 
                float(i)
            except ValueError: 
                cols.append(num)
                colcode = "col_" + str(num) + " = [] "
                exec colcode 
                for j in t_in:
                    if j != [] and j != None: 
                        #if j[num] not in col_num
                        #col_num.append(j[num])
                        colcheck = "if j[" + str(num) + "] not in col_" + str(num) + ": \r \t \t"
                        coladd = "col_" + str(num) + ".append(j[" + str(num) + "])" 
                        colcom = colcheck + coladd
                        exec colcom
            num = num + 1
    
    """
    Once the unique value lists have been crafted, replace string values with index of value within a given lists in the t_in 
    data structure
    """
    num = 0        
    for j in t_in:
        for i in cols:
            if j != [] and j != None:
                #t_in[num][i] = col_i.index(t_in[num][i])
                swapcode = "t_in[num][i] = col_" + str(i) + ".index(t_in[num][i])"
                exec swapcode
        num = num + 1    
      
    """
    Write the parsed data to a new csv file
    """ 
    
    if(lc == 0):
      newfile = t_file + ".parse"
      writefile = open(newfile,'wb')
      wr = csv.writer(writefile)
      wr.writerows(t_in)
    if(lc == 1):
      newfile = t_file + ".pdata"
      newfile2 = t_file +  ".plabel"
      w1 = open(newfile,'wb')
      w2 = open(newfile2, 'wb')
      t_lc = []
      end = len(t_in[0]) - 1
      tc = 0
      for i in t_in:
          if i != [] and i != None: 
              t_lc.append([i[end]])
              del t_in[tc][end]
          tc = tc + 1    
      wr1 = csv.writer(w1)
      wr2 = csv.writer(w2)
      wr1.writerows(t_in)
      wr2.writerows(t_lc)
      
    
            
    
    #subprocess.call(["./bal_con"])
      