from wiki_helper import *

while True:
    print('Im simple bot, and can only talk about selected topics.'
          'What you want to talk about?'
          'type "quit" to end conversation')
    category = input('chose either animals or vegetables').lower()
    if category == 'animals':
            while True:
                print(f'{category} chosen, if you want to change category, type "category"')
                talking = input(f'What {category} interests you?').lower()
                if talking == 'category':
                    break
                else:
                    while True:
                        question = input(f'You want to ask about {talking}? (If not type "question" to change it)').lower()
                        if question == 'question':
                            break
                        else:
                            page = (category + ' ' + talking)
                            try:
                                p = wikipedia.page(page)
                            except wikipedia.DisambiguationError as e:
                                random = random.choice(e.options)
                                page = random
                            text = wikipedia.page(page).content
                            while True:
                                question2 = input('Ask away!, if you want to change topic, type "topic"\n')
                                output = process(text, question2)
                                if output:
                                    print(output)
                                elif question2 == 'topic':
                                    break
                                else:
                                    print("I don't know.")

    elif category == 'polski':
        while True:
            print(f'{category} chosen, if you want to change category, type "category"')
            talking = input(f'What {category} interests you?').lower()
            if talking == 'category':
                break
            else:
                while True:
                    question = input(f'You want to ask about {talking}? (If not type "question" to change it)').lower()
                    if question == 'question':
                        break
                    else:
                        page = (category + ' ' + talking)
                        try:
                            p = wikipedia.page(page)
                        except wikipedia.DisambiguationError as e:
                            random = random.choice(e.options)
                            page = random
                        wikipedia.set_lang("pl") # to set polish
                        text = wikipedia.page(page).content
                        while True:
                            question2 = input('Ask away!, if you want to change topic, type "topic"\n')
                            output = process(text, question2)
                            if output:
                                print(output)
                            elif question2 == 'topic':
                                break
                            else:
                                print("I don't know.")

    elif category == 'cats':
        print("cats")

    elif category == 'dogs':
        print("cats")

    elif category == 'pigeons':
        print("cats")

    elif category == 'quit':
        print("bye!")
        break

    else:
        print("wrong choice!")




















# while True:
#     print("Im simple bot, and can only talk about selected topics."
#           "What you want to talk about?")
#     category = input("chose either animals or vegetables")
#     if category == "animals":
#         print("Animals chosen, if you want to change topic, type : change")
#         talking = input(f"What about {category} interests you?")
#         if talking == 'change':
#             pass
#         else:
#             question = input(f"What about {talking} you want to ask? (to change type change)")
#             if question != "change" or "pass":
#                 while question != "change":
#                     page = (category+' '+talking)
#                     print(wikipedia.summary(page))
#                     question = input(f"What about {talking} you want to ask? (to change type pass)")
#             elif question == "pass":
#                 break
#     elif category == "vegetables":
#         print("vegetables chosen")
#     else:
#         print("wrong choice")







# def topic():
#     import random
#     page = input("What topic you want to talk about?")
#     try:
#         p = wikipedia.page(page)
#     except wikipedia.DisambiguationError as e:
#         random = random.choice(e.options)
#         page = random
#     print("chosen: ", page)
#     text = wikipedia.page(page).content
#     return text
#
# def discussion():
#     while True:
#       question = input("Hi, what do you want to know?\n")
#       output = process(text, question)
#       if output:
#         print(output)
#       elif question=='quit':
#         break
#       else:
#         print("I don't know.")












# while True:
#     print("Im simple bot, and can only talk about selected topics."
#           "What you want to talk about?")
#     category = input("chose either animals or vegetables")
#     if category == "animals":
#             while True:
#                 print(f"{category}chosen, if you want to change category, type : change")
#                 talking = input(f"What about {category} interests you?")
#                 if talking == 'change':
#                     break
#                 else:
#                     while True:
#                         question = input(f"What about {talking} you want to ask? (to change topic talking)")
#                         if question == "talking":
#                             break
#                         else:
#                             page = (category + ' ' + talking)
#                             print(wikipedia.summary(page))
#
#     elif category == "vegetables":
#         print("vegetables chosen")
#     else:
#         print("wrong choice")




# page = input("What topic you want to talk about?")
# try:
#     p = wikipedia.page(page)
# except wikipedia.DisambiguationError as e:
#     random = random.choice(e.options)
#     page = random
# #print("chosen: ", page)
# text = wikipedia.page(page).content

# while True:
#   question = input("Hi, what do you want to know?\n")
#   output = process(text, question)
#   if output:
#     print(output)
#   elif question=='quit':
#     break
#   else:
#     print("I don't know.")
