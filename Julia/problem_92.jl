function count_arrivals(limit::Int)
    destinations = destination_lookup(81 * Int(ceil(log10(limit))))

    count = 0
    for n in 1:limit
        count += destinations[digit_square(n)]
    end
    println(count)
end

function destination_lookup(size::Int)
    destinations = Dict()
    for n in 1:size
        destinations[n] = final_destination(n)
    end
    return destinations
end

function final_destination(n::Int)
    while n != 1 && n != 89
        n = digit_square(n)
    end
    
    if n == 1
        return 0
    end

    return 1
end

function digit_square(n::Int)
    return sum(d^2 for d in digits(n))
end

count_arrivals(10000000)
