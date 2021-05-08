function main()
    e = zeros(2, 500)
    e[2, 500] = 2
    e[1, 500] = 2.004

    for k in 498:-1:0
        e[2, k+1] = 1000 * ((499 - k) * e[2, k+2]/500 + 1)/(999 - k)
        e[1, k+1] = 1000 * ((499 - k) * e[1, k+2]/500 + e[2, k+1]/1000 + 1)/(999 - k)
    end
    
    println(round(e[1, 1], digits=8))
end

main()
