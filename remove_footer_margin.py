import os

def remove_footer_margin():
    for f in sorted(os.listdir('.')):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()

            new_content = content.replace('class="mt-16 md:mt-24 ', 'class="')
            new_content = new_content.replace('class="mt-16 ', 'class="')
            new_content = new_content.replace('class="mt-24 ', 'class="')
            
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Removed top margin from footer in {f}")

if __name__ == "__main__":
    remove_footer_margin()
