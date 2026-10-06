# 图片样本说明

这些图片由队内提供的同一张浮漂照片裁剪而成，是程序的**固定输入样本**，不是运行时裁剪参数。它们用于检查“检测框 → 中心坐标 → 像素偏移 → 左中右判断”这条链路。

| 文件 | 预期位置 | 检查点 |
| --- | --- | --- |
| `buoy_left.jpg` | LEFT | 明显在画面左侧 |
| `buoy_center.jpg` | CENTER | 基本居中 |
| `buoy_right.jpg` | RIGHT | 明显在画面右侧 |
| `buoy_near_left.jpg` | LEFT | 接近中心容差边界 |
| `buoy_near_right.jpg` | RIGHT | 接近中心容差边界 |
| `buoy_tolerance_left.jpg` | CENTER | 恰好落在中心容差左边界 |
| `buoy_tolerance_right.jpg` | CENTER | 恰好落在中心容差右边界 |
| `buoy_partial_left.jpg` | LEFT | 目标一部分在画面外 |
| `buoy_partial_right.jpg` | RIGHT | 目标一部分在画面外 |
| `no_buoy.jpg` | NOT_FOUND | 没有目标，不应输出偏移 |

这些裁剪图不是独立拍摄的场景，不能用来证明检测器在真实水面、不同光照或不同浮漂上的准确率。公开发布本仓库前，请先由供图人或队伍确认原照片及裁剪图的发布权限；当前仅按队内培训素材使用。
