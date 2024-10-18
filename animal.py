import sys

def dog():
    print('bow')

def default():
    print('hello')

def main():
    if sys.argv[1]=='cat':
        dog()
    else:
        default()

if __name__ =='__main__':
   main() 
