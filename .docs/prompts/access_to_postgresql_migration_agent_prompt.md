# Access → PostgreSQL 移行エージェント用プロンプト

## 目的

指定されたAccess DB（.accdb / .mdb）を解析し、PostgreSQLへ安全に移行するための設計・実装・検証を行う。

## 重要ルール

- Access側の元データは勝手に削除・統合・加工しない。
- 不明な項目は推測で確定せず、移行対応表に「要確認」として残す。
- PostgreSQL側では日本語テーブル名・日本語カラム名を避け、意味が追跡できる英語名またはローマ字名に変換する。
- `.env` の `DATABASE_URL` と `ACCESS_DB_PATH` を参照する。
- 移行後は件数比較、エラー記録、移行対応表の更新を行う。

## 成果物

- `migration_mapping.md`
- `migration_result.md`
- `migration_error.log`
- 必要に応じた移行スクリプト
