# encoding:utf-8
# baidu_apiKey，baidu_secretKey分别为百度ocr api，s_sckey与log_lev分别为Server酱和日志等级
# 微信日志等级 仅有0/1/2/3，越小越详细，注意每天接口调用有上限！
# 填入单引号内，这些只是临时，等待正式config上线
debug = False
baidu_apiKey = ''
baidu_secretKey = ''
s_sckey = ''
log_lev = '1'

async_screenshot_freq = 5
bad_connecting_time = 30

fast_screencut = True  # mincap 快速截图
fast_screencut_delay = 1.5  # 由于截图太快造成脚本崩溃，可以使用这个加上全局的截图delay，模拟卡顿。
fast_screencut_timeout = 10  # 等待服传输数据超时

end_shutdown = False  # 非常“危险”的Windows功能

lockimg_timeout = 90  # 90秒如果还在lockimg，则跳出重启

# 仅为调试使用
trace_exception_for_debug = False  # 开启后，所有的try向上传递错误信息，并且只用第一个device跑第一个任务（单进程）
use_template_cache = True  # 在开发工具使用时可以将其关闭
