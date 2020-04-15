''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    t = int(input())
    for i in range(t):
        vowels = 0
        consonants = 0
        st1 = str(input())
        for i in st1:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    
        print(str(vowels) , str(consonants) , str(vowels*consonants) )
main()

