from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("销量", [114, 55, 27, 101, 125, 27, 105])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
#bar.render()
bar.render("生成图表2.html")

