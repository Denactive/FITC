class CD_disk:
    """CD-диск"""
    def __init__(self, id, title, data_format, data_size_mb, lib_id):
        self.id = id
        self.title = title
        self.data_format = data_format
        self.data_size_mb = data_size_mb
        
        self.lib_id = lib_id

    def __repr__(self):
      return f"CD-диск {self.title}"
 

class CD_disk_lib:
    """Библиотека CD-дисков"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
      return "Библиотека CD-дисков"
 

class Disk_lib__disk__matching_table:
    """
    'CD-диски в Библиотеке CD-дисков отдела' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lib_id, disk_id):
        self.disk_id = disk_id
        self.lib_id = lib_id