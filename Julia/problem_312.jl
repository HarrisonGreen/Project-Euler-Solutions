function cyclic_paths(n)
    n = (n - 3) % 28960854
    c = BigInt(8)
    d = BigInt(8)

    for i in 1:n
        c = (3 * c)^3 % 13^8
        d = (3 * d)^3 % (6 * 13^8)
    end

    return d, c
end

function main()
    n = 10000
    local c

    for i in 1:3
        n, c = cyclic_paths(n)
    end
    
    println(c)
end

main()
