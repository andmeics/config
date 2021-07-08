# Create a Linux Swap File

Swap is a space on a disk that is used when the amount of physical RAM memory is full. When a Linux system runs out of RAM, inactive pages are moved from the RAM to the swap space.

Swap space can take the form of either a dedicated swap partition or a swap file. In most cases, when running Linux on a virtual machine, a swap partition is not present, so the only option is to create a swap file.

This tutorial was tested on Linux systems with Ubuntu 18.04 and CentOS 7, but it should work with any other Linux distribution.

## How to add Swap File
Follow these steps to add 2GB of swap to your server.

Create a file that will be used for swap:

```bash
sudo fallocate -l 2G /opt/swapfile
```

If faillocate is not installed or if you get an error message saying fallocate failed: Operation not supported then you can use the following command to create the swap file:

```bash
sudo dd if=/dev/zero of=/opt/swapfile bs=1024 count=2097152
```

Only the root user should be able to write and read the swap file. To set the correct permissions type:

```bash
sudo chmod 600 /opt/swapfile
```

Use the mkswap utility to set up the file as Linux swap area:

```bash
sudo mkswap /opt/swapfile
```

Enable the swap with the following command:

```bash
sudo swapon /opt/swapfile
```

To make the change permanent open the /etc/fstab file and append the following line:

/etc/fstab
```bash
/swapfile swap swap defaults 0 0
```

To verify that the swap is active, use either the swapon or the free command as shown below:

```bash
sudo swapon --show
```

```shell
NAME      TYPE  SIZE   USED PRIO
/swapfile file 1024M 507.4M   -1
```
```bash
sudo free -h
```

```shell
              total        used        free      shared  buff/cache   available
Mem:           488M        158M         83M        2.3M        246M        217M
Swap:          1.0G        506M        517MCopy
```

How to adjust the swappiness value
Swappiness is a Linux kernel property that defines how often the system will use the swap space. Swappiness can have a value between 0 and 100. A low value will make the kernel to try to avoid swapping whenever possible, while a higher value will make the kernel to use the swap space more aggressively.

The default swappiness value is 60. You can check the current swappiness value by typing the following command:

```bash
cat /proc/sys/vm/swappiness
```

```shell
60
```
While the swappiness value of 60 is OK for most Linux systems, for production servers, you may need to set a lower value.

For example, to set the swappiness value to 10, you would run the following sysctl command:

```bash
sudo sysctl vm.swappiness=10
```
To make this parameter persistent across reboots append the following line to the /etc/sysctl.conf file:

```bash
/etc/sysctl.conf
```
```bash
vm.swappiness=10
```
The optimal swappiness value depends on your system workload and how the memory is being used. You should adjust this parameter in small increments to find an optimal value.

How to remove Swap File
If for any reason you want to deactivate and remove the swap file, follow these steps:

First, deactivate the swap by typing:

```bash
sudo swapoff -v /swapfile
```

Remove the swap file entry /swapfile swap swap defaults 0 0 from the /etc/fstab file.

Finally, delete the actual swapfile file using the rm command:

```bash
sudo rm /swapfile
```

Conclusion
You have learned how to create a swap file and activate and configure swap space on your Linux system.
