# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # 빈 리스트나 노드가 1개인 경우, 언제나 True 반환
        
        # deque 생성하고 연결 리스트의 값 저장
        values = deque()
        while head:
            values.append(head.val)
            head = head.next
        
        # palindrome인지 검사
        while len(values) > 1:
            if values.popleft() != values.pop():  # deque의 양 끝 값이 서로 다르면 False 반환
                return False
        
        return True  # deque의 모든 값이 서로 같으면 True 반환