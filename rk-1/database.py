from models import CD_disk, CD_disk_lib, Disk_lib__disk__matching_table

libs = [
  CD_disk_lib(1, 'Сборник фильмов Леши Иванова'),
  CD_disk_lib(2, 'ISO-образы ОС и программ сисадмина ООО "Храню диски"'),
  CD_disk_lib(3, 'Архив репортажей ВГТРК 2q2005'),
  CD_disk_lib(11, 'Игры Ubisoft'),
  CD_disk_lib(22, 'Архив музея CD-дисков и доисторических устройств хранения данных'),
  CD_disk_lib(33, 'Список дисков, уничтоженных дисководом моего ноутбука'),
]
 
disks = [
  CD_disk(1, 'FarCry 6 (2021)', 'iso', 700, 11),
  CD_disk(2, 'Запись концерта "Владимир Путин молодец"', 'mp4', 350, 3),
  CD_disk(3, 'Терминатор 4: Да придёт спаситель (2009)', 'mp4', 450, 1),
  CD_disk(4, 'Терминатор: Тёмные судьбы мексиканца (2019)', 'mp4', 656, 1),
  CD_disk(11, 'Терминатор (1984)', 'mp4', 656, 22),
  CD_disk(10, 'Бабушка легкого поведения 2 (2021)', 'mp4', 620, 1),
  CD_disk(5, 'Assassin\'s Creed 3 (2008)', 'iso', 650, 11),
  CD_disk(6, 'Урок химии. Сера (1978)', 'mp4', 50, 22),
  CD_disk(7, 'Windows 98', 'iso', 450, 2),
  CD_disk(8, 'Arch Linux', 'iso', 325, 2),
  CD_disk(9, 'GTA San Andreas', 'iso', 125, 2),
]
 
libs__disks__matching_table = [
  Disk_lib__disk__matching_table(1, 3),
  Disk_lib__disk__matching_table(1, 4),
  Disk_lib__disk__matching_table(1, 10),

  Disk_lib__disk__matching_table(2, 1),
  Disk_lib__disk__matching_table(2, 5),
  Disk_lib__disk__matching_table(2, 7),
  Disk_lib__disk__matching_table(2, 8),
  Disk_lib__disk__matching_table(2, 9),

  Disk_lib__disk__matching_table(3, 2),

  Disk_lib__disk__matching_table(11, 1),
  Disk_lib__disk__matching_table(11, 5),

  Disk_lib__disk__matching_table(22, 11),
  Disk_lib__disk__matching_table(22, 6),
  Disk_lib__disk__matching_table(22, 3),
  Disk_lib__disk__matching_table(22, 7),
  Disk_lib__disk__matching_table(22, 9),

  # no disks in 33
]