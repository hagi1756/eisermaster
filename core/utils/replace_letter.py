

# letter={
#         'ə':'e',
#         'ü':'u',
#         'ö':'o',
#         'ı':'i',
#         'ğ':'g',
#         'ş':'s',
#         'ç':'c',
#         'Ə':'E',
#         'Ü':'U',
#         'Ö':'O',
#         'I':'İ',
#         'Ğ':'G',
#         'Ş':'S',
#         'Ç':'C',
#         '?':'',
#         '':'-',
#         '!':'',
#         '.':'',
#         ',':'',
#         ';':'',
#         ':':'',
#         '*':'',
#         '%':'',
#         '^':'',
#         '&':'',
#         '$':'',
#         '#':'',
#         '@':'',
       


# }

# def replace_letter(text):
#     for key, value in letter.items():  # Değişken adını `letter` olarak değiştirin
#         text = text.replace(key, value)
#     return text

# def replace_letter(text):
#     for key,value in replace_letter.items():
#         text=text.replace(key,value)
#     return text

letter = {
    'ə': 'e',
    'ü': 'u',
    'ö': 'o',
    'ı': 'i',
    'ğ': 'g',
    'ş': 's',
    'ç': 'c',
    'Ə': 'E',
    'Ü': 'U',
    'Ö': 'O',
    'I': 'İ',
    'Ğ': 'G',
    'Ş': 'S',
    'Ç': 'C',
    '?': '',
    ' ': '-',
    '!': '',
    '.': '',
    ',': '',
    ';': '',
    ':': '',
    '*': '',
    '%': '',
    '^': '',
    '&': '',
    '$': '',
    '#': '',
    '@': '',
}

def replace_letter(text):
    for key, value in letter.items():
        text = text.replace(key, value)
    return text

