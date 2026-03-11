import pandas as pd

# Load financial dataset
df = pd.read_csv("financial_data.csv")

def financial_chatbot(query):
    query = query.lower()

    # Revenue questions
    if "revenue" in query:
        if "lowest" in query:
            company = df.loc[df["Total Revenue"].idxmin()]
            return f"{company['Company']} has the lowest revenue at {company['Total Revenue']} million USD."
        else:
            company = df.loc[df["Total Revenue"].idxmax()]
            return f"{company['Company']} has the highest revenue at {company['Total Revenue']} million USD."

    # Net income questions
    elif "net income" in query or "income" in query:
        if "lowest" in query:
            company = df.loc[df["Net Income"].idxmin()]
            return f"{company['Company']} has the lowest net income at {company['Net Income']} million USD."
        else:
            company = df.loc[df["Net Income"].idxmax()]
            return f"{company['Company']} has the highest net income at {company['Net Income']} million USD."

    # Assets questions
    elif "assets" in query:
        if "lowest" in query:
            company = df.loc[df["Total Assets"].idxmin()]
            return f"{company['Company']} has the lowest total assets at {company['Total Assets']} million USD."
        else:
            company = df.loc[df["Total Assets"].idxmax()]
            return f"{company['Company']} holds the highest total assets at {company['Total Assets']} million USD."

    # Liabilities questions
    elif "liabilities" in query:
        if "lowest" in query:
            company = df.loc[df["Total Liabilities"].idxmin()]
            return f"{company['Company']} has the lowest liabilities at {company['Total Liabilities']} million USD."
        else:
            company = df.loc[df["Total Liabilities"].idxmax()]
            return f"{company['Company']} has the highest liabilities at {company['Total Liabilities']} million USD."

    # Cash flow questions
    elif "cash flow" in query:
        if "lowest" in query:
            company = df.loc[df["Operating Cash Flow"].idxmin()]
            return f"{company['Company']} has the lowest operating cash flow at {company['Operating Cash Flow']} million USD."
        else:
            company = df.loc[df["Operating Cash Flow"].idxmax()]
            return f"{company['Company']} generates the highest operating cash flow at {company['Operating Cash Flow']} million USD."

    # Help command
    elif "help" in query:
        return (
            "You can ask questions like:\n"
            "- Who has the highest revenue?\n"
            "- Who has the lowest revenue?\n"
            "- Which company has the highest net income?\n"
            "- Who has the lowest net income?\n"
            "- Which company has the highest assets?\n"
            "- Who has the lowest liabilities?\n"
            "- Which company has the highest cash flow?"
        )

    # Unknown question
    else:
        return "Sorry, I can answer questions about revenue, net income, assets, liabilities, or cash flow. Type 'help' for example questions."


# Chat loop
print("Financial Chatbot for Microsoft, Apple, and Tesla")
print("Ask questions about revenue, income, assets, liabilities, or cash flow.")
print("Type 'help' to see example questions.")
print("Type 'exit' to stop.\n")

while True:
    question = input("Ask a financial question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = financial_chatbot(question)
    print(answer)