import MySQLdb
from Random import randint 

db = MySQLdb.connect(
    host="localhost",
    user="denis",
    passwd="denis",
    db="wad_db_lab_5",
)

c=db.cursor()
fill_disk_query = "INSERT INTO disks (title, format, size) VALUES (%s, %s, %s);"
disk_vals = [
  # ('Трансформеры', '.mp4', 2059),
  ('Тихоокеанский рубеж', 'mp4', 2341),
  ('Тихоокеанский рубеж 2', 'mp4', 4341),
  ('Лесная братва', 'mp4', 421),
  ('Морская братва', 'mp4', 445),
  ('В поисках Немо', 'mp4', 512),
  ('Саундтек к фильму В поисках Немо', 'wav', 12),
  ('Scooter - Devils symphony', 'mp3', 7),
  ('Tenebrax album', 'mp3', 69),
]
def fulfillDisks():
  for disk in disk_vals:
    c.execute(fill_disk_query, disk)

fill_lib_query = "INSERT INTO libraries (title, owner, fk_storedDisks) VALUES (%s, %s, %s);"
lib_vals = [
]
def fulfillLibs(num):
  indexes = c.execute("select id from disks")
  for iter in range(num):
    rand = randint(0, len(indexes))
    c.execute(fill_lib_query, (...rand))

db.commit()
c.close()
db.close()