# nukebot
Discordで利用できるサーバーNukeBotです。

# 機能
- チャンネル全消去
- 最大500チャンネルの作成
- メッセージスパム
- チャンネル名とメッセージの指定
- ロールの全消去
- ユーザーの全員Ban

# 使用方法
1 - このディレクトリをzipとしてダウンロード<br>
画像の通りに進めると、通常通りダウンロードすることができます。<br>
![2022-03-13_13h19_18](https://user-images.githubusercontent.com/84906515/158044900-072bf7d1-eb4f-42a8-8a7b-4fb854be29fb.png)
<hr>
2 - ダウンロードしたらzipを解凍<br>
zipを解凍するだけで大丈夫です。<br>
Windows標準の解凍ソフトでも大丈夫です。<br>
もちろん外部ソフトも利用できます。<br>
<hr>
3 - config.ymlを開く<br>
設定を行うためにconfig.ymlを開きます。<br>
![2022-03-13_13h20_38](https://user-images.githubusercontent.com/84906515/158044935-5db13717-6582-40c8-812f-d5f33f5d064e.png)
<hr>
4 - tokenを設定する<br>
tokenを設定しましょう。<br>
config.yml内の`token: "TOKEN"`の部分を編集します。<br>
「"」に囲まれた「TOKEN」の文字を消して、Tokenに置き換えます。<br>
このTokenはBotのTokenでなくてはなりません。<br>
また基本的に「"」で囲む必要があります。<br>
![2022-03-13_13h23_41](https://user-images.githubusercontent.com/84906515/158045001-b93e5126-7f5e-4106-b910-4984a85b7190.png)
<hr>
5 - idを設定する<br>
idを設定しましょう。<br>
ほかの人がnukeコマンドを実行するのを防いだりできます。<br>
また、設定しないと自分もコマンドを実行できなくなってしまいます。<br>
config.yml内の`allow_user: 0`の部分を編集します。<br>
「0」の部分を自分のidにします。<br>
これは「"」で囲う必要はありません。<br>
自分のidを取得するには、discordの詳細設定を開きます。<br>
詳細設定のタブへ移動して、「開発者モード」を有効にします。<br>
後は、サーバーのメンバーリストで自分の名前等で右クリックをして「IDをコピー」を押します。<br>
そうすると自分のIDが取得できます。<br>
<hr>
6 - 動作設定<br>
動作設定をしましょう。<br>
全ユーザーをBanしたい場合は`users_ban: false`を変えましょう。<br>
`false`を`true`にすると全ユーザーをBanするように動作されます。<br>
ロールをすべて消したい場合は`roles_del: false`を変えます。<br>
`false`を`true`にすると全ロールを消すように動作されます。<br>
<hr>
7 - ゲームプレイの変更<br>
〇〇をプレイ中を出すには、config.yml内の`gameplay_display: ""`を変更します。<br>
「"」で囲んで変更しましょう。<br>
例えば「testをプレイ中」にしたい場合は`gameplay_display: "game"`となります。<br>
好きに変更できます。<br>
ただ、無効にだけはできないことをご注意ください。<br>
<hr>
8 - チャンネル名の設定<br>
nuke時に生成されるチャンネルの名前を決めることができます。<br>
これはリストで、リストの中からランダムに毎回選ばれて生成されます。<br>
書き方は`["a", "b", "c"]`といった感じです。<br>
まず`[]`で囲まれている中に「"」で囲まれた文字を入れます。<br>
`["text"]`このような感じです。<br>
文字を追加したい場合は「,」で区切りをつけて文字を追加できます。<br>
`["text","test"]`このような感じです。<br>
<hr>
9 - メッセージの設定<br>
nuke時に生成送信されるメッセージの内容を決めることができます。<br>
これはリストで、リストの中からランダムに毎回選ばれて送信されます。<br>
書き方は`["a", "b", "c"]`といった感じです。<br>
まず`[]`で囲まれている中に「"」で囲まれた文字を入れます。<br>
`["text"]`このような感じです。<br>
文字を追加したい場合は「,」で区切りをつけて文字を追加できます。<br>
`["text","test"]`このような感じです。
