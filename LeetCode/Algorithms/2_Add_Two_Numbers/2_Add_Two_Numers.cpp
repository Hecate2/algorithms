/*
Runtime: 28 ms, faster than 38.01% of C++ online submissions for Add Two Numbers.
Memory Usage: 11.8 MB, less than 5.14% of C++ online submissions for Add Two Numbers.

HOW CAN THAT BE EVEN FASTER AND MORE MEMORY-SAVING? May I overwrite the input linked lists?
*/

/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int head=1;//指示当前步骤是否为第一步(即pthis指向答案链表的头部)
        int carry=0;//进位
        ListNode *pthis,*ans;
        while(l1 || l2 || carry)
        {
        	if(head)
        	{
	        	pthis=new ListNode(0);
        		ans=pthis;
        		head=0;
        	}//借助CPU的流水线并发，这一步不会消耗O(链表长度)那么多时间，而是与其他步骤并行完成
        	else
        	{
        		pthis->next=new ListNode(0);
        		pthis=pthis->next;
        	}

	        if(l1)
	        {
	        	pthis->val+=(l1->val);
	        	l1=l1->next;
	        }
	        if(l2)
	        {
	        	pthis->val+=(l2->val);
	        	l2=l2->next;
	        }
	        //if(carry)
	        //{
	        	pthis->val+=carry;
	        //}

	        if(pthis->val >= 10)//the maximum can only be 19
	        {
	        	carry=1;
	        	pthis->val -= 10;
	        }
	        else
	        {
	        	carry=0;
	        }
        }

        return ans;
    }
};
