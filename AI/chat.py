import os

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq


def main():
    """
    This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction.
    """

    # Get Groq API key
    groq_api_key = os.environ['GROQ_API_KEY']
    model = 'llama3-8b-8192'
    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
    )
    
    # Define the bot's name, personality, and background
    bot_name = "小傑"
    bot_personality = "體貼善良的"
    bot_background = "目前就讀金門大學資訊工程三年級，精通C、C++、資料庫、Python、JavaScript和網頁設計"

    print(f"哈囉！我是 {bot_name}，{bot_personality}聊天機器人。我 {bot_background}。很高興能幫助你！讓我們開始我們的對話吧！")

    system_prompt = f'你遇到問題時，我會 {bot_personality} 幫助你'
    conversational_memory_length = 5 # 對話中聊天機器人將記住的前幾個消息數量

    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    while True:
        user_question = input("你有什麼問題想問我嗎？ ")

        # 如果用戶提出了問題，
        if user_question:

            # 使用各種組件構建聊天提示模板
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(
                        content=system_prompt
                    ),  # 這是始終包含在對話開始處的系統提示。

                    MessagesPlaceholder(
                        variable_name="chat_history"
                    ),  # 這個占位符將在對話期間用實際聊天記錄替換。它有助於保持上下文。

                    HumanMessagePromptTemplate.from_template(
                        "{human_input}"
                    ),  # 這個模板是用戶當前輸入將注入到提示中的地方。
                ]
            )

            # 使用 LangChain LLM (Language Learning Model) 創建一個對話鏈
            conversation = LLMChain(
                llm=groq_chat,  # 先前初始化的 Groq LangChain 聊天物件。
                prompt=prompt,  # 構建的提示模板。
                verbose=False,   # TRUE 啟用詳細輸出，這對於調試很有用。
                memory=memory,  # 存儲和管理對話記憶的對話記憶物件。
            )
            # 通過將完整提示發送到 Groq API 來生成聊天機器人的回答。
            response = conversation.predict(human_input=user_question)
            print(f"{bot_name}:", response)

if __name__ == "__main__":
    main()
