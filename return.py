# def square(number):
#     return number * number


# result = square(3)
# print(result)
# print(square(4))



def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😓"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input("> ")
print(emoji_converter(message))




