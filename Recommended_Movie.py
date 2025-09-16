import streamlit as st
import streamlit.components.v1 as components

#################################################################################################################################
# 웹 앱 환경설정
#================================================================================================================================
st.set_page_config(
    page_title="영화 추천 웹앱",
    layout="wide"
)

#################################################################################################################################
# 아이프레임으로 삽입할 Google Apps Script URL 입력
#================================================================================================================================

# 탭 이름과 각 탭에 임베드할 URL 리스트
TAB_INFOS = [
    ("버전A", "https://script.google.com/macros/s/AKfycbzEamEHydpiKQNUuZ83pJR3nTibhGNwDMgpjyDqE4R3NtcRCOmpzxEJPARnGzi1DuE1/exec"),
    ("버전B", "https://script.google.com/macros/s/AKfycbzR-lprxOR-nzrtCrtowSYpnHMJyLEiREI8e0vHt2-5bVCi5e4CuOcHtSk-AEwHx1EY/exec"),
    ("버전C", "https://script.google.com/macros/s/AKfycby-HEyTKkkqcVfu58NMdybx-eJ2ghz-LLf7WD16niUOzUbHj3uLcZeVSqymfA3YQDd0DA/exec"),
]

#################################################################################################################################
# 아이프레임 생성 - st.components.v1.iframe을 사용하여 웹 앱을 아이프레임으로 임베드
#================================================================================================================================

# 탭 생성 및 각 탭에 iframe 삽입
tabs = st.tabs([name for name, _ in TAB_INFOS])
for tab, (_, url) in zip(tabs, TAB_INFOS):
    with tab:
        components.iframe(url, width=None, height=800, scrolling=True)
