# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)




#emoji convertor

message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😓"
}
output = ""
for word in words:
    output+= emojis.get(word, word) + ' '
print(output)


