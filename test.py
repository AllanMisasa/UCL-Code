import requests

file_url = 'https://www.gutenberg.org/cache/epub/72577/pg72577.txt'
response = requests.get(file_url)

if (response.status_code):
    data = response.text
    for character in data:
        if character in ['.', ',', '!', '?', ';', ':']:
            data = data.replace(character, '')
    words = data.split()

print(len(words))