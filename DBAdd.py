from pymysql import IntegrityError, Error, connect
from pymysql.cursors import DictCursor
from json import loads
from sys import stderr


class DBAdd:
    def __init__(self):
        with open("config.json") as f:
            self.config = loads(bytes(f.read(), encoding='utf8'))
        self.sql = connect(host=self.config.get("rds"),
                           user=self.config.get("user"),
                           password=self.config.get("password"),
                           db=self.config.get("db"),
                           cursorclass=DictCursor)

    def add_bucket(self, bucket, product, company=None):
        status = False
        cursor = None
        try:
            cursor = self.sql.cursor()
            cursor.execute("""INSERT INTO monitor (bucket,company,product,checked) VALUES (%s,%s,%s,%s)""",
                           (bucket, company, product, 0))
            self.sql.commit()
            cursor.close()
            status = True
        except IntegrityError:
            print(">>>SQL encountered an IntegrityError while adding {} {} {}to the monitor table. Buckets must be "
                  "unique".format(bucket, company, product), file=stderr)
        except Error as e:
            print(">>>SQL encountered an Error while adding {} {} {} to the monitor table.".format(bucket, company,
                                                                                                   product),
                  file=stderr)
        finally:
            if cursor is not None:
                cursor.close()
            return status
