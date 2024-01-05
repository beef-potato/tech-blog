# 开机启动脚本

https://stackoverflow.com/questions/20575257/how-do-i-run-a-powershell-script-when-the-computer-starts



`win + R` 输入 `shell:common startup` 会打开 `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` 在其中加入脚本需要管理员权限，加入脚本后，另外加入运行脚本的脚本 `startup.cmd`，其中加入

```cmd
PowerShell "%USERPROFILE%\Desktop\autoopen.ps1"
```

其中 %USERPROFILE%是默认盘用户名路径的缩写, 需要注意如果路径存在空格，需要加上 `""` 。

另外`win + R` 输入 `shell:startup` 则会打开当前用户的startup文件夹，加入快捷方式或者脚本即可开机执行，不需要管理员权限。

