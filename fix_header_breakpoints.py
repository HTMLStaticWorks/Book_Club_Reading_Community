import os
import re

def fix_header_breakpoints():
    files = ['about.html', 'home2.html']
    for f in files:
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # The top menu is inside <header class="fixed top-0...
            # We'll just replace 'lg:flex', 'lg:hidden', 'lg:block' in the header block
            
            header_start = content.find('<header')
            header_end = content.find('</header>') + len('</header>')
            
            if header_start != -1:
                header_content = content[header_start:header_end]
                
                new_header_content = header_content.replace('lg:flex', 'xl:flex')
                new_header_content = new_header_content.replace('lg:hidden', 'xl:hidden')
                new_header_content = new_header_content.replace('lg:block', 'xl:block')
                
                content = content[:header_start] + new_header_content + content[header_end:]
            
            # Also replace in the JS block
            content = content.replace("classList.contains('lg:flex')", "classList.contains('xl:flex')")
            content = content.replace("classList.contains('lg:hidden')", "classList.contains('xl:hidden')")
            content = content.replace("className = 'hidden lg:hidden", "className = 'hidden xl:hidden")
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Fixed breakpoints in {f}")

if __name__ == "__main__":
    fix_header_breakpoints()
