import subprocess
import time
import os
from PIL import ImageGrab

# 设置截图的时间间隔（秒）
interval = 5

# 设置截取区域的大小
width, height = 2880, 1920

# 设置保存截图的路径为 D:\Desktop
desktop_path = "D:\\Desktop"

# 如果目录不存在，则创建它
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# 启动 scrcpy
scrcpy_process = subprocess.Popen(["scrcpy"])

try:
    while True:
        # 截取整个屏幕
        screenshot = ImageGrab.grab()

        # 获取屏幕的宽度和高度
        screen_width, screen_height = screenshot.size

        # 检查截取区域是否超出屏幕范围
        if width > screen_width or height > screen_height:
            print("截取区域超出屏幕范围，使用全屏截图")
            left, top, right, bottom = 0, 0, screen_width, screen_height
        else:
            # 计算截取区域的左上角和右下角坐标
            left = (screen_width - width) // 2
            top = (screen_height - height) // 2
            right = left + width
            bottom = top + height

        # 截取指定区域
        cropped_image = screenshot.crop((left, top, right, bottom))

        # 生成带时间戳的文件名
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_name = f"screenshot_{timestamp}.png"

        # 保存截图到 D:\Desktop
        file_path = os.path.join(desktop_path, file_name)
        cropped_image.save(file_path)
        print(f"截图已保存到: {file_path}")

        # 等待指定的时间间隔
        time.sleep(interval)

except KeyboardInterrupt:
    # 用户按下 Ctrl+C 时停止脚本
    print("脚本已由用户停止。")

finally:
    # 终止 scrcpy 进程
    if scrcpy_process.poll() is None:  # 检查进程是否仍在运行
        scrcpy_process.terminate()
        print("scrcpy 进程已终止。")