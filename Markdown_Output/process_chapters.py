import os
import json
import glob
import google.generativeai as genai
from PIL import Image

def process_chapter(chapter_dir, prompt_text):
    print(f"Processing chapter: {chapter_dir}")
    md_files = glob.glob(os.path.join(chapter_dir, "*.md"))
    if not md_files:
        print("No markdown file found.")
        return
    md_file = md_files[0]
    
    image_files = glob.glob(os.path.join(chapter_dir, "*.jpeg"))
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    for img_path in image_files:
        img_name = os.path.basename(img_path)
        json_path = os.path.join(chapter_dir, img_name.replace('.jpeg', '.json'))
        
        if os.path.exists(json_path):
            print(f"Skipping {img_name}, JSON already exists.")
            continue
            
        print(f"Analyzing {img_name}...")
        img = Image.open(img_path)
        
        try:
            response = model.generate_content([prompt_text, img])
            response_text = response.text
            
            # Extract JSON block if it's wrapped in markdown
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                json_str = response_text.split("```")[1].strip()
            else:
                json_str = response_text.strip()
                
            # Parse to ensure it's valid JSON
            data = json.loads(json_str)
            
            with open(json_path, 'w', encoding='utf-8') as jf:
                json.dump(data, jf, indent=2)
                
            # Update MD content
            img_markdown = f"![]({img_name})"
            replacement = f"{img_markdown}\n\n[JSON Extraction]({os.path.basename(json_path)})"
            md_content = md_content.replace(img_markdown, replacement)
            
        except Exception as e:
            print(f"Error processing {img_name}: {e}")
            
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Finished processing {chapter_dir}")

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        return
        
    genai.configure(api_key=api_key)
    
    base_dir = r"C:\Users\musha\Downloads\Brave\UALink-Full\UALink\Markdown_Output"
    prompt_file = os.path.join(base_dir, "prompt")
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_text = f.read()
        
    chapters = [
        "2_UPLI_Interface_Definition_and_Operation_Rules",
        "3_Reliability_Availability_and_Serviceability_RAS",
        "4_UPLI_Interface_Reset_Signaling_and_Connection",
        "5_Transaction_Layer_TL"
    ]
    
    for chapter in chapters:
        chapter_dir = os.path.join(base_dir, chapter)
        if os.path.exists(chapter_dir):
            process_chapter(chapter_dir, prompt_text)
        else:
            print(f"Directory not found: {chapter_dir}")

if __name__ == "__main__":
    main()
