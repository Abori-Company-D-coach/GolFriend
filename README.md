# ゴルフレ！
「ゴルフレ！」開発用のリポジトリです。

# ディレクトリ構成
```
GolFriend/
├─ mysql                #データベースコンテナ
├─ nginx                #Webサーバーコンテナ
├─ python
├─ sql
├─ src                  #ソースコードファイル(このディレクトリで作業が主)
|    └─app              #プロジェクトディレクトリ
|         └─
|         └─
|         └─
|         └─
|         └─
|         └─
|         └─
|         └─
|         └─
|    └─board            #掲示板アプリディレクトリ
|         └─migrations
|         └─templates
|               └─simple_pagination.html
|               └─board
|                    └─_footer.html			#フッター by Tett
|                    └─_navbar.html			#ナビゲーションバー by Tett(環境統合時にコメントアウトした)
|                    └─about.html			#開発メンバーページ by Tett
|                    └─base.html			#ベースファイル
|                    └─board_confirm_delete.html	#投稿の削除確認ページ by Tett
|                    └─board_detail.html		#投稿の詳細ページ by Tett
|                    └─board_form.html		#投稿のフォーム	
|                    └─board_list.html		#投稿リストページ by Tett
|                    └─create.html			#新規投稿 by Koo
|                    └─detail.html			#投稿詳細 by Koo	
|                    └─index.html			#トップページ by Tett
|                    └─list.html			#投稿リスト by Koo
|                    └─login.html			#ログイン by Koo
|                    └─main.html			#メインページ by Tett(環境統合時にコメントアウトした)
|                    └─mypage.html			#マイページトップ by Tett
|                    └─mypage_answers.html		#マイページAnswers by Tett
|                    └─mypage_niceswings.html		#マイページNice Swings by Tett
|                    └─signup.html			#会員登録 by Koo
|         └─__init__.py
|         └─admin.py
|         └─apps.py
|         └─forms.py
|         └─models.py
|         └─tests.py
|         └─urls.py
|         └─views.py
|    └─manage.py
├─ static               #静的ファイル    
|    └─
├─ docker-compose.yml   
├─ README.md
```


# 備考

