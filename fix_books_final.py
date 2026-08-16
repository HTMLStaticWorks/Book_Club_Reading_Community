import re

def fix_books_final():
    with open('books.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Make sure we didn't already replace it
    if 'lg:w-[calc' not in content:
        content = re.sub(
            r'flex flex-col h-full bg-surface-container-lowest',
            r'w-full sm:w-[calc(50%-1rem)] md:w-[calc(33.333%-1.333rem)] lg:w-[calc(25%-1.5rem)] flex flex-col h-full bg-surface-container-lowest',
            content
        )

        with open('books.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated books.html")
    else:
        print("Already updated")

if __name__ == "__main__":
    fix_books_final()
