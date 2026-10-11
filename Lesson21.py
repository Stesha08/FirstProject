# Дан словарь stock = {'apples': 50, 'bananas': 20, 'oranges': 15}.
# Приехала поставка: добавьте к яблокам ещё 30 штук. Бананы раскупили — удалите ключ 'bananas'.
# Добавьте новый товар 'kiwi' в количестве 10 штук. Выведите итоговый словарь.
stock ={
'apples': 50, 
'bananas': 20,
'oranges': 15
}
stock["apples"] += 30
if"bananas" in stock:
    del stock['bananas']
stock['kiwi']= 10
for key,value in stock.items():
    print(f"{key}:{value}")

# Дан словарь scores={'Math': 95, 'English': 82, 'Code': 100}.
# Выведите все предметы и их баллы через .items(). Найдите и выведите максимальный балл.
# scores={'Math': 95, 'English': 82, 'Code': 100}
# for key,value in scores.items():
#     print(f"{key}:{value}")
# max_t=max(scores.values())
# print(max_t)

# #вариант2
# scores={'Math': 95, 'English': 82, 'Code': 100}
# max_scores=0
# for key,value in scores.items():
#     print(f"{key}:{value}")
#     if value>max_scores:
#         max_scores=value

# print(f'максимальный балл:{max_scores}')     if "cat" in words:print(f"{words}")

# words={"apple":"яблоко","book":"книга","cat":"кот"}
# if "cat" in words:
#     print(words.get("кот"))
# for value in words.values():
#     print(value)
# words["dog"]="собака"
# words["mouse"]="мышь"
# print(words)
# english_words=["apple","book","cat","dog","mouse"]
# print (len(english_words))
# print(english_words)

# shop={
# 'apple': 50,
# 'banana': 30,
# 'cherry': 80
# }
# shops=shop
# for key in shops:
#     shops[key]-=5
# print(shops)