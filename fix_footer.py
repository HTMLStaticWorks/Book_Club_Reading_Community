import os

def remove_footer_margin():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Remove mt-section-gap from footer class across all files
            new_content = content.replace(' mt-section-gap', '')
            
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)

if __name__ == "__main__":
    remove_footer_margin()
