# UKB-RAPの使い方メモ



## 使えるライブラリ

[UKB-RAP Tools library](https://dnanexus.gitbook.io/uk-biobank-rap/working-on-the-research-analysis-platform/running-analysis-jobs/tools-library)

- Genomicsのみ特有のツール
- それ以外（主要な統計、MRI等含む）は DXJupyterLab App (DNAnexus Platform App) 経由で使えというものが多い


## DXJupyterLabの使い方

- [DXJupyterLab](https://ukbiobank.dnanexus.com/panx/tool/app/dxjupyterlab) アプリは、様々なツールを導入済みのJupyterLabサーバーを実行するDockerコンテナである
 - DXJupyterLabを起動する（Dockerコンテナをインスタンス化する）と、サーバーが立ち上がる
 - このサーバーにブラウザからHTTPSで接続してサーバー上のJupyter Notebookを動かす
 - ユーザーから見るとブラウザアプリに見える

![DXJupyterLab](https://hosokawakenchi.github.io/ukb_rap_usage_notes/DXJupyterLab_diagram.svg)


### ローカルにJupyterLab環境を立ち上げる時の使い方（我々は使用しない）
 
起動はVisual Studio Codeのターミナルから以下のコマンドを実行する。
なぜかVS Code以外のプロンプトからは成功しない。

```bash
python -m pip install jupyterlab
python -m jupyterlab
```
