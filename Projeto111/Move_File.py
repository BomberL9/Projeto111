import os
import shutil

from_dir = 'C:/Users/leona/Downloads'
to_dir = 'C:/Users/leona/Documents/Arquivos_Documentos'

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
  i = os.path.splitext(i)