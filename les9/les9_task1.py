'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
>>> func("papa")
6
>>> func("sova")
9
'''
import hashlib

# сравнение двух строк, функция с вебинара
def is_eq_str(a: str, b: str) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    return ha == hb

# сравнение строки и подстроки, функция с вебинара
def Rabin_Karp(s: str, subs: str) -> bool:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока длиннее строки'
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i

    return -1
# подсчет количества подстрок в строке
def get_substrings_count(s):
    subs_lst = []
    for i_beg in range(len(s)):
        for i_end in range(i_beg, len(s)):
            # проверка длины подстроки, чтобы не учитывать всю строку целиком
            if len(s[i_beg:i_end + 1]) < len(s):
                if Rabin_Karp(s, s[i_beg:i_end + 1]) >= 0 and s[i_beg:i_end + 1] not in subs_lst:
                    subs_lst.append(s[i_beg:i_end + 1])
    return subs_lst

if __name__ == "__main__":
    while True:
        s = input('Введите строку: ')
        if len(s) == 0:
            print('Строка не может быть пустой!')
            continue
        subs_lst = get_substrings_count(s)
        print(f'Количество подстрок: {len(subs_lst)}')
        print(f'Значения подстрок:{subs_lst}')
        break