from agent import run_agent

def main():
    print("Welcome to HR Bot!")
    print("Type your HR-related query or 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = run_agent(user_input)
            print(f"HR Bot: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
