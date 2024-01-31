"""
There is an array of integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like allthe integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. For each i integer in the array,
ifi € A, you add 1 to your happiness. 
If i € B, you add - 1 to your happiness. Otherwise, your happiness does
not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate
elements.

Constraints
1 <= n <= 105
1 <= m <= 105
1 Any integer in the input 10

Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Sample Input:
3 2
1 5 3
3 1
5 7

Sample Output:
1
"""

def happy_counter(arr: list, A: set, B: set)-> int:
    happy_score = 0
    for i in arr:
        if i in A:
            happy_score += 1
            
        elif i in B:
            happy_score -= 1
            
        else:
            pass
    print(happy_score)
    

if __name__ == '__main__':
    n,m = map(int, (input().split()))
    arr = list(map(int, (input().split()))) #len arr == n  
    A = set(map(int, (input().split()))) #len A == m
    B = set(map(int, (input().split()))) #len B == m
    happy_counter(arr,A,B)