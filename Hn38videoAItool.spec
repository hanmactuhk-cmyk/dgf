# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project = Path(SPECPATH)

a = Analysis(
    [str(project / "desktop" / "main.py")],
    pathex=[str(project)],
    binaries=[],
    datas=[
        (str(project / "assets"), "assets"),
        (str(project / "data"), "data"),
    ],
    hiddenimports=[
        "desktop",
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

pyz = PYZ(a.pure)

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
    upx=True,
    console=False,
)
