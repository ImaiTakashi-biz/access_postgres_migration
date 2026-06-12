# Access → PostgreSQL 移行対応表

## 1. 移行概要

- 対象Access DB:
- 移行先PostgreSQL DB:
- 接続情報:
  - `.env` の `DATABASE_URL` を参照
- 移行日:
- 作成者:
- 備考:

## 2. 移行対象テーブル一覧

| No | Accessテーブル名 | PostgreSQLテーブル名 | 種別 | Access件数 | PostgreSQL件数 | 備考 |
|---:|---|---|---|---:|---:|---|

## 3. テーブル別カラム対応表

### Accessテーブル名:
### PostgreSQLテーブル名:

| No | Accessカラム名 | Access型 | PostgreSQLカラム名 | PostgreSQL型 | NULL許可 | 備考 |
|---:|---|---|---|---|---|---|

## 4. 主キー・インデックス情報

| Accessテーブル名 | PostgreSQLテーブル名 | 主キー | インデックス | 備考 |
|---|---|---|---|---|

## 5. 型変換ルール

| Access型 | PostgreSQL型 | 備考 |
|---|---|---|
| Short Text | varchar / text | 文字列 |
| Long Text | text | 長文 |
| Number | integer / numeric | 内容に応じて判断 |
| Date/Time | timestamp / date | 日付のみの場合はdate |
| Yes/No | boolean | True/False |
| Currency | numeric | 金額 |
| AutoNumber | serial / integer | 主キー候補 |

## 6. 注意事項・要確認事項

- 
