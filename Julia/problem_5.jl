using Primes

function smallest_multiple(n)
    prime_powers = Dict()

    for i in 2:n
        prime_factors = factor(i)
        for (prime, power) in prime_factors
            prime_powers[prime] = max(power, get(prime_powers, prime, 0))
        end
    end

    println(prod([prime^power for (prime, power) in prime_powers]))
end

smallest_multiple(20)
