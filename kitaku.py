import location
import requests as req

#現在地取得
current_location = location.get_location()
#取得した現在地を可視化
results = location.reverse_geocode(current_location)
result = [{'State' and 'City' and 'Street'}]
#可視化した文をファイルに書き込み
file = open('GPS.txt', 'w', encoding='utf-8')
file.write(str(result))
file.close()



