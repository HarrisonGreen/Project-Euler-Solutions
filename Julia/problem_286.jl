function prob(q)
    p = zeros(Float64, 21, 50)

    p[1, 50] = 50/q
    p[2, 50] = 1 - 50/q

    for k in 49:-1:1
        for n in 0:min(51-k, 20)
            if n == 0
                p[n+1, k] = (k/q) * p[n+1, k+1]
            elseif n + k == 51
                p[n+1, k] = (1 - k/q) * p[n, k+1]
            else
                p[n+1, k] = (k/q) * p[n+1, k+1] + (1 - k/q) * p[n, k+1]
            end
        end
    end
    
    return p[21, 1]
end

function main()
    l = 50
    h = 55
    e = 10^-12

    while h - l > e
        p = prob((h + l)/2)
        if p > 0.02
            l = (h + l)/2
        else
            h = (h + l)/2
        end
    end

    println(round((h + l)/2, digits=10))
end

main()
