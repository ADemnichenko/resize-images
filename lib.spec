# -*- mode: python -*-

block_cipher = None


a = Analysis(['lib', 'not', 'found:', 'Qt5Gui.dll', 'dependency', 'of', os.path.join(HOMEPATH,'PyQt5\\QtGui.pydresize_images.py')],
             pathex=['WARNING:', 'D:\\Demnichenko\\Programming\\resize_image\\resize_image'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='lib',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='lib')
