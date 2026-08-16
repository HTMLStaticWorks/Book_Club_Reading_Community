import re

def fix_books_grid():
    try:
        with open('books.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace grid container
        content = content.replace(
            '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">',
            '<div class="flex flex-wrap justify-center gap-8">'
        )

        # The cards have this class:
        # <div class="group scroll-animate opacity-0 translate-y-8 transition-all duration-700 delay-... flex flex-col h-full bg-surface-container-lowest
        
        # We need to insert the width classes before 'flex flex-col'
        # Let's use regex to find the card wrapper and insert the width classes
        card_pattern = re.compile(r'(<div class="group scroll-animate[^"]*?)(flex flex-col h-full bg-surface-container-lowest)')
        
        width_classes = 'w-full sm:w-[calc(50%-1rem)] md:w-[calc(33.333%-1.333rem)] lg:w-[calc(25%-1.5rem)] '
        
        content = card_pattern.sub(r'\1' + width_classes + r'\2', content)

        with open('books.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Updated books.html successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_books_grid()
