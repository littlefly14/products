products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

products[0][0] #表大清單中第一個小清單的第一個位置

for p in products:
	print(p[0], "的價格是", p[1])


with open('products.csv', 'w', encoding='utf-8') as f:  #csv是常用的檔案類型 可用excel開
	f.write('商品,價格\n')#寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')