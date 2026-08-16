import os
import re

def fix_last_section_padding():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find the section just before the footer
            # It could be separated by </main>
            # We want to find the LAST <section... in the file before <footer>
            
            footer_idx = content.find('<footer')
            if footer_idx == -1:
                continue
                
            before_footer = content[:footer_idx]
            last_section_start = before_footer.rfind('<section')
            
            if last_section_start != -1:
                # We have the last section. Let's replace py-section-gap with pt-section-gap pb-0
                # or py-section-gap-mobile with pt-section-gap-mobile pb-0
                section_end = before_footer.find('>', last_section_start)
                section_tag = before_footer[last_section_start:section_end+1]
                
                new_section_tag = section_tag
                
                # Replace py-section-gap
                new_section_tag = re.sub(r'\bpy-section-gap\b', 'pt-section-gap pb-0', new_section_tag)
                new_section_tag = re.sub(r'\bpy-section-gap-mobile\b', 'pt-section-gap-mobile pb-0', new_section_tag)
                
                # Also replace md:py-section-gap
                new_section_tag = re.sub(r'\bmd:py-section-gap\b', 'md:pt-section-gap md:pb-0', new_section_tag)
                
                if section_tag != new_section_tag:
                    new_content = content[:last_section_start] + new_section_tag + content[section_end+1:]
                    with open(f, 'w', encoding='utf-8') as out_file:
                        out_file.write(new_content)
                    print(f"Updated padding in {f}")

if __name__ == "__main__":
    fix_last_section_padding()
