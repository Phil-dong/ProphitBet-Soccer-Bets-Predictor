import streamlit as st
import subprocess
import pandas as pd
import os

# 设置页面标题
st.title("ProphitBet 足球比赛预测工具")
st.subheader("支持：英超/英冠/意甲/西甲/德甲/法甲/荷甲/中超")

# 步骤1：抓取最新数据
if st.button("🔄 抓取最新赛事数据"):
    with st.spinner("正在抓取数据...请稍等"):
        # 运行数据抓取脚本
        result = subprocess.run(
            ["python", "scrape_data.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            st.success("数据抓取完成！")
            st.text(result.stdout)
        else:
            st.error("数据抓取失败！错误信息：")
            st.text(result.stderr)

# 步骤2：执行预测
if st.button("⚽ 开始预测所有联赛"):
    with st.spinner("正在预测比赛...请稍等"):
        # 运行预测脚本
        result = subprocess.run(
            ["python", "predict.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            st.success("预测完成！结果如下：")
            st.text(result.stdout)
            
            # 显示预测结果文件（如果存在）
            prediction_files = [f for f in os.listdir("data/") if "prediction" in f.lower()]
            if prediction_files:
                st.subheader("预测结果表格")
                for file in prediction_files:
                    df = pd.read_csv(f"data/{file}")
                    st.dataframe(df)
        else:
            st.error("预测失败！错误信息：")
            st.text(result.stderr)

# 说明
st.info("提示：先点击「抓取最新数据」，再点击「开始预测」，结果会自动显示~")
