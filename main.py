from termo_bot import TermoBot

words_file = open("fwords.txt", "r", encoding="utf8")
bot = TermoBot(words_file)

bot.add_contains('o')
bot.add_contains('s')
# bot.add_contains('a')
# bot.add_contains('g')

#bot.add_no_contains('c')
#bot.add_no_contains('a')

bot.add_contains_exact('o', 4)
bot.add_contains_exact('s', 4)
# bot.add_contains_exact('s', 0)
# bot.add_contains_exact('u', 1)

bot.add_no_contains_exact('c', 0)
bot.add_no_contains_exact('o', 1)
bot.add_no_contains_exact('r', 2)
bot.add_no_contains_exact('a', 3)

bot.add_no_contains_exact('r', 0)
bot.add_no_contains_exact('a', 1)
bot.add_no_contains_exact('t', 2)
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
