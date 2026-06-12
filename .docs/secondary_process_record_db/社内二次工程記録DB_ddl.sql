-- PostgreSQL DDL 草案（Access メタデータから自動生成）
-- ※ 型・制約は必ず手動で確認・修正してください

CREATE TABLE "t_カゴマスタ" (
    "コード" VARCHAR(2),
    "カゴ" VARCHAR(4)
);


CREATE TABLE "t_バフ記録" (
    "ID" BIGSERIAL,
    "作業日" TIMESTAMP,
    "品番" VARCHAR(30),
    "品名" VARCHAR(30),
    "客先" VARCHAR(30),
    "材質" VARCHAR(35),
    "製造日" TIMESTAMP,
    "製造日2" VARCHAR(30),
    "号機" VARCHAR(5),
    "数量" INTEGER,
    "作業者" VARCHAR(6),
    "作業者2" VARCHAR(6),
    "時間" INTEGER,
    "作業終了日" TIMESTAMP,
    "備考" VARCHAR(20)
);


CREATE TABLE "t_ブラスト記録" (
    "ID" BIGSERIAL,
    "作業日" TIMESTAMP,
    "品番" VARCHAR(30),
    "品名" VARCHAR(30),
    "客先" VARCHAR(30),
    "材質" VARCHAR(35),
    "製造日" TIMESTAMP,
    "製造日2" VARCHAR(30),
    "号機" VARCHAR(5),
    "数量" INTEGER,
    "作業者" VARCHAR(6),
    "処理時間" INTEGER,
    "圧力" VARCHAR(8),
    "次工程" VARCHAR(8),
    "カゴ" VARCHAR(4),
    "備考" VARCHAR(20)
);


CREATE TABLE "t_作業マスタ" (
    "作業コード" VARCHAR(2),
    "作業名" VARCHAR(15)
);


CREATE TABLE "t_作業者マスタ" (
    "コード" VARCHAR(2),
    "作業者名" VARCHAR(6),
    "退職" VARCHAR(1)
);


CREATE TABLE "t_使用ピンマスタ" (
    "コード" VARCHAR(2),
    "ピン" VARCHAR(5)
);


CREATE TABLE "t_回転方向マスタ" (
    "コード" VARCHAR(2),
    "回転方向" VARCHAR(8)
);


CREATE TABLE "t_圧力マスタ" (
    "コード" VARCHAR(2),
    "圧力" VARCHAR(8)
);


CREATE TABLE "t_機番マスタ" (
    "機械ID" VARCHAR(3),
    "機番" VARCHAR(5)
);


CREATE TABLE "t_次工程マスタ" (
    "コード" VARCHAR(2),
    "次工程" VARCHAR(10)
);


CREATE TABLE "t_洗浄工程日報" (
    "ID" BIGSERIAL,
    "日付" TIMESTAMP,
    "曜日" VARCHAR(1),
    "作業者コード" VARCHAR(2),
    "作業コード1" VARCHAR(2),
    "作業コード2" VARCHAR(2),
    "作業コード3" VARCHAR(2),
    "作業コード4" VARCHAR(2),
    "作業コード5" VARCHAR(2),
    "作業コード6" VARCHAR(2),
    "作業コード7" VARCHAR(2),
    "作業コード8" VARCHAR(2),
    "作業コード9" VARCHAR(2),
    "作業コード10" VARCHAR(2),
    "作業コード11" VARCHAR(2),
    "作業コード12" VARCHAR(2),
    "作業コード13" VARCHAR(2),
    "作業コード14" VARCHAR(2),
    "作業コード15" VARCHAR(2),
    "作業コード16" VARCHAR(2),
    "作業コード17" VARCHAR(2),
    "作業コード18" VARCHAR(2)
);


CREATE TABLE "t_研磨石マスタ" (
    "コード" VARCHAR(2),
    "研磨石" VARCHAR(10)
);


CREATE TABLE "t_磁気バレル記録" (
    "ID" BIGSERIAL,
    "作業日" TIMESTAMP,
    "品番" VARCHAR(30),
    "品名" VARCHAR(30),
    "客先" VARCHAR(30),
    "材質" VARCHAR(35),
    "製造日" TIMESTAMP,
    "製造日2" VARCHAR(30),
    "号機" VARCHAR(5),
    "数量" INTEGER,
    "作業者" VARCHAR(6),
    "使用ピン" VARCHAR(5),
    "回転方向" VARCHAR(8),
    "回転数" INTEGER,
    "時間" INTEGER,
    "作業LOT" INTEGER,
    "備考" VARCHAR(20)
);


CREATE TABLE "t_製品マスタ" (
    "品番" VARCHAR(30),
    "品名" VARCHAR(30),
    "客先" VARCHAR(30),
    "材質材料径" VARCHAR(30),
    "ID" VARCHAR(6)
);


CREATE TABLE "t_遠心バレル記録" (
    "ID" BIGSERIAL,
    "作業日" TIMESTAMP,
    "品番" VARCHAR(30),
    "品名" VARCHAR(30),
    "客先" VARCHAR(30),
    "材質" VARCHAR(35),
    "製造日" TIMESTAMP,
    "製造日2" VARCHAR(30),
    "号機" VARCHAR(5),
    "数量" INTEGER,
    "作業者" VARCHAR(6),
    "研磨石1" VARCHAR(10),
    "時間1" INTEGER,
    "研磨石2" VARCHAR(10),
    "時間2" INTEGER,
    "備考" VARCHAR(20)
);

