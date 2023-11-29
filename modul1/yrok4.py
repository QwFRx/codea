import time

for t in range(1, 4):
    for vek in range(1, 11):
        for god in range(1, 101):
            for mes in range(1, 13):
                for day in range(1, 31):
                    for i in range(24):
                        for j in range(60):
                            for k in range(60):
                                print("Сейчас: "+str(day)+" день "+str(mes)+" месяца " + str(god)+ " года " + str(vek)+ " века " + str(t) + " тысячелетия ")
                                print("Время: "+ str(i)+":"+str(j)+':'+str(k))
                                time.sleep(1)