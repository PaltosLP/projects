

def determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix[0]) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

    if len(matrix) != 2:
        new_matrix = matrix[1::]
        res = 0
        for i in range(len(matrix[0])): 
            res_minor = list()
            for j in range(len(matrix[0])-1):
                minor_1 = new_matrix[j][0:i] + new_matrix[j][i+1::]
                res_minor.append(minor_1)
            # print(res_minor)
            
            res = res + (-1)**i * matrix[0][i] * determinant(res_minor)         

    return res




m0 = [[1]] #1
m1 = [ [1, 3], [2,5]] #-1
m2 = [ [2, 5, 3],
       [1,-2,-1],
       [1, 3, 4]] #-20


print(determinant(m2))  
#a*d - b*c

#[a b c]
#[d e f]
#[g h i]

#[a b c d]
#[e f g h]
#[i j k l]
#[m n o p]
