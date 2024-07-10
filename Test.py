from XPyDevTools.Functions import Functions
import inspect

@Functions
def main(name):
    print('Test')
print('Test')
    print('Test')

main.init(__file__)
main.debug()
