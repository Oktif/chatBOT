# chatBOT
This is overview of this project.
## Goal
Goal of this project is to create bilingual chatbot, which will be capable of having a conversation about hobbys of project members.
Since our team consist of one member, it doesnt need to know broad range of topics (or to be more precise, in given timeframe it's impossible to
implement it better, because our sole member lacks experience and skills.

Team members:
Oktawian Filipkowski

##
Complete bot resides in naibot.ipynb file, there is also video presentation bot.mp4

## Covered topics:
This chatbot is semi-capable of discussion about few topics:
- animals
- manga
- vegetables
- music
- games

## Principles of operation

Our one-member team tried to implement this chat-bot in a interesting way.

It will try to converse with user using two methods.
First it will try to use cosine similarity to match question with contents of wiki article.
If coefficiency will be sufficient, it will use selected sentence.
If its doesnt find anything similar, it will use its pre-trained model to match answer with a question.

Since model need to be bilingual, user can decide if he wants to communicate using eng or pl language.
This was implemented using using translate library. This solution is far from perfect, and after finishing this project i see that training two models in two languages
would be better idea.
Unfortunetly, after some tests translate library works very wonky, and is buggy with longer sentences. Programming team tried to fix this using some roundabout methods.

More information will be made avalible in presentation.



sidenote:
I started working in main.py but for some reason i was unable to install Tensorflow on my pc, thats why i moved to google collab.
Since creating imports etc. is not as intuitive on collab i ditched that file, so its obsolete.
It contains early trial version of bot.
I will try to make full version later, when i manage to fix my pc.
