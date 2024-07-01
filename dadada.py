import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# CSV 파일 경로
csv_file_path = '극성사전.csv'

# CSV 파일을 읽어 데이터프레임으로 변환
df = pd.read_csv(csv_file_path)

# 불필요한 컬럼 제거
columns_to_remove = ['prob_feature_given_hawkish', 'prob_feature_given_dovish']
df = df.drop(columns=columns_to_remove)

# hawkish 컬럼의 상위 20개 데이터 가져오기
top_20_hawkish = df.nlargest(20, 'hawkish')

# 맑은 고딕 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 폰트 파일 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Streamlit 애플리케이션
st.title('극성사전 데이터프레임')
st.write('아래는 불필요한 컬럼을 제거한 극성사전.csv 파일에서 hawkish 컬럼의 상위 20개 데이터입니다.')

# 데이터프레임 표시
st.dataframe(top_20_hawkish)

# 막대그래프 그리기
st.write('### Hawkish 상위 20개 막대그래프')
plt.figure(figsize=(12, 8))
plt.bar(top_20_hawkish['ngram'], top_20_hawkish['hawkish'], color='skyblue')
plt.xlabel('ngram')
plt.ylabel('Hawkish')
plt.title('Top 20 Hawkish Features')
plt.xticks(rotation=90)  # X축 레이블 회전

# 그래프를 Streamlit에 표시
st.pyplot(plt)
