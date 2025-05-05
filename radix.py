def char_at(string, d):
    if len(string) <= d:
        return 256  
    return ord(string[d])

def MSD_sort(string_list, lo, hi, d):
    if hi <= lo or d >= len(string_list[0]):
        return

    count = [0] * 258
    temp = [None] * (hi - lo + 1)

    for i in range(lo, hi + 1):
        c = char_at(string_list[i], d) + 1
        count[c] += 1

    for r in range(257):
        count[r + 1] += count[r]

    for i in range(lo, hi + 1):
        c = char_at(string_list[i], d) + 1
        temp[count[c - 1]] = string_list[i]
        count[c - 1] += 1

    for i in range(lo, hi + 1):
        string_list[i] = temp[i - lo]

    for r in range(257):
        MSD_sort(string_list, lo + count[r - 1], lo + count[r] - 1, d + 1)

def count_words(string_list):
    word_count = {}
    for word in string_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def print_word_count(word_count, output_file):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[0].lower())
    for word, count in sorted_word_count:
        output_file.write(f"{word}: {count}\n")

def generate_ranking(word_count, output_file, top_n=2000):
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(top_n, len(sorted_word_count))):
        word, count = sorted_word_count[i]
        output_file.write(f"{word}: {count}\n")

if __name__ == '__main__':
    chunk_size = 1000
    
    string_list_frankenstein = []
    with open('Frankestein.txt', 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            string_list_frankenstein.extend(chunk.split())

    n_frankenstein = len(string_list_frankenstein)
    MSD_sort(string_list_frankenstein, 0, n_frankenstein - 1, 0)

    with open('frankenstein_sorted.txt', 'w', encoding='utf-8') as file:
        for word in string_list_frankenstein:
            file.write(f"{word}\n")

    word_count_frankenstein = count_words(string_list_frankenstein)

    with open('frankenstein_counted.txt', 'w', encoding='utf-8') as file:
        print_word_count(word_count_frankenstein, file)

    with open('frankenstein_ranked.txt', 'w', encoding='utf-8') as file:
        generate_ranking(word_count_frankenstein, file, top_n=2000)

    string_list_war_and_peace = []
    with open('War_and_Peace.txt', 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            string_list_war_and_peace.extend(chunk.split())

    n_war_and_peace = len(string_list_war_and_peace)
    MSD_sort(string_list_war_and_peace, 0, n_war_and_peace - 1, 0)

    with open('war_and_peace_sorted.txt', 'w', encoding='utf-8') as file:
        for word in string_list_war_and_peace:
            file.write(f"{word}\n")

    word_count_war_and_peace = count_words(string_list_war_and_peace)

    with open('war_and_peace_counted.txt', 'w', encoding='utf-8') as file:
        print_word_count(word_count_war_and_peace, file)

    with open('war_and_peace_ranked.txt', 'w', encoding='utf-8') as file:
        generate_ranking(word_count_war_and_peace, file, top_n=2000)
