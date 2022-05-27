def find_anagram(word, anagram):
    word =input("Word:")
    anagram =input("Anagram:")

    if sorted(word) == sorted(anagram):
        print("True")
    else: 
	    print("False")
find_anagram("word", "anagram")
