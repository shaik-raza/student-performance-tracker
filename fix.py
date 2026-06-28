with open('requirements.txt', 'rb') as f:
    content = f.read()

# Remove BOM if present
if content.startswith(b'\xff\xfe'):
    content = content[2:]

content = content.decode('utf-16-le')

with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')