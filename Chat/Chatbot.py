from chatterbot import ChatBot
chatbot = ChatBot('Brandon', trainer='chatterbot.trainers.ListTrainer')
while 1:
    input1 = input()
    if input1 == "1":
        break
    response = chatbot.get_response(input1)
    print(response)




# Check ChatterBotCorpusTrainer documentation 