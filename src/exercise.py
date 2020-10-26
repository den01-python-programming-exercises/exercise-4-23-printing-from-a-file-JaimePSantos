def main():
    #write your code below this line
    with open("data.txt", 'r') as f:
      lines = f.read().splitlines()
    
    for line in lines:
      print(line)

if __name__ == '__main__':
    main()
