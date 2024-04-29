# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Taap.py'],
    pathex=[],
    binaries=[],
    datas=[('car.png', '.'), ('All_TrafficAccident.csv', '.'), ('무면허_시간별_re.csv', '.'), ('음주_시간별_re.csv', '.'), ('어린이_시간별.csv', '.'), ('연도_나이_무면허.csv', '.'), ('연도_나이_음주.csv', '.'), ('연도_나이_어린이.csv', '.'), ('1.png', '.'), ('2.png', '.'), ('3.png', '.'), ('4.png', '.'), ('5.png', '.'), ('6.png', '.'), ('7.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Taap',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['car.ico'],
)
