# Internet SpeedTest
import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"Download Speed : {down}")
print(f"Upload Speed : {upload}")