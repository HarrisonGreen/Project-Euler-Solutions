function recurring_decimal_length(n)
    d = 1
    while true
        if powermod(10, d, n) == 1
            return d
        end
        d += 1
    end
end

function longest_recurring_decimal(upper_limit)
    longest = 0; arg = 0

    for i in 2:upper_limit
        if i % 2 == 0 || i % 5 == 0
            continue
        end

        len = recurring_decimal_length(i)
        if len > longest
            longest = len; arg = i
        end
    end

    return arg
end

println(longest_recurring_decimal(1000))
