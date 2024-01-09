#------------------------------------------------------------------
# Author: ZhangYuehao
# Email: yuehaozhang@njtech.edu.cn
# Zhihu: https://www.zhihu.com/people/bu-meng-cheng-kong-46/posts
# GitHub: https://github.com/ZhangAilan
#-------------------------------------------------------------------
# Date: 2024/01/08
# Function:
#   excel to gdb
#-------------------------------------------------------------------
import arcpy

arcpy.env.workspace="D:\\GISProjects\\data\\2020旅游人次"
excel_file="2020年度全国旅行社组织接待国内旅游情况表.xlsx"
table_name="Tourist_arrivals_province_2020.dbf"
arcpy.ExcelToTable_conversion(excel_file,table_name,"Sheet1")

gdb_path="D:\\GISProjects\\ChineseTourism\\ChineseTourism.gdb"
arcpy.TableToGeodatabase_conversion(table_name,gdb_path)
print("Done!")