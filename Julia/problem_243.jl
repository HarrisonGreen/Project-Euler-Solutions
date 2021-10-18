using Primes

function totient_func(n)
    prime_fact = factor(n)
    for (p, k) in prime_fact
        n *= (1-1/p)
    end
    return n
end

function find_increment()
    p = primes(30)
    for i in 1:length(p)
	x = prod((1-1/prime) for prime in p[1:i])
	n = prod(p[1:i])
	if x*n/(n-1) < 15499/94744
	    return prod(p[1:i-1])
	end
    end
end

function find_denominator(inc)
    n = 0
    while true
        n += inc
        x = totient_func(n)
        if x/(n-1) < 15499/94744
            return n
        end
    end
end

function main()
    inc = find_increment()
    denom = find_denominator(inc)
    println(denom)
end

main()
