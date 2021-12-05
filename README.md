# Genshin_Zither_Player
An auto zither player for Genshin Impact Winows Version,support midi files
Based on [pyautogui](https://github.com/asweigart/pyautogui) and [mido](https://github.com/mido/mido)

## Usage

Download Git repo and python, then input following command.   
```bash
python ./GenshinZitherPlayer
```
Then input the `path` of `.mid` file and bpm.

Enjoy!

----
# 原神自动弹琴脚本
这是一个支持在Windows端自动读取`midi`文件并演奏的原神弹琴脚本，基于[pyautogui](https://github.com/asweigart/pyautogui) 和 [mido](https://github.com/mido/mido)开发


## 使用方法

> 由于精力有限，目前版本暂无图形界面，后续会加入，可以点击star持续关注项目进展


### 环境准备

安装最新版本[Python](https://www.python.org/downloads/)并将其加入环境变量

在release界面下载并解压脚本

按`WIN`+`X`键打开菜单，选择`Powershell(管理员)`或`Windows Terminal(管理员)` ,键入以下命令

```shell
cd [脚本解压文件夹的路径]
python GenshinZitherPlayer.py
```

如正确无误会出现以下提示
```
Select midi file: 
```

### 选择曲目并演奏

在解压的脚本文件夹中的`midi_repo`文件夹中存放了脚本的曲目仓库，输入仓库中的midi文件名即可演奏对应曲目，也可以将别的midi文件存入midi_repo中进行演奏

输入曲目名称
```
Select midi file: little_star
```

选择bpm（演奏速度）
```
Input bpm: 90
```

选择升降调
```
Choose key and values:
1.Play +12keys
2.Play +0keys
>2
```

准备时间内将窗口焦点切换至原神游戏中
```
>2
5s...
4s...
3s...
2s...
1s...
```

Enjoy it!


### 自动升降调/midi自适应功能

由于原神琴键的限制，仅支持C大调音阶内三个八度的音符（即只能弹钢琴白键上的音符），因此许多原调的midi文件将不适用，使用本脚本可以解决这一问题，当选择了不是C大调/A小调的midi文件时，本脚本会尝试将其转调为Cmajor并演奏，对于市面上的流行歌曲成功率极高，只需要在选择升降调时按对应操作即可