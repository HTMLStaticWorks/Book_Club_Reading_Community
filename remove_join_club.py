import os
import re

def remove_join_club():
    pattern = r'\s*<a href="register\.html" class="[^"]*">Join Club</a>'
    
    for f in sorted(os.listdir('.')):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                
            new_content = re.sub(pattern, '', content)
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Removed Join Club from navbar in {f}")

if __name__ == "__main__":
    remove_join_club()
