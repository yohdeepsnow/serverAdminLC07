#tolong tambahkan pengurangan, pengalian dan pembagian dengan menggunakan function.

def penambahan(a,b):
	total = a+b
	return total

def pengurangan(a,b):
	total = a-b
	return total

def perkalian(a,b):
    total = a*b
    return total

def pembagian(a,b):
    total = a/b
    return total

def perpangkatan(a,b):
    total = a**b
    return total

def main():
	print(penambahan(10,5))
	print(pengurangan(10,5))
	print(perkalian(10,5))
	print(pembagian(10,5))
	print(perpangkatan(10,5))
main()
