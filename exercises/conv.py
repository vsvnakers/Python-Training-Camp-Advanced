# exercises/conv.py
"""
练习：二维卷积 (Convolution)

描述：
实现一个简单的二维卷积操作。

请补全下面的函数 `conv2d`。
"""
import numpy as np

def conv2d(x, kernel):
    """
    执行二维卷积操作 (无填充, 步幅为 1)。

    Args:
        x (np.array): 输入二维数组, 形状 (H, W)。
        kernel (np.array): 卷积核二维数组, 形状 (kH, kW)。

    Return:
        np.array: 卷积结果, 形状 (out_H, out_W)。
                  out_H = H - kH + 1
                  out_W = W - kW + 1
    """
    # 请在此处编写代码
    # 提示：
    # 1. 获取输入和卷积核的尺寸
    H, W = x.shape            # 输入图像大小
    kH, kW = kernel.shape     # 卷积核大小

    # 2. 计算输出大小（无填充 valid 模式）
    out_H = H - kH + 1
    out_W = W - kW + 1

    # 3. 初始化输出数组
    out = np.zeros((out_H, out_W))

    # 4. 遍历每个输出位置 (i, j)
    for i in range(out_H):
        for j in range(out_W):
            # 5. 提取输入中当前窗口 patch
            patch = x[i:i+kH, j:j+kW]

            # 6. 卷积操作：逐元素相乘再求和
            out[i, j] = np.sum(patch * kernel)

    return out