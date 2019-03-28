quadrant (x, y) =
    if or [x == 0, y == 0]
    then 0
    else (
        if and [x > 0, y > 0]
        then 1
        else (
            if and [x < 0, y > 0]
            then 2
            else (
                if and [x < 0, y < 0]
                then 3
                else (
                    if and [x > 0, y < 0]
                    then 4
                    else 0
                )
            )
        )
    )
