import os

paths = [
"sounds\きもいな.mp3",
"sounds\すき.mp3",
"sounds\そんなことないもん.mp3",
"sounds\なんで？.mp3",
"sounds\メンヘラはやだね.mp3",
"sounds\もう.mp3",
"sounds\君たちをいじるのが楽しい.mp3",
"sounds\効果音.mp3",
"sounds\眠たい.mp3",
"sounds\違う！.mp3",
]

for path in paths:
    fixed_path = path.replace("\\", "/")
    filename = os.path.basename(fixed_path)
    text = os.path.splitext(filename)[0]
    print(f'{{ text: "{text}", file: "{fixed_path}" }},')
