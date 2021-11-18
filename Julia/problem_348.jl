function find_nums(limit)
    count = Dict()
    total = 0
    
    for i in 2:Int(floor((limit-4)^(1/3)))
        for j in 2:Int(floor((limit-i^3)^(1/2)))
            n = i^3 + j^2
            count[n] = get(count, n, 0) + 1
        end
    end

    for (k, v) in count
        if v == 4 && is_palindrome(string(k))
            total += k
        end
    end

    println(total)
end

function is_palindrome(n)
    k = div(length(n), 2)
    
    for i in 1:k
        if n[i] != n[end-(i-1)]
            return false
        end
    end
    
    return true
end

find_nums(Int(1e9))
