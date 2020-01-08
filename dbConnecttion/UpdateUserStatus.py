from MySqlConn import Mysql

mysql = Mysql()
sql_up = "update market.market_user set status = 0 where telephone = 18626330613"
mysql.update(sql_up, param=None)

mysql.dispose()
