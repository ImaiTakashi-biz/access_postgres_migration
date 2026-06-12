"""環境変数と.envファイルから設定を読み込む。"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


DEFAULT_LOG_LEVEL = "INFO"


@dataclass(frozen=True)
class AppConfig:
    """移行処理で共通利用する設定。"""

    database_url: str
    access_db_path: Path
    log_level: str = DEFAULT_LOG_LEVEL
    env_file: Path | None = None


def load_config(env_file: str | Path | None = None, *, allow_example: bool = False) -> AppConfig:
    """指定された.envから設定を読み込む。

    allow_example=True の場合だけ、.envが存在しないときに.env.exampleを確認用として使用する。
    """

    env_path = resolve_env_file(env_file, allow_example=allow_example)
    if env_path is not None:
        load_dotenv(env_path, override=False)

    database_url = os.getenv("DATABASE_URL", "").strip()
    access_db_path = os.getenv("ACCESS_DB_PATH", "").strip()
    log_level = os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL).strip().upper()

    missing_keys = [
        key
        for key, value in {
            "DATABASE_URL": database_url,
            "ACCESS_DB_PATH": access_db_path,
        }.items()
        if not value
    ]
    if missing_keys:
        joined_keys = ", ".join(missing_keys)
        raise ValueError(f"必須設定が不足しています: {joined_keys}")

    return AppConfig(
        database_url=database_url,
        access_db_path=Path(access_db_path),
        log_level=log_level or DEFAULT_LOG_LEVEL,
        env_file=env_path,
    )


def resolve_env_file(env_file: str | Path | None = None, *, allow_example: bool = False) -> Path | None:
    """読み込み対象の.envファイルを決定する。"""

    if env_file:
        path = Path(env_file)
        if not path.exists():
            raise FileNotFoundError(f".envファイルが見つかりません: {path}")
        return path

    default_env = Path(".env")
    if default_env.exists():
        return default_env

    example_env = Path(".env.example")
    if allow_example and example_env.exists():
        return example_env

    return None
