import os
import re

def update_mobile_menu():
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['login.html', 'register.html']]
    
    new_script = """<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Mobile Menu Logic
        const nav = document.querySelector('nav') || document.querySelector('header');
        if (!nav) return;
        
        const hamburgerBtn = nav.querySelector('[data-icon="menu"]')?.closest('button') || Array.from(nav.querySelectorAll('button')).find(b => b.classList.contains('xl:hidden') || b.querySelector('[data-icon="menu"]'));
        const desktopMenu = nav.querySelector('.hidden') || Array.from(nav.querySelectorAll('div')).find(el => el.classList.contains('xl:flex') && el.classList.contains('hidden'));
        
        if (hamburgerBtn && desktopMenu && !document.getElementById('mobile-menu-container')) {
            // Create mobile menu container
            const mobileMenu = document.createElement('div');
            mobileMenu.id = 'mobile-menu-container';
            mobileMenu.className = 'hidden xl:hidden bg-background dark:bg-[#1a0f08] fixed top-[72px] left-0 w-full max-h-[calc(100vh-72px)] overflow-y-auto border-b border-outline-variant/10 dark:border-outline-variant/5 shadow-2xl flex-col px-8 py-6 space-y-4 z-50';
            
            // Clone links
            const links = desktopMenu.cloneNode(true);
            links.className = 'flex flex-col space-y-6';
            
            function openMobileMenu() {
                mobileMenu.classList.remove('hidden');
                mobileMenu.classList.add('flex');
                document.body.style.overflow = 'hidden';
                const icon = hamburgerBtn.querySelector('span');
                if(icon) icon.textContent = 'close';
            }

            function closeMobileMenu() {
                mobileMenu.classList.add('hidden');
                mobileMenu.classList.remove('flex');
                document.body.style.overflow = '';
                const icon = hamburgerBtn.querySelector('span');
                if(icon) icon.textContent = 'menu';
            }

            // Fix text size for mobile & add close click listener
            const anchorTags = links.querySelectorAll('a');
            anchorTags.forEach(a => {
                a.classList.add('text-base');
                a.addEventListener('click', function() {
                    closeMobileMenu();
                });
            });
            
            // Toggles Container
            const togglesContainer = document.createElement('div');
            togglesContainer.className = 'flex justify-center items-center gap-8 pt-4 border-t border-outline-variant/10 dark:border-white/10 w-full';
            
            // Theme Toggle
            const themeBtn = document.createElement('button');
            themeBtn.className = 'text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors flex items-center space-x-2';
            themeBtn.innerHTML = '<span class="material-symbols-outlined dark:hidden">dark_mode</span><span class="material-symbols-outlined hidden dark:block">light_mode</span><span class="font-label-sm font-bold">Theme</span>';
            themeBtn.addEventListener('click', function() {
                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark');
                    localStorage.theme = 'light';
                } else {
                    document.documentElement.classList.add('dark');
                    localStorage.theme = 'dark';
                }
            });
            
            // RTL Toggle
            const rtlBtnMobile = document.createElement('button');
            rtlBtnMobile.className = 'text-on-surface-variant dark:text-surface-variant hover:text-secondary dark:hover:text-secondary-fixed-dim transition-colors font-label-sm font-bold flex items-center';
            rtlBtnMobile.innerText = 'RTL';
            rtlBtnMobile.addEventListener('click', function() {
                if (document.documentElement.getAttribute('dir') === 'rtl') {
                    document.documentElement.setAttribute('dir', 'ltr');
                } else {
                    document.documentElement.setAttribute('dir', 'rtl');
                }
            });
            
            togglesContainer.appendChild(themeBtn);
            togglesContainer.appendChild(rtlBtnMobile);

            // Add Login to mobile menu
            const loginBtn = document.createElement('a');
            loginBtn.href = 'login.html';
            loginBtn.className = 'bg-primary-container dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed px-4 py-3 rounded font-label-sm font-bold text-center block w-full mt-4 text-base shadow-sm hover:bg-secondary-container dark:hover:bg-secondary-fixed transition-all';
            loginBtn.innerText = 'Login';
            loginBtn.addEventListener('click', function() {
                closeMobileMenu();
            });
            
            mobileMenu.appendChild(links);
            mobileMenu.appendChild(togglesContainer);
            mobileMenu.appendChild(loginBtn);
            
            nav.appendChild(mobileMenu);
            
            // Toggle Logic
            hamburgerBtn.addEventListener('click', function() {
                const isHidden = mobileMenu.classList.contains('hidden');
                if (isHidden) {
                    openMobileMenu();
                } else {
                    closeMobileMenu();
                }
            });
        }
    });
</script>"""

    pattern = r'<script>\s*document\.addEventListener\("DOMContentLoaded", function\(\)\s*\{\s*// Mobile Menu Logic.*?</script>'

    for fname in html_files:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if re.search(pattern, content, flags=re.DOTALL):
            new_content = re.sub(pattern, new_script, content, flags=re.DOTALL)
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated sticky/fixed mobile menu in {fname}")
        else:
            print(f"Pattern not found in {fname}")

if __name__ == "__main__":
    update_mobile_menu()
