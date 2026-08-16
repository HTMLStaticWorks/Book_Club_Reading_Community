import os
import re

def update_login_register():
    for filename in ['login.html', 'register.html']:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove back-home link and its CSS
        content = re.sub(r'<!-- Back to Home -->\s*<a href="index\.html" class="back-home">\s*<span class="material-symbols-outlined"[^>]*>arrow_back</span>\s*Book Haven\s*</a>', '', content)
        content = re.sub(r'/\* Back to Home link \*/[\s\S]*?(?=\/\* Theme toggle \*\/)', '', content)

        # Update Theme toggle CSS to remove fixed positioning so we can use a flex container
        css_replacement = """/* Theme & RTL toggle */
    .top-right-container {
        position: fixed;
        top: 24px;
        right: 24px;
        z-index: 50;
        display: flex;
        gap: 16px;
    }
    .theme-btn {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.35);
        border-radius: 50%;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #3d1f0d;
        font-family: 'Literata', serif;
        font-weight: 600;
        font-size: 14px;
    }"""
        
        content = re.sub(r'/\* Theme toggle \*/\s*\.theme-btn\s*\{\s*position:\s*fixed;\s*top:\s*24px;\s*right:\s*24px;\s*z-index:\s*50;\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.25\);\s*backdrop-filter:\s*blur\(10px\);\s*border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.35\);\s*border-radius:\s*50%;\s*width:\s*48px;\s*height:\s*48px;\s*display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*center;\s*cursor:\s*pointer;\s*transition:\s*all\s*0\.3s\s*ease;\s*color:\s*#3d1f0d;\s*\}', css_replacement, content)

        # Update Theme toggle HTML to include RTL toggle in a container
        html_replacement = """<!-- Toggles Container -->
<div class="top-right-container">
    <button class="theme-btn" id="rtl-toggle-btn" aria-label="Toggle RTL">RTL</button>
    <button class="theme-btn" id="theme-toggle-btn" aria-label="Toggle Dark Mode">
        <span class="material-symbols-outlined dark:hidden" data-icon="dark_mode">dark_mode</span>
        <span class="material-symbols-outlined hidden dark:block" data-icon="light_mode">light_mode</span>
    </button>
</div>"""
        
        content = re.sub(r'<!-- Theme Toggle -->\s*<button class="theme-btn"[^>]*>\s*<span class="material-symbols-outlined dark:hidden"[^>]*>dark_mode</span>\s*<span class="material-symbols-outlined hidden dark:block"[^>]*>light_mode</span>\s*</button>', html_replacement, content)
        content = re.sub(r'<!-- Theme Toggle -->\s*<button aria-label="Toggle Dark Mode" class="theme-toggle-btn" id="theme-toggle-btn">\s*<span class="material-symbols-outlined dark:hidden" data-icon="dark_mode">dark_mode</span>\s*<span class="material-symbols-outlined hidden dark:block" data-icon="light_mode">light_mode</span>\s*</button>', html_replacement, content)
        content = re.sub(r'<!-- Theme Toggle -->\s*<button aria-label="Toggle Dark Mode" class="theme-btn" id="theme-toggle-btn">\s*<span class="material-symbols-outlined dark:hidden">dark_mode</span>\s*<span class="material-symbols-outlined hidden dark:block">light_mode</span>\s*</button>', html_replacement, content)


        # Add RTL toggle JS logic
        js_addition = """
    const rtlBtn = document.getElementById('rtl-toggle-btn');
    if(rtlBtn) {
        rtlBtn.addEventListener('click', function() {
            if (document.documentElement.getAttribute('dir') === 'rtl') {
                document.documentElement.setAttribute('dir', 'ltr');
            } else {
                document.documentElement.setAttribute('dir', 'rtl');
            }
        });
    }"""
        
        content = content.replace("const themeBtn = document.getElementById('theme-toggle-btn');", js_addition + "\n\n    const themeBtn = document.getElementById('theme-toggle-btn');")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_login_register()
