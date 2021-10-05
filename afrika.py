#Hozz létre egy listát és a tartalmát
#írd ki a afrika.txt állományba"

afrika=["párduc","oroszlán","gorilla","makákó","bambusznád","majomkenyérfa","kókuszdió"]
celfajl=open("afrika.txt","w",encoding="utf8")
afrika.append("szavannák")
afrika.append("fekete nők")
for elem in afrika:
      print(elem,file=celfajl)
celfajl.close()
