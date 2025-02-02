import json
import re
import http.client
import os
import sys
from pathlib import Path

def extract_hugo_parts(content):
    # Split into frontmatter and body
    parts = content.split('+++', 2)
    if len(parts) != 3:
        raise ValueError("Invalid Hugo content format")
    
    return parts[1].strip(), parts[2].strip()

def translate_title(frontmatter):
    # Extract title line
    title_match = re.search(r'title\s*=\s*"([^"]+)"', frontmatter)
    if not title_match:
        return frontmatter
    
    title = title_match.group(1)
    translated_title = call_local_llm(f"Translate to Thai: {title}")
    return frontmatter.replace(title, translated_title)

def translate_content(content):
    return call_local_llm(f'''
        <purpose>
            Translate to Thai, preserve markdown formatting and special characters: {content}
            Don't use Chinese characters.
            Use only Thai and English. All the terms and abbreviations should be in English.
            Technical terms should be in English.
            HTML formatting should be preserved. 
            Hugo functions should be preserved.
            Translate only text
        </purpose>
        <output>
            <format>markdown</format>
        </output>
    ''')

def call_local_llm(prompt):
    conn = http.client.HTTPConnection("localhost", 4000)
    
    payload = json.dumps({
        # "model": "lm_studio/deepseek-r1-14b",
        "model": "lm_studio/phi4-14b",
        "prompt": prompt,
        "max_tokens": 2000,
        "temperature": 0.3,
        "stream": False
    })
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:
        conn.request("POST", "/v1/completions", payload, headers)
        response = conn.getresponse()
        
        if response.status != 200:
            print(f"API error: {response.status}")
            print(response.read().decode())
            raise Exception(f"API error: {response.status}")
            
        result = json.loads(response.read().decode())
        
        # Extract content and clean it
        content = result['choices'][0]['text'].strip()
        # Remove thinking process
        if '<think>' in content:
            content = content.split('</think>')[-1].strip()
        
        return content
    except Exception as e:
        print(f"Error calling LLM API: {str(e)}")
        raise
    finally:
        conn.close()

def process_file(input_path):
    print(f"Processing {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = extract_hugo_parts(content)
    translated_frontmatter = translate_title(frontmatter)
    translated_body = translate_content(body)
    
    translated_content = f"+++{translated_frontmatter}\n+++\n\n{translated_body}"
    
    output_path = str(input_path).replace('.md', '.th.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    print(f"Saved translation to {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tools/translate.py <filename>.md")
        sys.exit(1)
    
    input_path = sys.argv[1]
    if not input_path.endswith('.md'):
        print("Error: Input file must be a Markdown file.")
        sys.exit(1)
    
    process_file(input_path)

if __name__ == "__main__":
    main() 