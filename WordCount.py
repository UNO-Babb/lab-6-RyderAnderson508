#WordCount.py
#Name:Ryder Anderson
#Date:02/27/2025
#Assignment:Lab 06

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0 
  wordCount = 0 
  letterCount = 0

  for line in textFile:
  
    lineCount = lineCount + 1
    words = line.split()
    print(words)
    for w in words:
      wordCount = wordCount + 1

    #print(line)
  
  print("lines" , lineCount)
  print("words" , wordCount)
if __name__ == '__main__':
  main()
