# gitattributesFile

doc: https://git-scm.com/docs/gitattributes

在管理Git存储库时，可以提前添加`.gitattribute`文件，自定义特定文件的管理方式。

一个应用场景是管理大的二进制文件，比如 .zip 压缩包。 有一个98前辈的 [实例仓库](https://github.com/South-River/CC98-mmpictures/commit/312a9cb2d8a5ab69b2837dd96652e3aa47e01fda) . 其中 `.gitattribute` 文件的内容为： 

```git
.zip filter=lfs diff=lfs merge=lfs -text
```

其中 `lfs` 指 `large file storage`，专门用于大文件管理。 此文件告诉git将仓库内的所有 zip 文件均作为 二进制(`-text`) 的大文件，其文件差异的比对，`merge` 操作均以大文件管理形式进行。


