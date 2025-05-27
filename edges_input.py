import cv2
import numpy as np

import cv2
import numpy as np

def image_processing_pipeline(image_path):
    """
    使用 OpenCV 读取图像，进行高斯滤波和边缘检测。
    参数:
        image_path: 图像文件的路径 (字符串).
    返回:
        edges: Canny 边缘检测的结果 (NumPy 数组, 灰度图像).
               如果读取图像失败, 返回 None.
    """
    # 请在此处编写代码
    # 提示：
    # 1. 使用 cv2.imread() 读取图像。
    # 2. 检查图像是否成功读取（img is None?）。
    # 3. 使用 cv2.cvtColor() 将图像转为灰度图 (cv2.COLOR_BGR2GRAY)。
    # 4. 使用 cv2.GaussianBlur() 进行高斯滤波。
    # 5. 使用 cv2.Canny() 进行边缘检测。
    # 6. 使用 try...except 包裹代码以处理可能的异常。
    try:
        # 1️⃣ 读取图像（彩色）
        img = cv2.imread(image_path)

        # 2️⃣ 检查图像是否成功加载
        if img is None:
            print("图像读取失败！")
            return None

        # 3️⃣ 转为灰度图（从BGR转为单通道）
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 4️⃣ 高斯模糊（去除噪声，提高边缘检测稳定性）
        blurred = cv2.GaussianBlur(gray, (1, 1), sigmaX=0.01)

        # 5️⃣ Canny边缘检测（自动检测图像边缘）
        edges = cv2.Canny(blurred, threshold1=100, threshold2=200)

        return edges

    except Exception as e:
        print(f"处理失败: {e}")
        return None

if __name__ == "__main__":
    # 示例：替换为你自己的图片路径
    image_path = "picture.jpg"
    output_path = "edges_output.png"

    edges = image_processing_pipeline(image_path)

    if edges is not None:
        cv2.imwrite(output_path, edges)
        print(f"边缘图像已保存为: {output_path}")
    else:
        print("图像处理失败。")
