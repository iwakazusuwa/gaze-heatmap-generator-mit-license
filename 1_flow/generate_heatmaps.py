# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors
import japanize_matplotlib
from scipy.stats import gaussian_kde
from PIL import Image


# ========= パラメータ =========
DATA_DIR = "../2_data"
OUTPUT_DIR = "../3_output"
IMAGE_PATH = "fish.png"
BW_METHOD = 0.3      # KDEのスムージング幅
GRID_SCALE = 0.25    # 高速化用グリッド縮小率（1=フル解像度、0.5=半分）
# =============================

# 画像読み込み
img = mpimg.imread(IMAGE_PATH)
img_height, img_width = img.shape[:2]

# 出力ディレクトリ作成
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "per_user"), exist_ok=True)

# CSVファイル結合
csv_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
df_list = [pd.read_csv(f, encoding='utf-8') for f in csv_files]
df = pd.concat(df_list, ignore_index=True)
print(f"読み込んだデータ件数: {len(df)}")

# グリッド作成（縮小版）
grid_w = int(img_width * GRID_SCALE)
grid_h = int(img_height * GRID_SCALE)
x_grid, y_grid = np.meshgrid(np.arange(grid_w), np.arange(grid_h))
grid_coords = np.vstack([x_grid.ravel(), y_grid.ravel()])


# スケーリング関数（座標系変換）
def scale_positions(df_subset):
    return np.vstack([
        df_subset['position_x'] * GRID_SCALE,
        df_subset['position_y'] * GRID_SCALE
    ])

# KDE計算＆プロット保存
def make_heatmap_and_save(positions, weights, output_path, title):
    kde = gaussian_kde(positions, weights=weights, bw_method=BW_METHOD)
    density = kde(grid_coords).reshape((grid_h, grid_w))
    density /= density.max()

    # PILで拡大して元画像サイズに戻す
    density_img = Image.fromarray((density * 255).astype(np.uint8))
    density_img = density_img.resize((img_width, img_height), Image.BILINEAR)
    density = np.array(density_img) / 255.0

    # 元のカラーマップ取得
    cmap = plt.cm.jet
    
    # RGBA値を取得し、透明度(アルファ)を0から1へ線形変化させる
    colors = cmap(np.arange(cmap.N))
    colors[:, -1] = np.linspace(0, 1, cmap.N)
    
    # 透明度付きの新カラーマップ作成
    transparent_cmap = mcolors.ListedColormap(colors)    

    # 描画
    plt.figure(figsize=(10, 6))
    plt.imshow(img)
    plt.imshow(density, cmap=transparent_cmap, alpha=1)
    plt.colorbar(label='視線密度')
    plt.title(title)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

    # ① 全体ヒートマップ
print("全体ヒートマップ作成中...")
positions_all = scale_positions(df)
weights_all = df['time'].values
make_heatmap_and_save(positions_all, weights_all,
                      os.path.join(OUTPUT_DIR, "all_users_heatmap.png"),
                      "全体ヒートマップ")

# ② 個人別ヒートマップ
print("個人別ヒートマップ作成中...")
for user_id, group in df.groupby('id'):
    positions = scale_positions(group)
    weights = group['time'].values
    output_path = os.path.join(OUTPUT_DIR, "per_user", f"{user_id}.png")
    make_heatmap_and_save(positions, weights, output_path, f"ID: {user_id}")

print("完了しました！")
