# Linked Lists

class ListNode:
	def __init__(self, x = None):
		self.val = x
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None 

	def toList(self):
		l = []
		cur = self.head  
		while cur:
			l.append(cur.val)
			cur = cur.next 
		return l

	def fromList(self, l):
		self.head = ListNode()
		cur = self.head
		for val in l:
			cur.val = val
			cur.next = ListNode()
			self.tail = cur 
			cur = cur.next

		self.tail.next = None

l = LinkedList()
l.fromList([1,2,3])

assert(l.toList() == [1,2,3])

# ================================================================
# 1.Remove Dups 
# ================================================================
def removeDuplicates(head):
	alreadySeen = set()
	prev = None
	cur = head 
	while cur:
		if cur.val in alreadySeen:
			# prev can never be None if cur.val is duplicate
			prev.next = cur.next
			cur = cur.next
		else:
			alreadySeen.add(cur.val)
			prev = cur 
			cur = cur.next 
	return head 

l = LinkedList()
l.fromList([1,1,2,3,4,4,4])
removeDuplicates(l.head)
assert(l.toList() == [1,2,3,4])

# ================================================================
# 2. find the kth to last element
# ================================================================
# Assumption: k = 0 -> last element
# k = n-1 element -> first element
def kthToLast(head, k):
	kth = head
	end = head
	prev = None 
	for i in range(k):
		end = end.next
	while end:
		prev = kth 
		kth = kth.next
		end = end.next
	return prev

assert(kthToLast(l.head, 0).val== 4)
assert(kthToLast(l.head, 3).val== 1)
assert(kthToLast(l.head, 1).val== 3)

# ================================================================
# 3. delete node given only access to that node
# ================================================================
# cannot delete last node of the list 

def deleteThisNode(n):
	if not n:
		return
	cur = n
	next = n.next
	if next:
		cur.val = next.val
		cur.next = n.next.next 

deleteThisNode(l.head.next.next) # delete 3
assert(l.toList() == [1,2,4])
deleteThisNode(l.head) # delete 1
assert(l.toList() == [2,4])


# ================================================================
# 4. partition the list around value x such that all nodes
# earlier are less than and all nodes greater than are later
# ================================================================

def partitionList(head, x):
	left = head
	right = head
	cur = head
	while cur:
		if cur == head:
			cur = cur.next
		elif cur.val < x:
			temp = cur.next
			cur.next = left
			left = cur
			cur = temp 
		else:
			right.next = cur
			cur = cur.next
			right = right.next
			right.next = None
	return left

l = LinkedList()
l.fromList([10,2,3,8,4,7])
l.head = partitionList(l.head, 5)
# print l.toList()
# TODO: write tests for this

# ================================================================
# 5. 
# ================================================================































