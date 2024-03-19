#coding=utf-8
import openai
import pandas as pd

# 设置你的OpenAI GPT API密钥
openai.api_key = '**********************************************'

# 读取包含笑话的CSV文件
input_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/INPUT/jokes_all.csv'
output_csv_path = '/home/heng/Robot/Dataset/Humor/one_line/OUTPUT/rating/jokes_all.csv'

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
        "content": "Hello, GPT! Your expertise now extends to humor. Your task is to rate jokes by using integer from 1 to 10. 1 is not funny at all and 10 is very funny. Please treat the rating work seriously and behave more strictly. And also, please don't be too extreme when grading, most of the ratings should be between 4 and 8. The response format is only the rating score. Thanks"
        },
        {
        "role": "user",
        "content": joke
        }
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
    )

    response = completion.choices[0].message.content
    response = response.lstrip()
    # 将原始笑话和分类结果存储到结果数组中
    results.append({'joke': joke, 'rating': response})
    # print(response)
    count  = count +1
    print(count)

# 将结果写入新的CSV文件
output_df = pd.DataFrame(results)
output_df.to_csv(output_csv_path, index=False)

print(f"处理完成，结果保存在 {output_csv_path}")

