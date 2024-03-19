#coding=utf-8
import openai
import pandas as pd

# 设置你的OpenAI GPT API密钥
openai.api_key = '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'

# 读取包含笑话的CSV文件
input_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/INPUT/jokes_1_49.csv'
output_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/OUTPUT/keyword/jokes_1_49.csv'

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
        "content": "Hello, GPT! Your expertise now extends to keyword extraction. You need to extract the keyword from the following paragraphs. Please remember extract at least one keyword and no more than three keywords in each paragraph, and this must be strictly adhered to. You only need to give keywords in each answer. If there are multiple keywords, separate them with commas. Here, I want to tell you again the defination of the keyword. In linguistics, keywords usually refer to words that have special meaning or importance in a sentence or text. These words play a key role in understanding the semantics and context of a sentence. Keywords can be nouns, verbs, adjectives, etc., depending on the structure and content of the sentence. Please extract the keyword according to the above instructions. Thanks"
        },
        {
        "role": "user",
        "content": joke
        }
    ],
    temperature=0.5,
    max_tokens=64,
    top_p=1
    )

    # generated_text = response['choices'][0]['text'].strip()
    response = completion.choices[0].message.content
    response = response.lstrip()
    # 将原始笑话和分类结果存储到结果数组中
    results.append({'joke': joke, 'keyword': response})
    # print(response)
    count  = count +1
    print(count)

# 将结果写入新的CSV文件
output_df = pd.DataFrame(results)
output_df.to_csv(output_csv_path, index=False)

print(f"处理完成，结果保存在 {output_csv_path}")

