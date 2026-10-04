"""
EXERCISE 5.3: JSON Configuration Manager

OBJECTIVE:
Create a configuration management system using JSON files.

REQUIREMENTS:
1. Create these functions:
   - create_default_config(filename)
     Create a default configuration file with:
     - app_name, version
     - settings (theme, language, auto_save)
     - user_preferences (empty dict)
   
   - load_config(filename)
     Load configuration from JSON file
   
   - update_setting(filename, key, value)
     Update a specific setting in the config
   
   - get_setting(filename, key)
     Get a specific setting value
   
   - reset_config(filename)
     Reset to default configuration

2. Handle missing file errors
3. Pretty-print JSON (indented)

EXAMPLE USAGE:
create_default_config("config.json")
# Creates config with default values

update_setting("config.json", "theme", "dark")
update_setting("config.json", "language", "en")

theme = get_setting("config.json", "theme")
print(theme)  # "dark"

config = load_config("config.json")
print(config)

reset_config("config.json")
# Resets to defaults

BONUS:
Add validation - only allow valid theme values ("light", "dark", "auto")
and valid languages ("en", "es", "fr", "it").

GOOD LUCK! ⚙️
"""

# WRITE YOUR CODE BELOW:
