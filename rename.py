import os

paths = [
"sounds\あ～無理.mp3",
"sounds\イーヤーヤダヤダ (2).mp3",
"sounds\イーヤーヤダヤダ (3).mp3",
"sounds\イーヤーヤダヤダ.mp3",
"sounds\イヤーッハァー!!! (2).mp3",
"sounds\イヤーッハァー!!!.mp3",
"sounds\え、かわいい.mp3",
"sounds\えへへ.mp3",
"sounds\お巡りさん～こいつです.mp3",
"sounds\お酒飲みたい.mp3",
"sounds\お触り禁止です.mp3",
"sounds\かわいい.mp3",
"sounds\きも.mp3",
"sounds\キモイ.mp3",
"sounds\きもい.mp3",
"sounds\きもいきもいきもい.mp3",
"sounds\ギリギリアウト～.mp3",
"sounds\こいつばかなので.mp3",
"sounds\ご飯だ！.mp3",
"sounds\ドパァ.mp3",
"sounds\なんか欲が出てるお兄ちゃんがいるな.mp3",
"sounds\なんで？.mp3",
"sounds\ニート最高！.mp3",
"sounds\にゃんにゃん～.mp3",
"sounds\ののの脚が好き.mp3",
"sounds\ばか.mp3",
"sounds\ばかばかばかばかばか.mp3",
"sounds\パパ.mp3",
"sounds\ふふふ.mp3",
"sounds\マジでうるさい.mp3",
"sounds\ミリちゃんの声真似.mp3",
"sounds\ミリプロメンバーみんな好き.mp3",
"sounds\みんないい子だね〜 (2).mp3",
"sounds\みんないい子だね〜.mp3",
"sounds\みんなが好き.mp3",
"sounds\らこみんなが好き.mp3",
"sounds\先生！こいつ勝手にしっぽを触ていました.mp3",
"sounds\効果音.mp3",
"sounds\笑い声w.mp3",
"sounds\勘違いしないでください (2).mp3",
"sounds\聴かなかったことにして.mp3",
]

for path in paths:
    fixed_path = path.replace("\\", "/")
    filename = os.path.basename(fixed_path)
    text = os.path.splitext(filename)[0]
    print(f'{{ text: "{text}", file: "{fixed_path}" }},')
