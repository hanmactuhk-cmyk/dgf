# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

PROJECT_ROOT = Path(SPECPATH)

MAIN_FILE = PROJECT_ROOT / "desktop" / "main.py"
ASSETS_DIR = PROJECT_ROOT / "assets"
DATA_DIR = PROJECT_ROOT / "data"

a = Analysis(
    [str(MAIN_FILE)],

    pathex=[
        str(PROJECT_ROOT),
        str(PROJECT_ROOT / "desktop"),
    ],

    binaries=[],

    datas=[
        (str(ASSETS_DIR), "assets"),
        (str(DATA_DIR), "data"),
    ],

    hiddenimports=[
        "desktop",
        "desktop.main",

        "desktop.ui",
        "desktop.ui.app",

        "desktop.services",
        "desktop.services.backend",
        "desktop.services.job_manager",
        "desktop.services.bridge",
    ],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(
    a.pure
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],

    name="Hn38videoAItool",

    debug=False,
    bootloader_ignore_signals=False,

    strip=False,

    # Tắt UPX để tránh lỗi build trên một số runner
    upx=False,

    # Không hiện cửa sổ console khi chạy EXE
    console=False,
)
