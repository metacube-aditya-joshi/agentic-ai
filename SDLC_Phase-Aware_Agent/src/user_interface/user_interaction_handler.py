from llm_setup.openai_client import ask_question

def ai_menu():
    print("Hello user what is your question today !!\n")
    user_input =None
    while(user_input!="No" or user_input!="no" or user_input!="n" or user_input !="N"):
        user_input = input()
        print("\n", ask_question(user_input))
        print("Any other questions!!\n type yes or no ")
        user_input = input()
