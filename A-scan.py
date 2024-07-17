import pyautogui
import time
import json
import typer

from WF_SDK import device
from WF_SDK import scope
from WF_SDK import wavegen

app = typer.Typer()


@app.command()
def main(
    num_point: int = typer.Argument(10),
    rows: int = typer.Argument(3),
    output_path: str = typer.Option("./output.json", "--output", "-o"),
):
    # 设备初始化
    device_data = (
        device.open()
    )  # 需要确保这个对象正确地管理了Analog Discovery 2的连接和配置
    scope.open(device_data, sampling_frequency=20e06)  # 初始化示波器
    matrix = []
    button1_coords = (1829, 294)  # 右移按键位置
    button2_coords = (1763, 251)  # 下移按键位置
    button3_coords = (1695, 291)  # 左移按键位置

    # num_point = 2

    try:
        for i in range(rows):  # 扫描十个来回
            row = []
            for j in range(num_point):  # 从左到右扫描
                pyautogui.click(button1_coords)  # 点右移按钮
                time.sleep(0.05)  # 每次点击后短暂等待
                wavegen.generate(device_data, 1, "sine", 5e06)  # 发生5MHz的正弦波
                echo_data = scope.record(device_data, 1)  # 记录回波数据
                row.append(echo_data)  # 将数据添加到当前行
            matrix.append(row)
            pyautogui.click(button2_coords)  # 点击下移按钮一次
            time.sleep(0.05)  # 等待一段时间

            row = []
            for j in range(num_point):
                pyautogui.click(button3_coords)  # 点左移按钮
                time.sleep(0.05)  # 在每次点击后短暂等待
                wavegen.generate(device_data, 1, "sine", 5e06)  # 发生5MHz的正弦波
                echo_data = scope.record(device_data, 1)  # 记录回波数据
                row.append(echo_data)  # 将数据添加到当前行
            matrix.append(row)
            pyautogui.click(button2_coords)  # 点击下移按钮一次
            time.sleep(0.05)  # 等待一段时间
    finally:
        print("Script execution finished.")
        print(matrix[0])
    device.close(device_data)

    with open(output_path, "w") as f:
        json.dump(matrix, f, indent=4)


if __name__ == "__main__":
    app()
