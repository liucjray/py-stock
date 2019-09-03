import pymysql

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='ray',
                             password='1234qwer',
                             db='stock',
                             charset='utf8')

# 获取游标
cursor = connection.cursor()

# 插入数据(元组或列表)
effect_row = cursor.execute('INSERT INTO `stock` (`name`, `code`) VALUES (%s, %s)', ('中鋼', '2002'))

connection.commit()

last = cursor.lastrowid

print(last)