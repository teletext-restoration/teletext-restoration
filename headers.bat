@echo off
for /d %%i in (%~dp0*) do (
    for /d %%j in (%%i\*) do (
        for %%k in (%%j\*.t42) do (
            cd %%j
            if not exist %%~nk-headers.txt (
                teletext-decoder -i %%k -o %%~nk-headers.txt -h
            )
        )
    )
)
cd %~dp0