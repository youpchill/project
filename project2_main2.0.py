import string
alphabet = string.ascii_lowercase
alphabet1 = string.ascii_uppercase
russian_alphabet_lowercase = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                              'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


russian_alphabet_uppercase = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                              'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


a = input()
def d(s2):
    a_new = ''
    for i in range(0, len(a)):
        if a[i].isalpha():
            if a[i].isupper():
                if a[i] in alphabet1:
                    b = alphabet1.index(a[i])
                    c = 25 - b
                    e = alphabet1[c]
                    a_new += e
                else:
                    b = russian_alphabet_uppercase.index(a[i])
                    c = 25 - b
                    e = russian_alphabet_uppercase[c]
                    a_new += e
            else:
                if a[i] in alphabet:
                    b = alphabet.index(a[i])
                    c = 25 - b
                    e = alphabet[c]
                    a_new += e
                else:
                    b = russian_alphabet_lowercase.index(a[i])
                    c = 25 - b
                    e = russian_alphabet_lowercase[c]
                    a_new += e
        else:
            a_new += a[i]
    return a_new


j = input()
o = d(j)
print(o)


# def a1z26(s1):
#     s_new = ''
#     for i in range(0, len(s1)):
#         if s1[i].isalpha():
#             if s1[i].isupper():
#                 if s1[i] in alphabet1:
#                     b = alphabet1.index(s1[i])
#                     b += 1
#                     s_new += str(b)
#                     if i + 1 != len(s1) and s1[i + 1].isalpha():
#                         s_new += '-'
#                 else:
#                     b = russian_alphabet_uppercase.index(s1[i])
#                     b += 1
#                     s_new += str(b)
#                     if i + 1 != len(s1) and s1[i + 1].isalpha():
#                         s_new += '-'
#
#             else:
#                 if s1[i] in alphabet:
#                     b = alphabet.index(s1[i])
#                     b += 1
#                     s_new += str(b)
#                     if i + 1 != len(s1) and s1[i + 1].isalpha():
#                         s_new += '-'
#                 else:
#                     b = russian_alphabet_lowercase.index(s1[i])
#                     b += 1
#                     s_new += str(b)
#                     if i + 1 != len(s1) and s1[i + 1].isalpha():
#                         s_new += '-'
#         else:
#             s_new += s1[i]
#     return s_new
