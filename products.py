products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# write 寫入檔案
# 創造出"products.txt"
# 有不同屬性(名稱, 價格)的時候常常用 .csv
# 可以用excel打開
with open ('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
# +可以把字串跟字串合再一起