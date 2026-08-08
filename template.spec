# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec, generic starting point. Rename to match your project and
# add datas/hiddenimports/collect_all(...) as your dependencies grow
# (see PyInvest.spec in the original project for a fuller example: icon,
# collect_all for pandas/openpyxl/ttkbootstrap, hidden-imports for selenium
# and bs4/lxml/html5lib).

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='template-python-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
