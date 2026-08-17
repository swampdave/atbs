# def spam():
#   eggs = "sss"
# spam()
# print(eggs)
from __phello__ import ham
from __phello__.ham import eggs


# def spam():
#     eggs = "SPAMSPAM"
#     bacon()
#     print(eggs) # Prints "SPAMSPAM"
#
# def bacon():
#     ham = "hamham"
#     eggs = "BACONBACON"
#
# spam()

def spam():
    print(eggs) # Prints "GLOBALGLOBAL"
eggs = "GLOBALGLOBAL"
spam()
print(eggs)
