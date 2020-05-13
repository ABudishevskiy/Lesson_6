# Дан текст - найти все заглавные буквы и объединить их в слово.
#
# 'Help ELephant learn LOops. While's and fOrs. RLD!'

a = "Help ELephant learn LOops. While's and fOrs. RLD!"
b = ''
for i in a:
    if i.isupper():
        b = b + i
print(b)
