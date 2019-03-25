import os
from src.osdir import all_path
from src._jieba import split
from src._wordcloud import outputwordcloud
from src.utility import readattachment


class CloudGenerator():
    def __init__(self, sourceDir,  background, outputDir, maxwords):
        super().__init__()
        self.sourceDir = sourceDir
        self.background = background
        self.outputDir = outputDir
        self.maxwords = maxwords
        self.splittedContent = ''
        
    def readAndGenerate(self):
        self.readOnly()
        self.generateOnly()
            
    def readOnly(self):
        if os.path.exists(self.sourceDir):
            print('Reading files from ' + self.sourceDir)
            self.sourceDir = self.sourceDir.replace('/',  '\\')
            filePaths = all_path(self.sourceDir)
            readattachment(filePaths)
            print('正在分词')
            self.splittedContent = split()
            print('分词完成')
        else:
            self.trigger.emit('No such directory!')
        
    def generateOnly(self):
        #self.trigger.emit('正在生成图片')
        outputwordcloud(self.splittedContent, self.background,  self.outputDir, self.maxwords)
        #self.trigger.emit('图片已保存')
    
    def update(self, sourceDir,  background, outputDir, maxwords):
        self.sourceDir = sourceDir
        self.background = background
        self.outputDir = outputDir
        self.maxwords = maxwords
