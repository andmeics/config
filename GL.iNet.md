# 买了新的路由器当然要好好设置一番，探索网络的精彩。

## 转区
那第一件事肯定是转区。GLiNET的路由器固件无论哪个区域都是一样的，不存在像MIUI那种的按固件区分区域，也不存在刷固件转区。区域代码和其他配置信息（如SN码、设备ID等）一同被写在闪存的某个分区内。根据机型不同，分区位置也不一样。

MT3000的基础信息在/dev/mtdblock3，MT2500在/dev/mmcblk0boot1，AX1800/AXT1800/B3000在/dev/mtdblock8。在OpenWRT上可以使用lsblk或fdisk -l查看分区信息，并可以使用dd命令将分区dump到文件复制用于分析。

示例代码
注意，转区是直接写入闪存的，误操作可能导致设备无法启动。操作前请三思，操作时请谨慎。

MT3000
```bash
echo "US" | dd of=/dev/mtdblock3 bs=1 seek=136
sync
```

MT2500
```bash
echo 0 > /sys/block/mmcblk0boot1/force_ro
echo "US" | dd of=/dev/mmcblk0boot1 bs=1 seek=136
sync
```

AX1800
```bash
echo "US" | dd of=/dev/mtdblock8 bs=1 seek=152
sync
reboot
```

B3000
```bash
echo "US" | dd of=/dev/mtdblock8 bs=1 seek=136
sync
reboot
```

成功转区之后建议重置一下固件，并且（即便是重置了固件）此时也并不能在主页看到神秘的功能，因为简体中文下不考虑区域设置，直接就是隐藏的，切换到其他语言即可。

## 语言切换
在/www/i18n中，将后面带zh-cn的文件替换为zh-tw即可。
