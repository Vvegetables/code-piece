#coding=utf-8
def add(x,y):
	try:
		if x and y:
			return x + y
		else:
			return None
	except:
		raise Exception("参数错误")