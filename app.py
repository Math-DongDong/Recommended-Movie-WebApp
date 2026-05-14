import streamlit as st

# 1. 페이지 레이아웃 설정
st.set_page_config(
    page_title="동동쌤의 웹 아티클 모음",
    page_icon="./기타/동동이.PNG",
    layout="wide"
)

# 2. 메인 페이지 정의
def main_page():
    st.title("동동쌤의 웹 아티클 모음")

# 3. 메뉴바 설정(각 페이지의 실제 콘텐츠는 별도의 파일에 존재).
pages = {
    "웹 아티클": [
        st.Page("./Article/Recommended_Movie.py", title="영화추천 웹앱"),
    ],
    "메인페이지": [
        st.Page(main_page, title="마진",default=True),
    ],

}

# 3. 네비게이션 UI 생성(메뉴바 위치)
pg = st.navigation(pages, position="hidden")

# 4. 사용자가 선택한 페이지 실행
pg.run()