####################################################
#                  Revision: 1.0                   #
#              Updated on: 11/06/2015              #
####################################################

####################################################
#                                                  #
#   This File has all the Fixed Data that is used  #
#   to extract data from original .csv files and   #
#   generate Modified .csv files. This file also   #
#   contains fixed contents to generate a Word     #
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
import os


###################################################
#
#   This class contains all Fixed data used to 
#   extract and write data. Main purpose to keep
#   it in separate file is to make update process
#   easy.
# 
###################################################
class Fixed_Data:
   
    column_list=['\'Target Type','Target Name'
                ,'Access Specification Name',
                'IOps','MBps','Average Response Time'
                ,'Maximum Response Time',
                'Queue Depth','Read Errors','Write Errors']
            
            
    chassis_list=['D24','S2P','ATL','ULC','GLD','HRC']
        
    #cntrllr_list=['IOM_6G','IOM_Ga','IOM_XN']
        
    HP_option=['Y','N']
        
        
    ###################################################
    #
    #   Dictionary
    #   To make corresponding key 
    # 
    ###################################################    
    chassis_list_d={1:'D24',2:'S2P',3:'ATL',4:'ULC',5:'GLD'
                    ,6:'HRC'}
        
    cntrllr_list_d={1:'Nept',2:'Kryp',3:'Merc', 4:'Tita'
                    , 5:'Nitr', 6:'CrFX', 7:'CrMX', 8:'GaFX'
                    , 9:'GaLX', 10:'GaEX'}
        
    fw_type_d={'Q':'Qualification','R':'Regression'}
        
        
    ###################################################
    #
    #   Directory where template Word file is situated
    # 
    ###################################################
    fixed_dir= os.getcwd()
 
    fixed_dir=str(fixed_dir).replace('"','') 
    #removing double quotes
        
    
#####################################
#              END                  #
#####################################  