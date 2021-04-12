function calculate_sum(upper_limit)
    s = 0
    for i in 1 : upper_limit - 1
        if i % 3 == 0 || i % 5 == 0
            s += i
        end
    end
    println(s)
end

calculate_sum(1000)
