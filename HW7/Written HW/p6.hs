after (m1, d1, y1) (m2, d2, y2) =
    if y1 > y2
    then True
    else (
        if y1 < y2
        then False
        else (
            if m1 > m2 -- y1 == y2
            then True
            else (
                if m1 < m2
                then False
                else (
                    if d1 > d2 -- m1 == m2
                    then True
                    else False -- if d1 <= d2, it is not after
                )
            )
        )
    )
