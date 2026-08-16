import re

def deduplicate_classes():
    with open('books.html', 'r', encoding='utf-8') as f:
        content = f.read()

    width_classes = r'w-full sm:w-\[calc\(50%-1rem\)\] md:w-\[calc\(33\.333%-1\.333rem\)\] lg:w-\[calc\(25%-1\.5rem\)\] '
    duplicate_pattern = width_classes + width_classes
    
    content = re.sub(duplicate_pattern, 'w-full sm:w-[calc(50%-1rem)] md:w-[calc(33.333%-1.333rem)] lg:w-[calc(25%-1.5rem)] ', content)

    with open('books.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Deduplicated!")

if __name__ == "__main__":
    deduplicate_classes()
