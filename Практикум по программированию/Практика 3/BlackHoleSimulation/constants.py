c = 30
G = 2
dt = 0.5

def multVector (vector, n):
    for i in range(len(vector)):
        vector[i] *= n
    return vector

def lengthVector(vector):
    length = 0
    for i in range(len(vector)):
        length += vector[i] ** 2
    length = length ** 0.5
    return length

def normalizeVector(vector):
    length = lengthVector(vector)
    inv_length = 1 / length
    vector = multVector(vector, inv_length)
    return vector

def addVector (vector1, vector2):
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i]+vector2[i])
    return vector_result

def subVector (vector1, vector2):
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i]-vector2[i])
    return vector_result