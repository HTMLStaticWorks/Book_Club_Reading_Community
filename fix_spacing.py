import os

def fix_spacing():
    files = [f for f in os.listdir('.') if f.endswith('.html') or f == 'fix_menus.py']
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('space-x-gutter', 'gap-gutter')
        new_content = new_content.replace('space-x-stack-md', 'gap-stack-md')
        new_content = new_content.replace(' space-x-8 ', ' gap-8 ')
        new_content = new_content.replace(' space-x-2 ', ' gap-2 ')
        new_content = new_content.replace(' space-x-2"', ' gap-2"')
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")

if __name__ == "__main__":
    fix_spacing()
