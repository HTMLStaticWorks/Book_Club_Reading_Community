import os
import re

def fix_all_last_section_padding():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            footer_idx = content.find('<footer')
            if footer_idx == -1:
                continue
                
            before_footer = content[:footer_idx]
            
            # Find the last container (either section or main) before footer
            last_section_start = before_footer.rfind('<section')
            last_main_start = before_footer.rfind('<main')
            
            last_container_start = max(last_section_start, last_main_start)
            
            if last_container_start != -1:
                container_end = before_footer.find('>', last_container_start)
                container_tag = before_footer[last_container_start:container_end+1]
                
                new_container_tag = container_tag
                
                # Replace pb-something
                new_container_tag = re.sub(r'\bpb-[\w-]+\b', 'pb-0', new_container_tag)
                new_container_tag = re.sub(r'\bmd:pb-[\w-]+\b', 'md:pb-0', new_container_tag)
                
                # Replace py-something with pt-something pb-0
                new_container_tag = re.sub(r'\bpy-([\w-]+)\b', r'pt-\1 pb-0', new_container_tag)
                new_container_tag = re.sub(r'\bmd:py-([\w-]+)\b', r'md:pt-\1 md:pb-0', new_container_tag)
                
                # Also, if there's a mb-something, replace it
                new_container_tag = re.sub(r'\bmb-[\w-]+\b', 'mb-0', new_container_tag)
                
                if 'pb-0' not in new_container_tag:
                    new_container_tag = new_container_tag.replace('class="', 'class="pb-0 ')
                
                if container_tag != new_container_tag:
                    new_content = content[:last_container_start] + new_container_tag + content[container_end+1:]
                    with open(f, 'w', encoding='utf-8') as out_file:
                        out_file.write(new_content)
                    print(f"Updated padding in {f}")

if __name__ == "__main__":
    fix_all_last_section_padding()
