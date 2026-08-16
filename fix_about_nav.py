import os

def fix_about_nav():
    filename = 'about.html'
    if not os.path.exists(filename):
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_nav = """<!-- TopNavBar -->
<header class="fixed top-0 w-full h-[72px] z-50 bg-background/80 dark:bg-[#1a0f08]/90 backdrop-blur-md border-b border-outline-variant/10 dark:border-outline-variant/5 shadow-sm dark:shadow-none transition-all">
<div class="flex justify-between items-center h-full px-margin-safe max-w-[1200px] mx-auto">
<a class="flex items-center gap-2 hover:scale-105 transition-transform duration-300" href="index.html"><span class="material-symbols-outlined text-2xl text-primary-container dark:text-primary-fixed">menu_book</span><span class="font-display text-[22px] font-bold tracking-tight text-on-background dark:text-primary-fixed" style="font-family:'Playfair Display',serif">Book Haven</span></a>
<div class="hidden lg:flex gap-gutter">
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="index.html">Home</a>
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="home2.html">Home 2</a>
<a class="text-secondary dark:text-secondary-fixed-dim transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all font-bold border-b-2 border-secondary dark:border-secondary-fixed-dim pb-1" href="about.html">About</a>
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="books.html">Books</a>
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="discussions.html">Discussions</a>
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="blog.html">Blog</a>
<a class="text-on-surface-variant dark:text-surface-variant transition-colors duration-200 font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all" href="dashboard.html">Dashboard</a>
</div>
<div class="flex items-center gap-stack-md">
<button class="hidden lg:flex w-10 h-10 items-center justify-center rounded-full text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors hover:bg-surface-container-high dark:hover:bg-dark-surface" id="theme-toggle">
<span class="material-symbols-outlined dark:hidden">dark_mode</span>
<span class="material-symbols-outlined hidden dark:block">light_mode</span>
</button>
<button class="hidden lg:flex w-10 h-10 items-center justify-center rounded-full text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors font-label-sm font-bold hover:bg-surface-container-high dark:hover:bg-dark-surface" id="rtl-toggle" title="Toggle RTL">RTL</button>
<a href="login.html" class="hidden lg:block bg-primary-container dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed px-4 py-2 rounded font-label-sm text-label-sm hover:bg-secondary-container dark:hover:bg-secondary-fixed transition-all shadow-sm">Login</a>
<button class="text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors lg:hidden">
<span class="material-symbols-outlined" data-icon="menu">menu</span>
</button>
</div>
</div>
</header>"""

    # We will slice out everything from <!-- TopNavBar --> to the closing </header> BEFORE <main
    import re
    
    pattern = r'<!-- TopNavBar -->\s*<header.*?</header>'
    
    # Let's double check it only matches the first header block
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        new_content = content[:match.start()] + new_nav + content[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated about.html")
    else:
        print("Could not find TopNavBar section in about.html")

if __name__ == "__main__":
    fix_about_nav()
