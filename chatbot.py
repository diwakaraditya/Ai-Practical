from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot(
    "AI Assistant",
    read_only=True,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {'import_path': 'chatterbot.logic.MathematicalEvaluation'},
        {'import_path': 'chatterbot.logic.BestMatch'}
    ]
)

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # General conversation
trainer.train("chatterbot.corpus.english.greetings")  # Optional: greetings
trainer.train("chatterbot.corpus.english.conversations")  # Optional: dialogues

# Chat function
def chat():
    print("Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Bot:", response)

# Run chatbot
if __name__ == "__main__":
    chat()
