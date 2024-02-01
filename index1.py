import os
from openai import OpenAI

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务

client = OpenAI()

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "讲个笑话",
        }
    ],
    model="gpt-3.5-turbo",
)

print("---------------------11111111111111111111111---------------")
print(response)
print("---------------------22222222222222222222222---------------")
print(response.choices[0].message.content)  # 更具体的的打印

# ---------------------11111111111111111111111---------------
# ChatCompletion(id='chatcmpl-8nTckN514ePfnok1jHtEecZ6did2B', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='好的，下面给你一个笑话：\n\n有一天，一个人突然来到一个岛上，发现岛上有很多猴子。他走到猴子群里，对一只猴子打了个招呼，猴子立刻回应了他。他很惊讶，于是继续对其他猴子打招呼，每只猴子都能回应他。他觉得很好玩，就试着对所有的猴子大声问：“大家好！你们都能听懂人类的话吗？”所有的猴子都点头回应。他更加兴奋了，大声说：“那我们来玩一个游戏吧！我唱一首歌，你们猜猜是什么歌！”猴子们都很乐意参与，于是他开始唱：“泰山黄山美如画，喜马拉雅更锦绣，长江大江跨千山，黄河长河走万里……”  几分钟后，岛上的所有猴子都兴高采烈地跳了起来，欢呼雀跃。那个人十分惊讶，问猴子们：“你们猜对了歌名吗？”猴子们兴奋地摇着头，一个猴子跳上了他的肩膀，指着他的嘴巴说：“你闭嘴，你闭嘴！”', role='assistant', function_call=None, tool_calls=None))], created=1706802638, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=417, prompt_tokens=12, total_tokens=429))
# ---------------------22222222222222222222222---------------
# 好的，下面给你一个笑话：
# 有一天，一个人突然来到一个岛上，发现岛上有很多猴子。他走到猴子群里，对一只猴子打了个招呼，猴子立刻回应了他。他很惊讶，于是继续对其他猴子打招呼，每只猴子都能回应他。他觉得很好玩，就试着对所有的猴子大声问：“大家好！你们都能听懂人类的话吗？”所有的猴子都点头回应。他更加兴奋了，大声说：“那我们来玩一个游戏吧！我唱一首歌，你们猜猜是什么歌！”猴子们都很乐意参与，于是他开始唱：“泰山黄山美如画，喜马拉雅更锦绣，长江大江跨千山，黄河长河走万里……”  几分钟后，岛上的所有猴子都兴高采烈地跳了起来，欢呼雀跃。那个人十分惊讶，问猴子们：“你们猜对了歌名吗？”猴子们兴奋地摇着头，一个猴子跳上了他的肩膀，指着他的嘴巴说：“你闭嘴，你闭嘴！”
