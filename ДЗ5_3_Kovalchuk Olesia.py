import requests
import timeit

def read_text_from_google_drive(link):
    file_id = link.split("/")[-2]
    export_link = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(export_link)
    return response.text

def boyer_moore_search(text, pattern):

    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            i += m - min(j, 1 + last_occurrence.get(text[i], -1))
            j = m - 1

    return -1

def knuth_morris_pratt_search(text, pattern):

    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    prefix_function = [0] * m

    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_function[i] = j

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - j
            i += 1
            j += 1
        else:
            if j > 0:
                j = prefix_function[j - 1]
            else:
                i += 1

    return -1

def rabin_karp_search(text, pattern):

    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    prime = 101
    pattern_hash = sum(ord(pattern[i]) * (prime ** (m - 1 - i)) for i in range(m))
    text_hash = sum(ord(text[i]) * (prime ** (m - 1 - i)) for i in range(m))

    for i in range(n - m + 1):
        if pattern_hash == text_hash and pattern == text[i:i+m]:
            return i

        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * (prime ** (m - 1))) * prime + ord(text[i + m])

    return -1

text1_link = "https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing"
text2_link = "https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing"

text1 = read_text_from_google_drive(text1_link)
text2 = read_text_from_google_drive(text2_link)

substring_existing = "проблем"
substring_non_existing = "Olesia"

time_Boyer_Moore_text1 = timeit.timeit(lambda: boyer_moore_search(text1, substring_existing), number=10000)
time_Boyer_Moore_text2 = timeit.timeit(lambda: boyer_moore_search(text2, substring_existing), number=10000)

# Вимірювання часу виконання для Knuth-Morris-Pratt
time_KMP_text1 = timeit.timeit(lambda: knuth_morris_pratt_search(text1, substring_existing), number=10000)
time_KMP_text2 = timeit.timeit(lambda: knuth_morris_pratt_search(text2, substring_existing), number=10000)

# Вимірювання часу виконання для Rabin-Karp
time_Rabin_Karp_text1 = timeit.timeit(lambda: rabin_karp_search(text1, substring_existing), number=10000)
time_Rabin_Karp_text2 = timeit.timeit(lambda: rabin_karp_search(text2, substring_existing), number=10000)

print("Час Boyer-Moore (Текст 1):", time_Boyer_Moore_text1)
print("Час Boyer-Moore (Текст 2):", time_Boyer_Moore_text2)

print("Час Knuth-Morris-Pratt (Текст 1):", time_KMP_text1)
print("Час Knuth-Morris-Pratt (Текст 2):", time_KMP_text2)

print("Час Rabin-Karp (Текст 1):", time_Rabin_Karp_text1)
print("Час Rabin-Karp (Текст 2):", time_Rabin_Karp_text2)
