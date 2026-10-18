# Smart File Organizer & Reporter 🚀

A lightweight, automated Python backend script designed to clean up cluttered directories (like Downloads or Desktop) by sorting files into dedicated folders based on their extensions. It also generates an execution log report for tracking.

## Features ✨
- **Automated Sorting:** Categorizes Documents, Images, Audio/Video, and Archives instantly.
- **Automated Reporting:** Generates an English execution report (`folder_organizer_report.txt`) showing exactly what was moved.
- **Safe Execution:** Automatically skips critical system and development files (like `main.py`).

## Tech Stack 🛠️
- **Language:** Python 3
- **Core Modules:** `os`, `shutil`, `datetime`
- 
## How to Use 🚀
1. Run the `main.py` script.
2. Enter the full path of the folder you want to clean up (e.g., `C:\Users\Username\Downloads`).
3. Press **Enter** without typing anything to organize the current directory where the script is located.
