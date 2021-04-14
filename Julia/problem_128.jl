using Primes

function find_tiles(layers::Int, target::Int)
    prime_list = primes(Int(floor(sqrt(12 * layers + 5))))

    count = 0
    for n in 1:layers
        if is_prime(6 * n + 1, prime_list) && is_prime(6 * n - 1, prime_list) && is_prime(12 * n + 5, prime_list)
            count += 1
            if count == target
                println(3 * n^2 - 3 * n + 2)
            end
        end

        if is_prime(6 * n + 5, prime_list) && is_prime(6 * n - 1, prime_list) && is_prime(12 * n - 7, prime_list)
            count += 1
            if count == target
                println(3 * n^2 + 3 * n + 1)
            end
        end
    end
end

function is_prime(n::Int, prime_list::Array)
    root = sqrt(n)
    for prime in prime_list
        if prime > root
            return true
        end

        if n % prime == 0
            return false
        end
    end
    return true
end

function main()
    layers = 70000
    target = 2000
    find_tiles(layers, target)
end

main()
