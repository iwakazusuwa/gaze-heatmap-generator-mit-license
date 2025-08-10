# gaze-heatmap-mit-license

複数ユーザーによる視線データを統合し、広告などの画像に対して全体ヒートマップと個別ヒートマップを作成するPythonツールです。

## 概要

- 複数ユーザーのCSV形式視線データを統合し、KDEによるヒートマップを生成
- 全体マップとユーザーごとのマップを自動生成
- 画像サイズを縮小して処理を高速化（`GRID_SCALE` によって調整可能）
- 出力画像は透明度付きのヒートマップとして保存（`all_users_heatmap.png`、および `per_user/{user_id}.png`）

## 必要な環境・依存パッケージ

- Python 3.x  
- pandas, numpy, matplotlib, scipy, pillow, japanize_matplotlib など

```bash
pip install pandas numpy matplotlib scipy pillow japanize_matplotlib
```

## フォルダ構成例
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

## 使い方
```
python generate_heatmaps.py --image fish.png --data_dir data/ --output_dir output/
```

このスクリプトは、複数の視線データCSVを読み込み、全体およびユーザー別のヒートマップ画像を output/ フォルダへ自動保存します。

LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

開発者： iwakazusuwa(Swatchp)



