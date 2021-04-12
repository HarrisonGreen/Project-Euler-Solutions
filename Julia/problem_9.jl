function find_triple(target)
    a_limit = Int(floor(target/(2+sqrt(2))))
    for a in 1:a_limit
        b = ((target^2/2)-target*a)/(target-a)
        if isinteger(b)
            println(Int(prod([a, b, sqrt(a^2+b^2)])))
        end
    end
end

find_triple(1000)
