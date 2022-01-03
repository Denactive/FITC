from itertools import islice
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import glob
import MySQLdb
from random import randint, shuffle, seed, choice
from faker.providers.person.en import Provider

fill_disk_query = "INSERT INTO disks (title, format, size) VALUES (%s, %s, %s);"
formats_list = ['mp3', 'mp4', 'wav', 'ogg', 'mov']
fill_lib_query = "INSERT INTO libraries (title, owner) VALUES (%s, %s);"
fill_fk_query = "INSERT INTO libraries_fk_storeddisks (library_id, disk_id) VALUES (%s, %s);"

class Command(BaseCommand):
  help = "filling db with random data"

  def add_arguments(self, parcer):
    parcer.add_argument("-d", "--disks", type=int)
    parcer.add_argument("-l", "--libs", type=int)
    parcer.add_argument("-all", "--all", type=int)
      

  def handle(self, *args, **options):
    disks_amount = options["disks"]
    libs_amount = options["libs"]
    total_amount = options["all"]

    if total_amount:
      self.fill_disks(total_amount * 5)
      self.fill_libs(total_amount)
    if disks_amount:
      self.fill_disks(disks_amount)
    if libs_amount:
      self.fill_libs(libs_amount)

  def fill_libs(self, n):
    db = MySQLdb.connect(
      host="localhost",
      user="denis",
      passwd="denis",
      db="wad_db_lab_5",
    )
    c=db.cursor()
    c.execute("select id from disks")
    disks_indexes = c.fetchall()
    print(c)
    for i in range(n):
      title=Faker().sentence()[:20]
      owner = Faker().user_name()
      c.execute(fill_lib_query, (title, owner))
      c.execute('select id from libraries where title=%s and owner=%s', (title, owner))
      lib_id = c.fetchone()
      # many-to-many filling
      for j in range(3):
        try:
          disk_id = choice(disks_indexes)
          c.execute(fill_fk_query, (lib_id, disk_id))
        except MySQLdb.DatabaseError as err:       
          print("Error: ", err)

    db.commit()
    c.close()
    db.close()

  def fill_disks(self, n):
    db = MySQLdb.connect(
      host="localhost",
      user="denis",
      passwd="denis",
      db="wad_db_lab_5",
    )
    c=db.cursor()
    for i in range(n):
      title=Faker().sentence()[:20]
      format = choice(formats_list)
      size = Faker().random.randint(0,10000)
      c.execute(fill_disk_query, (title, format, size))
    db.commit()
    c.close()
    db.close()


    