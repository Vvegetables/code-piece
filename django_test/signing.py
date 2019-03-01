#coding=utf-8
import extra_usage

def signer_test():
    from django.core.signing import Signer
    #使用默认secret_key
    signer = Signer()
    value = signer.sign('zhao chongxu')
    print(value)
    
    #使用自定义secret_key
    signer2 = Signer("hello-world")
    value2 = signer2.sign("zhao chongxu")
    print(value2)
    
    #使用salt，使得特定的字符串有不同的签名
    signer3 = Signer(salt='zhao')
    value3 = signer3.sign('My string')
    signer4 = Signer()
    value4 = signer4.sign('My string')
    print(value3)
    print(value4)

#带时间的签名验证
def timestampsigner_test():
    from django.core.signing import TimestampSigner
    signer = TimestampSigner()
    value = signer.sign('hello')
    print(value)
    original = signer.unsign(value)
    print(original)
    
    original = signer.unsign(value, max_age=10)
    print(original)
    
#保护复杂数据结构
def signer_protect_data_test():
    from django.core import signing
    sign_value = signing.dumps({"foo" : "bar"})
    print(sign_value)
    raw_value = signing.loads(sign_value)
    print(raw_value)



if __name__ == "__main__":
    signer_protect_data_test()