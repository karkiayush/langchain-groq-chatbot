from app.agent.service import AgentService
from app.tool.web_search import create_web_search_tool
from app.llm.groq_client import get_groq_llm
from app.util.logger import setup_logger


def main():
    setup_logger()

    llm = get_groq_llm()
    search_tool = create_web_search_tool()

    agent = AgentService(llm=llm, tools=[search_tool])

    print("\n===== Groq AI Agent =====")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Goodbye 👋")
            break

        if not user_message:
            continue

        response = agent.generate_response(user_message=user_message)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
