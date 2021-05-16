# ゴルフレ！
「ゴルフレ！」開発用のリポジトリです。

# ディレクトリ構成
```
GolFriend/
|─ mysql                	#データベースコンテナ
|─ nginx                	#Webサーバーコンテナ
|─ python               	#pythonコンテナ
|─ sql
|─ src                  	#ソースコードディレクトリ
|    └─manage.py
|    └─app             	    #プロジェクトディレクトリ
|         └─__init__.py
|         └─settings.py
|         └─urls.py
|         └─wsgi.py
|    └─board                #掲示板アプリディレクトリ
|         └─migrations
|         └─templates
|               └─board
|                    └─about.html			        #開発メンバーページ
|                    └─base.html			        #ベースファイル
|                    └─board_confirm_delete.html	#投稿の削除確認ページ
|                    └─board_detail.html		    #投稿の詳細ページ
|                    └─board_form.html		        #投稿のフォーム	
|                    └─board_list.html		        #投稿リストページ	
|                    └─index.html			        #トップページ
|                    └─login.html			        #ログインページ
|                    └─mypage.html			        #マイページトップ
|                    └─signup.html			        #会員登録ページ
|                    └─layouts
|                    	└─_footer.html
|                    	└─_navbar.html
|                    	└─simple_pagination.html
|         └─__init__.py
|         └─admin.py
|         └─apps.py
|         └─forms.py
|         └─models.py
|         └─tests.py
|         └─urls.py
|         └─views.py
|─ static               #静的ファイル格納ディレクトリ
|    └─board
|         └─css	        #cssファイル格納ディレクトリ					
|               └─layouts
|                   └─_footer.css
|                   └─_navbar.css
|               └─about.css
|               └─base.css
|               └─index.css
|               └─login.css
|               └─mypage.css
|               └─sognup.css
|               └─board.css
|         └─img
|─ docker-compose.yml   
|─ README.md
```


# 備考

