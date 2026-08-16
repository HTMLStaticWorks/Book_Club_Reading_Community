import os
import re

def remove_footer_para():
    para_pattern = r'<p class="[^"]*text-on-surface-variant[^"]*mb-8[^"]*">\s*Elevating the art of slow reading[\s\S]*?</p>'
    
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Verify if it has footer
            if '<footer' in content:
                new_content = re.sub(para_pattern, '', content)
                if new_content != content:
                    with open(f, 'w', encoding='utf-8') as out:
                        out.write(new_content)
                    print(f"Removed paragraph in {f}")

if __name__ == "__main__":
    remove_footer_para()
