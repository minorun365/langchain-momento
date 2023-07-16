# レイテンシー計測開始
import time
time_start = time.time()

# 環境変数のセット
from dotenv import load_dotenv
load_dotenv()

# セッションIDを生成
import uuid
session_id = str(uuid.uuid4())

# 履歴の作成
from langchain.memory import ChatMessageHistory
history = ChatMessageHistory(session_id=session_id)

# メモリーの作成
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(chat_memory=history)

# LLMの作成
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)

# 会話の作成
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
conversation = ConversationChain(llm=llm, verbose=True, memory=memory)

# AIとの会話1
input1 = "私の名前は渡辺直美です。"
conversation.predict(input=input1)

# AIとの会話2
input2 = "私の名前なんだっけ？"
conversation.predict(input=input2)

# 会話履歴を表示
print("【セッションID】")
print(session_id)
print()
print("【AIとの会話履歴】")
print(history.messages)

# レイテンシー計測終了
time_end = time.time()
tim = time_end- time_start

print()
print("【実行にかかった時間】")
print(tim)