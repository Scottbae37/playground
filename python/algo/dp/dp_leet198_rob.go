func rob(nums []int) int {
    if len(nums) <= 1 {
        return nums[0]
    }
    if len(nums) == 2 {
        if nums[0] > nums[1] {
            return nums[0]
        }
        return nums[1]
    }
    da := make(map[int]int, len(nums) + 1)
    db := make(map[int]int, len(nums) + 1)
    na := nums[:len(nums)-1]
    nb := nums[1:]

    n := len(na)
    da[n-1] = na[n-1]
    db[n-1] = nb[n-1]
    fmt.Println(n)

    for i := n-2; i >= 0; i -= 1 {
        tmp := da[i+2] + na[i]
        fmt.Printf("i=%d, tmp=%d\n", i, tmp)
        if tmp > da[i+1] {
            da[i] = tmp
        } else {
            da[i] = da[i+1]
        }

        tmp = db[i+2] + nb[i]
        if tmp > db[i+1] {
            db[i] = tmp
        } else {
            db[i] = db[i+1]
        }
    }
    fmt.Printf("%#v", da)
    fmt.Printf("%#v", db)
    if da[0] > db[0] {
        return da[0]
    }
    return db[0]
}