@echo off

del/f/s/q %systemdrive%\*.tmp

del/f/s/q %systemdrive%\*._mp

del/f/s/q %systemdrive%\*.log

del/f/s/q %systemdrive%\*.gid

del/f/s/q %systemdrive%\*.chk

del/f/s/q %systemdrive%\*.old

del/f/s/q %windir%\*.bak

del/f/q %systemdrive%\recycled\*.*

del/f/q %windir%\pre.etch\*.*

rd/s/q %windir%\temp & md %windir%\tempemp% &md %temp%

del/f/q %userprofile%\cookies\*.*

del/f/q %userprofile%\recent\*.*

rd/s/q \“%userprofile%\Local S.ttings\Temp.rary internet Files\”

cls & echo 系统垃圾清除完成:)

echo. & pause