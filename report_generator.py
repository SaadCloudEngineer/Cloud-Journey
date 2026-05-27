# ================================
# Phase 1 Completion Report
# Engineer: Saad Khan Pathan
# ================================

import datetime
import os

# Report data
engineer = "Saad Khan Pathan"
university = "Parul University"
date = datetime.datetime.now()
goal = "Top 5% Cloud Engineer"

# Skills mastered
skills = {
    "Internet & Packets": "✅ Mastered",
    "IP Address & DNS":   "✅ Mastered",
    "HTTP & HTTPS":       "✅ Mastered",
    "Firewall & Router":  "✅ Mastered",
    "Linux Terminal":     "✅ Mastered",
    "Linux Permissions":  "✅ Mastered",
    "Python Scripting":   "✅ Mastered"
}

# Labs completed
labs = {
    "Lab 1 Internet":     "✅ Complete",
    "Lab 2 DNS":          "✅ Complete",
    "Lab 3 HTTP/HTTPS":   "✅ Complete",
    "Lab 4 Firewall":     "✅ Complete",
    "Lab 5 Linux":        "✅ Complete",
    "Lab 6 Permissions":  "✅ Complete",
    "Lab 7 Python":       "✅ Complete"
}

# Generate report
print("=" * 50)
print("   PHASE 1 COMPLETION REPORT")
print("=" * 50)
print("Engineer   : " + engineer)
print("University : " + university)
print("Date       : " +
      date.strftime("%d %B %Y"))
print("Goal       : " + goal)
print("=" * 50)

print("\n📚 SKILLS MASTERED:")
print("-" * 50)
for skill, status in skills.items():
    print(status + " " + skill)

print("\n🔬 LABS COMPLETED:")
print("-" * 50)
for lab, status in labs.items():
    print(status + " " + lab)

total = len(skills)
mastered = sum(1 for s in skills.values()
               if "Mastered" in s)

print("\n📊 FINAL SCORE:")
print("-" * 50)
print("Skills  : " + str(mastered) +
      "/" + str(total))
print("Labs    : 7/7")
print("GitHub  : ✅ Active")
print("Streak  : 4 days 🔥")
print("")

if mastered == total:
    print("🏆 PHASE 1 = 100% COMPLETE!")
    print("☁️  READY FOR PHASE 2 AWS!")
    print("🚀 TOP 5% JOURNEY ACTIVE!")

# Save report to file
with open("phase1_report.txt", "w") as f:
    f.write("Phase 1 Report\n")
    f.write("Engineer: " + engineer + "\n")
    f.write("Date: " +
            date.strftime("%d %B %Y") + "\n")
    f.write("Score: 7/7 Complete\n")
    f.write("Status: Ready for Phase 2\n")

print("\n✅ Report saved to phase1_report.txt")
print("=" * 50)