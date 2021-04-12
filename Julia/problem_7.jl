function generate_primes(target)
    primes = [2]
    i = 3

    while length(primes) != target
        square_root = sqrt(i)
        for prime in primes

            if prime > square_root
                push!(primes, i)
                break
            end

            if i % prime == 0
                break
            end

        end
        i += 2
    end

    return primes[end]
end

println(generate_primes(10001))
