from termo_bot import TermoBot

words_file = open("fwords.txt", "r", encoding="utf8")
bot = TermoBot(words_file)

bot.add_contains('o')
bot.add_contains('s')
bot.add_contains('a')
bot.add_contains('g')

bot.add_no_contains('c')
bot.add_no_contains('i')
bot.add_no_contains('m')
bot.add_no_contains('b')

bot.add_contains_exact('o', 4)
bot.add_contains_exact('s', 5)
bot.add_contains_exact('a', 2)

bot.add_no_contains_exact('a', 1)
bot.add_no_contains_exact('d', 1)
bot.add_no_contains_exact('d', 3)
bot.add_no_contains_exact('c', 1)
bot.add_no_contains_exact('i', 3)
bot.add_no_contains_exact('g', 1)

print("processando...")
print(bot.find())
print("finish")
