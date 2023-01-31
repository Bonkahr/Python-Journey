# jabber = open('Jabberwocky.txt', 'r')
# for line in jabber:
#     print(line.strip())  # , end="")
#     # print(len(line))
#
# jabber.close()

# more python-nic way
# with open('Jabberwocky.txt', 'r') as jabbers:
#     # for line in jabbers:
#     #     print(line.strip())
#     lines = jabbers.readlines()
# print(lines)
# print(lines[: 1])
# print(lines[: -1])
#
# # print lines in reverse order
# for line in reversed(lines):
#     print(line, end='')

# l = 'James'
# r_l = ''
# for r in reversed(l):
#     r_l += r
#
# print(r_l)


with open('Jabberwocky.txt', 'r') as jabbered:
    text = jabbered.read()

for char in reversed(text):
    print(char, end="")

