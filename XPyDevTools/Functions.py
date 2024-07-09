import os

class Functions:
    def __init__(self,func):
        file = ''
        self.filepath = os.path.__all__
        print(self.filepath)
        self.func = func
        self.funcname = func.__name__
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
            self.func()
        except IndentationError:
            print("There\'s an Indentation Error.")
        except SyntaxError:
            print('Rewrite Code.')
        except ImportError:
            print("There\'s an error while importing.")

        
            
        
        