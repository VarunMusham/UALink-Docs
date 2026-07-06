# How to Run Markdown Processing Scripts

This document provides instructions on how to use the scripts included in the `Markdown_Output` directory to process and update your markdown files.

## `add_json_links.py`

This standalone Python script automatically scans markdown files for image inclusions (e.g., `![](_page_4_Figure_2.jpeg)`) and appends a link to the corresponding JSON extraction file right below it. 

### Key Features:
- **Automatic Matching:** Looks for `.jpeg`, `.jpg`, and `.png` image inclusions and expects a similarly named `.json` file.
- **Idempotent:** Safe to run multiple times. It will detect if a JSON link has already been appended and skip duplicates.
- **Recursive Scanning:** Can scan the entire directory tree or target specific files.

### Usage Instructions

Open a command prompt or PowerShell window and navigate to the `Markdown_Output` directory:
```powershell
cd C:\Users\musha\Downloads\Brave\UALink-Full\UALink\Markdown_Output
```

**1. Process all markdown files in the current directory and all subdirectories:**
```powershell
python add_json_links.py
```

**2. Process a specific markdown file:**
```powershell
python add_json_links.py "10__UALink_Switch_Requirements/10__UALink_Switch_Requirements.md"
```

**3. Process a specific directory:**
```powershell
python add_json_links.py "10__UALink_Switch_Requirements"
```

**4. Process multiple specific files/directories at once:**
```powershell
python add_json_links.py "file1.md" "folder1" "file2.md"
```
