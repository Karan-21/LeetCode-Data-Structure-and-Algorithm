class Spreadsheet(object):

    def __init__(self, rows):
        self.rows=rows
        self.header=[chr(65+i) for i in range(26)]
        self.sheet=[self.header]
        for i in range(self.rows):
          self.sheet.append([0 for j in range(26)])
        
    def setCell(self,  value,val):
        self.sheet[int(value[1:])][ord(value[0])-65]=val
        
    def resetCell(self, cell):
        self.setCell(cell,0)
    
    def getValue(self, formula):
        entity=formula[1:].split("+")
        print(entity)
        val=[]
        for i in entity:
          if i[0].isnumeric():
            val.append(int(i))
          else:
            val.append(self.sheet[int(i[1:])][ord(i[0])-65])
            
          
        return sum(val)
