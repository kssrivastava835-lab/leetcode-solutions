class Solution(object):
    def decodeString(self, s):
        stack = []
        current_num = 0
        current_string = ""
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                stack.append((current_string,current_num))
                current_string = ""
                current_num = 0

            elif char == ']':
                previous_string,repeat_count = stack.pop()
                current_string = previous_string + current_string * repeat_count

            else:
                current_string += char

        return current_string