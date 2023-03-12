function removeNthFromEnd(head, n) {
  // Create a dummy node to handle edge cases (list with one node or removing the head)
  let dummy = new ListNode(0);
  dummy.next = head;

  // Initialize two pointers: fast and slow
  let fast = dummy;
  let slow = dummy;

  // Move fast n nodes ahead
  for (let i = 1; i <= n + 1; i++) {
    fast = fast.next;
  }

  // Move both pointers until fast reaches the end of the list
  while (fast != null) {
    fast = fast.next;
    slow = slow.next;
  }

  // Remove the nth node from the end by skipping over it
  slow.next = slow.next.next;

  // Return the head of the modified list
  return dummy.next;
}
