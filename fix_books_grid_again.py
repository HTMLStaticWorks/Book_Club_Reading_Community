import os

def fix_books_grid_again():
    try:
        with open('books.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # The card div starts like this:
        old_classes = 'flex flex-col h-full bg-surface-container-lowest dark:bg-[#28180c] rounded-xl overflow-hidden soft-shadow wood-border hover:shadow-lg'
        new_classes = 'w-full sm:w-[calc(50%-1rem)] md:w-[calc(33.333%-1.333rem)] lg:w-[calc(25%-1.5rem)] ' + old_classes
        
        content = content.replace(old_classes, new_classes)

        with open('books.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Updated books.html successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_books_grid_again()
