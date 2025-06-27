# UKB-RAPの使い方メモ



## DXJupyterLabの使い方

- [DXJupyterLab](https://ukbiobank.dnanexus.com/panx/tool/app/dxjupyterlab) アプリは、様々なツールを導入済みのJupyterLabサーバーを実行するDockerコンテナである
    - DXJupyterLabを起動する（Dockerコンテナをインスタンス化する）と、サーバーが立ち上がる
    - このサーバーにブラウザからHTTPSで接続してサーバー上のJupyter Notebookを動かす
    - ユーザーから見るとブラウザアプリに見える

![DXJupyterLab](https://hosokawakenchi.github.io/ukb_rap_usage_notes/images/DXJupyterLab_diagram.svg)


## UKB-RAPの動かし方（最初に）

- [UKBioBank DNAnexus](https://ukbiobank.dnanexus.com/)にアクセスする
    - 自分のユーザーIDとパスワードでログイン
- (Optional) プロジェクトを作る
    - 画面右上の "+ New Project" ボタンから作る
    - 一度やっておけば2回目は使いまわし
- (Optional) JupyterLabのインスタンスを作る
    - 画面上部のツールバーから "TOOLS > JupyterLab" を選択
    - 右上の "+ New JupyterLab" を選択
    - 一度やっておけば2回目は使いまわし
- インスタンスの設定を記入して"Start Environment"
    - **ここから料金が発生するため注意**
- JupyterLabのコンテナを立ち上げる
    - しばらく待ち(20分ほど)，以下の表示になったら使用可能
    - "Open" からJupyterLabを開く
    - (スクショ)のような表示になり、分析を行うことができる
- おそらくデータは左の「DNAnexus」タブに入っている
    - 必要なファイルを選択して右クリックでパスをコピーできるので、そこから使用するのが良いかも



## [基本的な挙動？](https://www.youtube.com/watch?v=YIPdhf3qbQA&t=11m45s)

- 計算をするのに以下の設定が必要
    1. プロジェクトのCohort Browserで"コホート"を作る
    2. Table Expoterでコホートのフィールド（*データベース用語、エクセルで言うセル*）を選び、TSV（*タブ区切りCSV*）に変換する
    3. JupyterLabにデータを読み込み計算する
    4. 結果をプロジェクトに戻す
- おそらく「JupyterLabにデータを読み込み計算する」で[以下のフロー]((https://www.youtube.com/watch?v=YIPdhf3qbQA&t=11m45s))で動作が行われる
    1. インスタンスを立ち上げる
    2. (Optional) 追加の実行環境（R等のアプリ）を入れる
    3. プロジェクト中のNotebooksをインスタンスに読み込ませる
    4. プロジェクトで指定したコホートフィールドをインスタンスに読み込ませる
    5. 計算を実行する
    6. 計算結果をプロジェクトに返す


 
 

- UKB RAPには2種類のインスタンスがある
    - シングルノードJupyterLab: 既に抽出済みのデータを使用する場合や，Sparkでの分散処理を必要としない場合　
    - SparkクラスターJupyterLab: HAILやGLOWなどのSparkツールを使用する場合，または複雑な処理を必要とする場合に直接データセットに対するクエリを呼びたい場合に使用する
- UKB RAPには2種類のストレージがある
    - Research Analysis Project Storage
    - Jupyter Lab Storage: セッションが終了すると消失する一時的なストレージ

- [用語](https://www.youtube.com/watch?v=YIPdhf3qbQA&t=8m33s)
    - Kernel
        - JupyterLabでの専門用語
        - 各インスタンス内で呼び出す実行環境
            - **Python_R** : Python + Rが走るカーネル
            - **Stata** : Stata
            - **ML_IP** : ML
            - 他にカスタムなカーネルも作れそう
    - Feature
        - UKB RAPでの専門用語
        - 事前に構築済みのカーネルの集合

## UKB-RAPへのアクセス

- [UK Biobank Research Analysis Platform](https://www.ukbiobank.ac.uk/enable-your-research/research-analysis-platform)
- [UKBioBank DNAnexus](https://ukbiobank.dnanexus.com/)

### ツール類
- [DNANexusのCLIツール](https://documentation.dnanexus.com/downloads)
    - APIキーの管理 はプロフィールページのTokensから行う
- ローカルのシェルスクリプトからAPI経由でコマンドを実行する？
    - [1](https://dnanexus.gitbook.io/uk-biobank-rap/getting-started/training-videos/general#how-to-create-an-app-workflow-and-bring-your-own-tools)
    - [2](https://dnanexus.gitbook.io/uk-biobank-rap/working-on-the-research-analysis-platform/running-analysis-jobs/command-line-interface)

## 使えるライブラリ

[UKB-RAP Tools library](https://dnanexus.gitbook.io/uk-biobank-rap/working-on-the-research-analysis-platform/running-analysis-jobs/tools-library)

- Genomicsのみ特有のツール
- それ以外（主要な統計、MRI等含む）は DXJupyterLab App (DNAnexus Platform App) 経由で使えというものが多い


**Youtube Tutorial**
- [Introduction to Jupyter Notebooks on UKB-RAP (youtube)](https://www.youtube.com/watch?v=YIPdhf3qbQA)
- [Exploring and Analyzing UK Biobank Data with Jupyter Notebooks](https://www.youtube.com/watch?v=jodNjrYF8po)
- [Building Applications for Efficient Analysis on UKB-RAP](https://www.youtube.com/watch?v=LC3JcBYj-Mo)



### ローカルにJupyterLab環境を立ち上げる時の使い方（我々は使用しない）
 
起動はVisual Studio Codeのターミナルから以下のコマンドを実行する。
なぜかVS Code以外のプロンプトからは成功しない。

```bash
python -m pip install jupyterlab
python -m jupyterlab
```
