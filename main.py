import encoder
import gf256
import matrix
import reed_solomon

data = input("enter input:")
bits = encoder.string_to_bits(data)
bits = encoder.pad_bits(bits, 152)
log, exp = gf256.generate_tables()

print(gf256.mul(5, 20, log, exp))
gen = reed_solomon.gen_poly(7, log, exp)
print(gen)
qr = matrix.cr_matrix()
matrix.add_patterns(qr)
matrix.place_bits(qr, bits)
matrix.print_mat(qr)
