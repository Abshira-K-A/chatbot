print("hello ! , I 'm pyBot")

while True:
    user_input = input("you : ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot : Hello, How can i assist you?")
        
    elif user_input == "how are you?":
        print("Bot : I am fine, What about you? Tell me how can i assist you?")
        
    elif user_input == "what can you do?":
        print("Bot : I can assist you with answering some basic questions.")
        
    elif user_input == "what is your name?":
        print("Bot : my name is pyBot , I am version 2.0")
        
    elif user_input == "bye" or  user_input == "exit":
        print("Bot: Bye, Have a good day ")
    break

else:
    print("Bot : I am sorry , I didnt understand that....")
        
