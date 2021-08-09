using Primes

function count_prime_sums(limit::Int)
    p_list = primes(limit)
    counts = Dict(0=>1)

    for p in p_list
        for i in p:limit
            counts[i] = get(counts, i, 0) + get(counts, i - p, 0)
        end
    end

    for i in 2:limit
        if counts[i] > 5000
            return i
        end
    end
end

println(count_prime_sums(100))
