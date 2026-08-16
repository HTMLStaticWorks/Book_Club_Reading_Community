import os
import re

def check_footer_gap():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find the section just before the footer
            match = re.search(r'(<section[^>]*>[\s\S]*?</section>)\s*<footer', content)
            if match:
                section_tag = re.search(r'<section[^>]*>', match.group(1)).group(0)
                print(f"File: {f}")
                print(f"Section before footer: {section_tag}")
                print("-" * 40)

if __name__ == "__main__":
    check_footer_gap()
