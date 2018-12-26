import platform
from ctypes import *

#导入dll文件
if platform.system() == "Windows":
    libc = cdll.msvcrt  
    #libc = cdll.LoadLibrary('msvcrt.dll')
    #libc = windll.LoadLibrary('msvcrt.dll')  # Windows only
    #libc = oledll.LoadLibrary('msvcrt.dll')  # Windows only
    #libc = pydll.LoadLibrary('msvcrt.dll')
  
    #libc = CDLL('msvcrt.dll')
    #libc = WinDLL('msvcrt.dll')  # Windows only
    #libc = OleDLL('msvcrt.dll')  # Windows only
    #libc = PyDLL('msvcrt.dll')
    
elif platform.system() == "Linux":
    
    libc = cdll.LoadLibrary('libc.so.6') #64-bit Ubuntu
    #libc = pydll.LoadLibrary('libc.so.6')

    #libc = CDLL('libc.so.6')
    #libc = PyDLL('libc.so.6')

#调用c
libc.printf(b"Hello ctypes!")
print(libc.time(None))
libc.printf(b"An int %d, a double %f\n", 1234, c_double(3.14))


#string_buffer
p = create_string_buffer(3)
print(sizeof(p),p.raw,p.value)


class Bottles:
    def __init__(self,number):
        self._as_parameter_ = number ## means __str__

bottles = Bottles(42)
libc.printf(b"%d bottles of bear\n",bottles)


#函数返回值
libc.strchr.restype = c_char_p # or function
#形参限定
libc.strchr.argtypes = [c_char_p,c_char]
res = libc.strchr(b"abcdef",b"d") 
print(res)
        

#参数引用传递(byref、pointer)
i = c_int()
f = c_float()
s = create_string_buffer(b'\000' * 32)

print(i.value,f.value,repr(s.value))
libc.sscanf(b"1 3.14 Hello",b"%d %f %s",
            byref(i),byref(f),s)
print(i.value,f.value,repr(s.value))

#结构体和联合
class POINT(Structure):
    _fields_ = [
        ("x",c_int),
        ("y",c_int)
    ]        

point = POINT(10,20)
print(point.x,point.y)
point = POINT(y=5)
print(point.x,point.y)

        
        
        
        
        
        
        
        
        
        
        
        

