
list = ["Aashish", "Rahul", "   Vatsal   ", "   Anup    ", "Akash"]
def rem_words(n):
    list.remove(n)
    # b = l.strip() for l in list
    return list

n = input("Enter the word: ")
a = rem_words(n)
print(a)
print(list.strip())





# # Another way to do this problem
# def rem(l, word):
#     n = []
#     for item in l:
#         n.append(item.strip(word))
#     return n

# l = ["Aashish", "Rahul", "   Vatsal   ", "   Anup    ", "Akash"]
# print(rem(l, "sh"))