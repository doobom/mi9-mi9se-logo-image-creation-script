# mi9/mi9se splash/logo boot Image creation script

`mi9_logo.py` `mi9_logo-1080-2340.py` 转自 XDA，原文： <https://forum.xda-developers.com/t/mi-9-splash-boot-image-creation-script.3952572/>

mi9se 基于以上脚本修改。

mi9se `logo.img` 用到 5 张图片，参考 `mi9se` 目录内的图片

图片分辨率均为 `1080x2340`, 原版图片 1~4 为 24 位，5 为 8 位，如果均为 24 位，有个定义文件大小的位置（偏移量 `0x402c`, `0x402d`) 需要修改为 `0x3b`, `0x07`.

注：启动时显示的图片在 logo 分区，并不在 splash 分区。

如果用的是 8 位的图，修改第 28 行 及 31 行：

```python
outpt.write(bytearray(emptyContent0))

outpt.seek(offset0)
outpt.write(bytearray(mi9seOffset0))
```

如果用的是 24 位的图，就保持目前的。

图片定义：

* `pic1.bmp` : 启动画面
* `pic2.bmp` : fastboot 画面
* `pic3.bmp` : 未解锁画面
* `pic4.bmp` : 已经解锁画面
* `pic5.bmp` : 系统损坏

## 用法

将 pic1~5.bmp 与脚本 `mi9se_logo-1080-2340.py` 放置同一目录，然后运行 `python mi9se_logo-1080-2340.py`, 即可打包生成 `logo_new_mi9se.img`。

完成后重启手机至 `fastboot` 模式，运行以下命令：

```shell
fastboot flash logo logo_new_mi9se.img
fastboot reboot
```

用 `shell` 也是可以的，如果 `pic5.bmp` 是 8 位图，就：

```shell
cat mi9se/header0.img pic1.bmp pic2.bmp pic3.bmp pic4.bmp pic5.bmp > logo_new_mi9se.img
```

 `pic5.bmp` 是 24 位图就：

```shell
cat mi9se/header1.img pic1.bmp pic2.bmp pic3.bmp pic4.bmp pic5.bmp > logo_new_mi9se.img
```
