import os

class Functions:
    def __init__(self,func):
        try:
            if self.func:
                
                if self.filepath :
                    self.funcname = func.__name__
                    self.func = func
                else:
                    self.funcname = func.__name__
                    self.func = func
            else:
                self.func = func
                
        except AttributeError:
            self.func = func
            pass
                
    def init(self,FilePath):
        self.filepath = FilePath
        if os.path.exists(self.filepath):
            pass
        else:
            print('file doesn\'t exists.')
    def run(self):
        self.func()
    def timer(self):
        import time
        start = time.time()
        self.func()
        end = time.time()
        self.sec = start / end
        print(f'sec:{self.sec}')
    def debug(self):
        try:
            with open(self.filepath,'r') as ff:
                ffl = ff.readlines()
                found = False
                ind = 0
                for i in range(len(ffl)):
                    if ffl[i] == '@Functions\n':
                        ind = i
                        found = True
                    else:
                        continue
                print(ffl[ind:len(ffl)])
        finally:
            pass 
# except:
#            print('You must Init your function.')
        
        
        try:
            self.func()
        except IndentationError:
            print("There\'s an Indentation Error.")
        except SyntaxError:
            print('Rewrite Code.')
        except ImportError:
            print("There\'s an error while importing.")

        
            
        
        