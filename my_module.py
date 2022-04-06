"""
Bu kisim fonksiyon tanimi olarak yazilmistir.
Bu fonksiyon üs alma islemi yapar...
"""

__all__= ['fonksiyonum']        #   modul icerisindeki fonksiyonu secilebilir yapar

def fonksiyonum(a):
    return print('sayinin karesi: ',a**2)
if __name__ == '__main__':                      #   modül olarak cagirilirsa buranin altini yazdirmaz
    print('sayinin karesi: ', fonksiyonum(8))
