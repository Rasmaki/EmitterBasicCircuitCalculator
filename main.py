import numpy as np
userInput = [0, 0, 0, 0, 0, 0, 0]
strArrayInput = ["Is [A]", "B", "Rc [Ω]", "Ub [V]", "Ir2/Ib", "Ut [V]", "Round by how many digits?"]
strArrayOutput = ["Uout", "Ic", "Ib", "Ir2", "Ube", "R2", "Ur1", "Ir1", "R1"]


def calc(i_s, b, r_c, u_b, factor_ir2, u_t, index):
    u_out = u_b/2
    i_c = (u_b-u_out)/r_c
    i_b = i_c/b
    i_r2 = factor_ir2 * i_b
    u_be = np.log((i_b/i_s)*b)*u_t
    r_2 = u_be/i_r2
    u_r1 = u_b - u_be
    i_r1 = i_r2 + i_b
    r_1 = u_r1/i_r1
    index = int(index)
    calc_array = np.around([u_out, i_c, i_b, i_r2, u_be, r_2, u_r1, i_r1, r_1], index)
    return calc_array


print("Emitter Basic Circuit Calculator")
print("Please use this format of scientific notation if needed: Example: 1e-08")

for i in range(7):
    userInput[i] = float(input("Type Value for " + strArrayInput[i] + " = "))

print("Finished!")
for j in range(9):
    print(strArrayOutput[j] + " = " + str(calc(userInput[0], userInput[1], userInput[2], userInput[3], userInput[4],
                                               userInput[5], userInput[6])[j]))
