# 专业实验一
（1）模拟生成一组实验需要的传感器数据样本，这些数据可以是温度、湿度、压力等常见的传感器读数。
（2）异常检测算法实现：利用基本的统计学原理，如标准差规则（例如，识别那些超出均值±2标准差的值作为异常值）。	编写代码实现简单统计方法的异常检测，标记出数据中的异常点。
（3）数据可视化：使用数据可视化库（如Python matplotlib或seaborn）将原始数据和检测到的异常值进行可视化，以便直观展示分析结果。绘制数据分布的直方图或箱线图，辅助识别异常值。

"""    while 1:
        a = generate.mudata_generate(20, 30, 50)
        analyze.outlier(a, abnum, abnum_index)
        if len(abnum) >= 4:
            break
        abnum = []
        abnum_index = []"""