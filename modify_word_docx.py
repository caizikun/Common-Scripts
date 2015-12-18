####################################################
#                  Revision: 1.0                   #
#              Updated on: 11/06/2015              #
####################################################

####################################################
#                                                  #
#   This File Replaces KEYWORDS with User Inputs   #
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
import os
import zipfile


######################################
#
# Modifying contents of Word Template 
#
######################################
def Modify_Word_Docx(word_file,fixed_dir,part_no,replaceText
                    ,replaceText_f,test_name):

    ######################################
    #
    # Changing Body/Document of Word 
    # Template
    #
    ######################################
    templateDocx = zipfile.ZipFile(r''+str(word_file))
    newDocx = zipfile.ZipFile(r''+str(fixed_dir)
                              +'\\temp_doc.docx', "a")

    with open(templateDocx.extract("word/document.xml"
              , "C:/"),encoding="utf8") as tempXmlFile:
              
        tempXmlStr = tempXmlFile.read()

    for key in replaceText.keys():
        tempXmlStr = tempXmlStr.replace(str(key)
                                , str(replaceText.get(key)))

    with open("C:/temp.xml", "w+",encoding="utf8") as tempXmlFile:
                                            
        tempXmlFile.write(tempXmlStr)

    for file in templateDocx.filelist:
        if not file.filename == "word/document.xml":
            newDocx.writestr(file.filename
                            , templateDocx.read(file))

    newDocx.write("C:/temp.xml", "word/document.xml")
    templateDocx.close()
    newDocx.close()
    
    
    ######################################
    #
    # Changing Footer of Word Template
    # 
    ######################################
    templateDocx1 = zipfile.ZipFile(r''+str(fixed_dir)
                                    +'\\temp_doc.docx')
       
    newDocx1 = zipfile.ZipFile(r''+str(fixed_dir)+'\\'
                                +str(part_no)+str(test_name)
                                +'.docx',"a")
    
    newDocx1_list = templateDocx1.namelist()

    footers_index=[]
    for i in range(len(newDocx1_list)):
        if 'footer' in newDocx1_list[i]:
             footers_index.append(i)

    
    for j in range (len(footers_index)):            
        with open(templateDocx1.extract(
                    str(newDocx1_list[footers_index[j]])
                    , "C:/"),encoding="utf8") as footerXmlFile:
                    
                footerXmlStr = footerXmlFile.readlines()  

        f_str='FOOTER'
        for k in range(len(footerXmlStr)):
            if f_str in str(footerXmlStr[k]):

             footer_no=j
             break

    templateDocx2 = zipfile.ZipFile(r''+str(fixed_dir)
                                    +'\\temp_doc.docx')
   
    with open(templateDocx2.extract(
                str(newDocx1_list[footers_index[footer_no]])
                , "C:/"),encoding="utf8") as footerXmlFile2:
                
                            
        footerXmlStr2 = footerXmlFile2.read()

    for key in replaceText_f.keys():
        footerXmlStr2=footerXmlStr2.replace(str(key)
                        , str(replaceText_f.get(key)))

    with open("C:/temp1.xml", "w+",encoding="utf8") as footerXmlFile2:                     
           footerXmlFile2.write(footerXmlStr2)

    for file in templateDocx2.filelist:
        if not file.filename == str(newDocx1_list
                                [footers_index[footer_no]]):
                                
            newDocx1.writestr(file.filename, templateDocx2.read(
                                                            file))

    newDocx1.write("C:/temp1.xml", str(newDocx1_list
                                    [footers_index[footer_no]]))
    
    templateDocx2.close()
    newDocx1.close()

  
#####################################
#              END                  #
##################################### 