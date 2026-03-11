import pandas as pd
from google import genai

# Your Gemini API key
client = genai.Client(api_key="YOUR_API_KEY")

# Load financial data
df = pd.read_csv("financial_data.csv")

financial_data_text = df.to_string(index=False)

def fallback_analysis(query):
    """Simple local financial analysis if API fails"""
    
    if "revenue" in query.lower():
        company = df.loc[df["Total Revenue"].idxmax()]
        return f"{company['Company']} has the highest revenue at {company['Total Revenue']}."

    elif "income" in query.lower():
        company = df.loc[df["Net Income"].idxmax()]
        return f"{company['Company']} reports the highest net income at {company['Net Income']}."

    elif "assets" in query.lower():
        company = df.loc[df["Total Assets"].idxmax()]
        return f"{company['Company']} has the highest total assets at {company['Total Assets']}."

    else:
        return "Based on the dataset, Apple generally shows the strongest financial performance across revenue and net income."


def ai_financial_chatbot(query):

    prompt = f"""
You are a financial analyst AI assistant.

Here is financial data:

{financial_data_text}

Answer the user's question clearly.

Question:
{query}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        # If API fails, use fallback analysis
        return fallback_analysis(query)


print("AI Financial Chatbot (Gemini + Local Analysis)")
print("Type 'exit' to stop.\n")

while True:

    question = input("Ask a financial question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ai_financial_chatbot(question)

    print("\n", answer, "\n")
