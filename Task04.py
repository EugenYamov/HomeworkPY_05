#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_zip(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_unzip(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += (char * int(count))
            count = ''
    return decode

data = 'AAAAABBBBBHHHHHdddddaaaasssqqqwwEE'
print(' Входные данные:','\n',data,'\n')

zip = rle_zip(data)
print(' Кодированные данные:','\n',zip,'\n')

unzip = rle_unzip(str(zip))
print(' Декодированные данные:','\n',unzip)