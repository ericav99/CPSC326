unordered3 x y z =
    if x <= y
    then (
        if y <= z
        then False
        else True
    ) else (
        if x >= y
        then (
            if y >= z
            then False
            else True
        ) else True
    )
