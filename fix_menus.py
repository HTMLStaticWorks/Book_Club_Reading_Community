import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

active_class = 'text-secondary dark:text-secondary-fixed-dim transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all font-bold border-b-2 border-secondary dark:border-secondary-fixed-dim pb-1'
inactive_class = 'text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all'

pages = [
    ('index.html', 'Home'),
    ('home2.html', 'Home 2'),
    ('about.html', 'About'),
    ('books.html', 'Books'),
    ('discussions.html', 'Discussions'),
    ('blog.html', 'Blog'),
    ('dashboard.html', 'Dashboard')
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix logo
    content = re.sub(
        r'<a class="font-headline-md.*?href="index\.html">Book Haven</a>',
        '<a class="font-headline-md text-headline-md font-bold text-on-background dark:text-primary-fixed" href="index.html">Book Haven</a>',
        content, flags=re.DOTALL
    )

    # Build the correct menu block for this file
    menu_html = '<div class="hidden lg:flex space-x-gutter">\n'
    for href, text in pages:
        cls = active_class if file == href else inactive_class
        menu_html += f'<a class="{cls}" href="{href}">{text}</a>\n'
    menu_html += '</div>'

    # Replace the menu block
    content = re.sub(
        r'<div class="hidden lg:flex space-x-gutter">.*?</div>',
        menu_html,
        content, flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
