import re

def fix_dashboard():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract aside
    aside_start = content.find('<aside')
    aside_end = content.find('</aside>') + len('</aside>')
    aside_content = content[aside_start:aside_end]

    # Change classes in aside
    # 1. left-0 -> right-0
    aside_content = aside_content.replace('left-0', 'right-0')
    # 2. -translate-x-full -> translate-x-full
    aside_content = aside_content.replace('-translate-x-full', 'translate-x-full')
    # 3. border-r -> border-l
    aside_content = aside_content.replace('border-r ', 'border-l ')
    # 4. Remove md:translate-x-0? No, md:translate-x-0 is fine, it resets transform.

    # Extract overlay
    overlay_start = content.find('<div class="fixed inset-0 bg-primary/20', aside_end)
    overlay_end = content.find('</div>', overlay_start) + len('</div>')
    overlay_content = content[overlay_start:overlay_end]

    # Extract main
    main_start = content.find('<main')
    main_end = content.find('</main>') + len('</main>')
    main_content = content[main_start:main_end]

    # Remove aside and overlay from before main
    new_content = content[:aside_start] + main_content + '\n' + aside_content + '\n' + overlay_content + content[main_end:]

    # Fix the JS error
    js_to_replace = """        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebar-overlay');

        function toggleSidebar() {
            sidebar.classList.toggle('-translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        }

        mobileMenuBtn.addEventListener('click', toggleSidebar);
        sidebarOverlay.addEventListener('click', toggleSidebar);"""
    
    fixed_js = """        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebar-overlay');

        function toggleSidebar() {
            sidebar.classList.toggle('translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        }

        // sidebarOverlay.addEventListener('click', toggleSidebar);"""

    new_content = new_content.replace(js_to_replace, fixed_js)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed dashboard layout")

if __name__ == "__main__":
    fix_dashboard()
