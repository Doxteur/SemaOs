from fast_speedtest import FastSpeedtest

def test_speed():
    st = FastSpeedtest()
    download_speed = st.download() / 1000000 # Convert to Mbps
    return download_speed

print("Your download speed is: {:.2f} Mbps".format(test_speed()))
