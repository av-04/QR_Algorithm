import encoder
import matrix

data = input("enter input:")
bits = encoder.string_to_bits(data)
bits = encoder.pad_bits(bits, 152)

qr = matrix.cr_matrix()
matrix.add_patterns(qr)
matrix.place_bits(qr, bits)
matrix.print_mat(qr)
