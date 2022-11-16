import numpy as np
userInput = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
strArrayInput = ["Is [A]", "B", "Rc [Ω]", "Ub [V]", "Ir2/Ib", "Ut [V]", "Uearly [v]", "Vu", "Ri [Ω]", "Rl [Ω]",
                 "Fs", "Round by how many digits?"]
strArrayOutput = ["Uout", "Re", "Ic", "Ib", "Ir2", "Ube", "Ur2", "R2", "Ur1", "Ir1", "R1", "Fg", "Rbe", "Rin", "Rce",
                  "Rout", "Cin", "Cout", "Alpha", "Beta", "Amp-Factor"]


def calc(i_s, b, r_c, u_b, factor_ir2, u_t, u_early, v_u, r_i, r_l, fs, index):
    u_out = (u_b/2)*(1+1/(1+abs(v_u)))
    r_e = r_c/abs(v_u)
    i_c = (u_b-u_out)/r_c
    i_b = i_c/b
    i_r2 = factor_ir2 * i_b
    u_be = np.log((i_b/i_s)*b)*u_t
    u_r2 = u_be + i_c * r_e
    r_2 = u_r2/i_r2
    u_r1 = u_b - u_r2
    i_r1 = (factor_ir2+1) * i_b
    r_1 = u_r1/i_r1
    fg = fs/1.55
    r_be = b * u_t/i_c
    r_in = 1/((1/r_1)+(1/r_2)+(1/(r_be+(b+1)*r_e)))
    r_ce = u_early/i_c
    r_out = 1/((1/r_c)+(1/r_ce))
    c_in = 1/(2*np.pi*fg*(r_i+r_in))
    c_out = 1/(2*np.pi*fg*(r_l+r_out))
    alpha = r_in/(r_in+r_i)
    beta = r_l/(r_l+r_out)
    amp_factor = alpha * beta * abs(v_u)
    index = int(index)
    calc_array = np.around([u_out, r_e, i_c, i_b, i_r2, u_be, u_r2, r_2, u_r1, i_r1, r_1, fg, r_be, r_in, r_ce, r_out,
                            c_in, c_out, alpha, beta, amp_factor], index)
    return calc_array


print("Emitter Basic Circuit Calculator")
print("Please use this format of scientific notation if needed: Example: 1e-08")

for i in range(12):
    userInput[i] = float(input("Type Value for " + strArrayInput[i] + " = "))

print("Finished!")
for j in range(21):
    print(strArrayOutput[j] + " = " + str(calc(userInput[0], userInput[1], userInput[2], userInput[3], userInput[4],
                                               userInput[5], userInput[6], userInput[7], userInput[8], userInput[9],
                                               userInput[10], userInput[11])[j]))
