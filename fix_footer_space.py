import os
import re

def fix_footer_space():
    for f in sorted(os.listdir('.')):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()

            footer_idx = content.find('<footer')
            if footer_idx == -1:
                continue

            before_footer = content[:footer_idx]
            last_section_start = before_footer.rfind('<section')

            if last_section_start != -1:
                section_end = before_footer.find('>', last_section_start)
                section_tag = before_footer[last_section_start:section_end+1]
                
                new_section_tag = section_tag
                new_section_tag = re.sub(r'\bmd:pb-0\b', 'md:pb-section-gap', new_section_tag)
                new_section_tag = re.sub(r'\bpb-0\b', 'pb-section-gap-mobile md:pb-section-gap', new_section_tag)
                
                if section_tag != new_section_tag:
                    content = content[:last_section_start] + new_section_tag + content[section_end+1:]
                    footer_idx = content.find('<footer')

            footer_start = footer_idx
            footer_end = content.find('>', footer_start)
            footer_tag = content[footer_start:footer_end+1]

            new_footer_tag = footer_tag
            if 'mt-' not in new_footer_tag:
                new_footer_tag = new_footer_tag.replace('class="', 'class="mt-16 md:mt-24 ')
            new_footer_tag = new_footer_tag.replace('pt-20 pb-10', 'pt-24 pb-16')
            
            if footer_tag != new_footer_tag:
                content = content[:footer_start] + new_footer_tag + content[footer_end+1:]

            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated footer spacing in {f}")

if __name__ == "__main__":
    fix_footer_space()
