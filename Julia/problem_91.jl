function right_angle_check(x1::Int, y1::Int, x2::Int, y2::Int)
    if x1 == 0 && x2 == 0
        return 0
    end

    if x1 == x2
        if y1 == 0
            return 1
        end
        return 0
    end
    
    if x1 == 0
        if y2 == y1 || y2 == 0 || y2//x2 * (y2 - y1)//(x2 - x1) == -1
            return 1
        end
        return 0
    end

    if x2 == 0
        if y1 == y2 || y1 == 0 || y1//x1 * (y2 - y1)//(x2 - x1) == -1
            return 1
        end
        return 0
    end

    g_1 = y1//x1
    g_2 = y2//x2
    g_3 = (y2 - y1)//(x2 - x1)

    if g_1 * g_2 == -1 || g_1 * g_3 == -1 || g_2 * g_3 == -1
        return 1
    end

    return 0
end

function count_triangles(dim::Int)
    count = 0
    for p in 1:(dim ^ 2 - 2)
        for q in (p + 1):(dim ^ 2 - 1)
            count += right_angle_check(p % dim, Int(floor(p/dim)), q % dim, Int(floor(q/dim)))
        end
    end
    println(count)
end

count_triangles(51)
