import inspect
import os

class Functions:
    def __init__(self,func,*args, **kwargs):
        try:
            if self.func:
            
                if self.filepath :
                    self.funcname = func.__name__
                    self.func = func
                    self.args = inspect.getfullargspec(self.func).args
                else:
                    self.funcname = func.__name__
                    self.args = inspect.getfullargspec(self.func).args
                    self.func = func
            else:
                self.funcname = func.__name__
                self.func = func
                self.args = inspect.getfullargspec(self.func).args
                
        except AttributeError:
            self.funcname = func.__name__
            self.func = func
            self.args = inspect.getfullargspec(self.func).args
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
                d =1
                x=1
                fu = f'def {self.funcname}({self.args[0]}):\n'
                fuend =False
                for x in range(len(ffl[ind:len(ffl)])):
                    if x == 1 :
                        if ffl[ind+x] == fu:
                            print("def without errors")
                        else:
                            print(ffl[ind+x])
                            print('Error\n')
                            print(fu)
                        break
                    elif x <= 2:
                        if fuend == False and ffl[ind+x][0:5] == '    ':
                            print('indentation good!')
                            continue
                        else:
                            fuend =True
                        if fuend == True and ffl[ind+x][0:5] == '    ':
                            print(f"{len(ffl) - ind+x}{ffl[ind+x - 1]} ")
                        else:
                            print(f"Function {self.funcname} without errors for now.:)")                  
        except AttributeError as AE:
            print(AE)
            print('DEBUGERROR:You must Init your function.')
        
        
        #try:
        #    self.func()
        #except IndentationError:
        #    print("There\'s an Indentation Error.")
        #except SyntaxError:
        #    print('Rewrite Code.')
        #except ImportError:
        #    print("There\'s an error while importing.")

        
            
        
        