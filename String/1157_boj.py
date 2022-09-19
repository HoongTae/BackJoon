word = input().upper()
unique_word = list(set(word))

word_cnt = []
for uw in unique_word:
    word_cnt.append(word.count(uw))

if word_cnt.count(max(word_cnt)) > 1:
    print("?")
else:
    print(unique_word[word_cnt.index(max(word_cnt))])


# word = input().upper()
# word_list = list(set(word))
#
# cnt = []
# for i in word_list:
#     count = word.count
#     cnt.append(count(i))
#
# if cnt.count(max(cnt)) > 1:
#     print("?")
# else:
#     print(word_list[(cnt.index(max(cnt)))])
#