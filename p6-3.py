set_A = {20, 30, 40, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C = {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}

print ("irisan a, c, dan d:", set_A & set_C & set_D)
print ("selisih gabungan a dan b dengan d", (set_A | set_B) - set_D)
print ("selisih simetris b dan c:", set_B ^ set_C)
print ("selisih dari gabungan AB dengan CD:", (set_A | set_B)&(set_C | set_D))