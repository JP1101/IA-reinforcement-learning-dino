def ReLu(x):
    return max(0, x)

def Calculate_Neurone(x1, x2, x3, w1, w2, w3, b):
    y = ReLu(x1 * w1 + x2 * w2 + x3 * w3 + b)
    return y
def Calculate_Output(x1,x2,x3,x4,x5, w1,w2,w3,w4,w5,b):
    y = ReLu(x1*w1 + x2*w2 + x3*w3 + x4*w4 + x5*w5 + b)
    return y


w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,      1,1,1,1,1]
bias = 1
input = [-1, 1, 1]
x = []
output = [0]

def Actualize_Neurones(input, w, bias):
    updated_values = [
        Calculate_Neurone(input[0], input[1], input[2], w[i], w[i+1], w[i+2], bias)
        for i in range(0, len(w)-2, 3)
    ]
    return updated_values


def Actualize_Result(x, w, b):
    result = Calculate_Output(x[1], x[2], x[3], x[4], x[5], w[26], w[27], w[28], w[29], w[30], b)
    return result




x = Actualize_Neurones(input, w, bias)
print(x)
output = Actualize_Result(x, w, bias)
print(output)