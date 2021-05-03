function area(r)
    return (r^2 * asin(sqrt(r^2 - 1)/r)/2) - sqrt(r^2 - 1) - (r^2 * asin(1/r)/2) + 1
end

function prob(k)
    if k == 1
        return area(k + 1/2)/k^2
    else
        return (area(k + 1/2) - area(k - 1/2))/k^2
    end
end

function main(limit)
    expectation = sum(k * prob(k) for k in 1:limit)
    println(expectation)
end

main(100000)
