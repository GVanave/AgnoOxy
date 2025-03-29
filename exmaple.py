import ollama
from mem0 import Memory
import os
from dotenv import load_dotenv
import streamlit as st


import os
import shutil

try:
    shutil.rmtree('C:/Users/ganes/OneDrive/Desktop/Machine Vision')
except FileNotFoundError:
    print("Directory or file not found. Skipping deletion.")

load_dotenv()

memory = Memory()

st.title("Add the Information About the Memory")

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    relevant_memories = memory.search(query=message, user_id=user_id, limit=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])

    st.write(f"The memory string is:\n{memories_str}")

    system_prompt = (
        "You are a helpful AI. Answer the question based on the query and memories.\n"
        f"User Memories:\n{memories_str}"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]

    response = ollama.chat(model='llama3.2:1b', messages=messages)

    assistant_response = response['message']['content']

    st.write(f"Response from LLM:\n{assistant_response}")

    messages.append({"role": "assistant", "content": assistant_response})
    memory.add(messages, user_id=user_id)
    
    st.write(f"New Memory Added:\n{messages}")

    return assistant_response



def console_main():
    print("Chat with AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"AI: {chat_with_memories(user_input)}")

if __name__ == "__main__":
    
        console_main()





