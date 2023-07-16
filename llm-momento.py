# レイテンシー計測開始
import time
time_start = time.time()

# 環境変数のセット
from dotenv import load_dotenv
load_dotenv()

# Momentoキャッシュの有効化
from datetime import timedelta

import langchain
from langchain.cache import MomentoCache
from momento import CacheClient, Configurations, CredentialProvider

cache_client = CacheClient(
    Configurations.Laptop.v1(),
    CredentialProvider.from_environment_variable("MOMENTO_AUTH_TOKEN"),
    default_ttl=timedelta(days=1))

cache_name = "langchain-llm"
langchain.llm_cache = MomentoCache(cache_client, cache_name)

# AIへの質問文をセット
input = "KDDIアジャイル開発センター株式会社について教えて？"

# LangChainのLLMを呼び出し
from langchain.llms import OpenAI

llm = OpenAI(temperature=1)
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