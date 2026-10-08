gizli_reqem = 19
texmin = 0
while texmin != gizli_reqem:
    texmin = int(input("Gizli doğum günü rəqəmini daxil edin (1-31 arası): "))
    if texmin == gizli_reqem:
        print("Təbriklər, tapdınız!")
    elif texmin < gizli_reqem:
        print("Bir az yuxarı qalxın (daha büyük rəqəm deyin).")
    else:
        print("Bir az aşağı enin (daha kiçik rəqəm deyin).")
