function count_arrangements(limit::Int)
    k1 = floor(sqrt(limit))
    k2 = floor(limit/4) + 1

    count = k1/2 * (k1/2 - 1)

    for n in (k1 + 1):k2
        count += floor((n - ceil(sqrt(n^2 - limit)))/2)
    end
    
    println(Int(count))
end

count_arrangements(1000000)
