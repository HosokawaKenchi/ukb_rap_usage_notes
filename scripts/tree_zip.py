import zipfile
import shutil
import os
import subprocess
import argparse

def process_zip_file(zip_file_path: str, output_dir: str):
    """
    指定されたzipファイルをカレントディレクトリに移動し、解凍し、
    treeコマンドでファイル一覧を取得してテキストファイルに保存します。

    Args:
        zip_file_path (str): 処理するzipファイルのフルパス。
    """

    # 1. zipファイルをカレントディレクトリに移動
    try:
        # zipファイル名を取得
        zip_file_name = os.path.basename(zip_file_path)
        destination_path = os.path.join(os.getcwd(), zip_file_name)

        if zip_file_path != destination_path:
            shutil.copy(zip_file_path, os.getcwd())
        else:
            print(f"'{zip_file_name}' は既にカレントディレクトリにあります。")

    except Exception as e:
        print(f"zipファイルの移動中にエラーが発生しました: {e}")
        return

    # 2. zipファイルを解凍
    # 解凍先のディレクトリを作成（zipファイル名から拡張子を除いたもの）
    extract_dir_name = os.path.splitext(zip_file_name)[0]
    extract_path = os.path.join(os.getcwd(), extract_dir_name)

    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    try:
        with zipfile.ZipFile(destination_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
    except zipfile.BadZipFile:
        print(f"エラー: '{zip_file_name}' は有効なzipファイルではありません。")
        return
    except Exception as e:
        print(f"zipファイルの解凍中にエラーが発生しました: {e}")
        return

    # 3. treeコマンドでファイル一覧を取得してテキストファイルに保存
    output_file_path = output_dir + f"{os.path.splitext(zip_file_path)[0]}.txt"
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    try:
        result = subprocess.run(['tree', extract_path], capture_output=True, text=True, check=True, encoding="utf-8")
        with open(output_file_path, 'w', encoding="utf-8") as f:
            f.write(result.stdout)
        print(f"ファイル一覧を '{output_file_path}' に保存しました。")
    except FileNotFoundError:
        print("エラー: 'tree' コマンドが見つかりません。'tree' がインストールされていることを確認してください。")
    except subprocess.CalledProcessError as e:
        print(f"treeコマンドの実行中にエラーが発生しました: {e}")
        print(f"標準エラー出力: {e.stderr}")
    except Exception as e:
        print(f"ファイル一覧の保存中にエラーが発生しました: {e}")
    
    shutil.rmtree(extract_path)
    os.remove(destination_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file")
    parser.add_argument("-o", "--output_dir")
    args = parser.parse_args()
    
    process_zip_file(args.input_file, args.output_dir)