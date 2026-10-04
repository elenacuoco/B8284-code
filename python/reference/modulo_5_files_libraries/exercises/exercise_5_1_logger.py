"""
EXERCISE 5.1: File Logger

OBJECTIVE:
Create a logging system that writes messages to a file with timestamps.

REQUIREMENTS:
1. Create these functions:
   - log_message(filename, level, message)
     Levels: "INFO", "WARNING", "ERROR"
     Format: "2024-01-15 10:30:15 [INFO] Application started"
   
   - read_logs(filename)
     Read and display all log entries
   
   - count_by_level(filename)
     Count how many of each log level

2. Use datetime for timestamps
3. Append to file (don't overwrite)
4. Handle file errors

EXAMPLE USAGE:
log_message("app.log", "INFO", "Application started")
log_message("app.log", "WARNING", "High memory usage")
log_message("app.log", "ERROR", "Database connection failed")

read_logs("app.log")
# Should display:
# 2024-01-15 10:30:15 [INFO] Application started
# 2024-01-15 10:30:16 [WARNING] High memory usage
# 2024-01-15 10:30:17 [ERROR] Database connection failed

stats = count_by_level("app.log")
print(stats)  # {"INFO": 1, "WARNING": 1, "ERROR": 1}

BONUS:
Add a filter_logs(filename, level) function that returns only logs of a specific level.

GOOD LUCK! 📝
"""

# WRITE YOUR CODE BELOW:
