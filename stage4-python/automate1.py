import os 

folders = ["Servers","logs",'Backup','configs']

for folder in folders:
  os.makedirs(folder, exist_ok=True)
  print(f" Created : {folder}")

print("All Folder Created ")