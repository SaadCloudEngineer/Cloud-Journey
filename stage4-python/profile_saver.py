def save_profile(name, city, goal):
  with open("profile.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"City: {city}\n")
    f.write(f"Goal: {goal}\n")
  print("✅ Profile saved!")

def read_profile():
  with open("profile.txt", "r") as f:
    print(f.read())


save_profile("Saad", "Dubai", "Cloud Engineer")
print("--- Reading profile ---")
read_profile()


