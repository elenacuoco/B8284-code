"""
EXERCISE 5.3: JSON Configuration Manager - SOLUTION
"""

import json
import datetime

DEFAULT_CONFIG = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "settings": {
        "theme": "light",
        "language": "en",
        "auto_save": True,
        "save_interval": 300
    },
    "user_preferences": {},
    "created_at": None,
    "last_modified": None
}

# BONUS: Validation
VALID_THEMES = ["light", "dark", "auto"]
VALID_LANGUAGES = ["en", "es", "fr", "it"]


def create_default_config(filename):
    """Create a new configuration file with default values."""
    try:
        config = DEFAULT_CONFIG.copy()
        config["created_at"] = datetime.datetime.now().isoformat()
        config["last_modified"] = datetime.datetime.now().isoformat()
        
        with open(filename, "w") as file:
            json.dump(config, file, indent=2)
        
        print(f"✓ Created default config: {filename}")
        return True
    except Exception as e:
        print(f"Error creating config: {e}")
        return False


def load_config(filename):
    """Load configuration from JSON file."""
    try:
        with open(filename, "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Config file '{filename}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in '{filename}'")
        return None
    except Exception as e:
        print(f"Error loading config: {e}")
        return None


def save_config(filename, config):
    """Save configuration to JSON file."""
    try:
        config["last_modified"] = datetime.datetime.now().isoformat()
        with open(filename, "w") as file:
            json.dump(config, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False


def update_setting(filename, key, value):
    """Update a specific setting in the configuration."""
    config = load_config(filename)
    if config is None:
        return False
    
    # Navigate nested settings
    if key in config["settings"]:
        # BONUS: Validate theme and language
        if key == "theme" and value not in VALID_THEMES:
            print(f"Invalid theme. Valid options: {VALID_THEMES}")
            return False
        if key == "language" and value not in VALID_LANGUAGES:
            print(f"Invalid language. Valid options: {VALID_LANGUAGES}")
            return False
        
        config["settings"][key] = value
        if save_config(filename, config):
            print(f"✓ Updated {key} = {value}")
            return True
    else:
        print(f"Setting '{key}' not found")
    
    return False


def get_setting(filename, key):
    """Get a specific setting value."""
    config = load_config(filename)
    if config is None:
        return None
    
    if key in config["settings"]:
        return config["settings"][key]
    else:
        print(f"Setting '{key}' not found")
        return None


def reset_config(filename):
    """Reset configuration to default values."""
    try:
        create_default_config(filename)
        print(f"✓ Reset config to defaults")
        return True
    except Exception as e:
        print(f"Error resetting config: {e}")
        return False


def display_config(config):
    """Display configuration in a readable format."""
    if config is None:
        return
    
    print("\n=== Configuration ===")
    print(f"App: {config['app_name']} v{config['version']}")
    print("\nSettings:")
    for key, value in config["settings"].items():
        print(f"  {key}: {value}")
    print(f"\nCreated: {config.get('created_at', 'N/A')}")
    print(f"Last modified: {config.get('last_modified', 'N/A')}")


# Test the configuration manager
print("=== Configuration Manager ===\n")

config_file = "app_config.json"

# Create default configuration
print("1. Creating default configuration...")
create_default_config(config_file)

# Load and display
config = load_config(config_file)
display_config(config)

# Update settings
print("\n2. Updating settings...")
update_setting(config_file, "theme", "dark")
update_setting(config_file, "language", "es")
update_setting(config_file, "auto_save", False)

# Display updated config
config = load_config(config_file)
display_config(config)

# Get specific setting
print("\n3. Getting specific settings...")
theme = get_setting(config_file, "theme")
print(f"Current theme: {theme}")

language = get_setting(config_file, "language")
print(f"Current language: {language}")

# BONUS: Test validation
print("\n4. Testing validation (BONUS)...")
update_setting(config_file, "theme", "invalid")  # Should fail
update_setting(config_file, "language", "xx")    # Should fail
update_setting(config_file, "theme", "auto")     # Should succeed

# Reset to defaults
print("\n5. Resetting to defaults...")
reset_config(config_file)

config = load_config(config_file)
display_config(config)
