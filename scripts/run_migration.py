"""移行処理を手動実行するためのスクリプト。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from access_migration.main import run  # noqa: E402


def main() -> int:
    """移行処理を実行する。"""

    parser = argparse.ArgumentParser(description="Access DBからPostgreSQLへの移行を実行")
    parser.add_argument("--env-file", required=True, help="移行対象フォルダ内の.envファイル")
    args = parser.parse_args()
    return run(args.env_file)


if __name__ == "__main__":
    raise SystemExit(main())
