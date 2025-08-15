# gaze-heatmap-generator-mit-license

複数ユーザーによる視線データを統合し、広告などの画像に対して全体ヒートマップと個別ヒートマップを作成する Python ツールです。

---

## 概要

- 複数ユーザーの CSV 形式視線データを統合し、KDE によるヒートマップを生成
- 全体マップとユーザーごとのマップを自動生成
- 画像サイズを縮小して処理を高速化（`GRID_SCALE` によって調整可能）
- 出力画像は透明度付きのヒートマップとして保存（`all_users_heatmap.png`、および `per_user/{user_id}.png`）

---

## 特徴

- 複数ユーザーの視線データを統合し、全体の注視傾向を可視化
- ユーザーごとの個別ヒートマップも生成可能
- 画像サイズの縮小による処理速度の向上
- 出力画像は PNG 形式で保存され、透明度付きで視覚的にわかりやすい

---

## フォルダ構成

```
gaze-heatmap-generator-mit-license/
├── 1_flow/
│   ├── generate_heatmaps.py       # 複数ユーザー分の視線ヒートマップ生成スクリプト
│   └── fish.png                   # サンプル画像（著作権要確認）
├── 2_data/                          # 複数ユーザーの視線CSVファイル
├── 3_output/
│   ├── all_users_heatmap.png      # 全体ヒートマップ
│   └── per_user/
│       ├── user1.png
│       └── user2.png
├── README.md                      # 使い方や概要
└── LICENSE                        # MIT License
```


---

## 使い方

1. `2_data/gaze_data.csv` にユーザーごとの視線データを準備（CSV 形式）
2. `1_flow/generate_heatmaps.py` を実行してヒートマップを生成

```bash
python 1_flow/generate_heatmaps.py
```

# 必要な環境・依存パッケージ
- Python 3.x
- 必要なパッケージ：
```
pip install pandas numpy matplotlib scipy pillow japanize_matplotlib
```

# 今後の展望
- ユーザーインターフェースの改善
- 他の視線データ形式への対応
- ヒートマップ生成の高速化

# 貢献方法
プロジェクトへの貢献は以下の方法で歓迎します：
- バグ報告や機能追加の提案は Issues で
- コード改善や新機能追加は Pull Request で
- ドキュメント改善や翻訳も歓迎

# LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)



