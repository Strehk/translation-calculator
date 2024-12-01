# -*- mode: python ; coding: utf-8 -*-
import os

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('base_values.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

version = os.getenv('APP_VERSION', '0.0.0')

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Translation Calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Ensure this is set to True
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version_info={
        'FileVersion': version,
        'ProductVersion': version,
        'FileDescription': 'Translation Calculator',
        'CompanyName': 'Tade Strehk',
        'ProductName': 'Translation Calculator',
    },
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Translation Calculator'
)

app = BUNDLE(
    coll,
    name='Translation-Calculator.app',
    icon="img/icon.icns",
    bundle_identifier=None
)
