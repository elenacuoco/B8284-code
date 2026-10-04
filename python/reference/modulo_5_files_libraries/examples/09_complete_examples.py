"""
Example 09: Complete File Processing Examples

Real-world examples combining file operations and data processing.
"""

import csv
import json
import datetime

print("=== Example 1: Log File Analyzer ===")

# Create a sample log file
logs = """2024-01-15 10:30:15 INFO: Application started
2024-01-15 10:30:20 INFO: User login successful
2024-01-15 10:31:00 WARNING: High memory usage detected
2024-01-15 10:32:15 ERROR: Database connection failed
2024-01-15 10:32:30 INFO: Retrying connection
2024-01-15 10:32:35 INFO: Connection successful"""

with open("app.log", "w") as file:
    file.write(logs)

# Analyze the log file
error_count = 0
warning_count = 0
info_count = 0

with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

print(f"Log analysis:")
print(f"  INFO: {info_count}")
print(f"  WARNING: {warning_count}")
print(f"  ERROR: {error_count}")
print()

print("=== Example 2: CSV to JSON Converter ===")

# Create sample CSV
csv_data = [
    ["id", "name", "email", "age"],
    ["1", "Alice", "alice@email.com", "25"],
    ["2", "Bob", "bob@email.com", "30"],
    ["3", "Charlie", "charlie@email.com", "28"]
]

with open("users.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Convert CSV to JSON
users = []
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append({
            "id": int(row["id"]),
            "name": row["name"],
            "email": row["email"],
            "age": int(row["age"])
        })

with open("users.json", "w") as file:
    json.dump(users, file, indent=2)

print("✓ Converted users.csv to users.json")
print(f"  {len(users)} users converted")
print()

print("=== Example 3: Grade Report Generator ===")

# Student grades
grades = [
    {"name": "Alice", "math": 95, "english": 88, "science": 92},
    {"name": "Bob", "math": 78, "english": 85, "science": 80},
    {"name": "Charlie", "math": 92, "english": 95, "science": 93},
    {"name": "Diana", "math": 88, "english": 90, "science": 87}
]

# Calculate averages and generate report
report_lines = ["Grade Report", "=" * 50, ""]

for student in grades:
    name = student["name"]
    subjects = {k: v for k, v in student.items() if k != "name"}
    average = sum(subjects.values()) / len(subjects)
    
    report_lines.append(f"Student: {name}")
    for subject, grade in subjects.items():
        report_lines.append(f"  {subject.capitalize()}: {grade}")
    report_lines.append(f"  Average: {average:.1f}")
    report_lines.append("")

# Write report
with open("grade_report.txt", "w") as file:
    file.write("\n".join(report_lines))

print("✓ Generated grade_report.txt")
print("Preview:")
print(report_lines[0])
print(report_lines[1])
for line in report_lines[3:7]:
    print(line)
print()

print("=== Example 4: Configuration Manager ===")

# Default configuration
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "language": "en",
        "notifications": True,
        "auto_save": True,
        "save_interval": 300
    },
    "last_updated": datetime.datetime.now().isoformat()
}

# Save configuration
with open("config.json", "w") as file:
    json.dump(config, file, indent=2)

print("✓ Created config.json")

# Load and modify configuration
with open("config.json", "r") as file:
    loaded_config = json.load(file)

loaded_config["settings"]["theme"] = "light"
loaded_config["last_updated"] = datetime.datetime.now().isoformat()

# Save updated configuration
with open("config.json", "w") as file:
    json.dump(loaded_config, file, indent=2)

print("✓ Updated config.json")
print(f"  App: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"  Theme: {loaded_config['settings']['theme']}")
print()

print("=== Example 5: Data Backup System ===")

# Create some data files
data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ],
    "timestamp": datetime.datetime.now().isoformat()
}

# Save with timestamp in filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"backup_{timestamp}.json"

with open(backup_filename, "w") as file:
    json.dump(data, file, indent=2)

print(f"✓ Created backup: {backup_filename}")
print(f"  Users backed up: {len(data['users'])}")
