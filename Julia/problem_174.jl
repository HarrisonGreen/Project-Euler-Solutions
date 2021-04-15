function count_arrangements(limit::Int)
    k1 = floor(sqrt(limit))
    k2 = floor(limit/4) + 1
    counts = Dict()

    for n in 3:k1
        for m in (n - 2):-2:1
            counts[n^2 - m^2] = get(counts, n^2 - m^2, 0) + 1
        end
    end

    for n in (k1 + 1):k2
        for m in (n - 2):-2:sqrt(n^2 - limit)
            counts[n^2 - m^2] = get(counts, n^2 - m^2, 0) + 1
        end
    end

    types = Dict()
    for (key, value) in counts
        types[value] = get(types, value, 0) + 1
    end

    println(sum(types[n] for n in 1:10))
end

count_arrangements(1000000)
