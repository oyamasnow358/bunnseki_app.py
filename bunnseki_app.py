import streamlit as st

# タイトル
st.title("特別支援教育サポートアプリ")

# 療法・分析法の一覧
methods = {
    "ABA（応用行動分析）": "pages/aba.md",
    "FBA/PBS（機能的行動評価/ポジティブ行動支援）": "pages/fba_pbs.md",
    "CBT（認知行動療法）": "pages/cbt.md",
    "ソーシャルスキルトレーニング": "pages/sst.md",
    "感覚統合療法": "pages/sensory_integration.md",
    "PECS（絵カード交換式コミュニケーション）": "pages/pecs.md",
    "TEACCH": "pages/teacch.md",
    "SEL（社会情動的学習）": "pages/sel.md",
    "マインドフルネス": "pages/mindfulness.md",
    "プレイセラピー": "pages/play_therapy.md",
    "アートセラピー": "pages/art_therapy.md",
    "ミュージックセラピー": "pages/music_therapy.md",
    "セルフモニタリング":"pages/self_monitar.md",
}

# セッションステートを使用して、選択された療法を記憶
if "selected_method" not in st.session_state:
    st.session_state.selected_method = None  # 初期状態はNone

# サイドバーに療法・分析法の一覧
st.sidebar.title("療法・分析法一覧")
selected_method = st.sidebar.radio("選択してください", list(methods.keys()), index=None)

# サイドバーで選択があれば、セッションステートを更新
if selected_method:
    st.session_state.selected_method = selected_method

# メイン画面に実態選択フォーム
st.subheader("児童・生徒の実態を選択してください")

# 実態リスト
student_conditions = {
    "言葉で気持ちを伝えるのが難しい": ["プレイセラピー", "アートセラピー", "PECS（絵カード交換式コミュニケーション）"],
    "感情のコントロールが苦手": ["CBT（認知行動療法）", "SEL（社会情動的学習）", "マインドフルネス"],
    "対人関係が苦手": ["ソーシャルスキルトレーニング", "TEACCH"],
    "学習の集中が続かない": ["ABA（応用行動分析）", "感覚統合療法", "セルフモニタリング"],
    "行動の問題がある": ["FBA/PBS（機能的行動評価/ポジティブ行動支援）", "ABA（応用行動分析）"],
}

# 実態を選択
condition = st.selectbox("実態を選んでください", list(student_conditions.keys()))

# 適した療法を表示
st.write("この実態に適した療法・分析法:")

# 選択肢ごとにボタンを作成
for method in student_conditions[condition]:
    if method in methods:  # methods に存在するかチェック
        if st.button(method):  # ボタンを押したらサイドバーで選択したのと同じ状態にする
            st.session_state.selected_method = method
            st.rerun()  # ✅ 最新のStreamlitではこちらを使う
    else:
        st.error(f"{method} のページが見つかりません")

# 選択された療法の説明を表示（サイドバーorボタンで選択時のみ）
if st.session_state.selected_method:
    st.markdown(f"### {st.session_state.selected_method}")
    file_path = methods.get(st.session_state.selected_method)
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            st.markdown(file.read(), unsafe_allow_html=True)
    else:
        st.error(f"{st.session_state.selected_method} の説明ページが見つかりません")

        # **別のWebアプリへのリンク**
st.markdown("---")  # 区切り線   
st.markdown("関連Webアプリに移動する")
st.markdown("[自立活動指導支援内容](https://aspecialeducationapp-6iuvpdfjbflp4wyvykmzey.streamlit.app/)")
