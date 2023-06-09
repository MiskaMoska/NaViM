# 导入我们所开发的映射仿真工具包——Maptools
from maptools import *
from maptools.toksim import TokSim
import onnx

import torch
import onnxruntime as rt

# 读取onnx模型
config = {
    'mapname': 'resnet18',
    'quantize': True
}

model = onnx.load("onnx_models/simp-resnet18.onnx")

# 创建onnx转换器
oc = OnnxConverter(model, arch=NNModelArch.RESNET, **config)

# 执行模型转换
oc.run_conversion()

# 显示转换得到的设备算子图
oc.plot_device_graph()

# 获得转换得到的设备算子图
og = oc.device_graph

# 创建逻辑映射器，设置Xbar尺寸
xm = TileMapper(og, 256, 256*5, **config)

# 执行映射
xm.run_map()

# 打印映射信息
xm.print_config()

# 获得映射得到的CTG
ctg = xm.ctg
ctg.plot_ctg(direction='UD')

params = read_quantparams(config['mapname'])

# 创建CalcuSim仿真器, tm是TileMapper, oc是OnnxConverter
csim = CalcuSim(
    xm.ctg, oc.host_graph, params,
    quantize=True, physical=True, stats=True
)

# 获取输入图片数据, 缩放至 224 × 224
input = get_input('work/test1.png', resize=(768, 768))

# 运行CalcuSim仿真, 获得输出结果
output = csim(input)


# # 创建Tile阵列拓扑图，设置阵列规模
# acg = ACG(8, 9)

# # 创建物理映射器
# nm = NocMapper(ctg, acg, **config)

# # 执行智能布局布线
# nm.run_layout()
# nm.run_routing()

# # 保存布局布线图
# nm.save_layout()
# nm.save_routing()

# # 保存硬件配置信息
# nm.save_config()

toksim = TokSim(ctg, **config)
toksim.run()

plot_tokens(config['mapname'])