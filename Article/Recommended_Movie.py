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
    ("버전B", "https://script.google.com/macros/s/AKfycbzM1pcZWQJi3WF8nm9mMkPO8iAQpJ1FIQ4_Gp1CaCzGddUcCaQu0PQLOJqYCfk3pTv1/exec"),
    ("버전C", "https://script.google.com/macros/s/AKfycbznmGFIjVCNcg8p87Tx1ocq0fvY1KlQ7MkmUqoe0jt6hkRkVJxH20knAb2O00vezFRn3g/exec"),
]

#################################################################################################################################
# 아이프레임 생성 - st.components.v1.iframe을 사용하여 웹 앱을 아이프레임으로 임베드
#================================================================================================================================

# 탭 생성 및 각 탭에 iframe 삽입
tabs = st.tabs([name for name, _ in TAB_INFOS])
for tab, (_, url) in zip(tabs, TAB_INFOS):
    with tab:
        components.iframe(url, width=None, height=2500, scrolling=True)
