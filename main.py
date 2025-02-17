import os
import json
import yaml

# 配置
json_dir = 'D:/Desktop/KR-16'  # JSON 文件路径
out_dir = 'D:/Desktop/YOLO_txt'  # 输出的 TXT 文件路径
yaml_file = 'D:/Desktop/best/yolov8n.yaml'  # YOLOv8 配置文件路径

# 读取 YAML 文件，获取类别名称
with open(yaml_file, 'r') as f:
    yaml_content = yaml.safe_load(f)
class_names = yaml_content['classes']  # 类别名称列表
class_mapping = {name: i for i, name in enumerate(class_names)}  # 类别名称到 ID 的映射

# 确保输出目录存在
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def convert_json_to_yolo(json_file, txt_file):
    """
    将单个 JSON 文件转换为 YOLO 格式的 TXT 文件
    :param json_file: JSON 文件路径
    :param txt_file: 输出的 TXT 文件路径
    """
    # 读取 JSON 文件
    with open(json_file, 'r') as f:
        content = json.load(f)

    # 获取图像尺寸
    image_width = content['imageWidth']
    image_height = content['imageHeight']

    # 创建或清空 TXT 文件
    with open(txt_file, mode="w", encoding="utf-8") as f:
        pass  # 创建一个空文件然后关闭

    # 处理每个标注
    for shape in content['shapes']:
        label = shape['label']
        points = shape['points']
        shape_type = shape['shape_type']

        # 只处理矩形标注
        if shape_type != 'rectangle':
            print(f"Skipping non-rectangle shape in {json_file}")
            continue

        # 获取类别 ID
        if label not in class_mapping:
            raise ValueError(f"Unknown label: {label}")
        class_id = class_mapping[label]

        # 提取边界框的四个顶点坐标
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]

        # 计算边界框的中心点坐标和宽高（归一化）
        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords)
        y_max = max(y_coords)

        x_center = (x_min + x_max) / 2 / image_width
        y_center = (y_min + y_max) / 2 / image_height
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        # 将信息写入 TXT 文件（格式：class_id x_center y_center width height 0000）
        line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f} 0000\n"
        with open(txt_file, mode="a", encoding="utf-8") as f:
            f.write(line)

def main():
    # 遍历 JSON 文件夹中的所有文件
    for file in os.listdir(json_dir):
        if not file.endswith('.json'):
            continue

        # 生成输入和输出文件路径
        json_file = os.path.join(json_dir, file)
        filename = os.path.splitext(file)[0]
        txt_file = os.path.join(out_dir, filename + '.txt')

        # 转换 JSON 文件
        try:
            convert_json_to_yolo(json_file, txt_file)
            print(f"Converted: {file} -> {filename}.txt")
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == '__main__':
    main()
