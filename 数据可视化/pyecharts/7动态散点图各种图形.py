from pyecharts import EffectScatter

es = EffectScatter("动态散点图各种图形实例")

#新建各种样式的散点图
#      标注     坐标            大小                                      图样类型
es.add("1",[10],[10],symbol_size=10,effect_scale=3.5,effect_period=3,symbol="pin")#大头针
es.add("2",[60],[60],symbol_size=15,effect_scale=3.5,effect_period=4,symbol="rect")#矩形
es.add("3",[20],[20],symbol_size=20,effect_scale=4.5,effect_period=5,symbol="roundRect")#圆边矩形
es.add("4",[30],[30],symbol_size=15,effect_scale=5.5,effect_period=6,effect_brushtype='fill',symbol="diamond")#钻石
es.add("5",[40],[40],symbol_size=15,effect_scale=6.5,effect_period=7,symbol="arrow")#弓形
es.add("6",[50],[50],symbol_size=15,effect_scale=5.5,effect_period=8,symbol="triangle")#三角形
es.render(r'C:\Users\Administrator\Desktop\数据可视化\pyecharts\html\7.html')
