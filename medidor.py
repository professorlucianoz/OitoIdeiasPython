import speedtest

st = speedtest.Speedtest()

print("Minha velocidade de download é:", st.download())
print("Minha velocidade de upload é:", st.upload())