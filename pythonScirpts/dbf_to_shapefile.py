#------------------------------------------------------------------
# Author: ZhangYuehao
# Email: yuehaozhang@njtech.edu.cn
# Zhihu: https://www.zhihu.com/people/bu-meng-cheng-kong-46/posts
# GitHub: https://github.com/ZhangAilan
#-------------------------------------------------------------------
# Date: 2024/01/08
# Function:
#   add the dbf to the shapefile
#-------------------------------------------------------------------
import arcpy

# set the workspace
arcpy.env.workspace="D:\\GISProjects\\temp"

shapefile="省级.shp"
dbf="Tourist_arrivals_province_2020.dbf"

shapefile_join_filed="接待人"
dbf_join_filed="接待人"

arcpy.JoinField_management(shapefile,shapefile_join_filed,dbf,dbf_join_filed)
print("Done!")