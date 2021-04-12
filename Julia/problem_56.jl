function max_digit_sum(limit)
    max_sum = 0

    for a in 1:limit - 1
        for b in 1:limit - 1
            digit_sum = sum(digits(BigInt(a) ^ b))
            if digit_sum > max_sum
                max_sum = digit_sum
            end
        end
    end

    return max_sum
end

println(max_digit_sum(100))
