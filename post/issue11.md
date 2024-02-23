# windows修改用户名

使用pwsh修改windows用户名，需要管理员权限。

输入 ` get-localuser | Select-Object -ExpandProperty name`可以获取当前计算机上所有的用户名。


```pwsh
PS C:\Windows\System32> get-localuser | Select-Object -ExpandProperty name
Administrator
bdd
DefaultAccount
Guest
WDAGUtilityAccount

```

随后输入 `Rename-LocalUser -Name "OLDNAME" -NewName "NEWNAME"`, 即可修改用户名称。

