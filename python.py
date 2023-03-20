import os
import openai
import streamlit as st



# 设置OpenAI API Key
openai.api_key = st.secrets["openai"]["api_key"]

# 根据用户输入生成摘要的函数
def generate_summary(prompt, summary_length, tone, quality):
    # TODO: 使用OpenAI API生成摘要
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=summary_length,
        temperature=0.2,
        n=1,
        stop=None,
        presence_penalty=0,
        frequency_penalty=0,
    )
    # 从 OpenAI API 的响应中获取摘要
    summary = response.choices[0].text
    
    return summary

# Streamlit应用程序
def main():
    # 页面标题
    st.title("春萍的文案小助手")

    # 用户输入
    prompt = st.text_area("输入你想知道的")

    summary_length = st.slider("选择输出字数（10≈5个汉字）", 50, 1000, 300)

    tone = st.selectbox("选择输出语气（灰度）", ["正式", "非正式"])

    quality = st.selectbox("选择输出质量（灰度）", ["高", "中", "低"])

    # 按钮，触发生成摘要的函数
    if st.button("查看答案"):
        # 生成摘要
        summary = generate_summary(prompt, summary_length, tone, quality)

        # 显示生成的摘要
        st.write(summary)

if __name__ == "__main__":
    main()
