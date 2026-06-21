import os
import datetime

def create_backup():
  now = datetime.datetime.now()
  date_str = now.strftime("%Y%m%d")

  folder = f"backup_{date_str}"
  os.makedirs(folder, exist_ok=True)

  with open(f"{folder}/info.txt", "w") as f:
    f.write(f"Backup created: {now}\n")
    f.write("Status: Success\n")

    print(f"✅ Backup created: {folder}")

create_backup()
