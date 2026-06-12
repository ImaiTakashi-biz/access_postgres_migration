"""開発・実行環境の初期確認スクリプト。"""

from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


REQUIRED_MODULES = {
    "dotenv": "python-dotenv",
    "pyodbc": "pyodbc",
    "psycopg2": "psycopg2-binary",
    "sqlalchemy": "SQLAlchemy",
    "pandas": "pandas",
    "openpyxl": "openpyxl",
}


def main() -> int:
    """環境確認を実行する。"""

    args = parse_args()
    checks = [
        check_python_version(),
        check_required_modules(),
        check_env(args.env_file),
    ]
    return 0 if all(checks) else 1


def parse_args() -> argparse.Namespace:
    """コマンドライン引数を解析する。"""

    parser = argparse.ArgumentParser(description="Access移行プロジェクトの環境確認")
    parser.add_argument("--env-file", help="読み込む.envファイルのパス")
    return parser.parse_args()


def check_python_version() -> bool:
    """Python 3.12系で実行されているか確認する。"""

    version = sys.version_info
    if version.major == 3 and version.minor == 12:
        print(f"[OK] Pythonバージョン: {sys.version.split()[0]}")
        return True

    print(f"[NG] Python 3.12系で実行してください。現在: {sys.version.split()[0]}")
    return False


def check_required_modules() -> bool:
    """requirements.txtの主要ライブラリがimportできるか確認する。"""

    succeeded = True
    for module_name, package_name in REQUIRED_MODULES.items():
        try:
            importlib.import_module(module_name)
            print(f"[OK] import確認: {package_name}")
        except ImportError:
            print(f"[NG] importできません: {package_name}")
            succeeded = False
    return succeeded


def check_env(env_file: str | None) -> bool:
    """設定ファイルから必須値を読み込めるか確認する。"""

    try:
        from access_migration.config import load_config

        config = load_config(env_file, allow_example=True)
    except ImportError as error:
        print(f"[NG] .env読み込みに必要なライブラリが不足しています: {error}")
        return False
    except (FileNotFoundError, ValueError) as error:
        print(f"[NG] .env読み込み: {error}")
        return False

    env_label = config.env_file if config.env_file else ".env未指定"
    print(f"[OK] .env読み込み: {env_label}")
    print(f"[OK] DATABASE_URL取得: {mask_database_url(config.database_url)}")
    print(f"[OK] ACCESS_DB_PATH取得: {config.access_db_path}")
    print(f"[OK] LOG_LEVEL取得: {config.log_level}")

    if config.env_file and config.env_file.name == ".env.example":
        print("[WARN] .envがないため.env.exampleで確認しました。実行時は対象フォルダの.envを指定してください。")

    return True


def mask_database_url(database_url: str) -> str:
    """表示用にDATABASE_URLのパスワードを伏せる。"""

    if "://" not in database_url or "@" not in database_url:
        return database_url

    scheme, rest = database_url.split("://", 1)
    credentials, host_part = rest.split("@", 1)
    user_name = credentials.split(":", 1)[0]
    return f"{scheme}://{user_name}:***@{host_part}"


if __name__ == "__main__":
    raise SystemExit(main())
