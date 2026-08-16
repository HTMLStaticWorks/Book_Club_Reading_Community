import os, re

def update_buttons():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace theme toggle class
            content = re.sub(
                r'<button class="hidden lg:block text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors" id="theme-toggle">',
                '<button class="hidden lg:flex w-10 h-10 items-center justify-center rounded-full text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors hover:bg-surface-container-high dark:hover:bg-dark-surface" id="theme-toggle">',
                content
            )
            
            # Replace rtl toggle class
            content = re.sub(
                r'<button class="hidden lg:block text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors font-label-sm font-bold" id="rtl-toggle" title="Toggle RTL">',
                '<button class="hidden lg:flex w-10 h-10 items-center justify-center rounded-full text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors font-label-sm font-bold hover:bg-surface-container-high dark:hover:bg-dark-surface" id="rtl-toggle" title="Toggle RTL">',
                content
            )

            # Mobile menu updates if needed
            # "themeBtn.className = 'text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors flex items-center gap-2';"
            # Let's see if we need to do anything there. Mobile already has flex.

            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    update_buttons()
