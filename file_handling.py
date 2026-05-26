# ================================
# Python File Handling
# Cloud Engineer: Saad
# ================================

# Writing to a file
print("--- Writing to file ---")

file = open("cloud_notes.txt", "w")
file.write("Cloud Computing Notes\n")
file.write("====================\n")
file.write("1. Internet = Global network\n")
file.write("2. IP = Unique address\n")
file.write("3. DNS = Phonebook\n")
file.write("4. HTTP = Unsecured\n")
file.write("5. HTTPS = Secured\n")
file.close()

print("✅ File written successfully!")

# Reading from file
print("\n--- Reading from file ---")

file = open("cloud_notes.txt", "r")
content = file.read()
file.close()

print(content)


# Appending to existing file
print("--- Appending to file ---")

file = open("cloud_notes.txt", "a")
file.write("6. Firewall = Security guard\n")
file.write("7. Router = Traffic director\n")
file.write("8. Linux = Cloud OS\n")
file.close()

print("✅ Content appended!")

# Read updated file
file = open("cloud_notes.txt", "r")
content = file.read()
file.close()

print("\n--- Updated file content ---")
print(content)

# Best practice file handling
print("--- Safe file handling ---")

# Writing safely
with open("safe_notes.txt", "w") as f:
    f.write("This is safer way!\n")
    f.write("File closes automatically!\n")

# Reading safely
with open("safe_notes.txt", "r") as f:
    content = f.read()
    print(content)

print("✅ File handled safely!")