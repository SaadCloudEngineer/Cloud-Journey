def launch_server(name, type):
  print(f" Launching {name}")
  print(f"   Type: {type}")
  print(f"   Status: Running ✅")
  print("---")

def check_health(server):
  print(f" Checking {server}")
  print(f"   Health: Good ✅")
  print("------")


#launch server

launch_server("WebServer", "t2.micro")
launch_server("Database", "t2.small")


# Check health
check_health("WebServer")
check_health("Database")

