import os # operating system 作業系統


# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續 把下面的跳過 直接繼續下一廻廻圈
			name, price = line.strip().split(',') # .strip 把換行(/n)去掉    # split 切一刀分隔開
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# 印出所有商品價格(購買紀錄)
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# write 寫入檔案
# 創造出"products.txt"
# 有不同屬性(名稱, 價格)的時候常常用 .csv
# 可以用excel打開
def write_file(filename, products):
	with open (filename, 'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
# +可以把字串跟字串合再一起
# path 路徑(模組) # isfile(): path裡面的尋找檔案功能


# 執行
def main():
	filename = 'products.csv'
	print('正在尋找檔案...')
	if os.path.isfile(filename): # 檢查檔案在不在
		print('找到檔案了!')
		products = read_file(filename)
		print(products)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()


# refactor重構 (用function來重新設計)