单链表如果占据内存空间
For example, if the list initially allocates enough space for eight nodes, on the ninth insertion the list will have to double its allocated space to 16 and copy over the original 8 nodes, a more expensive operation than a normal insertion.

所以求解链表中间元素的解题思路是：快慢指针法 
    public Node getMid(Node head){
      if(head == null){
         return null;
      }
      
      Node slow = head;
      Node fast = head;
      
      // fast.next = null 表示 fast 是链表的尾节点
      while(fast != null && fast.next != null){
         fast = fast.next.next;
         slow = slow.next;
      }
      return slow;
    }

由单链表的增加删除可以看出，链表的想要对指定索引进行操作（增加，删除），的时候必须获取该索引的前一个元素。记住这句话，对链表算法题很有用。
判断一个链表是否是循环链表
首先此题也是也是考察快慢指针的一个题，也是快慢指针的第二个应用。先简单说一下什么循环链表，循环链表其实就是单链表的尾部指针指向头指针，构建成一个环形的链表，叫做循环链表。 如 1 -> 2 - > 3 -> 1 -> 2 .....。为什么快慢指针再循环链表中总能相遇呢？你可以想象两个人在赛跑，A的速度快，B的速度慢，经过一定时间后，A总是会和B相遇，且相遇时A跑过的总距离减去B跑过的总距离一定是圈长的n倍。这也就是 Floyd判环(圈)算法。

单链表问题
https://juejin.im/post/5aa299c1518825557b4c5806#heading-23

#链表删除理解一下
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
