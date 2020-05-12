import pymysql

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='888888',
                             db='guest_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        # sql = 'INSERT INTO sign_event (sign_event.name,sign_event.limit,sign_event.status,address,start_time,create_time)' \
        #       'VALUES("小米1发布会",1001,0,"高新区1",NOW(),NOW()),' \
        #       '("小米2发布会",1002,1,"高新区2",NOW(),NOW()),' \
        #       '("华为发布会",1003,1,"高新区3",NOW(),NOW());'
        # cursor.execute(sql)

        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time)VALUES ("alen",18800110001,"alen@mail.com",0,5,NOW());'
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()