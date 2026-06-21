import datetime

def monitor_servers():
  servers = ["WebServer", "Database", "Backup", "Cache"]
  now = datetime.datetime.now()

  print("=== Server Monitor ===")
  print(f"Time: {now.strftime('%H:%M:%S')}")
  print("---")

  for server in servers:
    cpu = 45  # pretend value
    if cpu < 80:
      status = " Healthy"
    else:
      status = " Warning"
    print(f"{server}: {status} (CPU: {cpu}%)")

  print("=== Complete ===")

# run monitor
monitor_servers()

