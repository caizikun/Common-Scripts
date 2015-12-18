####################################################
#                  Revision: 1.1                   #
#              Updated on: 12/16/2015              #
#                                                  #
#   What's new:                                    #
#               Minor tweaks in formatting         #
#               including addition of SSD string   #
#               in some questions.                 #
####################################################

####################################################
#                  Revision: 1.0                   #
#              Updated on: 11/06/2015              #
####################################################

####################################################
#                                                  #
#   This File prompts all User Inputs used to      #
#   extract data from original .csv files and      #
#   generate Modified .csv files.                  #
#                                                  #
#   Author: Zankar Sanghavi                        #
#                                                  #
#   © Dot Hill Systems Corporation                 #
#                                                  #
####################################################


###################################################
#   Importing required packages
###################################################
import pandas
import numpy as np
import extract_lists
import fixed_data 


######################################################
#
#   This class has All User inputs for Data Extraction
#   (i.e. For Modified .csv file(s)) and Word 
#   Report Generation.
# 
######################################################
class User_Inputs:

    ###################################################
    #
    #   This section has variables designed used to 
    #   save bunch of User inputs depending upon 
    #   no. of Files.
    # 
    ###################################################
    original_file_path=''
    no_files_concatenate=0
    file_names=[] 
    cap_names=[]
    model_no_names=[]
    chassis_names=[]
    cntrllr_names=[]
    fw_no_names=[]
    vendor_names=[]
    eco_names=[]
    fw_type_names=[]
    product_fnames=[]
    word_file=''

    ##########################################
    #
    #   Prompts for Original .csv file 
    #
    ##########################################
    def org_path(number):
        original_file_path = input('\nEnter full file path of'\
                    ' Original file #'+str(number)+' to execute: ')
                    
        original_file_path=str(original_file_path).replace('"','')
        return original_file_path


    ##########################################
    #
    #   Prompts for HP drives or BB/SSD 
    #   drives selection
    #
    ##########################################
    def hp_question():
    
        HP_option= fixed_data.Fixed_Data.HP_option
        
        while True:
            HP_dec=input('\nPlease Enter (Y/N) for HP Drives'\
                         ' selection: ')
                         
            if HP_dec in HP_option:
                print('\nValid Entry')
                break
            else:
                print('\nInvalid entry, Please Re-enter')

        return HP_dec
            
            
    ##########################################
    #
    #   Prompts for Qualification or Regression 
    #   selection
    #
    ##########################################
    def fw_type():
        fd = fixed_data.Fixed_Data
        while True:
                fw_type= input('\nIs it a Q: Qualification or'\
                               ' R: Regression of HDD/SSD Firmware? : ')
                fw_type=str(fw_type)
                if fw_type in (fd.fw_type_d).keys():
                    print('\nValid Entry \n')
                    break
                else:
                    print('\nInvalid Entry \n') 
        return fw_type
            
    
    ##############################################
    #
    #   1.)Prompts to Enter Model Number till it  
    #   is from "Supported_drives.xlsx" file. 
    #
    #   2.)Extracts Capacity, Vendor, Firmware, ECO 
    #   number, and Product family name of User 
    #   entered Model number. 
    #
    ##############################################
    def hdd_model(HP_dec):
        el= extract_lists.Extract_Lists
        
        [model_list, capacity_list, vendor_list,
        fw_list, eco_list, product_fname_list,
        model_list_HP, capacity_list_HP, vendor_list_HP,
        fw_list_HP, eco_list_HP
        , product_fname_list_HP]=el.get_data()

        flag=0
        while flag==0:
            if HP_dec=='N':
                model_no= input('\nPlease enter a Valid HDD/SSD Model'\
                                ' No. : ')
                for i in range(len(model_list)):
                    if str(model_no)==model_list[i]:
                        cap_index=i

                        temp_model=model_list[cap_index]
                        temp_capacity=capacity_list[cap_index]
                        temp_fw=fw_list[cap_index]
                        temp_vendor=vendor_list[cap_index]
                        temp_eco=eco_list[cap_index]
                        temp_product_name=product_fname_list[cap_index]
                        flag=1
                        break
                        
                        if flag == 0:
                            print('\nInvalid Model No.'\
                            ', Please enter a HDD/SSD Valid Model'\
                            ' No.\n') 
                        else:
                            print('\nValid HDD/SSD Model No.\n')
                            
            elif HP_dec=='Y':
                model_no= input('\nPlease enter a Valid HDD/SSD Model'\
                                ' No. : ')
                for i in range(len(model_list_HP)):
                    if str(model_no)==model_list_HP[i]:
                        cap_index=i

                        temp_model=model_list_HP[cap_index]
                        temp_capacity=capacity_list_HP[cap_index]
                        temp_fw=fw_list_HP[cap_index]
                        temp_vendor=vendor_list_HP[cap_index]
                        temp_eco=eco_list_HP[cap_index]
                        temp_product_name=product_fname_list_HP[cap_index]
                        flag=1
                        break
                        
                        if flag == 0:
                            print('\nInvalid Model No.,'\
                            'Please enter a HDD/SSD Valid Model No.\n') 
                        else:
                            print('\nValid HDD/SSD Model No.\n')
        return [temp_model,
                    temp_capacity,
                    temp_fw,
                    temp_vendor,
                    temp_eco,
                    temp_product_name]

    
    ############################################
    #
    #   Prompts to enter Chassis number till it
    #   is from a pre-defined list.
    #
    ############################################
    def chassis_in(f1):
        fd = fixed_data.Fixed_Data
        chassis_list_d= fd.chassis_list_d  


        print(' --------------- ')
        print('| No. | Chassis |')
        print(' --------------- ')
        
        for keys,values in chassis_list_d.items():
            print('| ',keys,'|   ',values,'  |')
            print(' --------------- ')
            
        print('\n')

        while True:
            i1=input('\nPlease select a number for a Chassis'\
                    ' of File #' +str(f1+1)+ ' : ' )
            i1=int(i1)
            
            if i1 in chassis_list_d.keys():
                print('\nValid No.\n')
                break
            else:
                print('\nInvalid No.\n') 

        return i1


    ##########################################
    #
    #   Prompts to enter Controller number till 
    #   it is from a pre-defined list.
    #
    ########################################## 
    def cntrller_in(f1):
        fd = fixed_data.Fixed_Data
        cntrllr_list_d= fd.cntrllr_list_d

        print(' ------------------ ')
        print('| No. | Controller |')
        print(' ------------------ ')
        for keys,values in cntrllr_list_d.items():
            print('| ',keys,'|   ',values,'  |')
            print(' ----------------- ')
        print('\n')

        while True:
            i1=input('\nPlease select a number for a Controller'\
                     ' of File # ' +str(f1+1)+ ' : ' )
            i1=int(i1)
            
            if i1 in cntrllr_list_d.keys():
                print('\nValid No.\n')
                break
            else:
                print('\nInvalid No.\n') 
                
        return i1


    ##########################################
    #
    #   Prompts to enter Word Template Path 
    #   with fixed Path.
    #
    ########################################## 
    def word_in():
        word_file=input('\nPlease enter full path of Word Template: ')
        word_file=str(word_file).replace('"','')
        return word_file


        
#####################################
#              END                  #
#####################################