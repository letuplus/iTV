import requests

# 获取接口数据
url = "https://raw.githubusercontent.com/MemoryCollection/IPTV/main/itvlist.txt"
response = requests.get(url)
data = response.text

# 将txt格式转换为m3u格式
lines = data.split("\n")
m3u_data = "#EXTM3U\n"
for line in lines:
    if line.strip():  # 如果不是空行
        m3u_data += f"#EXTINF:-1,Channel\n{line}\n"

# 输出到iptvv4.m3u文件
with open("iptvv4.m3u", "w", encoding="utf-8") as file:
    file.write(m3u_data)

print("转换完成，已输出到iptvv4.m3u文件")
