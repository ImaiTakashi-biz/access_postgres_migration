"""Access → PostgreSQL移行処理の初期入口。"""

from __future__ import annotations

from pathlib import Path

from access_migration.access_reader import AccessReader
from access_migration.config import load_config
from access_migration.logger import setup_logger
from access_migration.postgres_writer import PostgresWriter


def run(env_file: str | Path | None = None) -> int:
    """移行処理を実行する。

    初期構築段階では実DB接続を行わず、設定読み込みと入力ファイル確認まで実施する。
    """

    config = load_config(env_file)
    logger = setup_logger(level=config.log_level)

    reader = AccessReader(config.access_db_path)
    writer = PostgresWriter(config.database_url)

    logger.info("移行処理を開始します")
    logger.info("PostgreSQL接続先: %s", writer.mask_database_url())
    logger.info("Access DBパス: %s", config.access_db_path)

    if not reader.validate_source_exists():
        logger.error("Access DBファイルが見つかりません: %s", config.access_db_path)
        return 1

    logger.info("初期確認が完了しました。移行ロジックは対象システムごとに追加してください。")
    return 0
