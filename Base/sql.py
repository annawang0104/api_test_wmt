"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""

"""
-*- coding: utf-8 -*-

Author: wangmengting


"""

import pymysql

db = pymysql.connect(host="10.80.82.13", user="vms_developer", passwd="WDSFREWFD2@VDVdc2d", database="t2", port=3306,
                     charset="utf8")
cursor = db.cursor()

user_id_sql = "select u.id from `tbl_pro_user` pu ,tbl_user u where pu.uid = u.uid and pu.dept_id = 78 " \
    # "or " \
# "pu.dept_id = 76 or pu.dept_id = 77 or pu.dept_id = 78 or pu.dept_id = 79" \
# " or pu.dept_id = 81 or pu.dept_id = 86 or pu.dept_id = 141)"


cursor.execute(user_id_sql)
records = cursor.fetchall()


def upload_num_sql():
    count_num = 0

    if records:
        for i in records:
            upload_num_count_sql = "select id from `material_core_attr` where  draft =1 and status = 0 and meta_data_type = 0 " \
                                   "and ((create_user = " + str(
                i[0]) + " and create_time between '2020-04-01' and '2020-06-02') " \
                        "or (check_user_id = " + str(i[0]) + " and check_update_time " \
                                                             "between '2020-04-01' and '2020-06-02'))"

            #
            # print(upload_num_count_sql)

            cursor.execute(upload_num_count_sql)
            sql_record = cursor.fetchall()
            count_num = count_num + sql_record[0][0]
            print(sql_record[0][0])
            # if sql_record:
            #     for n in sql_record:
            #         print(n[0])


def update_sql():
    list = []

    if records:

        for i in records:
            upload_id_sql = "select id from `material_core_attr` where  draft =1 and status = 0 and meta_data_type = 0 " \
                            "and ((create_user = " + str(
                i[0]) + " and create_time between '2020-04-01' and '2020-06-02') " \
                        "or (check_user_id = " + str(i[0]) + " and check_update_time " \
                                                             "between '2020-04-01' and '2020-06-02'))"

            cursor.execute(upload_id_sql)
            sql_record = cursor.fetchall()
            if sql_record:
                for n in sql_record:
                    list.append(n[0])

    id_list = str(list).split("[")

    list2 = str(id_list[1]).split("]")
    # print(str(list2))

    if list:
        ref_sql = "select count(distinct id),ref_value ,ref_id from material_map where type = 4 " \
                  "and status =0 and origin_id in (" + list2[0] + " ) group by ref_value"
        cursor.execute(ref_sql)
        sql_record = cursor.fetchall()
        print(sql_record)


def get():
    sql = "select version from `workflow_core_attr`  where id = 397"
    cursor.execute(sql)
    mun = cursor.fetchall()
    print(mun[0][0]
          )




def getDataFromMysql():
    # 创建数据库连接对象
    db = pymysql.connect(host="rm-2ze31xr3ozr0q298q.mysql.rds.aliyuncs.com", user="vms_developer", passwd="WDSFREWFD2@VDVdc2d", database="t7", port=3306,
                     charset="utf8")
    cursor = db.cursor()
    sql = "select * from tbl_user where email='wangmengting@3202.com' and status =0"
    cursor.execute(sql)
    records = cursor.fetchall()
    #获取当前项目版本号
    sql_version_id = records[0][0]
    print(sql_version_id)


if __name__ == '__main__':
    getDataFromMysql()




