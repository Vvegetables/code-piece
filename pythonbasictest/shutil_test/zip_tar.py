import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write(r'./folder/a.log')
z.write(r'./folder/b.log')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
k = z.extractall(r"C:\Users\Zcxu\Desktop")
z.close()
print(k)