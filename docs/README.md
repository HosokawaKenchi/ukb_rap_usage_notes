# docs

## tree

UKB-RAP上のzipファイルを展開し，`tree`コマンドでディレクトリ構造を可視化した結果を`txt`ファイルで保存しています．
全てのファイルを展開することは不可能なので，各ディレクトリに保存されている一部のzipファイルに対して処理を行いました．

例えば，`docs/tree/mnt/project/Bulk/Brain MRI/Native atlases/10/1000011_31000_2_0.txt`に保存されているファイルの場合，UKB-RAP上の`/mnt/project/Bulk/Brain MRI/Native atlases/10/1000011_31000_2_0.zip`に保存されているzipファイルを展開した結果となります．

同じディレクトリにあるファイルでも，ファイル名に含まれる`Field ID`が異なる場合は中身が異なります．
例えば，`T1/10/1000011_20252_2_0.txt`と`T1/10/1000011_20263_2_0.txt`は，同じ`T1`ディレクトリに保存されていますが，それぞれ`Field ID`が`20252`と`20263`で異なるため，中身が違います．

`Field ID`と対応するデータについては[biobankの公式ドキュメント](https://dnanexus.gitbook.io/uk-biobank-rap/getting-started/data-structure/data-release-versions#bulk-fields-in-the-latest-release)を確認してください．

```code: bash
./docs/tree
└── mnt
    └── project
        └── Bulk
            └── Brain MRI
                ├── ASL
                │   └── 10
                │       ├── 1000205_20266_2_0.txt
                │       ├── 1000205_26300_2_0.txt
                │       ├── 1000464_20266_3_0.txt
                │       ├── 1000464_26300_3_0.txt
                │       ├── 1001710_20266_2_0.txt
                │       ├── 1001710_26300_2_0.txt
                │       ├── 1002539_20266_2_0.txt
                │       ├── 1002539_26300_2_0.txt
                │       ├── 1003425_20266_2_0.txt
                │       ├── 1003425_26300_2_0.txt
                │       └── 1003749_20266_3_0.txt
                ├── Connectomes
                │   └── 10
                │       ├── 1000011_31020_2_0.txt
                │       ├── 1000011_31021_2_0.txt
                │       ├── 1000011_31022_2_0.txt
                │       ├── 1000011_31023_2_0.txt
                │       ├── 1000011_31024_2_0.txt
                │       ├── 1000011_31025_2_0.txt
                │       ├── 1000011_31026_2_0.txt
                │       ├── 1000011_31027_2_0.txt
                │       ├── 1000011_31028_2_0.txt
                │       ├── 1000135_31020_2_0.txt
                │       ├── 1000135_31021_2_0.txt
                │       └── 1000135_31022_2_0.txt
                ├── Functional time series
                │   └── 10
                │       ├── 1000011_31014_2_0.txt
                │       ├── 1000011_31015_2_0.txt
                │       ├── 1000011_31016_2_0.txt
                │       ├── 1000011_31017_2_0.txt
                │       ├── 1000011_31018_2_0.txt
                │       ├── 1000011_31019_2_0.txt
                │       ├── 1000135_31014_2_0.txt
                │       ├── 1000135_31015_2_0.txt
                │       ├── 1000135_31016_2_0.txt
                │       ├── 1000135_31017_2_0.txt
                │       ├── 1000135_31018_2_0.txt
                │       └── 1000135_31019_2_0.txt
                ├── Native atlases
                │   └── 10
                │       ├── 1000011_31000_2_0.txt
                │       ├── 1000135_31000_2_0.txt
                │       ├── 1000162_31000_2_0.txt
                │       ├── 1000239_31000_2_0.txt
                │       ├── 1000261_31000_2_0.txt
                │       ├── 1000261_31000_3_0.txt
                │       ├── 1000371_31000_2_0.txt
                │       ├── 1000437_31000_2_0.txt
                │       ├── 1000445_31000_2_0.txt
                │       └── 1000464_31000_2_0.txt
                ├── Native atlases (Diffusion)
                │   └── 10
                │       ├── 1000011_31001_2_0.txt
                │       ├── 1000011_31002_2_0.txt
                │       ├── 1000011_31003_2_0.txt
                │       ├── 1000011_31004_2_0.txt
                │       ├── 1000011_31005_2_0.txt
                │       ├── 1000011_31006_2_0.txt
                │       ├── 1000011_31007_2_0.txt
                │       ├── 1000011_31008_2_0.txt
                │       ├── 1000135_31001_2_0.txt
                │       ├── 1000135_31002_2_0.txt
                │       ├── 1000135_31003_2_0.txt
                │       ├── 1000135_31004_2_0.txt
                │       └── 1000135_31005_2_0.txt
                ├── Native atlases (Structural and functional)
                │   └── 10
                │       ├── 1000011_31009_2_0.txt
                │       ├── 1000011_31010_2_0.txt
                │       ├── 1000011_31011_2_0.txt
                │       ├── 1000011_31012_2_0.txt
                │       ├── 1000011_31013_2_0.txt
                │       ├── 1000135_31009_2_0.txt
                │       ├── 1000135_31010_2_0.txt
                │       ├── 1000135_31011_2_0.txt
                │       ├── 1000135_31012_2_0.txt
                │       ├── 1000135_31013_2_0.txt
                │       ├── 1000162_31009_2_0.txt
                │       └── 1000162_31010_2_0.txt
                ├── SWI
                │   └── 10
                │       ├── 1000011_20219_2_0.txt
                │       ├── 1000011_20251_2_0.txt
                │       ├── 1000022_20219_2_0.txt
                │       ├── 1000135_20219_2_0.txt
                │       ├── 1000135_20251_2_0.txt
                │       ├── 1000162_20219_2_0.txt
                │       ├── 1000162_20251_2_0.txt
                │       ├── 1000205_20219_2_0.txt
                │       ├── 1000205_20251_2_0.txt
                │       ├── 1000239_20219_2_0.txt
                │       └── 1000239_20251_2_0.txt
                ├── Scout
                │   └── 10
                │       ├── 1000011_20224_2_0.txt
                │       ├── 1000022_20224_2_0.txt
                │       ├── 1000135_20224_2_0.txt
                │       ├── 1000162_20224_2_0.txt
                │       ├── 1000205_20224_2_0.txt
                │       ├── 1000239_20224_2_0.txt
                │       ├── 1000261_20224_2_0.txt
                │       ├── 1000261_20224_3_0.txt
                │       ├── 1000371_20224_2_0.txt
                │       ├── 1000437_20224_2_0.txt
                │       ├── 1000445_20224_2_0.txt
                │       ├── 1000464_20224_2_0.txt
                │       ├── 1000464_20224_3_0.txt
                │       ├── 1000486_20224_2_0.txt
                │       └── 1000529_20224_2_0.txt
                ├── Surface-based analysis of resting and task fMRI
                │   └── 10
                │       ├── 1000011_32136_2_0.txt
                │       ├── 1000135_32136_2_0.txt
                │       ├── 1000162_32136_2_0.txt
                │       ├── 1000205_32136_2_0.txt
                │       ├── 1000239_32136_2_0.txt
                │       ├── 1000261_32136_2_0.txt
                │       ├── 1000261_32136_3_0.txt
                │       ├── 1000371_32136_2_0.txt
                │       └── 1000437_32136_2_0.txt
                ├── Susceptibility weighted brain MRI
                │   └── 10
                │       ├── 1000011_26301_2_0.txt
                │       ├── 1000135_26301_2_0.txt
                │       ├── 1000162_26301_2_0.txt
                │       ├── 1000205_26301_2_0.txt
                │       ├── 1000239_26301_2_0.txt
                │       ├── 1000261_26301_2_0.txt
                │       ├── 1000261_26301_3_0.txt
                │       ├── 1000371_26301_2_0.txt
                │       ├── 1000445_26301_2_0.txt
                │       ├── 1000464_26301_2_0.txt
                │       ├── 1000464_26301_3_0.txt
                │       ├── 1000486_26301_2_0.txt
                │       └── 1000529_26301_2_0.txt
                ├── T1
                │   └── 10
                │       ├── 1000011_20252_2_0.txt
                │       ├── 1000011_20263_2_0.txt
                │       ├── 1000135_20252_2_0.txt
                │       ├── 1000135_20263_2_0.txt
                │       ├── 1000162_20252_2_0.txt
                │       ├── 1000162_20263_2_0.txt
                │       ├── 1000205_20252_2_0.txt
                │       ├── 1000239_20252_2_0.txt
                │       ├── 1000239_20263_2_0.txt
                │       ├── 1000261_20252_2_0.txt
                │       ├── 1000261_20252_3_0.txt
                │       ├── 1000261_20263_2_0.txt
                │       ├── 1000261_20263_3_0.txt
                │       ├── 1000371_20252_2_0.txt
                │       ├── 1000371_20263_2_0.txt
                │       ├── 1000437_20252_2_0.txt
                │       └── 1000437_20263_2_0.txt
                ├── T2 FLAIR
                │   └── 10
                │       ├── 1000011_20253_2_0.txt
                │       ├── 1000135_20253_2_0.txt
                │       ├── 1000162_20253_2_0.txt
                │       ├── 1000205_20253_2_0.txt
                │       ├── 1000239_20253_2_0.txt
                │       ├── 1000261_20253_2_0.txt
                │       ├── 1000261_20253_3_0.txt
                │       ├── 1000371_20253_2_0.txt
                │       ├── 1000437_20253_2_0.txt
                │       ├── 1000445_20253_2_0.txt
                │       ├── 1000464_20253_2_0.txt
                │       ├── 1000464_20253_3_0.txt
                │       ├── 1000486_20253_2_0.txt
                │       ├── 1000529_20253_2_0.txt
                │       ├── 1000556_20253_2_0.txt
                │       ├── 1000625_20253_2_0.txt
                │       ├── 1000669_20253_2_0.txt
                │       ├── 1000694_20253_2_0.txt
                │       ├── 1000744_20253_2_0.txt
                │       └── 1000758_20253_2_0.txt
                ├── dMRI
                │   └── 10
                │       ├── 1000011_20218_2_0.txt
                │       ├── 1000011_20250_2_0.txt
                │       ├── 1000022_20218_2_0.txt
                │       ├── 1000135_20218_2_0.txt
                │       ├── 1000135_20250_2_0.txt
                │       ├── 1000162_20218_2_0.txt
                │       ├── 1000162_20250_2_0.txt
                │       ├── 1000205_20218_2_0.txt
                │       └── 1000205_20250_2_0.txt
                ├── rfMRI
                │   └── 10
                │       ├── 1010767_20225_2_0.txt
                │       ├── 1012813_20225_2_0.txt
                │       ├── 1016470_20227_2_0.txt
                │       ├── 1037614_20225_2_0.txt
                │       ├── 1041760_20227_2_0.txt
                │       ├── 1046855_20227_3_0.txt
                │       ├── 1065417_20227_2_0.txt
                │       ├── 1065572_20225_2_0.txt
                │       ├── 1073531_20225_2_0.txt
                │       └── 1086378_20225_2_0.txt
                └── tfMRI
                    └── 10
                        ├── 1000011_20217_2_0.txt
                        ├── 1000011_20249_2_0.txt
                        ├── 1000022_20217_2_0.txt
                        ├── 1000135_20217_2_0.txt
                        ├── 1000135_20249_2_0.txt
                        ├── 1000162_20217_2_0.txt
                        ├── 1000162_20249_2_0.txt
                        ├── 1000205_20217_2_0.txt
                        ├── 1000205_20249_2_0.txt
                        ├── 1000239_20217_2_0.txt
                        └── 1000239_20249_2_0.txt
```