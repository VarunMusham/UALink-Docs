import os
import sys
import re

def process_file(md_path):
    if not os.path.exists(md_path):
        print(f"File not found: {md_path}")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match image tags: ![](filename.ext)
    pattern = re.compile(r'(!\[[^\]]*\]\(([^)]+\.(?:jpeg|png|jpg))\))')
    
    new_content = ""
    last_idx = 0
    
    for match in pattern.finditer(content):
        img_tag = match.group(1)
        img_filename = match.group(2)
        # Construct the expected JSON filename
        json_filename = img_filename.rsplit('.', 1)[0] + '.json'
        expected_link = f"[JSON Extraction]({json_filename})"
        
        start, end = match.span()
        # Append everything from the end of the last match to the end of the current match
        new_content += content[last_idx:end]
        
        # Look ahead up to 100 characters to see if the JSON link is already present
        lookahead = content[end:end+100]
        if expected_link not in lookahead:
            new_content += f"\n\n{expected_link}"
            
        last_idx = end
        
    new_content += content[last_idx:]
    
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {md_path}")
    else:
        print(f"No changes needed for: {md_path}")

def main():
    # If arguments are passed, process those specific files or directories
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.isfile(arg) and arg.endswith('.md'):
                process_file(arg)
            elif os.path.isdir(arg):
                for root, _, files in os.walk(arg):
                    for file in files:
                        if file.endswith('.md'):
                            process_file(os.path.join(root, file))
            else:
                print(f"Invalid path or not a markdown file: {arg}")
    else:
        # If no arguments are passed, process the current directory recursively
        print("Scanning current directory for markdown files...")
        for root, _, files in os.walk('.'):
            for file in files:
                if file.endswith('.md'):
                    process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
