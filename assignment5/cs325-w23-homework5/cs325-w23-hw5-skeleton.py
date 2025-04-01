import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2, ci = 1, cd = 1, cm = 1):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        ci: The cost of an insertion (1 by default).
        cd: The cost of a deletion (1 by default).
        cm: The cost of a mutation (1 by default).
    
    Returns:
        The edit distance between s1 and s2.
    """

    # TODO: Implement this function!
    
    len_i = len(s1)
    len_j = len(s2)

    prev_row = [i for i in range(len_j + 1)]
    for i in range(1, len_i + 1):
        curr_row = [0 for i in range(len_j + 1)]
        curr_row[0] = i
        for j in range(1, len_j + 1):
            if (s1[i - 1] == s2[j - 1]):
                flex = 0
            else: flex = 1
            curr_row[j] = min(curr_row[j - 1] + 1, prev_row[j] + 1, prev_row[j - 1] + flex)
        prev_row = curr_row

    # print(curr_row[len_j])
    return curr_row[len_j]


    
def lcs(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """

    # TODO: Implement this function!
    m = len(s1)
    n = len(s2)
 
    L = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # print(L[m][n])
    return L[m][n]
    
def lcs3(s1, s2, s3):
    """
    Computes the length of the longest common subsequence between three strings: s1, s2, and s3.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The third string.
    
    Returns:
        The length of the longest common subsequence between s1, s2, and s3.
    """

    # TODO: Implement this function!
    m = len(s1)
    n = len(s2)
    p = len(s3)
 
    L = [[[0 for i in range (p + 1)] for j in range (n + 1)] for k in range (m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range (p + 1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif (s1[i-1] == s2[j-1]) and (s1[i-1] == s3[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k] , L[i][j-1][k], L[i][j][k-1])
 
    # print(L[m][n][k])
    return L[m][n][k]

s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
print(edit_distance(s1, s2))
print(lcs(s1, s2))

# s1 = "AGGCA"
# s2 = "CTTGA"
# s3 = "GTA"
# edit_distance(s1, s2)
# lcs(s1, s2)
# lcs3(s1, s2, s3)


# By running edit_distance(): 208
# By running lcs(): 29703