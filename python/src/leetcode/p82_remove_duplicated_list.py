from typing import Optional
from leetcode.utils import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # ダミーノードを作成して、先頭を簡単に管理できるようにする
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current is not None:
            # currentが重複している場合、次の重複しないノードまで進む
            if current.next and current.val == current.next.val:
                # 重複している値を記録
                duplicate_val = current.val
                # 重複をスキップ
                while current and current.val == duplicate_val:
                    current = current.next
                # 前のノードのnextを、重複しないノードにリンクする
                prev.next = current
            else:
                # 重複がなければ、prevを進める
                prev = current
                current = current.next

        return dummy.next
