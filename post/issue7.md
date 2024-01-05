# u盘 Trojan

今天帮老师传文件，用的朋友给的扩容u盘，由于事先出过类似问题已经把u盘里的`System Volume Information`改为只读了。

和实验室的电脑一样，老师的电脑也安装了360电脑管家，在我插入u盘后，我的所有文件夹被修改为`xxx.exe`格式，同时`System Volume Information`(只读)文件夹被加入了一个文件：

以下为正常文件：

```powershell
    Directory: E:\System Volume Information

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           2022/6/14    22:53             76 IndexerVolumeGuid
-a---           2022/6/14    22:53             12 WPSettings.dat

```


```diff
- 有一个`banana.exe`被 windows defender 识别并查杀了。
```
![windows defender识别](https://cdn.jsdelivr.net/gh/beef-potato/images-hosting@master/blog/threat.3otq2l3dm1y0.webp)

# windows defender 报告

windows defender 报告发现了 [Trojan:Win32/Tnega!MTB](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Trojan%3AWin32%2FTnega!MTB&threatid=2147758187)

:/

之所以怀疑是360的问题，因为我在实验室的电脑上两次出现过这种情况，但是自己使用没有任何问题。


## u盘

经提醒，可能是U盘自身存在病毒，插入其他电脑后修改自身的文件夹为可执行文件，用于传播病毒。但是对于电脑本身的修改不得而知。

鉴于对自己的电脑从未进行过全盘扫描，使用windows defender进行全盘扫描，以判断这块u盘对我的电脑的影响。

另外这块u盘在其他电脑上也有多次使用记录，包括两个打印店、我自己的电脑，似乎没有出现过报告病毒的问题。

