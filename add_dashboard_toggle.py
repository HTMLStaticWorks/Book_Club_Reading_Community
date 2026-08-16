import re

def add_sidebar_toggle():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the header inside main
    header_start = content.find('<header')
    header_end = content.find('</header>') + len('</header>')
    
    header_content = content[header_start:header_end]
    
    # Let's add a mobile toggle button in the header
    button_html = """
<div class="w-full md:hidden mb-4 flex justify-end">
    <button id="mobile-menu-btn" class="flex items-center gap-2 bg-surface-container-low dark:bg-[#3d1f0d] text-on-surface-variant dark:text-[#fcdcc9] px-4 py-2 rounded-lg font-label-sm shadow-sm border border-outline-variant/20 hover:bg-surface-container transition-colors">
        <span class="material-symbols-outlined text-[18px]">menu_open</span>
        Dashboard Menu
    </button>
</div>
"""
    
    # Inject it before the h1 block
    div_start = header_content.find('<div>')
    new_header = header_content[:div_start] + button_html + header_content[div_start:]
    
    content = content[:header_start] + new_header + content[header_end:]

    # Update the JS to attach to the new button
    old_js = """        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebar-overlay');

        function toggleSidebar() {
            sidebar.classList.toggle('translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        }

        // sidebarOverlay.addEventListener('click', toggleSidebar);"""
        
    new_js = """        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebar-overlay');

        function toggleSidebar() {
            sidebar.classList.toggle('translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        }

        if(mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', toggleSidebar);
        }
        if(sidebarOverlay) {
            sidebarOverlay.addEventListener('click', toggleSidebar);
        }"""
        
    content = content.replace(old_js, new_js)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added mobile menu button")

if __name__ == "__main__":
    add_sidebar_toggle()
