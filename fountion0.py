#檢查是否有檔案
import os #operating system


def read_file(filename):
	products = []
	with open(filename, 'r') as f:#encoding='utf-8'
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			#name = d[0]
			#price = d[1]
			products.append([name, price])
	return products



#請使用者輸入
def user_input(products):
	while True:
		name = input('產品名稱: ')
		if name == 'q':
			break
		price = input('產品價格: ')
		p = []
		p.append(name)
		p.append(price)
		# = p = [name, price]
		products.append(p)
		#products.append([name, price])
	print(products)
	return products



#所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
#印東西,不用回傳免return


#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:#encoding='utf-8'
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')#txt 改成 csv

def when_nofile(filename):
	with open(filename, 'w') as f:#encoding='utf-8'
		f.write('商品,價格\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #讀取檔案 #檢查檔案
		print('找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案....')
		when_nofile(filename)
		products = read_file(filename)
	user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()

#refactor 重構