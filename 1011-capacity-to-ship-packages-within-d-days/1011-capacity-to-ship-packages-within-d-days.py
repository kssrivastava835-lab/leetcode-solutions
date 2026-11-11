class Solution(object):
    def shipWithinDays(self, weights, days):
        def can_ship(capacity):
            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = weight

                    if days_needed > days:
                        return False

                else:
                    current_load += weight

            return True

        

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + (right - left) // 2

            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left