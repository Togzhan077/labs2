class Stringm:
    def __init__(self):
        self.input_string = ""
    
    def getstring(self):
        self.input_string = input("Enter a  string: ")
        
    def printstring(self):
        print(self.input_string.upper())
        
string_obj = Stringm()
string_obj.getstring()
string_obj.printstring()