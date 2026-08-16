import os

def update_login_button():
    for f in os.listdir('.'):
        if f.endswith('.html'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Desktop Login button
            old_desktop_login = '<a href="login.html" class="hidden lg:block text-secondary dark:text-secondary-fixed-dim font-label-sm text-label-sm hover:text-secondary dark:hover:text-secondary-fixed-dim transition-all">Login</a>'
            new_desktop_login = '<a href="login.html" class="hidden lg:block bg-primary-container dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed px-4 py-2 rounded font-label-sm text-label-sm hover:bg-secondary-container dark:hover:bg-secondary-fixed transition-all shadow-sm">Login</a>'
            
            content = content.replace(old_desktop_login, new_desktop_login)
            
            # Mobile Login button in JS
            old_mobile_class = "loginBtn.className = 'text-secondary dark:text-secondary-fixed-dim font-label-sm font-bold pt-4 block w-full text-center text-base';"
            new_mobile_class = "loginBtn.className = 'bg-primary-container dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed px-4 py-3 rounded font-label-sm font-bold text-center block w-full mt-4 text-base shadow-sm hover:bg-secondary-container dark:hover:bg-secondary-fixed transition-all';"
            
            content = content.replace(old_mobile_class, new_mobile_class)

            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    update_login_button()
