# ================================
# Cloud Engineer Daily Tracker
# Engineer : Saad Khan Pathan
# Goal     : Top 5% Cloud Engineer
# ================================

# Personal Info
name = "Saad"
goal = "Top 5% Cloud Engineer"
university = "Parul University"
days_studied = 1

# Skills tracker
skills_learned = [
    "Internet & Packets",
    "IP Address & DNS",
    "HTTP & HTTPS",
    "Firewall & Router",
    "Linux Terminal",
    "Linux Permissions",
    "Python Scripting"
]

# Print header
print("=" * 40)
print("   CLOUD ENGINEER TRACKER")
print("=" * 40)
print("Name     : " + name)
print("Goal     : " + goal)
print("Days     : " + str(days_studied))
print("=" * 40)

# Print skills
print("\n✅ SKILLS MASTERED:")
for i, skill in enumerate(skills_learned):
    print(str(i+1) + ". " + skill)

# Progress check
total_skills = 7
mastered = len(skills_learned)

print("\n📊 PROGRESS:")
print("Mastered : " + str(mastered) +
      "/" + str(total_skills))

if mastered == total_skills:
    print("🔥 Phase 1 Complete!")
    print("☁️  Ready for AWS!")
else:
    remaining = total_skills - mastered
    print("📚 Remaining: " +
          str(remaining) + " skills")

print("=" * 40)
print("💪 Keep Going " + name + "!")
print("Top 5% is waiting for you!")
print("=" * 40)