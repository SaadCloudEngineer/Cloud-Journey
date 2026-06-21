with open("cloud_log.txt", "w") as f:
  f.write("Cloud Journey Log\n")
  f.write("================\n")
  f.write("Day 1: Learned Python\n")
  f.write("Day 2: Learned functions\n")

print("✅ File written!")



with open("cloud_log.txt", "r") as f:
  content = f.read()
  print(content)