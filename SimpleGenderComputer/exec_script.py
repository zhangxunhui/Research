from simpleGenderComputer import SimpleGenderComputer
import os, warnings, sys, MySQLdb, logging

reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


gc = SimpleGenderComputer('nameLists')


def create_table(cur, tableName):
    # whether the table exists
    try:
        cur.execute("select max(id) from {}".format(tableName))
        cur.fetchone()
        exists = True
    except Exception as e:
        exists = False
    if exists == False:
        sql = "CREATE TABLE `" + tableName + "` (" \
                  "`id` int(11) NOT NULL AUTO_INCREMENT, " \
                  "`user_id` int(11) NOT NULL, " \
                  "`gender` varchar(255) DEFAULT NULL, " \
                  "PRIMARY KEY (`id`), " \
                  "KEY `user_id` (`user_id`) USING BTREE" \
              ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        cur.execute(sql)

# execute a list of names
db = MySQLdb.connect(host='localhost',
                user='root',
                passwd='111111',
                db='ght_msr_2014',

                local_infile=1,
                use_unicode=True,
                charset='utf8mb4',

                autocommit=False)
cur = db.cursor()

# create user_genders table
create_table(cur, "gender_SimpleGenderComputer")

# read users table from ghtorrent
cur.execute("select max(user_id) from gender_SimpleGenderComputer")
max_user_id = cur.fetchone()
if max_user_id[0] is None:
    max_user_id = 0
else:
    max_user_id = max_user_id[0]
print max_user_id
cur.execute("select id, name, location "
            "from users "
            "where id > %s", (max_user_id,))
users = cur.fetchall()
for user in users:
    id = user[0]
    name = user[1]
    if name is None or len(name.strip()) == 0:
        gender = None
        cur.execute("insert into gender_SimpleGenderComputer (user_id, gender) values (%s, %s)", (id, None))
    else:
        firstName = name.split(' ')[0].decode('utf-8', 'ignore')
        location = user[2]
        try:
            gender = gc.simpleLookup(firstName)
            cur.execute("insert into gender_SimpleGenderComputer (user_id, gender) values (%s, %s)", (id, gender))
        except Exception as e:
            # there are some special characters that cannot be regarded
            cur.execute("insert into gender_SimpleGenderComputer (user_id, gender) values (%s, %s)", (id, None))
    logging.info("user %d: %s; %s - %s" % (id, name, location, gender))
    if id % 10000 == 0:
        db.commit()
db.commit()
