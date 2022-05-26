def find_anagrams(str1, str2):
    str1 =input("String 1:")
    str2 =input("String 2:")

    if sorted(str1) == sorted(str2):
        print("True")
    else: 
	    print("False")
find_anagrams("str1", "str2")
