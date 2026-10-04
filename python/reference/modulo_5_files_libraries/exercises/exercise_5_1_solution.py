"""
EXERCISE 5.1: File Logger - SOLUTION
"""

import datetime

def log_message(filename, level, message):
    """
    Write a log message to file with timestamp.
    
    Args:
        filename: Path to log file
        level: Log level (INFO, WARNING, ERROR)
        message: Log message text
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} [{level}] {message}\n"
        
        with open(filename, "a") as file:
            file.write(log_entry)
        
        print(f"✓ Logged: {log_entry.strip()}")
    except Exception as e:
        print(f"Error writing log: {e}")

def read_logs(filename):
    """Read and display all log entries."""
    try:
        print(f"\n=== Log File: {filename} ===")
        with open(filename, "r") as file:
            logs = file.read()
            if logs:
                print(logs)
            else:
                print("  (empty)")
    except FileNotFoundError:
        print(f"Log file '{filename}' not found")
    except Exception as e:
        print(f"Error reading log: {e}")

def count_by_level(filename):
    """Count log entries by level."""
    try:
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        
        with open(filename, "r") as file:
            for line in file:
                for level in counts.keys():
                    if f"[{level}]" in line:
                        counts[level] += 1
                        break
        
        return counts
    except FileNotFoundError:
        print(f"Log file '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error counting logs: {e}")
        return None

def filter_logs(filename, level):
    """BONUS: Return only logs of a specific level."""
    try:
        filtered = []
        with open(filename, "r") as file:
            for line in file:
                if f"[{level}]" in line:
                    filtered.append(line.strip())
        return filtered
    except FileNotFoundError:
        print(f"Log file '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error filtering logs: {e}")
        return []


# Test the logger
print("=== File Logger System ===\n")

log_filename = "app.log"

# Clear old logs (for testing)
with open(log_filename, "w") as file:
    file.write("")

# Log some messages
log_message(log_filename, "INFO", "Application started")
log_message(log_filename, "INFO", "User login successful")
log_message(log_filename, "WARNING", "High memory usage detected")
log_message(log_filename, "ERROR", "Database connection failed")
log_message(log_filename, "INFO", "Retrying connection")
log_message(log_filename, "INFO", "Connection successful")

# Read all logs
read_logs(log_filename)

# Count by level
print("\n=== Log Statistics ===")
stats = count_by_level(log_filename)
if stats:
    for level, count in stats.items():
        print(f"{level}: {count}")

# BONUS: Filter logs
print("\n=== ERROR Logs Only ===")
errors = filter_logs(log_filename, "ERROR")
for error in errors:
    print(error)

print("\n=== WARNING Logs Only ===")
warnings = filter_logs(log_filename, "WARNING")
for warning in warnings:
    print(warning)
