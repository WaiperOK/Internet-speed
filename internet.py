from speedtest import Speedtest

st = Speedtest()

print("Downloads : (Скорость загрузки) ", st.download())
print ("Upload : (Скорость Выгрузки)", st.upload())

st.get_servers([])
print("Ping : (Пинг)", st.results.ping)
