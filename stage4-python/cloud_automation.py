import os
import datetime

def setup_cloud_project():
    now = datetime.datetime.now()
    
    print("=" * 40)
    print("   CLOUD PROJECT AUTOMATION")
    print("=" * 40)
    
    folders = ["aws", "scripts", "logs", "backups"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created: {folder}")
    
    with open("logs/setup.log", "w") as f:
        f.write(f"Setup: {now}\n")
        f.write("Engineer: Saad Khan\n")
        f.write("Status: Complete\n")
    
    print("Log created!")
    print("=" * 40)
    print("Cloud project ready!")
    print("Engineer: Saad Khan")
    print(f"Date: {now.strftime('%Y-%m-%d')}")
    print("=" * 40)

setup_cloud_project()