# レイテンシー計測開始
import time
time_start = time.time()

# 環境変数のセット
from dotenv import load_dotenv
load_dotenv()

# AIへの質問文をセット
input = "KDDIアジャイル開発センター株式会社について教えて？"

# LangChainのLLMを呼び出し
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
output = llm.predict(input)

# AIからの回答を表示
print("【AIからの回答】")
print(output)

# レイテンシー計測終了
time_end = time.time()
tim = time_end- time_start

print()
print("【実行にかかった時間】")
print(tim)