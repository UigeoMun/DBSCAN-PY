# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dbscan1d.py'],
             pathex=['/home/yaeger/Documents/repositroy/deepbio/gencurix/ddAnalyzer/src/py'],
             binaries=[],
             datas=[],
             hiddenimports=['cython','sklearn', 'sklearn.neighbors.typedefs', 'sklearn.utils._cython_blas', 'sklearn.neighbors.quad_tree', 'sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='dbscan1d',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
