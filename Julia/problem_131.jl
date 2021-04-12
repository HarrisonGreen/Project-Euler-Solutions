using Primes

function count_prime_cube_pairs(limit)
    cube_limit = Int(ceil((sqrt(12 * limit + 9) - 3)/6))
    prime_list = primes(limit)

    count = 0
    for n in 1:cube_limit - 1
        diff = (n + 1)^3 - n^3

        if diff in prime_list
            count += 1
        end
    end

    println(count)
end

count_prime_cube_pairs(1000000)
