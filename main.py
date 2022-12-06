from termo_bot import TermoBot

words_file = open("fwords.txt", "r", encoding="utf8")
bot = TermoBot(words_file)

bot.add_contains('o')
# bot.add_contains('s')
# bot.add_contains('a')
# bot.add_contains('g')

bot.add_no_contains('c')
bot.add_no_contains('r')
bot.add_no_contains('a')

bot.add_no_contains('f')
bot.add_no_contains('e')
bot.add_no_contains('t')

bot.add_no_contains('p')
bot.add_no_contains('i')
bot.add_no_contains('n')

bot.add_no_contains('l')
bot.add_no_contains('x')

bot.add_contains_exact('s', 4)
bot.add_contains_exact('o', 3)
bot.add_contains_exact('u', 1)
# bot.add_contains_exact('u', 1)

bot.add_no_contains_exact('o', 1)
# bot.add_no_contains_exact('o', 1)
# bot.add_no_contains_exact('r', 2)
# bot.add_no_contains_exact('a', 3)

# bot.add_no_contains_exact('r', 0)
# bot.add_no_contains_exact('a', 1)
# bot.add_no_contains_exact('t', 2)
# bot.add_no_contains_exact('o', 4)

# bot.add_no_contains_exact('r', 0)
# bot.add_no_contains_exact('e', 1)
# bot.add_no_contains_exact('m', 2)

# bot.add_no_contains_exact('i', 1)
# bot.add_no_contains_exact('t', 2)

# bot.add_no_contains_exact('l', 0)


print("processando...")
print(bot.find())
print(bot.get_words_sugestion())
print("finish")
