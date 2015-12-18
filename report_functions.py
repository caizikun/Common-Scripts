####################################################
#                  Revision: 1.0                   #
#              Updated on: 11/06/2015              #
####################################################

####################################################
#                                                  #
#   This File has all the Functions used to        #
#   extract data from original .csv files and      #
#   generate Modified .csv files. This file also   #
#   contains Functions to generate a Word          #
#   Report.                                        #
#                                                  #
#   Author: Zankar Sanghavi                        #
#                                                  #
#   © Dot Hill Systems Corporation                 #
#                                                  #
####################################################


###################################################
#
#   Importing required packages
# 
###################################################
import pandas
import numpy as np
from openpyxl import load_workbook
import csv
import matplotlib.pyplot as plt


class Report_Functions:

    ###################################################
    #
    #   "find_string" Function is used to search a
    #   particular string in a .csv file. It returns
    #   string(s)'s Index and its count/occurrence.
    #
    #   "data" should be any .csv format file
    #
    #   It can search string in Row-wise as well as
    #   Column-wise. It will search Row-wise if selection
    #   is set to 0. While for 1 it will search Column-wise
    #   
    #   "number" is used to select particular row or 
    #   column in which want column-wise or row-wise
    #   search. 
    #   
    #   Example:
    # 
    #   Let's say we have a .csv file called "ABC" 
    #   which has 2 columns and 4 rows. Now we want 
    #   to search string "XYZ" in 2st column, row-wise
    #   search. So our setting should be:
    #   
    #   find_string(ABC,1,0,'XYZ') 
    #   number=1 as python starts from 0
    #
    #   It returns: 
    #               1.)Index of that string 
    #               2.)Its occurrence/count 
    #
    #   TIP: 
    #   To find string in whole document(.csv), just
    #   keep it in a loop, where "number" should be a 
    #   variable.
    ###################################################
    def find_string(data,number,selection,input_string): 
    
        data=np.array(data)
        count = 0
        index=[]
    
        if selection==0: # 0 is for row-wise search
            for i in range(len(data)):
                if data[i,number]==''+str(input_string):
                    count += 1;
                    index.append(i)
            #print(count,index)
            return [count,index]
    
        elif selection==1: # 1 is for column-wise search
            for i in range(len(data[0,:])):
                if data[number,i]==''+str(input_string):
                    count += 1;
                    index.append(i)
            #print(count,index)
            return [count,index]
    
        else:
            return print('Invalid Selection, Enter 0'\
            'for Row-wise search OR 1 for Column-wise search')

            
            
    ###################################################
    #
    #   Average Function
    #   
    #   Basically this returns Average of a particular
    #   column and range is specified by "no_of_disks"
    #   
    #    This function is created to Add Average of IOps
    #   ,MBps, etcetera columns 
    ###################################################
    def avg_of_disks(data,column,no_of_disks):
    
        avg=0
        total=0
        
        for i in range(0,no_of_disks):
            total += float(data[i][column])
            
        avg=total/no_of_disks 
        return avg
    
    
    ###################################################
    #
    #   Swap Function
    #   
    #   It swaps a two elements of a list and returns
    #   a list. 
    #   
    ###################################################
    def swap_func(lst,i,j): # avg should be a list
        s1=lst[i]           # swaps i with j element 
        s2=lst[j]
        temp=0
        #print(s1,s2,temp)
        temp=s1
        s1=s2
        s2=temp

        lst[i]=s1
        lst[j]=s2
        #print(s1,s2,temp)
        return lst
        
        
    ###################################################
    #
    #   set_column_width Function
    #   
    #   It changes width of particular column in table
    #   where we write Modified .csv files to a Word
    #   template.
    #      
    ###################################################
    def set_column_width(column, width):
        for cell in column.cells:
            cell.width = width
    
    
    ###################################################
    #
    #   set_row_bold Function
    #   
    #   It changes font to bold of particular rows
    #      
    ###################################################
    def set_row_bold(rows):
        for cell in rows.cells:
            #font.bold=True
            #print('')
            pass    #disabled
            
      
    ###################################################
    #
    #   extract_data Function
    #   
    #   It extracts data of column from a Worksheet
    #   and returns a list.
    #   
    #   ws_x = worksheet
    #   x_column = particular column of worksheet with data
    #   data_lst = [] should be empty list for 1st instance
    #                 then we can continue to make list from
    #                 other worksheets in the same way
    #
    ###################################################
    def extract_data(ws_x,x_column,data_lst):
    #model_data=[]
        v=len(ws_x.rows)-1
        for row in (ws_x.iter_rows(str(x_column)+'2:'
                    +str(x_column)+str(v))):
                    
            for cell in row:
                data_lst.append(cell.value)
            
        return data_lst
        
    
    ###################################################
    #
    #   no_of_steps Function
    #   
    #   It finds Steps along with Number Disk(s) in a 
    #   Single Step.
    #   
    #   We use "find_string" function to find Index and 
    #   Count of a string "DISK"" in data. Using this 
    #   disk_count and disk_index, we can find total steps
    #   and Number of Disks in a Step.
    #   
    ###################################################
    def no_of_steps(disk_index,disk_count):
        for j in range(len(disk_index)):
            if disk_index[j]-disk_index[j-1]>1:
                disk_no=j #finding  no of disks
                break
        steps=int(disk_count/disk_no) # no. of steps  
        return [steps,disk_no]
        
  
#####################################
#              END                  #
#####################################   