import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import wikipedia

# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

def process(text, question):
  sentence_tokens = nltk.sent_tokenize(text)
  sentence_tokens.append(question)

  tv = TfidfVectorizer(tokenizer=lemma_me)
  tf = tv.fit_transform(sentence_tokens)
  values = cosine_similarity(tf[-1], tf)
  index = values.argsort()[0][-2]
  values_flat = values.flatten()
  values_flat.sort()
  coeff = values_flat[-2]
  if coeff > 0.2:
    return sentence_tokens[index]


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

    elif category == 'vegetables':
        print("vegetables chosen")

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
