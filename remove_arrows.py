import re

def remove_arrows():
    with open('blog.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The arrow is <span class="material-symbols-outlined text-sm">arrow_forward</span>
    # Sometimes there's a space before it.
    new_content = re.sub(r'\s*<span class="material-symbols-outlined text-sm">arrow_forward</span>', '', content)
    
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed arrows from blog.html")

if __name__ == "__main__":
    remove_arrows()
