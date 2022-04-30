import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'): #看有沒有找到檔案
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #換下一迴
			name, price = line.strip().split(",") #切完的東西存進name一個存進name
			products.append([name, price])
	print(products)
else:
	print('找不到檔案......')
	
#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#products[0][0] 表大清單中第一個小清單的第一個位置

#印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  #csv是常用的檔案類型 可用excel開 
	f.write('商品,價格\n')#寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')