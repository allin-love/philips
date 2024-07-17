import ctypes  # 导入C兼容的数据类型
from sys import platform, path  # 导入平台和路径模块，检查操作系统类型并获取路径
from os import sep  # 导入操作系统特定的文件路径分隔符

# 根据操作系统加载动态库，并获取常量路径（路径是操作系统特定的）
if platform.startswith("win"):
    # Windows平台
    dwf = ctypes.cdll.dwf
    constants_path = "C:" + sep + "Program Files (x86)" + sep + "Digilent" + sep + "WaveFormsSDK" + sep + "samples" + sep + "py"
elif platform.startswith("darwin"):
    # macOS平台
    lib_path = sep + "Library" + sep + "Frameworks" + sep + "dwf.framework" + sep + "dwf"
    dwf = ctypes.cdll.LoadLibrary(lib_path)
    constants_path = sep + "Applications" + sep + "WaveForms.app" + sep + "Contents" + sep + "Resources" + sep + "SDK" + sep + "samples" + sep + "py"
else:
    # Linux平台
    dwf = ctypes.cdll.LoadLibrary("libdwf.so")
    constants_path = sep + "usr" + sep + "share" + sep + "digilent" + sep + "waveforms" + sep + "samples" + sep + "py"

# 打印调试
print("Constants path:", constants_path)

# 导入常量
path.append(constants_path)
import dwfconstants as constants  # 导入dwfconstants模块中的常量
