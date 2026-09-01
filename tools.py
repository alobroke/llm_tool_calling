from langchain_core.tools import tool
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from tavily import TavilyClient


tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """
    Search the web for current information.
    Use this for recent news, current events,
    or information that may have changed.
    """

    try:
        response = tavily.search(
            query=query,
            max_results=5
        )

        results = []

        for result in response["results"]:
            results.append(
                f"Title: {result['title']}\n"
                f"Content: {result['content']}\n"
                f"URL: {result['url']}"
            )

        return "\n\n".join(results)

    except Exception as e:
        return f"Search failed: {str(e)}"



@tool
def email_tool(to: str, subject: str, body: str) -> str:
    """
    Create an email draft.
    This prototype does not actually send the email.
    """

    email = f"""
TO: {to}

SUBJECT: {subject}

BODY:
{body}
"""

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/email_draft.txt", "w", encoding="utf-8") as f:
        f.write(email)

    return f"Email draft created successfully for {to}."




@tool
def create_visualization(
    data: str,
    chart_type: str = "bar"
) -> str:
    """
    Create a visualization from simple CSV-style data.

    Example data:
    Month,Sales
    Jan,100
    Feb,150
    Mar,200

    Supported chart types: bar, line
    """

    try:
        from io import StringIO

        df = pd.read_csv(StringIO(data))

        os.makedirs("outputs/charts", exist_ok=True)

        x_column = df.columns[0]
        y_column = df.columns[1]

        plt.figure(figsize=(8, 5))

        if chart_type.lower() == "line":
            plt.plot(df[x_column], df[y_column], marker="o")
        else:
            plt.bar(df[x_column], df[y_column])

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{chart_type.title()} Chart")

        file_path = "outputs/charts/chart.png"

        plt.savefig(file_path)
        plt.close()

        return f"Chart created successfully: {file_path}"

    except Exception as e:
        return f"Visualization failed: {str(e)}"






tools = [
    web_search,
    email_tool,
    create_visualization
]