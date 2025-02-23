import streamlit as st

# タイトル
st.title("特別支援教育サポートアプリ")

# 療法・分析法の一覧
methods = {
    "ABA（応用行動分析）": "pages/aba.md",
    "FBA/PBS（機能的アセスメント/ポジティブ行動支援）": "pages/fba_pbs.md",
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
    "統計学的分析方法":"pages/toukei.md",
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
    "行動の問題がある": ["FBA/PBS（機能的アセスメント/ポジティブ行動支援）", "ABA（応用行動分析）"],
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

# 説明ページの表示
if st.session_state.selected_method:
    st.markdown(f"### {st.session_state.selected_method}")
    file_path = methods.get(st.session_state.selected_method)

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                st.markdown(file.read(), unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"{st.session_state.selected_method} の説明ページが見つかりません（ファイルが存在しません）")
    else:
        st.error(f"{st.session_state.selected_method} の説明ページが見つかりません（辞書に登録されていません）")

    # **CBT（認知行動療法）なら画像を表示**
    if st.session_state.selected_method == "CBT（認知行動療法）":
        st.image("images/cbt_diagram.png", caption="認知行動療法", use_container_width=True)

    elif st.session_state.selected_method == "PECS（絵カード交換式コミュニケーション）":
          st.image("images/pecs.png", caption="PECS（絵カード交換式コミュニケーション）", width=350)

     # **FBA/PBS（機能的行動評価/ポジティブ行動支援）の場合、Word・Excelダウンロードを追加**
    elif st.session_state.selected_method == "FBA/PBS（機能的アセスメント/ポジティブ行動支援）":
        st.markdown("---")  # 区切り線
        st.subheader("📂 参考データのダウンロード")

        # Wordファイルのダウンロード
        word_file_path = "data/機能的アセスメントについて.docx"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ①機能的アセスメントについてをダウンロード",
                data=f,
                file_name="機能的アセスメントについて.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート１　基礎情報.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ②ワークシート１　基礎情報をダウンロード",
                data=f,
                file_name="ワークシート１　基礎情報.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Excelファイルのダウンロード
        excel_file_path = "data/ワークシート２　MAS機能分析.xls"
        with open(excel_file_path, "rb") as f:
            st.download_button(
                label="📊 ③ワークシート２　MAS機能分析.xlsをダウンロード",
                data=f,
                file_name="ワークシート２　MAS機能分析.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート３　行動問題の特徴.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ④ワークシート３　行動問題の特徴をダウンロード",
                data=f,
                file_name="ワークシート３　行動問題の特徴.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ) 
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート４　ライフスタイルの特徴.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ⑤ワークシート４　ライフスタイルの特徴をダウンロード",
                data=f,
                file_name="ワークシート４　ライフスタイルの特徴.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート５　行動の記録スキャッターブロット.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ⑥ワークシート５　行動の記録スキャッターブロットをダウンロード",
                data=f,
                file_name="ワークシート５　行動の記録スキャッターブロット.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート６　１日の記録.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ⑦ワークシート６　１日の記録をダウンロード",
                data=f,
                file_name="ワークシート６　１日の記録.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート７　頭の中のアセスメント.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ⑧ワークシート７　頭の中のアセスメント.docをダウンロード",
                data=f,
                file_name="ワークシート７　頭の中のアセスメント.doc.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        # Wordファイルのダウンロード
        word_file_path = "data/ワークシート８　ＡＢＣ分析.doc"
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="📄 ⑨ワークシート８　ＡＢＣ分析をダウンロード",
                data=f,
                file_name="ワークシート８　ＡＢＣ分析.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        # **出典情報を追加**
        st.subheader("📖 出典情報")
        st.markdown("""
        - **参考文献:** Durand, V. M. (1990). Severe behavior problems: A functional communication training approach. Guilford Press..
        - **Webサイト:** [機能的アセスメント](http://www.kei-ogasawara.com/support/assessment/)
        """)

        st.markdown("---")  # 区切り線
        st.subheader("📂 機能的アセスメント分析ツール")
        st.markdown("""
        [機能的行動評価分析ツール](https://kinoukoudou-ptfpnkq3uqgaorabcyzgf2.streamlit.app/)
        """)

         # **応用行動分析ツール**
    elif st.session_state.selected_method == "ABA（応用行動分析）":
        st.markdown("---")  # 区切り線
        st.subheader("📂 簡単分析ツール")
        st.markdown("""
        [応用行動分析ツール](https://abaapppy-k7um2qki5kggexf8qkfxjc.streamlit.app/)
        """)
         # **統計学的分析方法ツール**
    elif st.session_state.selected_method == "統計学的分析方法":
        st.write("""※以下の分析ツールを気軽に試してみて下さい。初心者でも簡単に使えるようにはしましたが、説明が難しい箇所はあると思います。フォームで意見を入力して頂くか、直接小山にお声かけ下さい。""")
        st.markdown("---")  # 区切り線
        st.subheader("📂 統計学 分析ツール一覧")
        st.markdown("""
        [相関分析ツール](https://soukan-jlhkdhkradbnxssy29aqte.streamlit.app/)
        """)
        st.markdown("""
        [多変量回帰分析ツール](https://kaikiapp-tjtcczfvlg2pyhd9bjxwom.streamlit.app/)
        """)
        st.markdown("""
        [t検定](https://tkentei-flhmnqnq6dti6oyy9xnktr.streamlit.app/)""")
        st.markdown("""
        [ロジスティック回帰分析ツール](https://rojisthik-buklkg5zeh6oj2gno746ix.streamlit.app/)
        """)
        st.markdown("""
        [ノンパラメトリック統計分析ツール](https://nonparametoric-nkk2awu6yv9xutzrjmrsxv.streamlit.app/)
        """)
       
        

        # **別のWebアプリへのリンク**

st.markdown("---")  # 区切り線   
st.markdown("🌎関連Webアプリに移動する")
st.markdown("[自立活動指導支援内容](https://aspecialeducationapp-6iuvpdfjbflp4wyvykmzey.streamlit.app/)")
st.markdown("[発達段階能力チャート作成](https://specialexcel2apppy-bo6jrng9gyqw5dmfcgwbl5.streamlit.app//)")
st.markdown("---")  # 区切り線  
st.markdown("📁教育・心理分析ツール") 
st.markdown("[応用行動分析](https://abaapppy-k7um2qki5kggexf8qkfxjc.streamlit.app/)")
st.markdown("[機能的アセスメント分析](https://kinoukoudou-ptfpnkq3uqgaorabcyzgf2.streamlit.app/)") 
st.markdown("---")  # 区切り線
st.markdown("📁統計学分析ツール") 
st.markdown("[相関分析ツール](https://soukan-jlhkdhkradbnxssy29aqte.streamlit.app/)")
st.markdown("[多変量回帰分析](https://kaikiapp-tjtcczfvlg2pyhd9bjxwom.streamlit.app/)")
st.markdown("[t検定](https://tkentei-flhmnqnq6dti6oyy9xnktr.streamlit.app/)")
st.markdown("[ロジスティック回帰分析ツール](https://rojisthik-buklkg5zeh6oj2gno746ix.streamlit.app/)")
st.markdown("[ノンパラメトリック統計分析ツール](https://nonparametoric-nkk2awu6yv9xutzrjmrsxv.streamlit.app/)")
st.markdown("---")  # 区切り線
st.write("""※ それぞれのアプリに記載してある内容、分析ツールのデータや図、表を外部に出す物（研究など）に使用する場合は小山までご相談ください。無断での転記・利用を禁じます。""")
  