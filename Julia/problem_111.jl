using Primes

d = 10
p = primes(Int(10^(d-1)), Int(10^d))

maximums = Dict()

for prime in p
    prime = string(prime)
    
    for digit in UnitRange(0, 9)
        digit = string(digit)
        maximums[digit] = max(get(maximums, digit, 0), count(digit, prime))
    end 
end

rep_primes = []

for prime in p
    for digit in UnitRange(0, 9)
        digit = string(digit)
        if count(digit, string(prime)) == maximums[digit]
            append!(rep_primes, prime)
        end
    end
end

println(sum(rep_primes))
