处理逻辑：
    * GPR记录数据保存为bin文件
    * 使用RadarView将bin文件导出为sgy文件
    * 使用matlab将sgy文件转化为mat文件
    ！ 对mat数据进行增益等预处理处理成图像（相近增益 + 尺度）
    * 图像滑动裁剪 
    * 异常体识别得到predictions
    * 连接图像 
    ！ NMS后绘图
