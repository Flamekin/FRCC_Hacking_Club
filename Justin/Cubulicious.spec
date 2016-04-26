# -*- mode: python -*-

block_cipher = None


a = Analysis(['cubulicious.py'],
             pathex=['C:\\Users\\justin.brown\\Desktop\\GitHub\\FRCC_Hacking_Club\\Justin'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('Images/background.png', 'C:\\Users\\justin.brown\\Desktop\\GitHub\\FRCC_Hacking_Club\\Justin\\Images\\background.png', 'DATA'),
('Images/cube.png', 'C:\\Users\\justin.brown\\Desktop\\GitHub\\FRCC_Hacking_Club\\Justin\\Images\\cube.png','DATA'),
('Images/icon.png', 'C:\\Users\\justin.brown\\Desktop\\GitHub\\FRCC_Hacking_Club\\Justin\\Images\\icon.png','DATA'),
('Audio/main.ogg', 'C:\\Users\\justin.brown\\Desktop\\GitHub\\FRCC_Hacking_Club\\Justin\\Audio\\main.ogg','DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Cubulicious',
          debug=False,
          strip=False,
          upx=True,
          console=False)
