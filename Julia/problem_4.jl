function largest_palindrome()
    large = 0
    for i in 990:-11:100

        if i*999 < large
            return large
        end

        for j in 999:-1:100
            num = i*j

            if num < large
                break
            end

            if string(num) == reverse(string(num))
                large = num
                break
            end
            
        end
    end
end

println(largest_palindrome())
