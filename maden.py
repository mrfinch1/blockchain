import hashlib
def sha256(mesaj):
    return hashlib.sha256(mesaj.encode('ascii')).hexdigest() 
def maden(mesaj,zs = 1):
    assert zs >= 1
    on_ek = '1' * zs
    for i in range(1000):
        deger = sha256(str(hash(mesaj)) + str(i))
        if deger.startswith(on_ek):
            print(str(i),"eşelemeden sonra","Bulundu" , deger)
maden(1)

