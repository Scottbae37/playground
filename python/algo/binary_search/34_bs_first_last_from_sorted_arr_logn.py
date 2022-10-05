def search(s, e, target, nums):
    while s <= e:
        mid = int((s+e+1)/2)
        if mid == len(nums):
            break
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # divide serach area
        # 찾아도 계속 시도해서 갱신한다
        # 우선 타깃을 찾는 부분
        # 처음 것은 왼쪽으로 끝까지 가본다
        # 마지막 것은 오른쪽으로 끝까지 가본다
        s = 0
        e = len(nums) -1

        idx = search(s, e, target, nums)
        if idx == -1:
            return [-1, -1]

        # check
        max_val = idx
        min_val = idx
        s = idx + 1
        e = len(nums) -1

        # go down
        while s <= e:
            mid = int((s+e+1)/2)
            if mid == len(nums):
                break
            if target == nums[mid]:
                max_val = mid
                s = mid + 1
            if target < nums[mid]:
                e = mid - 1

        # go up
        s = 0
        e = idx-1
        while s <= e:
            mid = int((s+e+1)/2)
            if mid == len(nums):
                break
            if target == nums[mid]:
                min_val = mid
                e = mid - 1
            if target > nums[mid]:
                s = mid + 1
        print(max_val)
        print(min_val)
        return [min_val, max_val]

if __name__ == '__main__':
    