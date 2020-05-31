a = []
num = 0
while True:
    b = input('..........YoungPu Carnival.........\n Off-White [o]\n Balenciaga [l]\n Gucci [g]\n Onitsuka Tiger [t]\n ตระกร้าสินค้า [x]\n ออกจากร้าน [e]\n')
    b = b.lower()
    if b == 'o':
        print("..........Off-White.........")
        print("[A] MOTOWRAP SNEAKER ราคา 20141฿") 
        print("[B] 2.0 SNEAKER ราคา 13202฿")
        print("[C] LOW VULCANIZED SNEAKER ราคา 10155฿")
        b=input("เลือกสินค้าที่ท่านต้องการ: ")
        if b == "a":
            a.append("MOTOWRAP SNEAKER                          20141฿            20%            16113")    
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 20141-(20141*0.2)
        elif b == "b":
            a.append("2.0 SNEAKER                               13202฿            20%            10562")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 13202-(13202*0.2)
        elif b == "c" :
           a.append("Recycled Speed Sneaker                    10155฿            20%            8124")
           print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
           num+= 10155-(10155*0.2)
        else: print("\nกรุณากรอกอีกครั้งครับ\n")   
    if b == "l":
        print("..........Balenciaga.........")
        print("[A] Tyrex Sneaker ราคา 31917฿")
        print("[B] Recycled Speed Sneaker ราคา 23324฿")
        print("[C] Zen Sneakers ราคา 17186฿")
        b=input("เลือกสินค้าที่ท่านต้องการ: ")
        if b == "a" :
            a.append("Tyrex Sneaker                             31917฿            30%            22342")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 31917-(31917*0.3)
        elif b == "b" :
           a.append("Recycled Speed Sneaker                    23324฿            30%            16327")
           print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
           num+= 23324-(23324*0.3)
        elif b == "c" :
            a.append("Zen Sneakers                              17186฿            30%            12031")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 17186-(17186*0.3)
        else: print("\nกรุณากรอกอีกครั้งครับ\n")
    if b == "g":
        print('..........Gucci.........')
        print("[A] White Bee New Ace Sneakers ราคา 19948฿")
        print("[B] Off-White Vintage Logo Rhyton Sneakers ราคา 27314฿")
        print("[C] White Bee & Star New Ace Sneakers ราคา 22403฿")
        b=input("เลือกสินค้าที่ท่านต้องการ: ")
        if b == "a":
            a.append("White Bee New Ace Sneakers                19948฿            40%            11969")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 19948-(19948*0.4)
        elif b == "b":
            a.append("Off-White Vintage Logo Rhyton Sneakers    27314฿            40%            16389")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 27314-(27314*0.4)
        elif b == "c":
            a.append("White Bee & Star New Ace Sneakers         22403฿            40%            13442")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 22403-(22403*0.4)
        else: print("\nกรุณากรอกอีกครั้งครับ\n")
    if b == 't':
        print('..........Onitsuka Tiger.........')
        print("[A] Mexico 66 Sneakers ราคา 2609฿")
        print("[B] Serrano Sneakers ราคา 2302฿")
        print("[C] GSM Sneakers ราคา 4500฿")
        b=input("เลือกสินค้าที่ท่านต้องการ: ")
        if b == "a":
            a.append("Mexico 66 Sneakers                        2609            15%            2218")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 2609-(2609*0.15)
        elif b == "b":
            a.append("Serrano Sneakers                          2302            15%            1957")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 2302-(2302*0.15)
        elif b == "c":
            a.append("GSM Sneakers                              4500            15%            3825")
            print("\n.....ใส่ตระกร้าเรียบร้อย.....\n")
            num+= 22403-(22403*0.15)
        else: print("\nกรุณากรอกอีกครั้งครับ\n")
    if b == "x":
        print("="*100)
        print("              รุ่น                            ราคา            ส่วนลด            คงเหลือ  ")
        print("="*100)
        count=1
        for list in a: 
            print(count,end=" ")
            print(list)

            count+=1
        print("รวมราคาสุทธิ:%d\n"%(num))
    if b== "e":
        print("GOOD BYE")
        break