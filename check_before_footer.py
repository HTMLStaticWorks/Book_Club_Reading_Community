import re

def show_before_footer():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract 500 characters before the <footer> tag
    footer_idx = content.find('<footer')
    if footer_idx != -1:
        start_idx = max(0, footer_idx - 500)
        print("ABOUT.HTML:")
        print(content[start_idx:footer_idx])
        print("="*50)
        
    with open('home2.html', 'r', encoding='utf-8') as f:
        content = f.read()
    footer_idx = content.find('<footer')
    if footer_idx != -1:
        start_idx = max(0, footer_idx - 500)
        print("HOME2.HTML:")
        print(content[start_idx:footer_idx])
        print("="*50)

if __name__ == "__main__":
    show_before_footer()
