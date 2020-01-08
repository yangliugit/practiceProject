from MySqlConn import Mysql

# mysql = Mysql()
# sqlAll = "select * from t_perform_test"
# result = mysql.getAll(sqlAll)
# if result:
#     print "get all"
#     for row in result:
#         print "%s\t%s" %(row["name"], row["password"])
#
# mysql.dispose()

mysql = Mysql()
sql_in = "insert into test.t_perform_test values(%s, %s)"
for i in range(1, 1000):
    params = ["liuyang"+str(i), "password"+str(i)]
    num = mysql.insertOne(sql_in, params)
    print num

mysql.dispose()
