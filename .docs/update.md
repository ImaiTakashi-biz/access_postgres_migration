# 更新履歴

## 2026-06-12

- Access → PostgreSQL移行プロジェクトの初期構成を作成。
- 環境確認スクリプト、設定読み込み、ログ初期化、移行入口を追加。
- `.docs/appearance_inspection_db` のAccess DBをPostgreSQLへ移行。
- 移行対応表、移行結果、移行ログ、再実行用スクリプトを追加。
- `.docs/delivery_label_search_db` のAccess DBをPostgreSQLへ移行。
- 汎用移行スクリプトをメタJSON自動検出と対象別対応表生成に対応。
- 移行用Pythonスクリプトを共通配置ではなく各対象フォルダ配下へ保存する運用に変更。
- `.docs/delivery_label_search_db/migrate_access_to_postgres_delivery_label_search_db.py` を現品票検索DB専用の処理に整理。
- `.docs/appearance_inspection_db/migrate_access_to_postgres_appearance_inspection_db.py` を外観検査記録DB専用の処理に整理。
- 外観検査記録DBの再確認で、Access本体更新に伴う3テーブルの件数差異を記録。
- 対象専用の移行スクリプト名に対象フォルダ名を含める命名へ変更。
- 外観検査記録DBの移行成果物名に `appearance_inspection_db` を含める命名へ変更。
- 現品票検索DBの移行成果物名に `delivery_label_search_db` を含める命名へ変更。
