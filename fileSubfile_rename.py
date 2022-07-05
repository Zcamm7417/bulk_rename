from collections import deque
from pathlib import Path

FILTERS = ';;'.join(
    (
        'PNG Files(*.png)',
        'JPEG Files(*.jpeg)',
        'JPG Files(*.jpg)',
        'GIF Files(*.gif)',
        'Text Files(*.txt)',
        'python Files(*.py)',
    )
)
def main(self):
    #super().__init__()
    self._files = deque()
    self._filesCount = len(self._files)
    self._connectSignalsSlots()

def _connectSignalsSlots(self):
    self.loadFiles

def loadFiles(self):
    self.dstFileList.clear()
    if self.dirEdit.text():
        initDir = self.dirEdit.text()
    else:
        initDir = str(Path.home())
    #files, filter = QFileDialog.getOpenFileNames(
     #   self, 'choose files to rename', initDir, filter = FILTERS
    #)
    files, filter = input('Enter file', self, initDir, filter = FILTERS)
    if len(files)>0:
        fileExtension = filter[filter.index('*') : -1]
        self.extensionLabel.setText(fileExtension)
        scrDirName = str(Path(files[0]).parent)
        self.dirEdit.setText(scrDirName)
        for file in files:
            self._files.append(Path(file))
            #self.scrFileList.addItem(file)
            print(file)
        self._filesCount = len(self._files)
if main=='loadFiles':
    loadFiles()