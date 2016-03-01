# ./python
# -*-coding: utf-8-*-

import os


class LZW:
    """LZW Compression"""

    def __init__(self, txt):
        self.txt = txt
        self.dic = {}
        self.index = 0
        self.buff = []
        self.printOn = True

        print '\n\tText:\t', self.txt, '\n'
        self.printTable('Index', 'Letra', 'Salida')  # Table

        for l in self.txt:
            if l not in self.buff:
                self.buff.append(l)

        self.buff.sort()
        for l in self.buff:
            if l not in self.dic:
                self.dic[l] = self.index = self.index + 1
                self.printTable(self.index, l, l)   # Table
        print

    def compression(self):

        index = 0
        while index < len(self.txt):
            l = self.txt[index]

            while l in self.dic and index + len(l) < len(self.txt):
                s = self.dic[l]
                l += self.txt[index + len(l)]

            index += len(l) - 1

            if l not in self.dic and l[-1] in self.dic:
                self.dic[l] = self.index = self.index + 1
                self.printTable(self.index, l, s)   # Table
                self.buff.append(s)
            # ------------ Delete -------------
            elif l not in self.dic and l[-1] not in self.dic:
                l = l[-1]
                self.dic[l] = self.index = self.index + 1
                self.printTable(self.index, l, l)   # Table
                self.buff.append(l)
            # ------------ Delete -------------
            else:  # if l in self.dic:
                self.printTable('NaN', 'NaN', self.dic[l])  # Table
                self.buff.append(self.dic[l])
                break

    def printTable(self, *str):
        if self.printOn:
            strs = ['%s' % s for s in str]
            for s in strs:
                if len(s) <= 6:
                    strs[strs.index(s)] += '\t'
            print '\t---\t %s \t---\t %s \t---\t %s \t---' % tuple(strs)

    def comprssionRate(self):
        newTxt = ''.join(['%s' % s for s in self.buff])
        print newTxt
        return '%.2f%%' % (100.0 * len(newTxt) / len(self.txt))


if __name__ == '__main__':

    text = 'wabba_wabba_wabba_wabba_woo_woo_woo'
    os.system('cls&mode con lines=150 cols=120')
    lzw = LZW(text)
    lzw.compression()
    print 'Compression Rate:', lzw.comprssionRate()
