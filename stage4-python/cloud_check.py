print("=== Cloud Server Health Check ===")

servers = ["Webserver","DataBase","Backup"]

for server in servers:
   cpu = 45 
   if cpu <80:
    print(f"{server}:  Healthy (CPU {cpu}%)")
   else:
     print(f"{server}:  High load!")

     
print("=== Check Complete ===")

