#讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續 把下面的跳過 直接繼續下一廻廻圈
		name, price = line.strip().split(',') # .strip 把換行(/n)去掉    # split 切一刀分隔開
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有商品價格(購買紀錄)
for p in products:
	print(p[0], '的價格是', p[1])

# write 寫入檔案
# 創造出"products.txt"
# 有不同屬性(名稱, 價格)的時候常常用 .csv
# 可以用excel打開
with open ('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
# +可以把字串跟字串合再一起