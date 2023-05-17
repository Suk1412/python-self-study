#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os

# 返回当前工作目录
from signal import SIGHUP, SIGKILL

os.getcwd()

# 将当前工作目录更改为给定路径
path = '/home/wx/work/wangxiaogithub'
os.chdir(path)

# 返回给定目录（或当前目录，如果没有指定目录）中的文件和目录列表
os.listdir(path='.')

# 使用给定路径创建新目录
path = '/home/wx/work/wangxiaogithub/AAA'
os.mkdir(path, mode=0o777)

# 删除具有给定路径的目录
os.rmdir(path)

# 删除具有给定路径的文件
os.remove(path)

# 如果给定路径存在，则返回True，否则返回False
os.path.exists(path)

# 智能地连接一个或多个路径组件。生成的路径将具有当前操作系统的适当分隔符。
os.path.join("home", "wx", "work", "wangxiaogithub", "AAA")

# 将文件或目录从src重命名为dst
src = '/home/wx/work/wangxiaogithub/AAA'
dst = '/home/wx/work/wangxiaogithub/BBB'
"""
src: 目标文件路径
dst: 重命名后文件路径
"""
os.rename(src, dst)

# 返回有关给定路径的文件或目录的信息
os.stat(path)

# 检查进程是否可以访问指定的文件或目录
"""
mode参数可以是以下常量之一：
os.F_OK: 用于测试文件是否存在
os.R_OK: 用于测试文件是否可读
os.W_OK: 用于测试文件是否可写
os.X_OK: 用于测试文件是否可执行"""
mode = os.F_OK
os.access(path,mode)

# 更改文件或目录的权限
os.chmod(path, mode)

# 更改文件或目录的所有者和组
uid = 0
gid = 1
os.chown(path, uid, gid)

# 在子shell中执行给定的命令
command = 'll'
os.system(command)

# 返回当前进程的进程ID
os.getpid()

# 向指定的进程发送信号
pid = 1
os.kill(pid, SIGKILL)





# os.environ：包含当前进程环境中所有变量的字典。
# os.popen(command [, mode [, bufsize]])：打开一个管道，允许读取或写入命令的输入和输出。
# os.pipe()：创建一个具有读取和写入两端的管道。
# os.environ：包含当前进程环境中所有变量的字典。
# os.getpid()：返回当前进程的进程ID。
# os.kill(pid, signal)：向指定的进程发送信号。
# os.path.exists(path)：返回True如果给定路径存在，否则返回False。
# os.path.abspath(path)：返回给定路径的绝对路径。
# os.path.join(path1[, path2[, ...]])：将任意数量的路径组件连接在一起，并使用正确的分隔符。
# os.setsid()：将当前进程设置为新会话的领导者，并与控制终端分离。
# os.umask(mask)：设置当前进程的UMask值。
# os.times()：返回有关当前进程使用的CPU时间的信息。
# os.cpu_count()：返回可用的CPU数量。
# os.getloadavg()：返回平均系统负载（仅适用于类Unix系统）。
# os.get_terminal_size()：返回控制台终端的大小。
# os.fork()：在当前进程中创建一个子进程。
# os.exec*()：替换当前进程映像，以便从文件或字符串执行新程序。
# os.waitpid(pid, options)：等待指定的子进程完成并返回状态信息。
# os.killpg(pgid, signal)：向指定的进程组发送信号。
# os.makedirs(name[, mode])：创建指定名称的目录，包括所有必要的中间目录。
# os.removedirs(path)：删除空目录，包括所有未使用的中间目录。
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])：生成目录树下的所有文件名，包括子目录中的文件。
# os.path.isabs(path)：如果路径是绝对路径，则返回True，否则返回False。
# os.path.islink(path)：如果路径引用符号链接，则返回True，否则返回False。
# os.path.realpath(path)：返回给定路径的规范化绝对路径。
# os.path.samefile(path1, path2)：如果两个路径引用相同的文件，则返回True，否则返回False。
# os.path.getatime(path)：返回指定路径上文件或目录的最后访问时间。
# os.path.getmtime(path)：返回指定路径上文件或目录的最后修改时间。
# os.path.getctime(path)：返回指定路径上文件或目录的创建时间。
# os.path.getsize(path)：返回指定路径上文件的大小（以字节为单位）。
# os.path.normcase(path)：将路径转换为格式化的大小写格式。
# os.path.normpath(path)：返回规范化的路径。
# os.environ.get(key[, default])：获取环境变量key的值，如果没有找到这个变量则返回default。
# os.environ.setdefault(key[, default])：设置环境变量key的值，如果该变量不存在，则设置默认值为default。
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#