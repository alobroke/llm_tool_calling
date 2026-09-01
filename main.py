import json

from llm import call_llm
from tools import tools




tool_definitions = []

for tool in tools:
    tool_definitions.append({
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.args_schema.model_json_schema()
        }
    })




tool_map = {
    tool.name: tool
    for tool in tools
}




def main():

    
    print(" Tool calling .......")
    

    user_query = input("\nWhat are you thinking: ")

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful AI assistant.

You have access to tools:
- web_search: Search the web for information.
- email_tool: Create an email draft.
- create_visualization: Create charts from data.
- grep: Find text in files.

Use a tool when it is necessary to answer the user's request.
"""
        },
        {
            "role": "user",
            "content": user_query
        }
    ]

 

    print("\n🤖 Qwen is thinking...")

    response = call_llm(
        messages,
        tools=tool_definitions
    )

   

    if not response.tool_calls:

        print("\nQwen:", response.content)
        return

   
    messages.append(response)

    for tool_call in response.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print(f"\n🔧 Tool selected: {tool_name}")
        print(f"📦 Arguments: {arguments}")

        if tool_name not in tool_map:
            print("❌ Unknown tool")
            return

        tool = tool_map[tool_name]

        result = tool.invoke(arguments)

        print(f"📥 Tool result: {result}")

      

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_name,
            "content": str(result)
        })

   

    final_response = call_llm(messages)

    print("\n🤖 Qwen:")
    print(final_response.content)


if __name__ == "__main__":
    main()
