import os
import re

def fix_all():
    logo_html = """
<div class="fixed top-6 left-6 z-50">
    <a class="flex items-center gap-2 hover:scale-105 transition-transform duration-300" href="index.html">
        <span class="material-symbols-outlined text-2xl text-primary-container dark:text-primary-fixed">menu_book</span>
        <span class="font-display text-[22px] font-bold tracking-tight text-on-background dark:text-primary-fixed" style="font-family:'Playfair Display',serif">Book Haven</span>
    </a>
</div>
"""
    # 1. Add Logo to login.html and register.html
    for f in ['login.html', 'register.html']:
        if not os.path.exists(f): continue
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'Book Haven' not in content or '<div class="fixed top-6 left-6 z-50">' not in content:
            # insert after body
            content = re.sub(r'(<body[^>]*>)', r'\1' + logo_html, content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Added logo to {f}")

    # 2. Fix 'Join Club' buttons in all files
    for f in os.listdir('.'):
        if not f.endswith('.html'): continue
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()

        changed = False

        # Add "Join Club" next to "Login" in navbars if it doesn't exist
        login_btn = r'<a href="login\.html" class="([^"]*)">Login</a>'
        if re.search(login_btn, content) and 'Join Club</a>' not in content:
            # We add Join Club right after Login
            # We'll make Login secondary style and Join Club primary style, or both primary
            replacement = r'<a href="login.html" class="\1">Login</a>\n<a href="register.html" class="\1">Join Club</a>'
            content = re.sub(login_btn, replacement, content)
            changed = True
            
        # Fix the 'Join the Club' button in the hero sections (e.g. index.html)
        # If it's a <button> without onclick, add onclick
        join_btn_pattern = r'(<button class="[^"]*?)"?(>Join the Club</button>)'
        if re.search(join_btn_pattern, content):
            # Check if it doesn't already have onclick
            if 'onclick=' not in re.search(join_btn_pattern, content).group(1):
                content = re.sub(join_btn_pattern, r'\1 onclick="window.location.href=\'register.html\'"\2', content)
                changed = True

        # Check for any other <button>Join Club</button>
        join_btn_pattern2 = r'(<button class="[^"]*?)"?(>Join Club</button>)'
        if re.search(join_btn_pattern2, content):
            if 'onclick=' not in re.search(join_btn_pattern2, content).group(1):
                content = re.sub(join_btn_pattern2, r'\1 onclick="window.location.href=\'register.html\'"\2', content)
                changed = True

        if changed:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Fixed Join Club in {f}")

if __name__ == "__main__":
    fix_all()
