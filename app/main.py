from app.chatbot.service import ChatbotService
from app.llm.groq_client import get_groq_llm


def main():
    llm = get_groq_llm()
    chatbot_service = ChatbotService(llm=llm)

    print("\n===== LangChain Groq Chatbot =====")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Goodbye 👋")
            break

        if not user_message:
            continue

        response = chatbot_service.generate_response(user_message=user_message)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
