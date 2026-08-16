import os, re

def remove_join_club():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Remove the desktop "Join Club" button from the nav bar
            # We specifically look for the one with 'hidden lg:block' to ensure we only hit the navbar one
            content = re.sub(
                r'\n?\s*<a href="register\.html" class="hidden lg:block[^"]*">Join Club</a>',
                '',
                content
            )
            
            # Remove mobile menu JS logic for "Join Club"
            content = re.sub(
                r'\s*const joinBtn = document\.createElement\(\'a\'\);\s*joinBtn\.href = \'register\.html\';\s*joinBtn\.className = \'[^\']*\';\s*joinBtn\.innerText = \'Join Club\';',
                '',
                content
            )
            
            # Remove appending joinBtn to mobileMenu
            content = re.sub(
                r'\s*mobileMenu\.appendChild\(joinBtn\);',
                '',
                content
            )

            # Change comment from "Add Login and Join Club to mobile menu" to "Add Login to mobile menu"
            content = content.replace(
                '// Add Login and Join Club to mobile menu',
                '// Add Login to mobile menu'
            )

            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    remove_join_club()
