using Primes

function min_product(n)
    prime_factors = Dict()
    for i in 2:n
        for (p, k) in factor(i)
            prime_factors[p] = max(get(prime_factors, p, 0), k)
        end
    end
    return prod((p^k) for (p, k) in prime_factors)
end

function P(s, N)
    lower = Int(floor(N/min_product(s)))
    upper = Int(floor(N/min_product(s+1)))
    return lower - upper
end

function main()
    println(sum(P(i, 4^i) for i in 2:31))
end

main()