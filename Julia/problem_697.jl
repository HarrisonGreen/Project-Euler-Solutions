using Formatting

function prob(n, l)
    x = BigFloat(l * log(10))
    a = 1
    s = 1

    for k in 1:n-1
        a *= x/k
        s += a
    end

    s /= exp(x)
    return s
end

function main(n)
    l = Int(n * 0.4)
    h = Int(n * 0.5)
    e = 0.01

    while h - l > e
        if prob(n, (h + l)/2) > 0.25
            l = (h + l)/2
        else
            h = (h + l)/2
        end
    end

    println(format((h + l)/2, precision = 2))
end

main(10000000)
