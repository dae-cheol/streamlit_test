import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# CSV 파일을 읽어 데이터프레임으로 변환
hawkish_df = pd.read_csv('금리 상승 사전.csv')
tone_df = pd.read_csv('어조금리분석.csv')

# 불필요한 컬럼 제거
columns_to_remove = ['prob_feature_given_hawkish', 'prob_feature_given_dovish']
hawkish_df = hawkish_df.drop(columns=columns_to_remove)

# hawkish 컬럼의 상위 20개 데이터 가져오기
top_20_hawkish = hawkish_df.nlargest(20, 'hawkish')

# 맑은 고딕 폰트 설정
font_path = 'H2MJRE.TTF'  
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


# Streamlit 애플리케이션
st.title('tone & 기준금리 분석')

# 데이터프레임 표시
st.write('tone & base_rate')
st.dataframe(tone_df)

# 사용자 입력을 통해 시각화할 컬럼 선택
columns = tone_df.columns.tolist()
x_axis = st.selectbox('date', columns)
y_axis1 = st.selectbox('doc_tone', columns, index=1)
y_axis2 = st.selectbox('base_rate', columns, index=2)

# 선 차트 그리기
if x_axis and y_axis1 and y_axis2:
    st.write('### tone과 기준금리의 선 차트')
    fig, ax = plt.subplots()
    chart_data = tone_df[[x_axis, y_axis1, y_axis2]].set_index(x_axis)
    y_axis2.legend(loc='upper right')
    
    st.line_chart(chart_data)