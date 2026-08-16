import os
import re

def update_navbar_breakpoints():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            nav_start = content.find('<nav')
            if nav_start == -1:
                continue
                
            nav_end = content.find('</nav>') + len('</nav>')
            nav_content = content[nav_start:nav_end]
            
            # Replace lg: breakpoints with xl: in navbar
            new_nav_content = nav_content.replace('lg:flex', 'xl:flex')
            new_nav_content = new_nav_content.replace('lg:hidden', 'xl:hidden')
            new_nav_content = new_nav_content.replace('lg:block', 'xl:block')
            
            content = content[:nav_start] + new_nav_content + content[nav_end:]
            
            # Also fix the JS scripts that reference lg:flex or lg:hidden
            content = content.replace("classList.contains('lg:flex')", "classList.contains('xl:flex')")
            content = content.replace("classList.contains('lg:hidden')", "classList.contains('xl:hidden')")
            content = content.replace("className = 'hidden lg:hidden", "className = 'hidden xl:hidden")
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Updated breakpoints in {f}")

if __name__ == "__main__":
    update_navbar_breakpoints()
