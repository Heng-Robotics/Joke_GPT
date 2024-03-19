#coding=utf-8
import openai
import pandas as pd

# 设置你的OpenAI GPT API密钥
openai.api_key = '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'

# 读取包含笑话的CSV文件
input_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/jokes_1801_2100.csv'
output_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/output_1801_2100.csv'

# 从CSV文件中读取笑话到数组
df = pd.read_csv(input_csv_path)
jokes = df['joke'].tolist()

# 进行幽默类型的分类并保存结果到新的CSV文件
results = []
count = 0
for joke in jokes:
    # 使用OpenAI GPT API进行分类
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "Hello, GPT! Your expertise now extends to humor classification. You need to classify the types of humor in the following jokes. The four types of humor described here are Affiliative, Aggressive, Self-enhancing, and Self-defeating. Affiliative Humor emphasizes  good-natured attitude toward life, having the ability to laugh at yourself, your circumstances and the idiosyncrasies of life in constructive, non-detrimental manner, enhancing relationships in a light and positive manner. It is the most common type of humor. Sometimes when you are unsure of the humor type of a joke, you can categorize it as Affiliative type. For example, 'A recent study has found that women who carry a little extra weight live longer than the men who mention it.'. Aggressive humor relies on criticism, mockery, and sarcasm to create humor, often through making fun of others. For example,  'If you think people are laughing at you, they probably are'. Self-Enhancing Humor is associated with a positive mindset and coping mechanisms, using self-deprecation and a positive attitude to boost self-esteem. For example, 'Even when I'm by myself, I'm often amused by the absurdities of life.'.  Self-defeating humor often involves self-deprecation and self-sacrifice, humorously highlighting one's weaknesses or foolish behaviors. For example, 'I often try to make people like or accept me more by saying something funny about my own weaknesses, blunders, or faults'. Now you know what the four humor styles should be. Please use this response format when answering 'Affiliative' If you are not sure which humor style this joke belongs to, you can give two options, and each option is separated by a comma. Thanks"
        # "content": "Hello, GPT! Your expertise now extends to humor classification. Your task is to categorize jokes into four types: affiliative, aggressive, self-enhancing, and self-defeating. Affiliative Humor emphasizes a good-natured attitude, the ability to laugh at oneself and life's quirks in a constructive manner, enhancing relationships positively. It's the most common type. When unsure, categorize a joke as AFFILIATIVE. For example, 'A recent study found that women who carry a little extra weight live longer than men who mention it.' Aggressive humor relies on criticism and sarcasm, often making fun of others. For instance, 'If you think people are laughing at you, they probably are.' Self-Enhancing Humor is linked to a positive mindset, using self-deprecation and positivity to boost self-esteem. For example, 'Even when I'm alone, I'm amused by the absurdities of life.' Self-defeating humor involves self-deprecation and humorously highlighting weaknesses. Example: 'I often try to make people like me more by joking about my own faults.' Now you understand the four humor styles. Please use the response format when answering 'Affiliative.' If uncertain, provide two options, each separated by a comma. Thanks!"
        },
        {
        "role": "user",
        "content": joke
        }
    ],
    temperature=0.6,
    max_tokens=64,
    top_p=1
    )

    # 提取生成的文本，这里假设API的回复包含了 "affiliative"、"aggressive"、"self-enhancing"、"self-defeating" 中的一个
    # generated_text = response['choices'][0]['text'].strip()
    response = completion.choices[0].message.content
    response = response.lstrip()
    # 将原始笑话和分类结果存储到结果数组中
    results.append({'joke': joke, 'humor_type': response})
    # print(response)
    count  = count +1
    print(count)

# 将结果写入新的CSV文件
output_df = pd.DataFrame(results)
output_df.to_csv(output_csv_path, index=False)

print(f"处理完成，结果保存在 {output_csv_path}")

